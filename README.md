<div align="center">

# AetherCloud

<img alt="AetherCloud — the agentic desktop app" src="https://github.com/user-attachments/assets/0a6e50d7-7867-45a6-93d9-ff1a1875de3d" />

### The desktop app for the Aether AI platform.

Agents, projects, workflows, a living Vault and signed proof — on your machine,
connected to the same account you use on the web and in the terminal.

[![Beta](https://img.shields.io/badge/status-beta-f59e0b)](#beta)
[![Release notes](https://img.shields.io/badge/release_notes-june_2026-14b8a6)](RELEASE_NOTES.md)
[![Platform](https://img.shields.io/badge/platform-Windows-0ea5e9)](https://aethersystems.net/download)
[![Aether Agent](https://img.shields.io/badge/terminal-aether--agent-06b6d4)](https://github.com/AetherAI3/aether-agent)

**[⬇ Download free](https://aethersystems.net/download)** · **[Product page](https://aethersystems.net/aether-cloud)** · **[Pricing](https://aethersystems.net/pricing)** · **[Release notes](RELEASE_NOTES.md)**

[One platform](#one-connected-platform) · [The desktop app](#the-desktop-app) · [Aether Agent](#aether-agent--the-terminal) · [Aether Online & APR](#aether-online--the-project-runtime) · [Effort & CodePro](#effort-levels-and-codepro) · [Models & tiers](#models-and-tiers) · [UVT](#uvt--one-meter-for-everything) · [Actions & CI](#aether-actions-and-ci) · [Memory](#agentic-memory) · [Proof](#provenance--every-action-signed) · [Voice](#aether-voice)

</div>

<!--
  DESKTOP DEMO GIF — record a short loop (open a project → run an agent team →
  result lands in the Vault with its proof entry) and drop it in as
  assets/aethercloud-demo.gif, then swap the hero image above for:
  <img width="820" alt="AetherCloud desktop demo" src="assets/aethercloud-demo.gif" />
-->

> ## Stop chatting with AI. Start commanding a fleet.
>
> AetherCloud is where the work actually happens: teams of agents read your
> files, build multi-step results, and drop them back into your Vault — while you
> watch, or while you sleep. Every file operation and every model output is
> signed into a chain of custody you can read, search and export.

<a id="beta"></a>
> **AetherCloud is in beta.** It is used every day and updated constantly. Things
> will move under you sometimes. If something breaks, tell us — issues here, or
> security reports to the private path in [SECURITY.md](SECURITY.md).

---

## One connected platform

One account. One balance. One memory. Pick the surface that fits the moment.

| Surface | What it's for | Where |
|---|---|---|
| **AetherCloud Desktop** | The full app: agent teams, the Coder IDE, workflows, Vault, Voice, proof logs. | [Download](https://aethersystems.net/download) · [Product page](https://aethersystems.net/aether-cloud) |
| **Aether Online** | The hub. Projects, repositories, memory, connectors, collaborators and logs in one place. Home of the **Aether Project Runtime**. | [aethersystems.net/platform/online](https://aethersystems.net/platform/online) |
| **Aether Chat** | Live AI assistant. Research, build context, generate media, then hand the result to your agents. | [app.aethersystems.net/chat](https://app.aethersystems.net/chat) |
| **Aether Code** | Coding workspace in the browser. Same backend as the desktop app — Vault, Git and sharing built in. | [app.aethersystems.net/code](https://app.aethersystems.net/code) |
| **Aether Design** | Interactive canvas for visual work — layouts, generated images, video. | [app.aethersystems.net/design](https://app.aethersystems.net/design) |
| **Aether Agent** | Open-source coding agent for your terminal. Hosted models or your own local Ollama. | [github.com/AetherAI3/aether-agent](https://github.com/AetherAI3/aether-agent) |
| **Aether Browser** | A real Chrome your agent drives, with a live view you can take over. Built into Aether Agent, runs on Aether Cloud. | [github.com/AetherAI3/agent-browser](https://github.com/AetherAI3/agent-browser) |

Everything above talks to the same **Aether API**, shares the same **UVT**
balance, and writes to the same **Vault** and **memory**. Start a task in the
terminal, check on it from your phone, finish it on the desktop.

<div align="center">
<img width="900" alt="Aether Online — the hub: projects, repositories, memory, collaborators and logs" src="assets/aether-online-hub.png" />
<br />
<sub>Aether Online — the hub view. Contributions, active repositories, and one-click hops into Chat, Code, Design and the agent.</sub>
</div>

---

## The desktop app

AetherCloud is a native Windows app (Electron shell, local FastAPI runtime). It
is not a chat window with a file picker. Here is what's inside.

### 🤖 Agent teams

Build agents in the **Agent Studio** — give each one a name, a role and a model,
group them into teams, and deploy the team on a task. Teams plug into **MCP
servers**, a **skills library**, and can drive a sandboxed browser when a task
needs the live web. **Neo** plans and fans out, **Kronus** audits and repairs,
**Aether-Vision** chains image and video models from one prompt.

### 🗂 Projects and the Coder IDE

Open a project and work next to the agents on one surface: browse the tree, run
multi-step builds, review diffs, let agents edit alongside you. The IDE has
**Aether CI** built in (a `.aether-ci.yml` at the repo root, one-time consent,
checks that block commit or push), plus Git, terminal and a media viewport for
generated assets.

### ⚙️ Workflows

Chain agents into a repeatable pipeline — draft → build → verify → file the
result — then put it on a schedule in plain English (*"every weekday at 9am"*).
It runs unattended and lands signed output in your Vault.

### 🗄 The Vault

The Vault is the working memory your agents reason from: your files, your past
work, your decisions, rendered as a navigable galaxy you can search in plain
English (*"where is my patent filing?"*). It syncs to Aether Online, so the
same context is there in your browser and your terminal. Your files never touch
a third-party cloud.

### 🎙 Voice, 🧾 proof logs, 🧠 memory

Talk to the same agent you type to ([Aether Voice](#aether-voice)). Read and
export the signed record of everything that happened
([Provenance](#provenance--every-action-signed)). Let the system learn how you
work ([Agentic memory](#agentic-memory)).

---

## Aether Agent — the terminal

**[Aether Agent](https://github.com/AetherAI3/aether-agent)** is the open-source
(Apache-2.0) coding agent that bridges into the same platform. It reads your
repository, makes the change, runs the checks you name, and shows you the exit
code. Hosted models through your Aether account, or your own local Ollama with
no account at all.

<div align="center">
<img width="820" alt="Aether Agent starting up, then the slash-command help and the model picker" src="assets/aether-agent-demo.gif" />
<br />
<sub>Install → launch → <code>/help</code> → <code>/models</code>. That's the whole first run.</sub>
</div>

```bash
npm install -g aether-agents@latest --ignore-scripts
aether auth login
aether
```

What you get from the terminal:

- **Proof, not claims.** `--test-cmd` ties "done" to a real command and a real exit code.
- **The effort dial.** `/effort` from `LOW` to `CODEPRO` — the same dial the desktop uses. See [Effort levels and CodePro](#effort-levels-and-codepro).
- **Project Memory.** `aether -m` commits a versioned memory snapshot of your repo, linked to the Git commit, and pushes it to your project on Aether Online.
- **Sessions you can pick back up.** Project-scoped, resumable, hand-off-able as a redacted bundle.
- **MCP built in.** Inspect, diagnose and repair configured MCP servers.
- **Review → ship.** `aether review` picks what goes in, `aether ship` opens the pull request — and never publishes without naming the action.

### Aether Browser — the built-in remote browser

When an agent needs the live web — a login, a 2FA prompt, a portal with no API —
it gets a **real Chrome**, driven over MCP, with a live view you can watch from
any device and **take over** the moment a human is needed. The agent pauses, you
log in, the agent resumes. It runs on Aether Cloud (or self-hosted), it's built
into Aether Agent's remote-session (`/rc`) flow, and it also ships standalone as
[agent-browser](https://github.com/AetherAI3/agent-browser) (`npm i aether-browser` / `pip install aether-browser`).

---

## Aether Online & the Project Runtime

**[Aether Online](https://aethersystems.net/platform/online)** is the hub: your
projects, repositories, memory graph, connectors, collaborators and logs in one
place. It is also where the newest piece of the platform lives.

### APR — Aether Project Runtime

APR is the runtime under every Aether project. One project identity crosses
every surface; the project carries its **graph** (persistent knowledge), its
**DAG** (active execution state), and its **proof**. What that gives you today:

- **GitHub integration.** Connect a repository and the project follows it —
  branches, pull requests, checks and deployments show up in the hub, and Actions
  results project back onto GitHub as checks.
- **MCP routing.** Aether is an MCP server. Point **Claude**, **GPT / Codex**,
  **Hermes** or any MCP client at it and those agents can drive Aether models,
  project memory and media tools directly — other agents become connectors into
  your project, not separate silos.
- **The Aether API.** The single programmatic entry. It carries the model
  fleet, the **memory graph**, project memory (`status / get / stage / commit /
  open`), media generation and the asset library, development context and
  lanes, and bounded **Supercluster** runs — plan first, then dispatch with
  scoped, one-use authority.
- **Supercluster, behind the curtain.** When an objective needs parallel work,
  Aether organizes a Supercluster of agents behind the scenes. You never
  configure workers or a DAG by hand; you use Aether Online.

```text
you  →  Aether Online  →  Aether Project  →  Aether API  →  the right capability
```

---

## Effort levels and CodePro

Every run has an **effort dial**. It moves the number of phases, how many
sub-agents fan out, how many repair passes run, and the UVT ceiling for the run.

```text
LOW ─── MED ─── HIGH ─── MAX ─── ULTRA ─── CODEPRO ⚡
phases · sub-agent fan-out · repair passes · UVT ceiling     + System-2 review · unlimited context
```

**CodePro** is different in kind, not just in size. It switches on two things:

1. **Unlimited context.** The run gets a dedicated space — a large overpool with
   quantized recall and a context chain — so a long session never loses its
   own investigation past the model's window. This is
   [Unlimited Context](https://github.com/AetherAI3/Unlimited-Context-LLM),
   Aether's open-source engine, doing the heavy lifting.
2. **The System-2 compiler.** Instead of forty agents with forty private
   scratchpads, CodePro keeps one **live, shared transcript** — a compact
   intermediate representation every agent reads and writes. A 40-agent
   workflow is 40 agents, **one compiled mind**, orchestrated. The planner,
   the reviewers and every sub-agent coordinate through the same state, and the
   user-facing answer still comes back as plain prose.

### CodePro on SWE-bench

Same model, same tasks, official harness. Only the memory layer differs.

| Instances | Model alone | CodePro | Lift |
|---:|---:|---:|---:|
| 27 | 3 (11.1%) | 7 (25.9%) | 2.33× |
| 89 | 6 (6.7%) | 16 (18.0%) | 2.67× |
| **180** | **14 (7.7%)** | **27 (15.0%)** | **1.93×** |

SWE-bench-lite, scored by the official Docker harness — the repository's own
tests have to pass. Model held fixed at a mid-tier `gpt-4.1-mini`, because the
engine's value is clearest on a base model that forgets. The defensible
large-sample claim is **~2× more real bugs fixed**, and CodePro led at every
checkpoint. The full write-up, charts and the knob sweep (the context chain is
the load-bearing part) live in the AetherCloud benchmark docs.

---

## Models and tiers

One fleet across every surface. Models unlock by tier; what your account can
reach right now is whatever `aether models` prints while signed in, or the
picker in the app.

| | **Free** | **Solo** | **Pro** | **Team** |
|---|---|---|---|---|
| **Price** | $0 | $19.99 / mo | $49.99 / mo | $89.99 / mo |
| **UVT / month** | 15,000 | 400,000 | 1,500,000 | 3,000,000 pooled |
| **Max output** | 8k | 16k | 32k | 64k |
| **Concurrency** | 1 | 1 | 3 | 10 |
| **Workspace** | 1 active project | Individual | Multi-lane, autonomous | Shared, collaborative |
| **Text models** | Claude Haiku 4.5 · DeepSeek V4 Flash · Gemma 4 31B (free) | + Claude Sonnet 5 · GPT-5.4 mini | + everything below | Same as Pro, pooled, more seats |
| **Frontier** | — | — | Claude Opus 4.8 · Claude Opus 5 · GPT-5.5 · GPT-5.6 Sol / Terra / Luna · DeepSeek V4 Pro · Kimi K2.6 · Kimi K3 · Gemma 4 31B · Gemini 3.6 Flash | ✓ |
| **Newest (Sept 2026)** | — | — | **Claude Fable 5.1 · GPT-6 Astra · Gemini 3.8 Flash** · Qwen 3.8 Max · Grok 4.6 | ✓ |
| **Orchestrators** | — | Neo | Neo · Kronus · Aether-Vision | ✓ |
| **Image generation** | 1 teaser render | ✓ all image models | ✓ | ✓ |
| **Video generation** | — | — | ✓ | ✓ (higher caps) |

**Image models:** Nano Banana / Nano Banana 2 / Nano Banana Pro, FLUX.2 Klein /
Pro / Flex / Max, Recraft V3 / V4, Seedream 4.5, Riverflow V2 Fast / Pro,
GPT-5 Image / Image Mini, GPT Image 2.

**Video models:** Seedance 1.5 Pro / 2.0 / 2.0 Fast, Veo 3.1 / Fast / Lite,
Kling 3.0 Standard / Pro / Video O1, Sora 2 Pro, Wan 2.6 / 2.7, Hailuo 2.3,
Grok Imagine Video, HappyHorse 1.0.

**Orchestrators:** **Neo** plans, decomposes, fans out to workers and assembles
the result. **Kronus** runs a deep audit chain — scan, cross-reference, find,
fix. **Aether-Vision** pairs a reasoning brain with the vision fleet: one prompt
plans, prompt-engineers and renders image → video in a single run.

Live, authoritative pricing is at
**[aethersystems.net/pricing](https://aethersystems.net/pricing)**. Security
tiers (Shield, Fortress, Enterprise) and offensive-security engagements are
listed there too.

---

## UVT — one meter for everything

**UVT is Aether's universal compute credit.** It is the billing system behind
every product: one balance, shared across the desktop app, Aether Online, Chat,
Code, Design and the terminal. You can see the cost of a thing as it happens,
not on an invoice later.

What UVT pays for:

- **Model calls** — every text, image and video model, on every surface.
- **Aether Actions & CI** — hosted Build & Test and Security runs on Aether Cloud.
- **Compute services** — video editing and rendering with FFmpeg from Aether
  Code, media pipelines, and other hosted work.
- **Supercluster runs** — long, parallel, multi-agent objectives.

How a text call is metered:

```text
UVT = (input_tokens + 4 × output_tokens) × model_multiplier

  Haiku 4.5   0.25×      Sonnet 5     1.0×      Opus 4.8 / Fable 5.1 / GPT-6 Astra   5.0×
  cached input counts at 0.1×  →  repeated context is ~10× cheaper
```

Media is priced per image or per second of video, and scales with the vendor's
real cost so every model clears the same margin. A subscription includes a
monthly pool; **UVT top-ups** go beyond it on demand and apply instantly across
the whole platform. Per-model monthly caps sit on top of the plan pool so a
single expensive model can't drain a month in an afternoon.

The full model-by-model rate card is in [PRICING.md](PRICING.md) and on the
[pricing page](https://aethersystems.net/pricing).

---

## Aether Actions and CI

Actions is how work gets verified. From an edit in Aether Code (or a push on a
connected repo), one Actions decision runs **Build & Test** and/or **Security**,
either **on your device** or on **Aether Cloud**, and the outcome shows up where
you're working — and on GitHub as a check.

```text
edit  →  one Actions decision  →  Build & Test · Security
      →  this device  |  Aether Cloud (metered in UVT)
      →  visible activity, outcome, bounded repair  →  your review
```

**Local — Aether CI.** Drop an `.aether-ci.yml` in the repo root. Checks run in
the app sandbox on your machine — no cloud compute, no metering. Three gates,
any subset: block `git commit`, block `git push`, or expose a read-only `ci_run`
tool so the coding agent can run → read failures → fix → re-run → green on its
own. You approve the exact commands once; the agent can never self-approve.

```yaml
version: 1
gates:
  commit: false
  push: true
  agent: true
checks:
  - name: tests
    type: test
    run: pytest -q
  - name: lint
    type: lint
    run: ruff check .
```

**Hosted — Aether Cloud.** The same decision, executed on Aether's own runner
fleet with an immutable executor bundle, billed in UVT from your balance with
atomic reservation and settlement. **Security** runs through **Predator**,
Aether's vulnerability-find-and-fix engine, which returns a signed report and
proposed fixes rather than a wall of alerts.

Every approval and every run is signed into the Protocol C chain
([Provenance](#provenance--every-action-signed)). A signer outage logs the run
as `UNSIGNED`; it never blocks your local checks.

---

## Agentic memory

Most AI tools start from zero every session. AetherCloud doesn't. Memory lives
in the cloud, keyed to you, and every surface reads the same store — the
terminal, the web, the desktop. Teach it once anywhere, it knows everywhere.

There are four layers, and you can see and delete any of them:

| Layer | What it holds | How it gets there |
|---|---|---|
| **Facts** | Things about you, your projects and your decisions — episodic (*what happened*), semantic (*what's true*), behavioral (*how you work*). Scoped **global** or **per-project**. | Extracted from your sessions through a durable queue, scored for importance and confidence, re-scored over time. |
| **Skills (QOPC)** | The patterns the agent has learned from how you work — what you accept, revise, publish or discard. | The **Quantum Optimized Prompt Circuit** watches outcomes and tunes its own prompt weights. No config, no fine-tuning; it just gets better the more you use it. |
| **Dream Logs** | Ambient memory: between sessions the system clusters what it learned and writes a short synthesis, so it arrives already up to speed. | Nightly clustering over the fact store. |
| **Project Memory** | A versioned snapshot of a repository's structure and knowledge, tied to an exact Git commit. Commit, push, pull, diff, reconcile — like Git, for memory. | `aether -m commit --link-git HEAD` from the terminal, or automatically from the desktop. |

The **Memory Graph** in Aether Online shows how your code, memory and Vault
connect. Memory chips appear inline in chat so you can see what the agent is
drawing on. Retrieved memory is evidence for the agent, never instructions —
runs still enforce their own permission, checkpoint and proof boundaries.

---

## Provenance — every action signed

**Protocol C** is the chain of custody under everything. Every file operation
(create, read, modify, delete), every agent run, every model output, every
auth event and every chat turn is:

1. **hashed** — SHA-256 of the exact bytes,
2. **signed** — with a quantum-seeded ephemeral key destroyed after a single use,
3. **timestamped** — RFC 3161,
4. **appended** — to an immutable log that chains to the entry before it.

A tampered response fails its signature and the system refuses to proceed.
The log is **viewable** in the Logs tab and the Aether Online hub, **searchable**
by event type, and **exportable** as an evidence-grade proof package you can
hand to an auditor, a client or a court. Patent pending.

Two more things sit on top of it:

- **ATLAS** — a ground-truth engine between your models that keeps outputs
  anchored to verified reality.
- **Predator** — the vulnerability-find-and-fix engine behind Security runs,
  whose reports are signed into the same chain.

---

## Aether Voice

Voice isn't a separate app. The mic in the composer opens a session that speaks
into the **same chat thread**, runs the **same agent** — same tools,
permissions, memory and billing — and renders into the same transcript. Typing
and talking are two inputs to one conversation.

What makes it feel alive:

- **Live conversational awareness.** The surface you're on tells Voice what's on
  screen — the file you have open, the project you're in, the terms in front of
  you — so recognition and replies stay in context instead of guessing.
- **Barge-in.** Start talking while it's speaking and it stops, drops the
  synthesis, cancels the stream and listens. No waiting for it to finish.
- **Streaming speech.** Replies are chunked and voiced as they arrive, in order,
  with markdown turned into something that sounds right when spoken.
- **Provider failover.** If one TTS provider stumbles, the next one picks up
  mid-turn.

Available on the web and the desktop; the terminal exposes a status and doctor
rail (`aether voice`) and lets embedders inject capture and playback.

---

## Get AetherCloud

1. **[Download](https://aethersystems.net/download)** — free, no card. The
   installer provisions its own runtime (Node, Git, ripgrep). About a minute.
2. **Sign in** with your Aether account — the same one for
   [app.aethersystems.net](https://app.aethersystems.net) and `aether auth login`.
3. **Open a project, deploy a team.** Or just ask it something.

Want the terminal too?

```bash
npm install -g aether-agents@latest --ignore-scripts     # or: pipx install aether-agent
aether auth login
```

Upgrade or top up anytime at [aethersystems.net/pricing](https://aethersystems.net/pricing).

---

## Security and this repository

This repository holds the AetherCloud product docs, release notes and media. It
does not contain the application source. Security reports go to
**security@aethersystems.net** — see [SECURITY.md](SECURITY.md) for scope.

AetherCloud is proprietary. Aether Agent, Aether Browser and Unlimited Context
are open source under Apache-2.0. [Terms](TERMS.md).

---

<div align="center">

**AetherCloud** — Aether AI LLC · Proprietary · Patent Pending #64/010,131 · All Rights Reserved

Created by **[Brandon Barrante](https://github.com/AetherAI3)** · founder, Aether AI

[Download](https://aethersystems.net/download) · [Product page](https://aethersystems.net/aether-cloud) · [Aether Online](https://aethersystems.net/platform/online) · [Pricing](https://aethersystems.net/pricing) · [Release notes](RELEASE_NOTES.md) · [Terms](TERMS.md) · [Security](SECURITY.md)

</div>
