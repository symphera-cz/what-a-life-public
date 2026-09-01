# Jak si nastavit asistenta — Claude

Metodiku už znáte ze školení. Tenhle návod z ní udělá něco, co používáte každý den, aniž byste si museli cokoli pamatovat.

Je to **jedno odpoledne rozdělené na kousky**: nastavení zabere pár minut, projít si s asistentem role a vysypat hlavu je práce na hodinu až dvě. Nemusíte to dělat naráz.

> **Potřebujete placeného Claude** (Pro, Max, Team nebo Enterprise) a **počítač** — na mobilu se instalovat nedá. Jakmile to jednou nastavíte, na mobilu to funguje normálně.

---

## Nejjednodušší cesta: nechte se provést

Nemusíte tenhle návod číst celý. Otevřete Claude, vložte do konverzace **instalační prompt** z e-mailu, který jste dostali, a asistent vás instalací provede krok za krokem — zeptá se, co vidíte na obrazovce, a poradí, když se něco liší.

Zbytek téhle stránky je pro případ, že si to chcete udělat sami nebo se někde zaseknete.

---

## 1 · Přidat plugin

Plugin je balíček, který Claudovi přidá deset postupů z našeho školení. Sám o sobě se nikam nepřipojuje a nic o vás neví.

1. Otevřete **claude.ai** na počítači a přihlaste se.
2. Vlevo dole klikněte na **Customize**, pak na záložku **Plugins**.
3. V sekci osobních pluginů klikněte na **„+"** a vyberte **Add marketplace**.
4. Do políčka vložte **adresu, kterou máte v e-mailu**. Je to dlouhý řetězec začínající `https://github.com/` — nemusíte vědět, co je na druhé straně, jen ho vložte celý.
5. Najděte plugin **what-a-life** a klikněte na **Install**.

**Zkontrolujte, že je zapnutý.** V **Customize → Skills** by mělo přibýt deset položek začínajících `wal-`. Když tam nejsou nebo jsou vypnuté, zapněte je — jinak se nic nespustí.

