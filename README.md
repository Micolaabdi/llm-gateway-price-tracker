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

_Auto-updated 2026-10-12T09:59:51Z — 130 models, 91 matched on OpenRouter._

**63% average saving vs OpenRouter** across 91 matched models (75 of them cheaper).

## Cheapest 25 models (blended $/M tokens, 3:1 in:out)

| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |
|---|---|---|---|---|---|
| `alicn/qwen3.8-flash` | $0.0004 | $0.0012 | $0.0006 | −100% | 1000k |
| `alicn/qwen3.8-omni-flash` | $0.0004 | $0.0012 | $0.0006 | −100% | 1000k |
| `zai/glm-5.3-flash` | $0.0004 | $0.0013 | $0.0006 | −100% | 1000k |
| `alicn/deepseek-v4.1-flash` | $0.0004 | $0.0015 | $0.0007 | −100% | 1000k |
| `cb/deepseek-v4.1-flash` | $0.0004 | $0.0015 | $0.0007 | −100% | 1000k |
| `zai/glm-4.6v` | $0.0008 | $0.0022 | $0.0011 | −100% | 200k |
| `mm/MiniMax-M2.5` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M2.7` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M3` | $0.0008 | $0.0030 | $0.0013 | — | 1000k |
| `mm/MiniMax-M3.1-Flash-Preview` | $0.0008 | $0.0030 | $0.0013 | — | 1000k |
| `alicn/deepseek-v4-pro-0813` | $0.0016 | $0.0050 | $0.0025 | −100% | 1000k |
| `cx/gpt-6-luna` | $0.0013 | $0.0063 | $0.0025 | −99% | 272k |
| `ag/gemini-3.6-flash-high` | $0.0019 | $0.0094 | $0.0037 | — | 1000k |
| `alicn/glm-5.2` | $0.0035 | $0.011 | $0.0054 | −100% | 1000k |
| `alicn/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −100% | 1000k |
| `zai/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −100% | 1000k |
| `cb/gpt-6-luna` | $0.0027 | $0.014 | $0.0055 | −97% | 272k |
| `cx/gpt-5.6-luna` | $0.0025 | $0.015 | $0.0056 | −99% | 272k |
| `ali/deepseek-v4.1-flash` | $0.0037 | $0.015 | $0.0066 | −99% | 1000k |
| `alicn/qwen3.8-max` | $0.0050 | $0.015 | $0.0075 | — | 1000k |
| `grok/grok-4.6` | $0.0050 | $0.015 | $0.0075 | −100% | 500k |
| `grok/grok-4.7` | $0.0050 | $0.015 | $0.0075 | −100% | 500k |
| `ag/gemini-3.7-flash-high` | $0.0056 | $0.028 | $0.011 | — | 1000k |
| `mmcn/MiniMax-M2.5` | $0.0067 | $0.027 | $0.012 | — | 204k |
| `mmcn/MiniMax-M2.7` | $0.0067 | $0.027 | $0.012 | — | 204k |

_Full data for all 130 models: [`data/data.json`](data/data.json)._

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
