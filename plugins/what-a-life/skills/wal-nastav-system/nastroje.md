# Mapování destinací na konkrétní nástroje

Referenční příloha ke skillu `wal-nastav-system`. **Otevři ji, až víš, co uživatel používá** — ne dřív. Do rozhovoru z ní ber jen ten jeden nástroj, kterého se to týká.

Zdroj: interní rešerše konektorů, září 2026. Údaje o dostupnosti zastarávají v řádu týdnů — když si nejsi jistý, nech uživatele zkusit, jestli spojení funguje, místo abys tvrdil, že existuje.

---

## Zásada, která platí u všech

**Pět destinací unese skoro každý nástroj.** Projekt jménem ZALOŽ nebo sloupec ZALOŽ na nástěnce funguje všude. Otázka nikdy nezní „vejde se to tam", ale **„jak to tam bude vypadat"** — kolik úrovní, kam přijdou role, jestli existuje odložení bez data.

Takže: **nepřesvědčuj nikoho, aby změnil nástroj.** Vezmi ten, co má, a namapuj na něj metodiku. Nový nástroj navrhuj jen tehdy, když sám řekne, že žádný nemá nebo že mu ten současný nefunguje.

---

## Osobní správci úkolů

### Todoist

*Tvar dat:* projekt → sekce → úkol → podúkol · štítky · priority p1–p4 · **due a deadline zvlášť** · filtry dotazem.

Návrh struktury:

| Destinace | Kam |
|---|---|
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

⚠️ **Notion je past pro toho, kdo si systém rád staví.** Nejčastější výsledek je opuštěná databáze po třech týdnech. Když uživatel Notion nemá a ptá se, co si pořídit, **nedoporučuj mu ho** — doporuč něco, co funguje hned po instalaci. Když ho už má a používá, je to naopak dobrá volba.

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

Jeden zápisník, každá destinace jedna dvoustrana. Funguje. Sběr přes asistenta odpadá, plánování taky — ale zbytek metodiky platí beze změny a týdenní plánování se dá dělat nad papírem stejně dobře.

Nepřemlouvej člověka od papíru k appce. Kdo si systém udrží na papíře, má napůl vyhráno; digitální nástroj mu přidá jen rychlost, ne kázeň.

---

## Když si vybírá nový nástroj

Zeptej se na jedinou věc: **kde to bude nejčastěji otevírat** — mobil, počítač, papír. Pak doporuč **jednu** možnost a řekni proč. Neříkej „záleží na tobě".

Výchozí doporučení, když nic nenapovídá: **Todoist.** Funguje hned, nic se v něm nestaví, má due i deadline, a propojení s asistentem je na jedno kliknutí.
