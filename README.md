# Legends

Enter a ticker and a panel of legendary investors scores it against their own documented playbooks: Buffett, Munger, Lynch, Klarman, Marks, Druckenmiller, Livermore, Burry and 55 more.

Same house style as Meeting Brief, Frontier, Parity and Cadence (white report page, black hairlines, red brand rule, EN / 日本語, light and dark).

## What it shows

- **Snapshot** – last price, 1-year and YTD return, P/E, EV/EBITDA, volatility.
- **One year of price** with 50- and 200-day moving averages.
- **Fundamentals** – operating margin, revenue growth, ROE, dividend yield, distance from the 200-day line, worst 1-year drawdown, 52-week range, next results date.
- **The panel's view** – average fit (0–100), bullish / wait / bearish / out-of-scope tally, and a strip placing each investor by fit.
- **One card per investor** – verdict in that investor's own vocabulary, stance, fit score, one-line thesis, what they would do now, and an expandable checklist (✓ / ✕ / ?) with likes, concerns, invalidation triggers and the data they wanted.
- **Headlines** for the ticker.

Panels: Classic, Value, Growth, Trend, Macro, Skeptics, Asia, Crypto, or any custom pick of up to 10 from all 63.

## How it works

| Piece | Source |
|---|---|
| Market data | Keel connector (`api_comps`, `api_brief`) – OpenBB free public data |
| Investor playbooks | [questflowai/investorskills](https://github.com/questflowai/investorskills) (MIT), embedded in the page |
| Analysis | Claude, one call per investor, via the artifact `sample` capability |

Each investor's `SKILL.md` and `invest.md` go to Claude with the ticker's numbers; Claude judges the stock against that playbook only, takes every figure from the data, and marks criteria that need filings, cash flows or volume as "unclear".

The page runs **inside claude.ai** as an artifact (it needs the `mcp` capability for Keel and the `sample` capability for Claude). Opened anywhere else it shows the labelled example only.

Live artifact: https://claude.ai/artifact/FcHMjHGPMWt27xa1RNGxBz

## Files

```
index.html                 built page (template + embedded skills) – publish this
src/template.html          page source; __SKILLS__ is replaced at build time
data/skills.json           63 investor skills extracted from investorskills
scripts/extract_skills.py  investorskills repo → data/skills.json
scripts/build.py           template + skills → index.html
```

Refresh the playbooks:

```bash
git clone --depth 1 https://github.com/questflowai/investorskills /tmp/investorskills
python3 scripts/extract_skills.py /tmp/investorskills data/skills.json
python3 scripts/build.py
```

## Notes

- Educational analysis, not investment advice. These are documented methods applied by Claude, not the investors' own opinions.
- Data comes from free public sources and can be delayed or wrong.
- Investor playbooks © questflowai, MIT licence.
