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

_Auto-updated 2026-11-23T11:30:20Z — 169 models, 112 matched on OpenRouter._

**52% average saving vs OpenRouter** across 112 matched models (104 of them cheaper).

## Cheapest 25 models (blended $/M tokens, 3:1 in:out)

| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |
|---|---|---|---|---|---|
| `zai/glm-5.3-flash` | $0.0004 | $0.0013 | $0.0006 | −99% | 1000k |
| `mm/MiniMax-M3.1-Flash` | $0.0004 | $0.0015 | $0.0007 | — | 1000k |
| `mm/MiniMax-M3.1-Flash-Preview` | $0.0004 | $0.0015 | $0.0007 | — | 1000k |
| `zai/glm-4.6v` | $0.0008 | $0.0022 | $0.0011 | −100% | 200k |
| `mm/MiniMax-M2.5` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M2.7` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `mm/MiniMax-M3` | $0.0008 | $0.0030 | $0.0013 | — | 1000k |
| `mm/MiniMax-M2.5-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mm/MiniMax-M2.7-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `ali/qwen3.8-omni-flash` | $0.0034 | $0.011 | $0.0052 | −98% | 1000k |
| `zai/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −99% | 1000k |
| `mv/mistral-medium-3-5` | $0.0037 | $0.019 | $0.0075 | −100% | 262k |
| `nebula/glm-5.3-flash` | $0.010 | $0.030 | $0.015 | −70% | 1000k |
| `cb/glm-5.3-flash` | $0.011 | $0.036 | $0.017 | −65% | 1000k |
| `cb/hy3` | $0.010 | $0.042 | $0.018 | −93% | 192k |
| `cb/deepseek-v4.1-flash` | $0.011 | $0.043 | $0.019 | −78% | 1000k |
| `cb/deepseek-v4.1-flash-sg` | $0.011 | $0.043 | $0.019 | — | 1000k |
| `cb/minimax-m3.1-flash` | $0.011 | $0.043 | $0.019 | −93% | 1000k |
| `nebula/claude-haiku-5-5` | $0.010 | $0.050 | $0.020 | — | 1000k |
| `nebula/deepseek-v4.1-flash-1017` | $0.010 | $0.050 | $0.020 | −92% | 1000k |
| `nebula/gemini-3.8-flash` | $0.028 | $0.028 | $0.028 | −98% | 1000k |
| `nebula/glm-5.3` | $0.030 | $0.030 | $0.030 | −92% | 1000k |
| `cx/gpt-6-luna` | $0.018 | $0.087 | $0.035 | −82% | 400k |
| `nebula/gpt-5.6-terra` | $0.030 | $0.050 | $0.035 | −99% | 1000k |
| `cb/minimax-m3` | $0.022 | $0.087 | $0.038 | −93% | 1000k |

_Full data for all 169 models: [`data/data.json`](data/data.json)._

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
