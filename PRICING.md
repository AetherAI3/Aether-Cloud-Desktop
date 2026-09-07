# Pricing & UVT

AetherCloud bills on the shared Aether platform. **One account, one balance, one
bill** — across the desktop app, [Aether Online](https://aethersystems.net/platform/online),
Chat, Code, Design and [Aether Agent](https://github.com/AetherAI3/aether-agent).

> **Live, authoritative pricing lives at [aethersystems.net/pricing](https://aethersystems.net/pricing).**
> If this page and the site disagree, the site is right.

## Tiers

| | **Free** | **Solo** | **Pro** | **Team** |
|---|---|---|---|---|
| **Price** | $0 | $19.99 / mo | $49.99 / mo | $89.99 / mo |
| **UVT / month** | 15,000 | 400,000 | 1,500,000 | 3,000,000 pooled |
| **Max output tokens** | 8,000 | 16,000 | 32,000 | 64,000 |
| **Concurrent runs** | 1 | 1 | 3 | 10 |
| **Workspace** | 1 active project | Individual | Multi-lane, autonomous | Shared, collaborative |

### What each tier unlocks

| Tier | Text models | Orchestrators | Media |
|---|---|---|---|
| **Free** | Claude Haiku 4.5 · DeepSeek V4 Flash · Gemma 4 31B (free) | — | One teaser image render (Nano Banana Pro) |
| **Solo** | + Claude Sonnet 5 · GPT-5.4 mini | Neo | All image models |
| **Pro** | + Claude Opus 4.8 · Claude Opus 5 · GPT-5.5 · GPT-5.6 Sol / Terra / Luna · DeepSeek V4 Pro · Kimi K2.6 · Kimi K3 · Gemma 4 31B · Gemini 3.6 Flash · **Claude Fable 5.1 · GPT-6 Astra · Gemini 3.8 Flash** · Qwen 3.8 Max · Grok 4.6 | Neo · Kronus · Aether-Vision | Image + video |
| **Team** | Same as Pro | Same as Pro | Same as Pro, ~2× the per-model video caps |

Per-model monthly UVT caps apply on top of the plan pool, so one expensive
model can't drain a month in an afternoon.

## What is UVT?

**UVT is Aether's universal compute credit** — the billing system behind every
product. Everything that costs compute is metered in UVT, so you see the cost
of a thing as it happens, not on an invoice later:

- **Model calls** — every text, image and video model, on every surface.
- **Aether Actions & CI** — hosted Build & Test and Security runs on Aether Cloud.
  (Local Aether CI on your own machine is free and unmetered.)
- **Compute services** — video editing and rendering with FFmpeg from Aether Code,
  media pipelines, and other hosted work.
- **Supercluster runs** — long, parallel, multi-agent objectives.

A subscription includes a monthly pool. **UVT top-ups** are pay-as-you-go
credits that go beyond it on demand and apply instantly across the whole platform.

### How a text call is metered

```text
UVT = (input_tokens + 4 × output_tokens) × model_multiplier
```

| Model | Multiplier |
|---|---:|
| Gemma 4 31B (free) | 0.00× |
| Gemma 4 31B / 26B MoE | 0.03× |
| Claude Haiku 4.5 | 0.25× |
| Kimi K2.6 / K2.6 Thinking | 0.30× / 0.25× |
| GPT-5.4 mini | 0.30× |
| DeepSeek V4 Flash / Pro | 0.40× / 0.50× |
| Qwen 3.8 Max · Grok 4.6 | 0.62× |
| Gemini 3.8 Flash | 0.75× |
| Claude Sonnet 5 | 1.00× |
| GPT-5.5 | 1.20× |
| Claude Opus 4.8 · Claude Fable 5.1 · GPT-6 Astra | 5.00× |

- **Cached input** counts at 0.1× — repeated context is ~10× cheaper.
- **Reasoning tokens** count at 0.1×, except on models whose vendor bills
  reasoning at the full output rate (DeepSeek V4, Gemini 3.x Flash and the
  September 2026 frontier cohort), where they count at 1.0×.

**Example — a Sonnet 5 turn:** 300k input + 700k output → (300k + 4 × 700k) × 1.0
= 3,100 UVT.

### Media

Images are priced per render and video per second, scaled to the vendor's real
cost so every model clears the same margin. Rough guide: a Nano Banana Pro 2K
image is about 13,400 UVT; a 5-second Veo 3.1 clip is about 75,000 UVT. The
per-model card is on the [pricing page](https://aethersystems.net/pricing).

## How to subscribe or top up

1. Sign in at **[aethersystems.net](https://aethersystems.net)**.
2. Open **[Pricing](https://aethersystems.net/pricing)**.
3. Choose a subscription or buy UVT credits — they apply instantly to your
   shared balance.

Security tiers (Aether Shield, Fortress, Enterprise) and offensive-security
engagements are listed on the same page.
