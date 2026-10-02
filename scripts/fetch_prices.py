#!/usr/bin/env python3
"""Fetch current per-model prices from public gateway APIs and write data.json.

Sources:
  - OpenRouter   https://openrouter.ai/api/v1/models          (no auth, USD per token)
  - AtmoRouter   https://atmorouter.dev/api/dashboard/catalog (no auth, USD per M tokens)

Output: data/data.json  {generated_at, sources, models: [ ... ]}
Only AtmoRouter models are listed (the tracker compares them against OpenRouter),
sorted by AtmoRouter blended price so the cheapest appear first.
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone

OPENROUTER_URL = "https://openrouter.ai/api/v1/models"
ATMOROUTER_URL = "https://atmorouter.dev/api/dashboard/catalog"

# Blended price weights (standard 3:1 input:output heuristic used across the tracker)
IN_W, OUT_W = 3.0, 1.0


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "llm-gateway-price-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def norm(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources": {
            "atmorouter": ATMOROUTER_URL,
            "openrouter": OPENROUTER_URL,
        },
        "models": [],
    }

    atmo = fetch_json(ATMOROUTER_URL)
    atmo_models = atmo.get("data") or []
    if not atmo_models:
        print("ERROR: AtmoRouter catalog returned no models", file=sys.stderr)
        sys.exit(1)

    or_models = fetch_json(OPENROUTER_URL).get("data") or []
    # index OpenRouter by suffix match (atmo "ag/claude-opus-4-6" -> or "anthropic/claude-opus-4-6")
    or_by_suffix = {}
    for m in or_models:
        or_by_suffix.setdefault(m["id"].split("/")[-1], m)

    for m in atmo_models:
        if not m.get("enabled"):
            continue
        in_usd_m = norm(m.get("input_price"))
        out_usd_m = norm(m.get("output_price"))
        if in_usd_m is None or out_usd_m is None:
            continue
        blended = (in_usd_m * IN_W + out_usd_m * OUT_W) / (IN_W + OUT_W)

        or_in = or_out = None
        or_id = None
        suffix = m["id"].split("/")[-1]
        om = or_by_suffix.get(suffix)
        if om:
            or_id = om["id"]
            or_in = norm(om.get("pricing", {}).get("prompt"))
            or_out = norm(om.get("pricing", {}).get("completion"))
            # OpenRouter quotes USD per token -> convert to per-M
            if or_in is not None:
                or_in = or_in * 1_000_000
            if or_out is not None:
                or_out = or_out * 1_000_000

        row = {
            "id": m["id"],
            "family": m.get("family"),
            "atmorouter": {
                "input_per_m": in_usd_m,
                "output_per_m": out_usd_m,
                "blended_per_m": round(blended, 6),
                "context_length": m.get("context_length"),
            },
        }
        if or_id:
            row["openrouter"] = {
                "id": or_id,
                "input_per_m": round(or_in, 6),
                "output_per_m": round(or_out, 6),
            }
            if or_in and or_out:
                or_blended = (or_in * IN_W + or_out * OUT_W) / (IN_W + OUT_W)
                row["openrouter"]["blended_per_m"] = round(or_blended, 6)
                if or_blended > 0:
                    row["vs_openrouter_pct"] = round((or_blended - blended) / or_blended * 100, 1)
        out["models"].append(row)

    out["models"].sort(key=lambda r: r["atmorouter"]["blended_per_m"])

    path = "data/data.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    print(f"wrote {path}: {len(out['models'])} models "
          f"({sum(1 for r in out['models'] if 'openrouter' in r)} matched on OpenRouter)")


if __name__ == "__main__":
    main()
