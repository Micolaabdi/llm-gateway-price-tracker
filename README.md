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

_Auto-updated 2026-11-09T10:37:57Z — 154 models, 103 matched on OpenRouter._

**73% average saving vs OpenRouter** across 103 matched models (99 of them cheaper).

## Cheapest 25 models (blended $/M tokens, 3:1 in:out)

| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |
|---|---|---|---|---|---|
| `alicn/qwen3.8-flash` | $0.0004 | $0.0012 | $0.0006 | −100% | 1000k |
| `alicn/qwen3.8-omni-flash` | $0.0004 | $0.0012 | $0.0006 | −100% | 1000k |
| `zai/glm-5.3-flash` | $0.0004 | $0.0013 | $0.0006 | −99% | 1000k |
| `alicn/deepseek-v4.1-flash` | $0.0004 | $0.0015 | $0.0007 | −100% | 1000k |
| `alicn/deepseek-v4.1-flash-1017` | $0.0004 | $0.0015 | $0.0007 | −100% | 1000k |
| `alicn/deepseek-v4-flash-0731` | $0.0006 | $0.0016 | $0.0008 | −99% | 1000k |
| `zai/glm-4.6v` | $0.0008 | $0.0022 | $0.0011 | −100% | 200k |
| `mmcn/MiniMax-M2` | $0.0008 | $0.0030 | $0.0013 | — | 204k |
| `ali/deepseek-v4-pro-0813` | $0.0016 | $0.0050 | $0.0025 | −100% | 1000k |
| `alicn/deepseek-v4-pro-0813` | $0.0016 | $0.0050 | $0.0025 | −100% | 1000k |
| `mmcn/MiniMax-M2.1-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `mmcn/MiniMax-M2.5-highspeed` | $0.0015 | $0.0060 | $0.0026 | — | 204k |
| `ag/gemini-3.8-flash-high` | $0.0019 | $0.0094 | $0.0037 | — | 1000k |
| `alicn/kimi-k2.6` | $0.0024 | $0.010 | $0.0043 | −100% | 262k |
| `alicn/kimi-k2.7-code` | $0.0024 | $0.010 | $0.0043 | −100% | 262k |
| `ali/qwen3.8-omni-flash` | $0.0030 | $0.0094 | $0.0046 | −98% | 1000k |
| `ali/qwen3.8-flash` | $0.0034 | $0.011 | $0.0052 | −98% | 1000k |
| `alicn/glm-5.2` | $0.0035 | $0.011 | $0.0054 | −100% | 1000k |
| `alicn/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −99% | 1000k |
| `zai/glm-5.3` | $0.0035 | $0.011 | $0.0054 | −99% | 1000k |
| `ali/qwen3.8-max-0902` | $0.0050 | $0.015 | $0.0075 | −100% | 1000k |
| `alicn/qwen3.8-max` | $0.0050 | $0.015 | $0.0075 | — | 1000k |
| `alicn/qwen3.8-max-0902` | $0.0050 | $0.015 | $0.0075 | −100% | 1000k |
| `oai/gpt-6-luna` | $0.0043 | $0.021 | $0.0085 | −96% | 1050k |
| `alicn/kimi/kimi-k3.1-pro` | $0.0050 | $0.025 | $0.010 | −100% | 1000k |

_Full data for all 154 models: [`data/data.json`](data/data.json)._

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
