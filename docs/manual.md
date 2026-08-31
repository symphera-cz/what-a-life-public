# Manuál — jak si nastavit svého asistenta

Metodiku What a Life! už znáte ze školení. Tenhle návod vám ji pomůže **používat každý den**, aniž byste si museli cokoli pamatovat.

Zabere to **20 minut**. Pak už jen mluvíte normálně a asistent pozná, co je potřeba.

---

## Co to bude umět

Řeknete *„mám plnou hlavu"* — a asistent vás provede vysypáním hlavy po oblastech.
Vložíte seznam věcí — roztřídí je do **sedmi destinací**, které máte na plakátu.
Řeknete *„nemůžu se do toho pustit"* — najde s vámi první krok.
Řeknete *„přistálo mi tohle a nemám čas"* — napíše tři varianty **konstruktivního Ano**.

Nic si nepamatujete, nic nekopírujete. Jen mluvíte.

## K čemu má přístup

**Nic k vašim datům si sám nepřipojí.** Jestli asistent uvidí váš kalendář, maily nebo úkoly, si nastavujete vy u svého poskytovatele AI. My do toho nevstupujeme a ani nemůžeme.

**Když ten přístup má, ať ho využije.** Zapsat úkol rovnou do vašeho seznamu je přesně to, o co jde — čím míň přepisování, tím spíš vám systém vydrží. Pravidlo není „nezapisuj", ale **ukaž návrh, počkej na potvrzení, pak zapiš**. Co přesně smí dělat sám, si zvolíte při nastavování systému.

**Co nedělá:** neposílá notifikace a nepřipomíná se. Systém, který vás upomíná, si za tři týdny ztlumíte. Blok na review si dáváte do kalendáře sami.

---

## A · Claude — doporučená cesta

Funguje nejlíp: instalace na pár kliknutí, bez admina, a **skills fungují i v mobilní aplikaci** (jen se v ní nedají instalovat — to udělejte na počítači).

### 1. Nainstalujte plugin *(3 minuty, jednorázově)*

1. Otevřete **claude.ai** na počítači.
2. Vlevo dole **Customize → Plugins**.
3. **„+" → Add marketplace** a vložte odkaz na repozitář, který jste dostali.
4. Najděte plugin **what-a-life** a nainstalujte ho.

Tím máte všech jedenáct workflow naráz. Když se něco zlepší, dostanete to automaticky.

> Nedostanete-li se k repozitáři, jde to i po jednom: **Customize → Skills → + → Upload a skill**, a nahrát jedenáct ZIPů ze složky `dist/`. Aktualizace pak ale musíte dělat ručně.

### 2. Založte projekt *(5 minut)*

1. **Projects → + Create project**, pojmenujte třeba „Můj systém".
2. Otevřete **Set project instructions**.
3. Vložte celý obsah souboru **`instructions/01-agent.md`**.

### 3. Nechte si nastavit systém *(15 minut, to nejdůležitější)*

Napište do projektu: **„Pojďme nastavit systém."**

Asistent se vás zeptá, co používáte — kam vám padají věci, v čem máte úkoly, jaký kalendář — a navrhne, jak v tom postavit sedm destinací z metodiky. Funguje to s Trellem, Todoistem, Notionem, Outlookem i papírovým zápisníkem; metodika žádný nástroj nepředepisuje.

Na konci vám **vypíše text vaší nástrojové vrstvy**. Ten zkopírujte a vložte v projektu **pod** instrukce ze druhého kroku.

> Nevyplňujete žádnou šablonu. Vzniká to z rozhovoru, protože u každého to vypadá jinak. Až budete někdy měnit nástroj, řeknete si o to znovu a vyměníte jen tenhle jeden text.

### 4. Vyzkoušejte

Napište: **„Mám plnou hlavu, potřebuju to dostat ven."**
Mělo by se spustit vedené vysypání hlavy. Když se nespustí, viz Potíže níže.

---

## B · ChatGPT

Plugin sem nejde — je to formát Claude. Ale celý balíček máte v jednom souboru, takže o nic nepřijdete.