> **Nevidíte Customize?** Buď máte bezplatný účet, nebo vám to zakázal firemní správce. V obou případech použijte [náhradní cestu bez pluginu](#nahradni-cesta-bez-pluginu) níž, funguje stejně dobře.

## 2 · Založit projekt a vložit instrukce

1. Vlevo **Projects → Create project**. Pojmenujte ho třeba **Můj systém**.
2. V projektu otevřete **Set project instructions** *(česky „Upravit instrukce")*.
3. Vložte tam text **instrukcí agenta**, který máte v e-mailu jako přílohu.

To je jediné, co budete kopírovat ručně.

## 3 · Nechat si nastavit systém

Napište do projektu: **„Pojďme nastavit systém."**

Asistent se zeptá, kam si odhazujete nápady, v čem máte úkoly a jaký používáte kalendář, a navrhne, jak v tom postavit sedm destinací. Funguje to s Trellem, Todoistem, Notionem, Outlookem i s papírovým zápisníkem.

Na konci vám **vypíše hotový text** a řekne, kam ho vložit. Bude to zpátky do *Set project instructions* — označíte všechno, co tam je, a nahradíte to tím novým textem. Nic nepřilepujete na konec.

> Nevyplňujete žádnou šablonu. Vzniká to z rozhovoru, protože u každého to vypadá jinak. Až budete měnit nástroj, řeknete si o to znovu.

## 4 · Povolit zápis — tohle nepřeskočte

Až se asistent poprvé pokusí něco zapsat do vašeho seznamu úkolů, zeptá se, jestli smí.

**Nemačkejte „povolit jednou". Zvolte „povolit vždy".**

Jinak se vás to bude ptát pokaždé a za týden to vzdáte. Zeptá se víckrát — založit úkol, upravit ho a odškrtnout jsou tři různé věci. Pár dní to občas vyskočí, pak už ne.

**Ověřte si to za minutu:** řekněte *„založ úkol Zkouška zápisu"*, zamkněte telefon, chvíli počkejte a pak se podívejte **do svého nástroje, ne do konverzace**. Když tam úkol je, můžete od téhle chvíle diktovat a jít.

---

## Prvních pár hodin

Až budete hotoví, tohle pořadí funguje nejlíp:

1. **„Pojďme si projít role."** → mise, životní role, vize. Nejdůležitější a nejpomalejší část, klidně na dvakrát.
2. **„Mám plnou hlavu."** → vysypání hlavy. Nespěchejte.
3. **„Roztřiď mi to."** → sedm destinací.
4. **„Pojďme naplánovat týden."** → velké kameny do kalendáře, ze všech rolí.
5. **Blok na týdenní plánování do kalendáře.** Opakovaně, konec týdne nebo těsně před jeho začátkem.

Pořadí není libovolné. Role jsou první filtr celé metodiky — *prioritám přidělujeme úkoly, ne úkolům priority.* Kdo začne vysypáním hlavy, má hromadu, kterou nemá podle čeho třídit.

Ten poslední krok se nejčastěji vynechá a je nejdůležitější. Asistent vám ho nepřipomene, schválně. *Priorita, která nemá blok v kalendáři, je jen zbožné přání.*

---

## Aktualizace

**Nestahují se samy.** Claude to dělá automaticky jen u vlastních balíčků, u ostatních ne. Když vám přijde e-mail, že vyšla nová verze, klikněte v **Customize → Plugins** na **Update**. Podle ničeho jiného nepoznáte, že jste pozadu.

---

## <a id="nahradni-cesta-bez-pluginu"></a>Náhradní cesta bez pluginu

Když se k pluginu nedostanete — bezplatný účet, zakázané Customize — funguje tohle a přijdete jen o automatické rozpoznávání situace:

1. Založte projekt jako v kroku 2.
2. Mezi soubory projektu nahrajte **balíček v jednom souboru**, který máte v e-mailu.
3. Do instrukcí vložte krátký odkaz na něj — přesné znění je hned v hlavičce toho souboru.

Pak pokračujte krokem 3 normálně.

### Když vám to zakázalo IT

Napište jim tohle:

> Dobrý den, potřeboval/a bych v našem účtu Claude povolit sekci **Customize** (pluginy a skills), abych mohl/a nainstalovat metodický balíček ze školení time managementu. Nejde o připojení k firemním datům — balíček obsahuje jen textové postupy a sám o sobě nikam nepřistupuje. Děkuji.

---

## Kam patří jaká data

| | Kam |
|---|---|
| **Pracovní obsah** | jen do nástroje schváleného zaměstnavatelem |
| **Soukromé věci** | soukromý účet |
| **Nejste si jistí?** | zeptejte se svého IT, pravidla se firma od firmy liší |

Do soukromé AI nevkládejte jména klientů, čísla ani interní informace. Nahraďte je zástupnými — na kvalitu odpovědi to nemá vliv.

---

## Když něco nefunguje

**Nic se nespustilo.** Zkontrolujte **Customize → Skills**, jestli je tam deset položek `wal-` a jsou zapnuté. Pak zkuste říct věc konkrétněji: místo „pomoz mi" zkuste „mám plnou hlavu".

**Spustilo se něco, co jsem nechtěl.** Řekněte „to ne, chci jen odpověď". Když se to opakuje, dejte nám vědět — popis se dá zúžit.

**Asistent radí něco jiného, než jsme se učili.** Napište nám to. Buď je chyba u nás, nebo je to místo, kde metodika sama mlčí. Obojí potřebujeme vědět.

**Zapsal něco, ale v nástroji to není.** Nejspíš čeká na vaše svolení — viz krok 4.

**Na mobilu nevidím Customize.** Správně, instalace jde jen z počítače. Nahraná workflow na mobilu fungují.

---

## Časté otázky

**Uvidí někdo, co si s asistentem píšu?** Ne. Běží to na vašem účtu, Symphera k tomu přístup nemá.

**Musím používat konkrétní nástroj?** Ne. Metodika je nástrojově agnostická a asistent taky.

**Můžu začít papírem?** Ano. Napište to a asistent vám bude dávat výstupy tak, aby se daly opsat.

**Můžu si to upravit?** Ano, je to váš text. Jen počítejte s tím, že když změníte názvy destinací, přestane to sedět s plakátem i s tím, co jste slyšeli v sále.

---

© Symphera s.r.o. · metodika What a Life! — Martin Klusoň
