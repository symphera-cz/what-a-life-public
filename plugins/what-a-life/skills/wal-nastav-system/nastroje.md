# Mapování destinací na konkrétní nástroje

Referenční příloha ke skillu `wal-nastav-system`. **Otevři ji, až víš, co uživatel používá** — ne dřív. Do rozhovoru z ní ber jen ten jeden nástroj, kterého se to týká.

Zdroj: interní rešerše konektorů, září 2026. Údaje o dostupnosti zastarávají v řádu týdnů — když si nejsi jistý, nech uživatele zkusit, jestli spojení funguje, místo abys tvrdil, že existuje.

---

## Zásada, která platí u všech

**Schránka a pět destinací unese skoro každý nástroj.** Schránka je v každé tabulce níž první — je to místo, kam padá sběr, a **nikdy se nevynechává**; bez ní se člověk musí rozhodovat ve chvíli, kdy věc zachytává. Projekt jménem ZALOŽ nebo sloupec ZALOŽ na nástěnce funguje všude. Otázka nikdy nezní „vejde se to tam", ale **„jak to tam bude vypadat"** — kolik úrovní, kam přijdou role, jestli existuje odložení bez data.

Takže: **nepřesvědčuj nikoho, aby změnil nástroj.** Vezmi ten, co má, a namapuj na něj metodiku. Nový nástroj navrhuj jen tehdy, když sám řekne, že žádný nemá nebo že mu ten současný nefunguje.

**Role, mise a vize a roční plán nejsou destinace** — dostanou v tom samém nástroji **vlastní místo** vedle té pětice. Nikdy je nedávej do ZALOŽ: ztratily by se mezi věcmi, se kterými se nic nedělá, a přitom je to to jediné, proti čemu se každý týden plánuje. V praxi: vlastní sloupec na nástěnce (Trello, Asana) · vlastní stránka nebo databáze (Notion, Obsidian) · vlastní projekt mimo pětici (Todoist, TickTick, To Do) · vlastní list v tabulce · vlastní oddíl v sešitě. V tabulkách níž je proto uvedená jen pětice destinací; tohle místo přidej vždycky navíc.

---

## Osobní správci úkolů

### Todoist

*Tvar dat:* projekt → sekce → úkol → podúkol · štítky · priority p1–p4 · **due a deadline zvlášť** · filtry dotazem.

Návrh struktury:

