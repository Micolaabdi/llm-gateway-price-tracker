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

_Auto-updated 2026-10-02T17:48:59Z — 91 models, 69 matched on OpenRouter._

**84% average saving vs OpenRouter** across 69 matched models (69 of them cheaper).

## Cheapest 25 models (blended $/M tokens, 3:1 in:out)

| Model | In $/M | Out $/M | Blended | vs OpenRouter | Context |
|---|---|---|---|---|---|
| `cb/deepseek-v4.1-flash` | $0.0004 | $0.0015 | $0.0007 | −100% | 1000k |
| `ag/gemini-3.6-flash-high` | $0.0019 | $0.0094 | $0.0037 | — | 1000k |
| `ag/gemini-3.7-flash-high` | $0.0019 | $0.0094 | $0.0037 | — | 1000k |
| `ag/gemini-3.8-flash-high` | $0.0019 | $0.0094 | $0.0037 | — | 1000k |
| `ali/kimi-k2.7-code` | $0.0024 | $0.010 | $0.0043 | −100% | 262k |
| `cx/gpt-6-luna` | $0.0022 | $0.011 | $0.0045 | −98% | 272k |
| `ali/qwen3.8-omni-flash` | $0.0034 | $0.011 | $0.0052 | −98% | 1000k |
| `cbcn/deepseek-v4.1-flash` | $0.0053 | $0.021 | $0.0092 | −92% | 1000k |
| `cx/gpt-5.6-luna` | $0.0045 | $0.027 | $0.010 | −98% | 272k |
| `cb/gpt-5.6-luna` | $0.0050 | $0.030 | $0.011 | −98% | 1000k |
| `cb/minimax-m3` | $0.0075 | $0.030 | $0.013 | −98% | 1000k |
| `cbcn/glm-5.3-flash` | $0.0086 | $0.029 | $0.014 | −94% | 1000k |
| `ali/glm-5.2` | $0.011 | $0.033 | $0.016 | −99% | 1000k |
| `ali/qwen3.8-flash` | $0.011 | $0.034 | $0.017 | −93% | 1000k |
| `cbcn/deepseek-v4-flash` | $0.013 | $0.038 | $0.019 | −46% | 1000k |
| `ag/gemini-pro-agent` | $0.010 | $0.060 | $0.022 | — | 1000k |
| `cbcn/minimax-m2.7` | $0.017 | $0.069 | $0.030 | −92% | 1000k |
| `cbcn/minimax-m3` | $0.017 | $0.069 | $0.030 | −94% | 1000k |
| `cb/hy4-preview` | $0.021 | $0.063 | $0.031 | −97% | 1000k |
| `cp/cline-pass/deepseek-v4.1-flash` | $0.019 | $0.075 | $0.033 | −73% | 1000k |
| `cp/cline-pass/mimo-v2.5` | $0.029 | $0.059 | $0.037 | −79% | 1000k |
| `cp/cline-pass/mimo-v2.6-flash` | $0.029 | $0.059 | $0.037 | −79% | 1000k |
| `ali/qwen3.8-max-0902` | $0.025 | $0.075 | $0.037 | −99% | 1000k |
| `cbcn/hy4-preview` | $0.027 | $0.081 | $0.041 | −96% | 1000k |
| `ag/claude-sonnet-4-6` | $0.022 | $0.113 | $0.045 | — | 1000k |

_Full data for all 91 models: [`data/data.json`](data/data.json)._

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
