#!/usr/bin/env python3
"""
Složí instrukce agenta + všech 10 workflow do jednoho souboru pro platformy,
které neumí Claude pluginy (ChatGPT Projects, M365 Copilot).

Spuštění z kořene repa:  python build/make-onefile.py
Výstup:                  dist/wal-balicek-jeden-soubor.md
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "what-a-life" / "skills"
AGENT = ROOT / "instructions" / "01-agent.md"
OUT = ROOT / "dist" / "wal-balicek-jeden-soubor.md"

# pořadí podle toho, jak se to používá, ne abecedně
ORDER = [
    "wal-nastav-system",
    "wal-role-a-vize",
    "wal-vysyp-hlavu",
    "wal-protrid-schranku",
    "wal-rozpad-projektu",
    "wal-prioritizuj",
    "wal-konstruktivni-ano",
    "wal-naplanuj-tyden",
    "wal-navyk",
    "wal-energie",
]

HEADER = """# What a Life! — kompletní balíček v jednom souboru

Tenhle soubor je pro platformy, které neumí Claude pluginy — **ChatGPT Projects** a **M365 Copilot**.
Na Claude ho nepotřebuješ, tam se instaluje plugin.

## Jak ho použít

**ChatGPT:** Projects → nový projekt → nahraj tenhle soubor mezi soubory projektu.
Do *Instructions* vlož jen tohle:

> Řídím se metodikou What a Life! Kompletní pravidla i všechny postupy máš v přiloženém souboru
> `wal-balicek-jeden-soubor.md`. Než odpovíš, podívej se do něj — část A jsou pravidla, která platí
> pořád, část B jsou postupy pro konkrétní situace. Sám poznej, který postup se hodí, a řiď se jím.
> Nikdy mi nevypisuj seznam postupů a nečekej, až si o některý řeknu jménem.

**M365 Copilot:** vlož celý obsah tohoto souboru na začátek konverzace a pokračuj v ní.
Jakmile konverzaci zavřeš, kontext se ztratí.

---

## Obsah

**ČÁST A — pravidla, která platí pořád**

**ČÁST B — postupy pro konkrétní situace**

"""


def strip_frontmatter(text):
    """Odstraní YAML frontmatter a vrátí (description, telo)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return "", text
    fm = m.group(1)
    body = text[m.end():]
    d = re.search(r"^description:\s*(.+?)(?=\n\w+:|\Z)", fm, re.S | re.M)
    desc = " ".join(d.group(1).split()) if d else ""
    return desc, body


def demote_headings(text):
    """Posune nadpisy o úroveň níž. Uvnitř bloků kódu nesahá na nic."""
    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and re.match(r"^#{1,5}\s", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def main():
    parts = [HEADER]

    # obsah
    toc = []
    for i, name in enumerate(ORDER, 1):
        p = SKILLS / name / "SKILL.md"
        if not p.exists():
            print(f"  ! chybi {name}")
            continue
        title = re.search(r"^#\s+(.+)$", p.read_text(encoding="utf-8"), re.M)
        toc.append(f"{i}. **{title.group(1) if title else name}** (`{name}`)")
    parts.append("\n".join(toc) + "\n\n---\n\n")

    # část A
    agent = AGENT.read_text(encoding="utf-8")
    agent = re.sub(r"^# .+?\n", "", agent, count=1)
    agent = re.sub(r"^\*\*Vrstva 2\.\*\*.*?\n---\n", "", agent, flags=re.S)
    parts.append("# ČÁST A — pravidla, která platí pořád\n\n" + agent.strip() + "\n\n---\n\n")

    # část B
    parts.append("# ČÁST B — postupy pro konkrétní situace\n\n")
    parts.append(
        "Každý postup má u sebe **Kdy použít**. Podle toho poznáš, který se hodí. "
        "Použij vždycky jen jeden naráz.\n\n"
    )

    for name in ORDER:
        p = SKILLS / name / "SKILL.md"
        if not p.exists():
            continue
        desc, body = strip_frontmatter(p.read_text(encoding="utf-8"))
        body = demote_headings(body)
        # Odkazy na přílohy tady nedávají smysl — soubory se vkládají rovnou pod skill.
        body = re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]+\.md\)", r"\1", body)
        body = body.replace("otevři si `nastroje.md`", "použij tabulky níž")
        parts.append(f"\n---\n\n<a id=\"{name}\"></a>\n\n")
        parts.append(body.strip() + "\n")

        # Přílohy skillu — v pluginu si je agent otevře sám, tady musí být v textu,
        # jinak by odkaz vedl na soubor, který v ChatGPT ani Copilotu neexistuje.
        for extra in sorted(p.parent.glob("*.md")):
            if extra.name == "SKILL.md":
                continue
            _, ebody = strip_frontmatter(extra.read_text(encoding="utf-8"))
            parts.append("\n" + demote_headings(demote_headings(ebody)).strip() + "\n")
            print(f"     + priloha {name}/{extra.name}")

        parts.append(f"\n**Kdy použít:** {desc}\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("".join(parts), encoding="utf-8")
    words = len("".join(parts).split())
    print(f"OK  {OUT.relative_to(ROOT)}  ({words} slov, {OUT.stat().st_size // 1024} kB)")


if __name__ == "__main__":
    main()