1. **Projects → nový projekt.**
2. Mezi soubory projektu nahrajte **`dist/wal-balicek-jeden-soubor.md`**. Jsou v něm pravidla i všech jedenáct postupů.
3. Do *Instructions* vložte jen tohle:

   > Řídím se metodikou What a Life! Kompletní pravidla i všechny postupy máš v přiloženém souboru `wal-balicek-jeden-soubor.md`. Než odpovíš, podívej se do něj — část A jsou pravidla, která platí pořád, část B jsou postupy pro konkrétní situace. Sám poznej, který postup se hodí, a řiď se jím. Nikdy mi nevypisuj seznam postupů a nečekej, až si o některý řeknu jménem.

4. Pak pokračujte třetím krokem cesty A — *„pojďme nastavit systém"* — a výslednou nástrojovou vrstvu přidejte do Instructions.

Rozpoznávání situace je tu o něco slabší než na Claude. Když asistent postup nenajde sám, stačí říct „podívej se do toho souboru".

---

## C · Microsoft 365 Copilot

Copilot **neumožňuje běžnému uživateli instalovat vlastní workflow** — jde to jen přes firemní IT. Zbývá vkládání textu.

1. Otevřete Copilot Chat.
2. Na začátek konverzace vložte obsah **`dist/wal-balicek-jeden-soubor.md`**.
3. **Pokračujte v téže konverzaci** — jakmile ji zavřete, kontext se ztratí a musíte ho vložit znovu.

Nepohodlné, ale funkční, a máte celý balíček. Pokud máte i soukromý účet Claude nebo ChatGPT, použijte radši ten — ale **jen na soukromá data**.

### Kam patří jaká data

| | Kam |
|---|---|
| **Pracovní obsah** | jen do nástroje schváleného zaměstnavatelem (typicky firemní Copilot) |
| **Soukromé věci** | soukromý účet Claude / ChatGPT |
| **Nejste si jistí?** | zeptejte se svého IT — pravidla se firma od firmy liší |

Do soukromé AI nevkládejte jména klientů, čísla ani interní informace. Nahraďte je zástupnými — na kvalitu odpovědi to nemá vliv.

---

## Prvních třicet minut

Až budete hotoví, doporučuji tohle pořadí — je to zároveň nejrychlejší způsob, jak si systém postavit:

1. **„Mám plnou hlavu."** → vysypání hlavy, ~20 minut. Nespěchejte, projděte všech šest oblastí.
2. Výstup rovnou pošlete dál: **„Roztřiď mi to."** → sedm destinací.
3. **„Pojďme naplánovat týden."** → balvany do kalendáře.
4. **Založte si v kalendáři blok na týdenní review.** Pátek nebo neděle, 15 minut, opakovaně.

Ten čtvrtý krok je nejdůležitější a nejčastěji se vynechá. Asistent vám ho nepřipomene — schválně. *Priorita, která nemá blok v kalendáři, je jen zbožné přání.*

---

## Potíže

**Workflow se nespustilo.**
Zkontrolujte, že je v Customize → Skills zapnuté. Pak zkuste říct věc konkrétněji: místo „pomoz mi" zkuste „mám plnou hlavu" nebo „roztřiď mi tyhle věci".

**Spustilo se něco, co jsem nechtěl.**
Řekněte „to ne, chci jen odpověď". Když se to opakuje u téhož workflow, dejte vědět — popis se dá zúžit.

**Asistent radí něco jiného, než jsme se učili.**
Napište to. Buď je chyba v instrukcích, nebo je to místo, kde metodika sama mlčí — obojí potřebujeme vědět.

**Na mobilu nevidím Customize.**
Správně — instalace jde jen z počítače. Jakmile jsou workflow nahraná, **na mobilu fungují**.

**Nechci vyplňovat nástrojovou vrstvu.**
Nemusíte. Asistent se zeptá, když bude potřebovat vědět, kam co ukládáte.

---

## Časté otázky

**Uvidí někdo, co si s asistentem píšu?**
Ne. Běží to na vašem účtu. Symphera k tomu nemá přístup.

**Musím používat Trello / Outlook / cokoli konkrétního?**
Ne. Metodika je nástrojově agnostická a asistent taky. Vyplníte, co používáte.

**Co když nemám žádný nástroj a chci začít papírem?**
Funguje. Do nástrojové vrstvy napište „papírový zápisník" a asistent s tím bude počítat — bude vám dávat výstupy tak, aby se daly opsat.

**Můžu si to upravit?**
Ano, je to váš text. Jen počítejte s tím, že když změníte názvy destinací, přestane to sedět s plakátem i s tím, co jste slyšeli na sále.

---

© Symphera s.r.o. · metodika What a Life! — Martin Klusoň
