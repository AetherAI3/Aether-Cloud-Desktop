"""Generate the README's SVG cards. Self-contained, system fonts only (GitHub renders SVG as <img>)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
BG = "#0a0f1c"; CARD = "#0f172a"; CARD2 = "#111a2e"; BORDER = "#1f2a44"
TEAL = "#2dd4bf"; TEAL_D = "#14b8a6"; CYAN = "#22d3ee"; PURPLE = "#a78bfa"; AMBER = "#fbbf24"
TXT = "#e5edf7"; MUTED = "#8b9bb4"; DIM = "#5b6b85"; RED = "#f87171"; GREEN = "#4ade80"

def svg(w, h, body, defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<defs>
<linearGradient id="tealgrad" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{PURPLE}"/></linearGradient>
<linearGradient id="btn" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="#3b82f6"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="softglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
{defs}
</defs>
{body}
</svg>'''

def card(x, y, w, h, fill=CARD, stroke=BORDER, r=14, sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def text(x, y, s, size=14, fill=TXT, weight=400, anchor="start", mono=False, extra=""):
    s = s.replace("&", "&amp;")
    fam = f' font-family="{MONO}"' if mono else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{fam} {extra}>{s}</text>'

def pill(x, y, label, fill=TEAL, color="#04201c", size=11, pad=10, h=22, weight=700):
    w = int(len(label) * size * 0.62) + pad * 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}"/>'
            + text(x + w / 2, y + h / 2 + size * 0.36, label, size, color, weight, "middle")), w

def button(x, y, w, label, h=40, grad="url(#btn)", color="#04121f", size=15):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{grad}"/>'
            + text(x + w / 2, y + h / 2 + size * 0.36, label, size, color, 700, "middle"))

def bg(w, h):
    dots = "".join(f'<circle cx="{i*40+20}" cy="{j*40+20}" r="1" fill="#1b2740"/>' for i in range(w // 40 + 1) for j in range(h // 40 + 1))
    return f'<rect width="{w}" height="{h}" rx="18" fill="{BG}"/>{dots}<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="18" fill="none" stroke="{BORDER}"/>'

# ---------------------------------------------------------------- effort dial
def effort_dial():
    W, H = 920, 236
    stops = ["LOW", "MED", "HIGH", "MAX", "ULTRA", "CODEPRO"]
    x0, x1, ty = 90, 790, 110
    b = [bg(W, H)]
    b.append(text(40, 46, "EFFORT DIAL", 12, MUTED, 700, extra='letter-spacing="2"'))
    b.append(text(W - 40, 46, "phases · sub-agent fan-out · repair passes · UVT ceiling", 12, DIM, 400, "end", mono=True))
    # track
    b.append(f'<rect x="{x0}" y="{ty-5}" width="{x1-x0}" height="10" rx="5" fill="#16213a"/>')
    b.append(f'<rect x="{x0}" y="{ty-5}" width="{x1-x0}" height="10" rx="5" fill="url(#tealgrad)" opacity="0.85"/>')
    n = len(stops)
    for i, s in enumerate(stops):
        x = x0 + (x1 - x0) * i / (n - 1)
        last = i == n - 1
        if last:
            b.append(f'<circle cx="{x}" cy="{ty}" r="22" fill="{AMBER}" opacity="0.25" filter="url(#softglow)"/>')
            b.append(f'<circle cx="{x}" cy="{ty}" r="14" fill="{BG}" stroke="{AMBER}" stroke-width="3" filter="url(#glow)"/>')
            b.append(text(x, ty + 6, "⚡", 16, AMBER, 700, "middle"))
            b.append(text(x, ty + 46, s, 15, AMBER, 800, "middle", mono=True, extra='letter-spacing="1"'))
            b.append(text(x, ty + 68, "System-2 review · unlimited context", 11, AMBER, 400, "middle"))
        else:
            b.append(f'<circle cx="{x}" cy="{ty}" r="9" fill="{BG}" stroke="{TEAL}" stroke-width="3"/>')
            b.append(text(x, ty + 46, s, 13, TXT, 700, "middle", mono=True, extra='letter-spacing="1"'))
            hint = ["quick answers", "everyday work", "deeper passes", "full fan-out", "every gate"][i]
            b.append(text(x, ty + 68, hint, 11, DIM, 400, "middle"))
    b.append(text(40, H - 22, "Same dial on the desktop, the web and in the terminal (/effort). Higher = more work, more proof, more UVT.", 12, MUTED))
    (OUT / "effort-dial.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

# ---------------------------------------------------------------- protocol c card
def protocol_c_card():
    W, H = 920, 210
    b = [bg(W, H)]
    # shield icon
    b.append(f'<path d="M78 40 l34 12 v30 c0 22 -16 36 -34 44 c-18 -8 -34 -22 -34 -44 v-30 z" fill="#0b2a2a" stroke="{TEAL}" stroke-width="2.5" filter="url(#glow)"/>')
    b.append(f'<path d="M64 84 l10 10 l20 -22" fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(text(140, 58, "Protocol C", 26, TXT, 800))
    p, pw = pill(282, 40, "OPEN SOURCE · APACHE-2.0", TEAL, "#04201c", 10)
    b.append(p)
    b.append(text(140, 88, "The audit chain AetherCloud is built on. Every file operation, agent run and model output is hashed,", 14, MUTED))
    b.append(text(140, 108, "signed with a one-shot key, timestamped and appended to a tamper-evident log you can export as proof.", 14, MUTED))
    b.append(text(140, 140, "SHA-256 chain  ·  forward-secret one-use keys  ·  RFC 3161 timestamps  ·  pure Python stdlib, zero deps", 12, DIM, 400, mono=True))
    b.append(button(140, 158, 250, "View the repo on GitHub  →", 36, size=14))
    b.append(text(W - 40, 178, "github.com/AetherAI3/PROTOCOL-C", 12, DIM, 400, "end", mono=True))
    (OUT / "protocol-c-card.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

# ---------------------------------------------------------------- actions flow
def actions_flow():
    W, H = 920, 470
    b = [bg(W, H)]
    b.append(text(40, 46, "AETHER ACTIONS", 12, MUTED, 700, extra='letter-spacing="2"'))
    b.append(text(W - 40, 46, "Build, verify, secure and ship your repositories", 12, DIM, 400, "end"))
    # GitHub node (left)
    b.append(card(40, 100, 200, 120, CARD2, BORDER, 14))
    b.append(text(140, 136, "GitHub", 18, TXT, 800, "middle"))
    b.append(text(140, 160, "push · pull request", 12, MUTED, 400, "middle", mono=True))
    b.append(text(140, 178, "connected repo", 12, MUTED, 400, "middle", mono=True))
    b.append(text(140, 202, "← result lands as a check", 11, TEAL, 700, "middle"))
    # arrow to decision
    b.append(f'<path d="M240 160 H300" stroke="{TEAL}" stroke-width="2.5" marker-end="url(#arr)"/>')
    # decision node
    b.append(card(300, 118, 150, 84, "#0b2a2a", TEAL, 14, 1.5))
    b.append(text(375, 152, "one Actions", 14, TXT, 700, "middle"))
    b.append(text(375, 172, "decision", 14, TXT, 700, "middle"))
    # branches
    b.append(f'<path d="M450 160 C480 160 480 100 510 100" fill="none" stroke="{CYAN}" stroke-width="2.5" marker-end="url(#arr)"/>')
    b.append(f'<path d="M450 160 C480 160 480 330 510 330" fill="none" stroke="{PURPLE}" stroke-width="2.5" marker-end="url(#arr2)"/>')
    # Build & Test lane
    b.append(card(510, 64, 370, 190, CARD2, CYAN, 14, 1.2))
    b.append(text(534, 96, "Build & Test", 17, TXT, 800))
    b.append(text(534, 118, "Runs your project's configured checks — tests, lint,", 12, MUTED))
    b.append(text(534, 134, "typecheck, build — from your .aether-ci.yml.", 12, MUTED))
    # two sub-cards
    b.append(card(534, 150, 155, 84, "#0d1a30", BORDER, 10))
    b.append(text(611, 174, "On your device", 13, TXT, 700, "middle"))
    p, pw = pill(611 - 34, 184, "0 UVT", GREEN, "#052e16", 10, 9, 20); b.append(p)
    b.append(text(611, 224, "Local Actions in the desktop app", 10, DIM, 400, "middle"))
    b.append(card(707, 150, 155, 84, "#0d1a30", BORDER, 10))
    b.append(text(784, 174, "On Aether Cloud", 13, TXT, 700, "middle"))
    p, pw = pill(784 - 46, 184, "exact UVT quote", CYAN, "#062a33", 10, 9, 20); b.append(p)
    b.append(text(784, 224, "you approve before anything runs", 10, DIM, 400, "middle"))
    # Predator lane
    b.append(card(510, 270, 370, 170, CARD2, PURPLE, 14, 1.2))
    b.append(text(534, 302, "Predator Security", 17, TXT, 800))
    p, pw = pill(700, 286, "HOSTED · LOCKED", PURPLE, "#1e1b4b", 10); b.append(p)
    b.append(text(534, 324, "Verifies the exact commit against five locked assurance routes:", 12, MUTED))
    routes = ["Access Control", "File Boundaries", "Command Safety", "Network Request Safety", "Protected AI & Billing Authorization"]
    y = 346
    for i, r in enumerate(routes):
        cx = 534 if i < 3 else 700
        cy = y + (i % 3) * 20 if i < 3 else y + (i - 3) * 20
        b.append(f'<circle cx="{cx+5}" cy="{cy-4}" r="4" fill="{PURPLE}"/>')
        b.append(text(cx + 16, cy, r, 12, TXT))
    b.append(text(534, 424, "Clean run → a signed Predator Security Certificate.", 12, TEAL, 700))
    # footer
    b.append(text(40, 262, "Every approval and every run is signed", 12, MUTED))
    b.append(text(40, 280, "into the Protocol C chain.", 12, MUTED))
    b.append(text(40, 316, "Recent runs, UVT captured / released,", 12, DIM))
    b.append(text(40, 334, "and the GitHub check are all visible", 12, DIM))
    b.append(text(40, 352, "in Aether Online → Actions.", 12, DIM))
    defs = (f'<marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{CYAN}"/></marker>'
            f'<marker id="arr2" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{PURPLE}"/></marker>')
    (OUT / "actions-flow.svg").write_text(svg(W, H, "\n".join(b), defs), encoding="utf-8")

# ---------------------------------------------------------------- tier cards
def tiers():
    W, H = 920, 400
    b = [bg(W, H)]
    tiers = [
        ("Free", "$0", "15,000 UVT / mo", ["Claude Haiku 4.5", "DeepSeek V4 Flash", "Gemma 4 31B", "1 active project", "1 image teaser"], None, BORDER),
        ("Solo", "$19.99", "400,000 UVT / mo", ["+ Claude Sonnet 5", "+ GPT-5.4 mini", "+ Neo orchestrator", "All image models", "Individual workspace"], None, BORDER),
        ("Pro", "$49.99", "1,500,000 UVT / mo", ["+ Claude Fable 5.1", "+ GPT-6 Astra", "+ Gemini 3.8 Flash", "+ Opus 5 · GPT-5.6 · Kimi K3", "Video · Kronus · Vision"], "POPULAR", TEAL),
        ("Team", "$89.99", "3,000,000 UVT pooled", ["Everything in Pro", "Shared workspace", "10 concurrent runs", "64k output", "~2× video caps"], None, PURPLE),
    ]
    cw, gap, x, y, ch = 205, 15, 40, 40, 320
    for i, (name, price, uvt, feats, badge, stroke) in enumerate(tiers):
        cx = x + i * (cw + gap)
        b.append(card(cx, y, cw, ch, CARD2 if badge else CARD, stroke, 14, 1.5 if badge else 1))
        if badge:
            p, pw = pill(cx + cw - 86, y + 14, badge, TEAL, "#04201c", 9, 9, 20); b.append(p)
        b.append(text(cx + 20, y + 42, name, 18, TXT, 800))
        b.append(text(cx + 20, y + 84, price, 30, TEAL if badge else TXT, 800))
        if price != "$0":
            b.append(text(cx + 20 + len(price) * 17, y + 84, "/ mo", 12, MUTED))
        b.append(text(cx + 20, y + 108, uvt, 12, CYAN, 700, mono=True))
        b.append(f'<line x1="{cx+20}" y1="{y+124}" x2="{cx+cw-20}" y2="{y+124}" stroke="{BORDER}"/>')
        for j, f in enumerate(feats):
            fy = y + 152 + j * 26
            b.append(f'<path d="M{cx+20} {fy-4} l4 4 l8 -9" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linecap="round"/>')
            b.append(text(cx + 40, fy, f, 12, TXT if j < 3 else MUTED))
        b.append(button(cx + 20, y + ch - 52, cw - 40, "Get started" if name == "Free" else f"Choose {name}", 34, "url(#btn)" if badge else "#1b2740", "#04121f" if badge else TXT, 13))
    b.append(text(40, H - 18, "Live, authoritative pricing: aethersystems.net/pricing  ·  UVT top-ups apply instantly across every surface", 12, DIM, 400, mono=True))
    (OUT / "tiers.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

# ---------------------------------------------------------------- surfaces row
def surfaces():
    W, H = 920, 150
    b = [bg(W, H)]
    items = [("Desktop", "the full app", TEAL), ("Online", "the hub · APR", CYAN), ("Chat", "live assistant", "#60a5fa"),
             ("Code", "browser IDE", "#818cf8"), ("Design", "canvas", PURPLE), ("Agent", "terminal", "#f472b6"), ("Browser", "remote Chrome", AMBER)]
    n = len(items); cw = (W - 80 - (n - 1) * 12) / n
    for i, (name, sub, col) in enumerate(items):
        cx = 40 + i * (cw + 12)
        b.append(card(cx, 34, cw, 82, CARD2, BORDER, 12))
        b.append(f'<rect x="{cx}" y="34" width="{cw}" height="4" rx="2" fill="{col}"/>')
        b.append(text(cx + cw / 2, 68, name, 15, TXT, 800, "middle"))
        b.append(text(cx + cw / 2, 90, sub, 11, MUTED, 400, "middle"))
    b.append(text(W / 2, 138, "one account · one UVT balance · one Vault · one memory", 12, DIM, 400, "middle", mono=True))
    (OUT / "surfaces.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

# ---------------------------------------------------------------- uvt card
def uvt():
    W, H = 920, 250
    b = [bg(W, H)]
    b.append(text(40, 46, "UVT — ONE METER FOR EVERYTHING", 12, MUTED, 700, extra='letter-spacing="2"'))
    items = [("Model calls", "text · image · video", TEAL), ("Actions & CI", "hosted Build & Test", CYAN),
             ("Predator Security", "signed certificate", PURPLE), ("Compute", "FFmpeg · media pipelines", "#60a5fa"), ("Supercluster", "parallel objectives", AMBER)]
    n = len(items); cw = (W - 80 - (n - 1) * 12) / n
    for i, (name, sub, col) in enumerate(items):
        cx = 40 + i * (cw + 12)
        b.append(card(cx, 66, cw, 78, CARD2, BORDER, 12))
        b.append(f'<circle cx="{cx+22}" cy="{92}" r="6" fill="{col}"/>')
        b.append(text(cx + 36, 97, name, 13, TXT, 700))
        b.append(text(cx + 18, 124, sub, 11, MUTED))
    b.append(card(40, 162, W - 80, 60, "#0b1526", BORDER, 12))
    b.append(text(60, 188, "UVT = (input_tokens + 4 × output_tokens) × model_multiplier", 14, TXT, 700, mono=True))
    b.append(text(60, 210, "Haiku 0.25×   Sonnet 5 1.0×   GPT-5.5 1.2×   Opus · Fable 5.1 · GPT-6 Astra 5.0×   cached input 0.1×", 12, MUTED, 400, mono=True, extra='xml:space="preserve"'))
    b.append(text(W - 40, 240, "one balance across every surface · top-ups apply instantly", 11, DIM, 400, "end"))
    (OUT / "uvt.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

# ---------------------------------------------------------------- memory layers
def memory():
    W, H = 920, 230
    b = [bg(W, H)]
    b.append(text(40, 46, "AGENTIC MEMORY — FOUR LAYERS, ONE STORE", 12, MUTED, 700, extra='letter-spacing="2"'))
    layers = [("Facts", "what happened, what's true,", "how you work · per project too", TEAL),
              ("Skills · QOPC", "learned from what you accept,", "revise, publish or discard", CYAN),
              ("Dream Logs", "nightly synthesis so it", "arrives already up to speed", PURPLE),
              ("Project Memory", "versioned snapshot of a repo,", "tied to an exact Git commit", AMBER)]
    n = len(layers); cw = (W - 80 - (n - 1) * 14) / n
    for i, (name, l1, l2, col) in enumerate(layers):
        cx = 40 + i * (cw + 14)
        b.append(card(cx, 66, cw, 110, CARD2, BORDER, 12))
        b.append(f'<rect x="{cx}" y="66" width="4" height="110" rx="2" fill="{col}"/>')
        b.append(text(cx + 20, 96, name, 15, TXT, 800))
        b.append(text(cx + 20, 122, l1, 12, MUTED))
        b.append(text(cx + 20, 140, l2, 12, MUTED))
        b.append(text(cx + 20, 164, f"{i+1:02d}", 11, col, 700, mono=True))
    b.append(text(W / 2, 208, "shared by the terminal, the web and the desktop  ·  visible in the Memory Graph  ·  delete anything, anytime", 12, DIM, 400, "middle", mono=True))
    (OUT / "memory-layers.svg").write_text(svg(W, H, "\n".join(b)), encoding="utf-8")

if __name__ == "__main__":
    effort_dial(); protocol_c_card(); actions_flow(); tiers(); surfaces(); uvt(); memory()
    print("ok", sorted(p.name for p in OUT.glob("*.svg")))
