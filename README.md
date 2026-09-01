# What a Life! — AI agent

Digitální podpora pro aplikaci metodiky **What a Life!** (Symphera, autor Martin Klusoň).
Deset workflow, které si AI asistent volá sám, když pozná situaci — nic nekopírujete a nemusíte si pamatovat příkazy.

Určeno především **absolventům školení**. Bez kurzu to funguje taky, ale metodika je tu jen ve zkratce.

---

## Co to umí

Řeknete *„mám plnou hlavu"* — asistent vás provede vysypáním hlavy po oblastech.
Vložíte seznam věcí — roztřídí je do **sedmi destinací**.
Řeknete *„nemůžu se do toho pustit"* — najde s vámi první krok.
Řeknete *„přistálo mi tohle a nemám čas"* — napíše tři varianty **konstruktivního Ano**.

## K čemu má přístup

**Plugin sám nepřidává žádné připojení k vašim datům.** Jestli asistent uvidí váš kalendář, maily nebo úkoly, si nastavujete vy u svého poskytovatele AI — konektory, integrace, firemní politika. My do toho nevstupujeme.

**Když ten přístup má, ať ho používá.** Zapsat úkol rovnou do vašeho seznamu je přesně to, o co jde — čím míň přepisování a překlikávání, tím spíš vám systém vydrží.

Platí přitom rozdíl, na kterém stojí použitelnost celého systému: **co jen odhodíte, zapíše rovnou a neptá se.** Nadiktujete větu, zamknete telefon a je to uložené. **Rozhodnutí vám ale nejdřív ukáže** — kam to patří, jakou to má prioritu, kdy na to bude blok. A do kalendáře nezaloží nikdy nic tiše.

Co si nastavíte, patří do vaší **nástrojové vrstvy** — je tam k tomu sekce „Co smí agent sám". Výchozí je opatrná varianta, ale je to vaše volba, ne naše.

**Co nedělá:** neposílá notifikace a nepřipomíná se. Systém, který vás upomíná, si za tři týdny ztlumíte. Blok na plánování si dáváte do kalendáře sami — metodika ostatně učí, že priorita bez bloku je jen zbožné přání.

## Instalace

**Nejjednodušší je nechat se provést.** V e-mailu po školení máte text, který vložíte do prázdné konverzace s asistentem — provede vás nastavením krok za krokem a poradí, když nějaké tlačítko nenajdete.

Psané návody, kdybyste je chtěli:

- **→ [`docs/navod-claude.md`](docs/navod-claude.md)**
- **→ [`docs/navod-chatgpt.md`](docs/navod-chatgpt.md)**

### Ve zkratce, když si to chcete udělat sami

1. V Claude přidejte tenhle repozitář jako zdroj pluginů a nainstalujte **what-a-life**.
2. Ověřte v **Customize → Skills**, že přibylo deset položek `wal-` a jsou zapnuté.
3. Založte projekt a do **Set project instructions** vložte celý obsah tohohle souboru:

   ## 📄 **[`instructions/01-agent.md`](instructions/01-agent.md)** ← tohle se vkládá do projektu

   *Otevřete odkaz, klikněte vpravo nahoře na **Raw** a zkopírujte všechno.*

4. Napište **„pojďme nastavit systém"**. Asistent s vámi projde vaše nástroje a na konci vypíše hotový text — ten pak **nahradí** to, co jste vložili v kroku 3. Nic nepřilepujete na konec a nevyplňujete žádnou šablonu.

**Aktualizace se nestahují samy.** Když vyjde novější verze, klikněte v **Customize → Plugins** na **Update** — jinak vám dál běží ta, kterou jste nainstalovali, a nijak se to nepozná. Na novou verzi vás upozorníme e‑mailem.

### Ještě jedna věc, než začnete: „povolit vždy"

Až asistent poprvé něco zapíše do vašeho seznamu úkolů, zeptá se, jestli smí. **Nemačkejte „povolit jednou"** — zvolte **„povolit vždy"**. Jinak se vás to bude ptát pokaždé a za týden to vzdáte.

Zeptá se víckrát: založit úkol, upravit ho a odškrtnout jsou tři různé věci. Pár dní to občas vyskočí, pak už ne.

