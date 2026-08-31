# What a Life! — AI agent

Digitální podpora pro aplikaci metodiky **What a Life!** (Symphera, autor Martin Klusoň).
Jedenáct workflow, které si AI asistent volá sám, když pozná situaci — nic nekopírujete a nemusíte si pamatovat příkazy.

Určeno především **absolventům školení**. Bez kurzu to funguje taky, ale metodika je tu jen ve zkratce.

---

## Co to umí

Řeknete *„mám plnou hlavu"* — asistent vás provede vysypáním hlavy po oblastech.
Vložíte seznam věcí — roztřídí je do **sedmi destinací**.
Řeknete *„nemůžu se do toho pustit"* — najde s vámi první krok.
Řeknete *„přistálo mi tohle a nemám čas"* — napíše tři varianty **konstruktivního Ano**.

## K čemu má přístup

**Plugin sám nepřidává žádné připojení k vašim datům.** Jestli asistent uvidí váš kalendář, maily nebo úkoly, si nastavujete vy u svého poskytovatele AI — konektory, integrace, firemní politika. My do toho nevstupujeme.

**Když ten přístup má, ať ho používá.** Zapsat úkol rovnou do vašeho seznamu je přesně to, o co jde — čím míň přepisování a překlikávání, tím spíš vám systém vydrží. Pravidlo není „nezapisuj", ale **ukaž návrh, počkej na potvrzení, pak zapiš**.

Co si nastavíte, patří do vaší **nástrojové vrstvy** — je tam k tomu sekce „Co smí agent sám". Výchozí je opatrná varianta, ale je to vaše volba, ne naše.

**Co nedělá:** neposílá notifikace a nepřipomíná se. Systém, který vás upomíná, si za tři týdny ztlumíte. Blok na review si dáváte do kalendáře sami — metodika ostatně učí, že priorita bez bloku je jen zbožné přání.

## Instalace

**→ [`docs/manual.md`](docs/manual.md)** — návod krok za krokem pro Claude, ChatGPT i Copilot.

Nejkratší cesta (Claude):

1. **Customize → Plugins → „+" → Add marketplace**, vložte URL tohoto repozitáře.
2. Nainstalujte plugin **what-a-life**.
3. Založte projekt a vložte [`instructions/01-agent.md`](instructions/01-agent.md) do *Project instructions*.
4. Napište **„pojďme nastavit systém"**.

Ve čtvrtém kroku s vámi asistent projde vaše nástroje, navrhne strukturu a vypíše vaši osobní **nástrojovou vrstvu** — tu vložíte do instrukcí pod tu první. Nevyplňujete žádnou šablonu; vzniká to z rozhovoru, protože u každého to vypadá jinak: Trello, Todoist, Notion, Outlook To Do nebo papírový zápisník. Metodika žádný nástroj nepředepisuje.

Kdo se k marketplace nedostane, najde hotové ZIPy jednotlivých skills ve složce [`dist/`](dist) — **Customize → Skills → Upload**.

### ChatGPT a M365 Copilot

Plugin je Claude formát, jinam nejde. Pro ostatní platformy je celý balíček složený **do jednoho souboru**: [`dist/wal-balicek-jeden-soubor.md`](dist/wal-balicek-jeden-soubor.md) — pravidla i všech jedenáct postupů pohromadě.

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
| `wal-naplanuj-tyden` | PLAN AND DO IT | „pojďme naplánovat týden" |
| `wal-tydenni-review` | review napříč | „pojďme na review", „jak jsem na tom" |
| `wal-navyk` | MAKE IT A HABIT | „chci si zavést návyk", „nedaří se mi vydržet" |
| `wal-energie` | HAVE ENERGY FOR IT | „jsem vyčerpaný", „nemám energii" |
| `wal-role-a-vize` | DREAM IT | „chci si projít role", „nesedí mi nastavení" |

Blok **BELIEVE IT** workflow nemá záměrně — je to práce s postojem, ne s informací.

## Tři vrstvy

| Vrstva | Co obsahuje | Kde je |
|---|---|---|
| **1 · Metodika** | destinace, testy, pravidla | [`docs/metodika.md`](docs/metodika.md) |
| **2 · Instrukce agenta** | jak agent uvažuje a mluví | [`instructions/01-agent.md`](instructions/01-agent.md) |
| **3 · Nástrojová vrstva** | vaše boardy, seznamy, štítky | vznikne v rozhovoru, kostra v [`instructions/02-`](instructions/02-nastrojova-vrstva.md) |

Instrukce popisují **proces**, nástrojová vrstva popisuje **úložiště**. Když změníte nástroj, mění se jen vrstva 3.

## Co tady není

Tenhle repozitář obsahuje **operativní vrstvu** metodiky — to, co potřebuje asistent, aby mluvil stejným jazykem jako školení.

Výklad, příběhy, cvičení vedená lektorem a školicí materiály **součástí nejsou**. Ty patří ke kurzu. Pokud jste školením prošli, držte se materiálů ze sálu — tohle je jejich zkratka, ne náhrada.

## Licence a použití

Metodika What a Life! je duševní vlastnictví **Symphera s.r.o.** Obsah tohoto repozitáře je zveřejněn pro osobní použití absolventů a zájemců o metodiku.

Není dovoleno jej používat pro komerční školení, přeprodej ani odvozené kurzy bez souhlasu Symphery.

---

© Symphera s.r.o. · metodika What a Life! — Martin Klusoň · [symphera.com](https://symphera.com)
