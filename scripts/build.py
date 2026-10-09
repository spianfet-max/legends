"""Build index.html from src/template.html and data/skills.json.

Usage:
  python3 scripts/extract_skills.py path/to/investorskills data/skills.json   # refresh skills (optional)
  python3 scripts/build.py                                                     # write index.html
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
skills = json.loads((root / "data/skills.json").read_text(encoding="utf-8"))
for s in skills:
    if s.get("slug") == "grayscale-crypto-sectors" and s.get("cat") == "other":
        s["cat"] = "crypto"
blob = json.dumps(skills, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (root / "src/template.html").read_text(encoding="utf-8").replace("__SKILLS__", blob)
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html written: {len(skills)} investors, {len(html):,} bytes")