Jestli to funguje, ověříte za minutu: řekněte *„založ úkol Zkouška zápisu"*, zamkněte telefon, chvíli počkejte a pak se podívejte **do svého nástroje, ne do konverzace.**

Kdo se k marketplace nedostane, najde hotové ZIPy jednotlivých skills ve složce [`dist/`](dist) — **Customize → Skills → Upload**. Ve stejné složce je i [`rocni-plan-template.xlsx`](dist/rocni-plan-template.xlsx).

### ChatGPT a M365 Copilot

Plugin je Claude formát, jinam nejde. Pro ostatní platformy je celý balíček složený **do jednoho souboru**: [`dist/wal-balicek-jeden-soubor.md`](dist/wal-balicek-jeden-soubor.md) — pravidla i všech deset postupů pohromadě.

- **ChatGPT** — nahrajte ten soubor mezi soubory projektu a do *Instructions* dejte krátký odkaz na něj (přesné znění je v hlavičce souboru). Asistent si v něm postup najde sám.
- **Copilot** — vložte obsah souboru na začátek konverzace a pokračujte v ní.

Automatické rozpoznání situace je tam slabší než u pluginu na Claude, ale balíček zůstává celý.

## Workflow

| Skill | Blok metodiky | Spustí se, když… |
|---|---|---|
| `wal-nastav-system` | napříč | „pojďme nastavit systém", měníte nástroj |
| `wal-vysyp-hlavu` | COLLECT IT | „mám plnou hlavu", „něco mi uniká" |
| `wal-protrid-schranku` | ORGANIZE IT | vložíte seznam věcí nebo předmětů mailů |
| `wal-rozpad-projektu` | ORGANIZE IT | „nemůžu se do toho pustit", „pořád to odkládám" |
| `wal-prioritizuj` | PRIORITIZE IT | „nevím, co dřív", „všechno hoří" |
| `wal-konstruktivni-ano` | PRIORITIZE IT | „přistálo mi tohle a nemám čas" |
| `wal-naplanuj-tyden` | PLAN IT | „pojďme naplánovat týden", „chci roční plán" |
| `wal-navyk` | MAKE IT A HABIT | „chci si zavést návyk", „nedaří se mi vydržet" |
| `wal-energie` | HAVE ENERGY FOR IT | „jsem vyčerpaný", „nemám energii" |
| `wal-role-a-vize` | DREAM IT | „chci si projít role", „nesedí mi nastavení" |

Blok **OWN IT** workflow nemá záměrně — je to práce s postojem, ne s informací. Projevuje se v tom, jak agent mluví.

## Tři vrstvy

| Vrstva | Co obsahuje | Kde je |
|---|---|---|
| **1 · Glosář** | názvy bloků, destinací a pojmů | [`docs/metodika.md`](docs/metodika.md) |
| **2 · Instrukce agenta** | jak agent uvažuje a mluví | [`instructions/01-agent.md`](instructions/01-agent.md) |
| **3 · Nástrojová vrstva** | vaše boardy, seznamy, štítky | vznikne v rozhovoru, kostra v [`instructions/02-`](instructions/02-nastrojova-vrstva.md) |

Instrukce popisují **proces**, nástrojová vrstva popisuje **úložiště**. Když změníte nástroj, mění se jen vrstva 3.

## Co tady není

Tenhle repozitář obsahuje **operativní vrstvu** metodiky — to, co potřebuje asistent, aby mluvil stejným jazykem jako školení.

Výklad, příběhy, cvičení vedená lektorem a školicí materiály **součástí nejsou**. Ty patří ke kurzu. Pokud jste školením prošli, držte se materiálů z kurzu — tohle je jejich zkratka, ne náhrada.

## Licence a použití

Metodika What a Life! je duševní vlastnictví **Symphera s.r.o.** Obsah tohoto repozitáře je zveřejněn pro osobní použití absolventů a zájemců o metodiku.

Není dovoleno jej používat pro komerční školení, přeprodej ani odvozené kurzy bez souhlasu Symphery.

---

© Symphera s.r.o. · metodika What a Life! — Martin Klusoň · [symphera.com](https://symphera.com)