| Co | Kam |
|---|---|
| SCHRÁNKA | Inbox (Todoist ho má vestavěný) |
| PRIORITIZUJ | projekt `Udělat` — a hlídej těch deset položek |
| PROJEKT | projekt `Projekty`, jeden úkol = jeden projekt, příští akce jako podúkol |
| DELEGUJ | štítek `@cekam` a uložený filtr |
| ZALOŽ | projekt `Založ` (archiv i „chci někdy, nevím kdy") |
| Role | štítky |

Silné místo: **due a deadline jsou dvě různá pole.** To sedí na rozdíl „kdy se tomu budu věnovat" × „dokdy to musí být". Málokterý nástroj to umí — nabídni to.

### TickTick

Skoro totéž co Todoist: seznam → úkol → podúkol, tagy, priority. Navíc umí návyky a série — když si uživatel zavádí návyk, nemusí na to zvláštní aplikaci.

### Microsoft To Do

*Tvar dat:* seznam → úkol → krok · kategorie (barvy) · **bez hierarchie projektů**.

Destinace jako seznamy, role jako kategorie. Projekty jsou slabina — nemá pro ně úroveň, takže projekt = úkol s kroky. U složitějších projektů to nestačí; řekni to rovnou a nabídni, ať projekty žijí jinde.

⚠️ **Oficiální konektor Microsoft 365 To Do ani Planner nepokrývá** — kryje SharePoint, OneDrive, Outlook a Teams. Kdo chce, aby mu asistent zapisoval do To Do, potřebuje samostatné propojení. Neslibuj, že to půjde, dokud si to uživatel neověří.

### Google Tasks

*Tvar dat:* seznam → úkol → jedna úroveň podúkolů · datum · **bez štítků**.

Nejchudší z celé skupiny. Bez štítků nemáš kam dát role. Použitelné jako čistý seznam PRIORITIZUJ vedle kalendáře, ne jako celý systém. Oficiální Workspace konektor v Claude kryje Gmail, Kalendář a Disk — Tasks nejspíš ne; ať si to uživatel ověří.

### Apple Reminders

Seznamy → připomínky → podpoložky, tagy, chytré seznamy. Struktura stačí. Propojení s asistentem jde jen přes zapnutý Mac — na mobilu z konverzace nedosáhneš. Pro většinu lidí tedy sběr přes asistenta nefunguje.

### Things 3, OmniFocus

**K asistentovi je nepřipojíš.** Mimo Mac nemají veřejné API. Když je uživatel používá a je s nimi spokojený, **neber mu je** — jen mu řekni na rovinu, že sběr bude muset dělat sám a asistent do nich nevidí.

Stojí za zmínku, že jejich model je metodice nejblíž ze všech: Things má **Někdy**, což je přesně ZALOŽ; OmniFocus má **defer date**, tedy odložení bez termínu. Když někdo přechází od nich, hledej v novém nástroji náhradu za tyhle dvě věci.

---

## Kanban

### Trello

*Tvar dat:* workspace → nástěnka → seznam → karta → checklist · štítky · termín · členové.

Návrh struktury — **jedna nástěnka**, seznamy:

`Inbox · Udělat · Probíhá · Čekám na · Založ · Hotovo`

Projekty jako karty, kroky jako checklist v kartě, role jako štítky. Roční plán jako další seznam.

⚠️ **Kalendářový pohled je Premium.** Bez placeného Trella **nezkoušej v něm zakládat události ani plánovat bloky** — nepůjde to. Termíny na kartách fungují i zdarma, bloky patří do kalendáře. Zeptej se rovnou: *„Máš Trello placené, nebo zdarma?"*

⚠️ **Jedno propojení pokryje jeden workspace.** Kdo má pracovní a soukromou nástěnku v různých workspace, uvidí přes asistenta jen jednu. Když má dva světy, ať jsou obě nástěnky v jednom workspace — nebo ať počítá s tím, že druhý bude ručně.

### Asana, ClickUp, monday

Bohatší struktura než Trello: mají sekce, vlastní pole a u ClickUpu i vlastní stavy. Destinace se dají udělat jako stavy místo sloupců, což je čistší. Zeptej se, jak se tomu v jeho nástroji říká, a použij jeho slova.

### Jira, Linear

Firemní a vývojářské. Pro osobní life management je nepoužívej, i když je člověk zná z práce — model epic/issue/sprint táhne k jinému uvažování než metodika. Když v nich někdo trvá na tom mít i osobní věci, je to signál, že mu splývá práce a soukromí; zmiň to jednou.

---

## Databáze

### Notion

*Tvar dat:* databáze → stránka → typované vlastnosti · **pohledy místo seznamů** · relace mezi databázemi.

Návrh: **jedna databáze**, vlastnosti `Destinace`, `Role`, `Projekt`, `Termín`. Destinace nejsou složky, jsou to pohledy — filtr na hodnotu. Roční plán jako samostatná stránka.

⚠️ **Notion je past pro toho, kdo si systém rád staví.** Nejčastější výsledek je opuštěná databáze po třech týdnech.

Proto platí: **Notion doporučuj, ale strukturu v něm postav ty.** Nikdy neposílej člověka, ať si ji navrhne sám — ukaž hotový návrh, nech si ho odsouhlasit a založ ho. Když si o něm začne povídat jako o projektu („a co kdybych si tam ještě přidal…"), zastav to jednou větou: *„Nech to takhle měsíc. Až uvidíš, co ti chybí, doděláme to."*

Návrh při zakládání od nuly: **jedna stránka `Život`** a v ní **databáze** s vlastností `Destinace` — schránka a pět destinací jako hodnoty, ne jako podstránky. Podstránky vypadají jednodušeji, ale nejde v nich nic filtrovat ani přesouvat mezi destinacemi. Vedle databáze jedna stránka na role, misi a vize a jedna na roční plán.

### Airtable

Silná evidence, ale jako denní to-do to nikdo dlouho nevydrží. Použitelné na roční plán a přehledy, ne na PRIORITIZUJ.

### Obsidian

Složky a `.md` soubory, frontmatter, tagy, odkazy. Pro asistenta ideální tvar dat, pro netechnického uživatele odrazující, a dosáhne na něj jen přes zapnutý počítač. Doporučuj jen tomu, kdo v něm už žije.

---

## Kalendář-first plánovače

Akiflow, Sunsama, Motion. Sbírají úkoly z ostatních nástrojů a nutí je položit na kalendář — řeší tedy přesně tu díru, kterou seznam úkolů z principu neřeší: **seznam neví, kolik máš času.**

⚠️ **Pořadí.** Na „nestíhám" odpovídá metodika posterioritami a velkými kameny, ne nákupem plánovače. Tuhle kategorii nabízej až tomu, kdo priority srovnané má a pořád mu nevycházejí hodiny. Jinak si za peníze koupí lepší evidenci téhož problému.

---

## Papír

**Papír nikdy nenabízej ani nedoporučuj** — ani jako jednu z možností, ani jako otázku *„nebo radši papír?"*. Sběr přes asistenta na něm nefunguje, zápis taky ne, a člověk, který si přišel systém zdigitalizovat, dostane krok zpátky.

Když si o něj řekne sám, respektuj to a neodmlouvej: jeden zápisník, každá destinace jedna dvoustrana, týdenní plánování nad papírem funguje stejně dobře. Jen mu rovnou řekni, co tím ztrácí — nic ti nepůjde zapsat a nic ti nepřečtu.

---

## Když nemá nic a vybírá nový nástroj

Zeptej se na jedinou věc: **kde to bude nejčastěji otevírat** — mobil, nebo počítač. Pak doporuč **jednu** možnost a řekni proč. Nevypisuj katalog a neříkej „záleží na tobě".

**Výchozí doporučení: Notion.** Jediný, jehož free plán metodiku nijak neomezuje — neomezené stránky, jeden nástroj na destinace, roli, misi i roční plán, a asistent do něj umí zapisovat.

Kdy jinak:

| Situace | Nástroj | Proč |
|---|---|---|
| chce jen úkoly, žádnou ceremonii | **TickTick** | jednoduché, navíc umí návyky (free: 9 seznamů, 99 úkolů na seznam) |
| myslí vizuálně, chce nástěnku | **Trello** | sloupce a tažení myší; **řekni dopředu, že asistent neumí mazat, jen archivovat** — týká se destinace ZAHOĎ |
| firma jede na Atlassianu | **Confluence + Jira** | role a mise do Confluence, projekty do Jiry; nic navíc neplatí |
| kalendář | **Google Kalendář** | pro každého, kdo nemá Outlook: plný zápis, zdarma |

⚠️ **Todoist nedoporučuj někomu, kdo začíná.** Free plán má jen **pět aktivních projektů** — na pět destinací plus roli už to nevyjde. Když ho někdo používá a je spokojený, nech ho u něj a řekni mu, že destinace bude muset sloučit pod štítky, nebo si připlatit.

⚠️ **Než něco slíbíš o zápisu**, ověř tři věci: má **placený plán AI** (na free účtu webové konektory nejsou) · **oprávnění se dávají po částech**, takže bez povoleného zápisu to neprojde · **nic se nespustí samo** — týdenní rituál musí zahájit člověk.
