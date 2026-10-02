#!/usr/bin/env python3
"""Render README.md from data/data.json — sorted table + vs-OpenRouter savings."""
import json

with open("data/data.json") as f:
    data = json.load(f)

models = [m for m in data["models"] if m["atmorouter"]["input_per_m"] > 0]
top = models[:25]
matched = [m for m in models if "vs_openrouter_pct" in m and m["openrouter"].get("blended_per_m")]
avg_saving = sum(m["vs_openrouter_pct"] for m in matched) / len(matched) if matched else 0
n_cheaper = sum(1 for m in matched if m["vs_openrouter_pct"] > 0)


def fmt(x):
    if x >= 1:
        return f"${x:.2f}"
    if x >= 0.01:
        return f"${x:.3f}"
    return f"${x:.4f}"


lines = []
lines.append(f"_Auto-updated {data['generated_at']} — {len(models)} models, {len(matched)} matched on OpenRouter._")
lines.append("")
lines.append(f"**{avg_saving:.0f}% average saving vs OpenRouter** across {len(matched)} matched models ({n_cheaper} of them cheaper).")
lines.append("")
lines.append("## Cheapest 25 models (blended $/M tokens, 3:1 in:out)")
lines.append("")
lines.append("| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |")
lines.append("|---|---|---|---|---|---|")
for m in top:
    a = m["atmorouter"]
    vs = m.get("vs_openrouter_pct")
    vs_s = f"−{vs:.0f}%" if vs is not None and vs > 0 else (f"+{-vs:.0f}%" if vs is not None else "—")
    ctx = a.get("context_length")
    ctx_s = f"{ctx // 1000}k" if ctx else "—"
    lines.append(
        f"| `{m['id']}` | {fmt(a['input_per_m'])} | {fmt(a['output_per_m'])} | {fmt(a['blended_per_m'])} | {vs_s} | {ctx_s} |"
    )
lines.append("")
lines.append(f"_Full data for all {len(models)} models: [`data/data.json`](data/data.json)._")

table = "\n".join(lines)

readme = f"""# LLM Gateway Price Tracker

Weekly price comparison of **AtmoRouter** vs **OpenRouter** — per-model, per-million-token,
updated automatically by GitHub Actions every Monday.

> Disclosure: maintained by [AtmoRouter](https://atmorouter.dev). Data is fetched live from
> both gateways' public APIs and written by script — nothing here is hand-typed.
> The comparison methodology is open: blended price = (3 × input + 1 × output) / 4,
> the ratio most chat/agent workloads approximate.

## Why

Picking a gateway by price means tabbing between pricing pages. This repo does it
programmatically: one JSON snapshot, one README table, refreshed weekly, full history in
git.

## Latest snapshot

{table}

## How it works

- `scripts/fetch_prices.py` — pulls both public APIs (no auth needed), normalizes to $/M
  tokens, matches AtmoRouter model ids to OpenRouter by suffix, writes `data/data.json`
- GitHub Actions (`.github/workflows/update.yml`) runs it weekly, commits if changed
- Every commit = a historical price point; `git log data/data.json` is the price history

## Use the snapshot yourself

```bash
curl -s https://raw.githubusercontent.com/Micolaabdi/llm-gateway-price-tracker/main/data/data.json | jq '.models[0]'
```

Or fetch the live sources directly:

- AtmoRouter: `https://atmorouter.dev/api/dashboard/catalog` (public, no auth)
- OpenRouter: `https://openrouter.ai/api/v1/models` (public, no auth)

## Contributing

Found a mismatch or want another gateway added to the comparison? Open an issue or PR —
the fetcher is one Python file with no dependencies.

## License

MIT
"""

with open("README.md", "w") as f:
    f.write(readme)

print(f"README.md written: {len(models)} models, {len(matched)} matched, avg saving {avg_saving:.1f}%")
