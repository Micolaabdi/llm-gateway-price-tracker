# LLM Gateway Price Tracker

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

_Auto-updated 2026-11-16T10:22:19Z — 152 models, 99 matched on OpenRouter._

**60% average saving vs OpenRouter** across 99 matched models (95 of them cheaper).

## Cheapest 25 models (blended $/M tokens, 3:1 in:out)

| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |
|---|---|---|---|---|---|
| `mimotp/mimo-v2.6-flash` | $0.0003 | $0.0007 | $0.0004 | −100% | 1000k |
| `zai/glm-5.3-flash` | $0.0004 | $0.0013 | $0.0006 | −99% | 1000k |
| `mm/MiniMax-M3.1-Flash` | $0.0004 | $0.0015 | $0.0007 | — | 1000k |
| `mm/MiniMax-M3.1-Flash-Preview` | $0.0004 | $0.0015 | $0.0007 | — | 1000k |
| `zai/glm-4.6v` | $0.0008 | $0.0022 | $0.0011 | −100% | 200k |
| `mm/MiniMax-M2` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M2.1` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M2.5` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M2.7` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M3` | $0.0008 | $0.0030 | $0.0013 | — | 1000k |
| `mmcn/MiniMax-M2` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mimotp/mimo-v2.6-pro` | $0.0011 | $0.0022 | $0.0014 | −100% | 1000k |
| `mm/MiniMax-M2.1-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mm/MiniMax-M2.5-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mm/MiniMax-M2.7-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mmcn/MiniMax-M2.1-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mmcn/MiniMax-M2.5-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `cx/gpt-6-luna` | $0.0025 | $0.013 | $0.0050 | −98% | 272k |
| `zai/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −99% | 1000k |
| `mv/zai-glm-5-3-flash` | $0.0064 | $0.021 | $0.010 | — | 1000k |
| `cx/gpt-5.6-luna` | $0.0045 | $0.027 | $0.010 | −98% | 272k |
| `ali/qwen3.8-27b` | $0.0088 | $0.052 | $0.020 | −97% | 1000k |
| `cbcn/glm-5.3-flash` | $0.018 | $0.059 | $0.028 | −44% | 1000k |
| `grok/grok-4.5` | $0.020 | $0.060 | $0.030 | −99% | 500k |
| `grok/grok-4.6` | $0.020 | $0.060 | $0.030 | −99% | 500k |

_Full data for all 152 models: [`data/data.json`](data/data.json)._

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
