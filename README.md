# What a Life! â€” AI agent

DigitĂˇlnĂ­ podpora pro aplikaci metodiky **What a Life!** (Symphera, autor Martin KlusoĹ).
Deset workflow, kterĂ© si AI asistent volĂˇ sĂˇm, kdyĹľ poznĂˇ situaci â€” nic nekopĂ­rujete a nemusĂ­te si pamatovat pĹ™Ă­kazy.

UrÄŤeno pĹ™edevĹˇĂ­m **absolventĹŻm ĹˇkolenĂ­**. Bez kurzu to funguje taky, ale metodika je tu jen ve zkratce.

---

## Co to umĂ­

Ĺeknete *â€žmĂˇm plnou hlavu"* â€” asistent vĂˇs provede vysypĂˇnĂ­m hlavy po oblastech.
VloĹľĂ­te seznam vÄ›cĂ­ â€” roztĹ™Ă­dĂ­ je do **sedmi destinacĂ­**.
Ĺeknete *â€žnemĹŻĹľu se do toho pustit"* â€” najde s vĂˇmi prvnĂ­ krok.
Ĺeknete *â€žpĹ™istĂˇlo mi tohle a nemĂˇm ÄŤas"* â€” napĂ­Ĺˇe tĹ™i varianty **konstruktivnĂ­ho Ano**.

## K ÄŤemu mĂˇ pĹ™Ă­stup

**Plugin sĂˇm nepĹ™idĂˇvĂˇ ĹľĂˇdnĂ© pĹ™ipojenĂ­ k vaĹˇim datĹŻm.** Jestli asistent uvidĂ­ vĂˇĹˇ kalendĂˇĹ™, maily nebo Ăşkoly, si nastavujete vy u svĂ©ho poskytovatele AI â€” konektory, integrace, firemnĂ­ politika. My do toho nevstupujeme.

**KdyĹľ ten pĹ™Ă­stup mĂˇ, aĹĄ ho pouĹľĂ­vĂˇ.** Zapsat Ăşkol rovnou do vaĹˇeho seznamu je pĹ™esnÄ› to, o co jde â€” ÄŤĂ­m mĂ­Ĺ pĹ™episovĂˇnĂ­ a pĹ™eklikĂˇvĂˇnĂ­, tĂ­m spĂ­Ĺˇ vĂˇm systĂ©m vydrĹľĂ­. Pravidlo nenĂ­ â€žnezapisuj", ale **ukaĹľ nĂˇvrh, poÄŤkej na potvrzenĂ­, pak zapiĹˇ**.

Co si nastavĂ­te, patĹ™Ă­ do vaĹˇĂ­ **nĂˇstrojovĂ© vrstvy** â€” je tam k tomu sekce â€žCo smĂ­ agent sĂˇm". VĂ˝chozĂ­ je opatrnĂˇ varianta, ale je to vaĹˇe volba, ne naĹˇe.

**Co nedÄ›lĂˇ:** neposĂ­lĂˇ notifikace a nepĹ™ipomĂ­nĂˇ se. SystĂ©m, kterĂ˝ vĂˇs upomĂ­nĂˇ, si za tĹ™i tĂ˝dny ztlumĂ­te. Blok na plĂˇnovĂˇnĂ­ si dĂˇvĂˇte do kalendĂˇĹ™e sami â€” metodika ostatnÄ› uÄŤĂ­, Ĺľe priorita bez bloku je jen zboĹľnĂ© pĹ™ĂˇnĂ­.

## Instalace

**â†’ [`docs/manual.md`](docs/manual.md)** â€” nĂˇvod krok za krokem pro Claude, ChatGPT i Copilot.

NejkratĹˇĂ­ cesta (Claude):

1. **Customize â†’ Plugins â†’ â€ž+" â†’ Add marketplace**, vloĹľte URL tohoto repozitĂˇĹ™e.
2. Nainstalujte plugin **what-a-life**.
3. ZaloĹľte projekt a vloĹľte [`instructions/01-agent.md`](instructions/01-agent.md) do *Project instructions*.
4. NapiĹˇte **â€žpojÄŹme nastavit systĂ©m"**.

Ve ÄŤtvrtĂ©m kroku s vĂˇmi asistent projde vaĹˇe nĂˇstroje, navrhne strukturu a vypĂ­Ĺˇe vaĹˇi osobnĂ­ **nĂˇstrojovou vrstvu** â€” tu vloĹľĂ­te do instrukcĂ­ pod tu prvnĂ­. NevyplĹujete ĹľĂˇdnou Ĺˇablonu; vznikĂˇ to z rozhovoru, protoĹľe u kaĹľdĂ©ho to vypadĂˇ jinak: Trello, Todoist, Notion, Outlook To Do nebo papĂ­rovĂ˝ zĂˇpisnĂ­k. Metodika ĹľĂˇdnĂ˝ nĂˇstroj nepĹ™edepisuje.

**Aktualizace se nestahujĂ­ samy.** KdyĹľ vyjde novÄ›jĹˇĂ­ verze, kliknÄ›te v **Customize â†’ Plugins** na **Update** â€” jinak vĂˇm dĂˇl bÄ›ĹľĂ­ ta, kterou jste nainstalovali. Na novou verzi vĂˇs upozornĂ­me eâ€‘mailem.

Kdo se k marketplace nedostane, najde hotovĂ© ZIPy jednotlivĂ˝ch skills ve sloĹľce [`dist/`](dist) â€” **Customize â†’ Skills â†’ Upload**. Ve stejnĂ© sloĹľce je i [`rocni-plan-template.xlsx`](dist/rocni-plan-template.xlsx).

### ChatGPT a M365 Copilot

Plugin je Claude formĂˇt, jinam nejde. Pro ostatnĂ­ platformy je celĂ˝ balĂ­ÄŤek sloĹľenĂ˝ **do jednoho souboru**: [`dist/wal-balicek-jeden-soubor.md`](dist/wal-balicek-jeden-soubor.md) â€” pravidla i vĹˇech deset postupĹŻ pohromadÄ›.

- **ChatGPT** â€” nahrajte ten soubor mezi soubory projektu a do *Instructions* dejte krĂˇtkĂ˝ odkaz na nÄ›j (pĹ™esnĂ© znÄ›nĂ­ je v hlaviÄŤce souboru). Asistent si v nÄ›m postup najde sĂˇm.
- **Copilot** â€” vloĹľte obsah souboru na zaÄŤĂˇtek konverzace a pokraÄŤujte v nĂ­.

AutomatickĂ© rozpoznĂˇnĂ­ situace je tam slabĹˇĂ­ neĹľ u pluginu na Claude, ale balĂ­ÄŤek zĹŻstĂˇvĂˇ celĂ˝.

## Workflow

| Skill | Blok metodiky | SpustĂ­ se, kdyĹľâ€¦ |
|---|---|---|
| `wal-nastav-system` | napĹ™Ă­ÄŤ | â€žpojÄŹme nastavit systĂ©m", mÄ›nĂ­te nĂˇstroj |
| `wal-vysyp-hlavu` | COLLECT IT | â€žmĂˇm plnou hlavu", â€žnÄ›co mi unikĂˇ" |
| `wal-protrid-schranku` | ORGANIZE IT | vloĹľĂ­te seznam vÄ›cĂ­ nebo pĹ™edmÄ›tĹŻ mailĹŻ |
| `wal-rozpad-projektu` | ORGANIZE IT | â€žnemĹŻĹľu se do toho pustit", â€žpoĹ™Ăˇd to odklĂˇdĂˇm" |
| `wal-prioritizuj` | PRIORITIZE IT | â€žnevĂ­m, co dĹ™Ă­v", â€žvĹˇechno hoĹ™Ă­" |
| `wal-konstruktivni-ano` | PRIORITIZE IT | â€žpĹ™istĂˇlo mi tohle a nemĂˇm ÄŤas" |
| `wal-naplanuj-tyden` | PLAN IT | â€žpojÄŹme naplĂˇnovat tĂ˝den" |
| `wal-navyk` | MAKE IT A HABIT | â€žchci si zavĂ©st nĂˇvyk", â€žnedaĹ™Ă­ se mi vydrĹľet" |
| `wal-energie` | HAVE ENERGY FOR IT | â€žjsem vyÄŤerpanĂ˝", â€žnemĂˇm energii" |
| `wal-role-a-vize` | DREAM IT | â€žchci si projĂ­t role", â€žnesedĂ­ mi nastavenĂ­" |

Blok **OWN IT** workflow nemĂˇ zĂˇmÄ›rnÄ› â€” je to prĂˇce s postojem, ne s informacĂ­. Projevuje se v tom, jak agent mluvĂ­.

## TĹ™i vrstvy

| Vrstva | Co obsahuje | Kde je |
|---|---|---|
| **1 Â· Metodika** | destinace, testy, pravidla | [`docs/metodika.md`](docs/metodika.md) |
| **2 Â· Instrukce agenta** | jak agent uvaĹľuje a mluvĂ­ | [`instructions/01-agent.md`](instructions/01-agent.md) |
| **3 Â· NĂˇstrojovĂˇ vrstva** | vaĹˇe boardy, seznamy, ĹˇtĂ­tky | vznikne v rozhovoru, kostra v [`instructions/02-`](instructions/02-nastrojova-vrstva.md) |

Instrukce popisujĂ­ **proces**, nĂˇstrojovĂˇ vrstva popisuje **ĂşloĹľiĹˇtÄ›**. KdyĹľ zmÄ›nĂ­te nĂˇstroj, mÄ›nĂ­ se jen vrstva 3.

## Co tady nenĂ­

Tenhle repozitĂˇĹ™ obsahuje **operativnĂ­ vrstvu** metodiky â€” to, co potĹ™ebuje asistent, aby mluvil stejnĂ˝m jazykem jako ĹˇkolenĂ­.

VĂ˝klad, pĹ™Ă­bÄ›hy, cviÄŤenĂ­ vedenĂˇ lektorem a ĹˇkolicĂ­ materiĂˇly **souÄŤĂˇstĂ­ nejsou**. Ty patĹ™Ă­ ke kurzu. Pokud jste ĹˇkolenĂ­m proĹˇli, drĹľte se materiĂˇlĹŻ ze sĂˇlu â€” tohle je jejich zkratka, ne nĂˇhrada.

## Licence a pouĹľitĂ­

Metodika What a Life! je duĹˇevnĂ­ vlastnictvĂ­ **Symphera s.r.o.** Obsah tohoto repozitĂˇĹ™e je zveĹ™ejnÄ›n pro osobnĂ­ pouĹľitĂ­ absolventĹŻ a zĂˇjemcĹŻ o metodiku.

NenĂ­ dovoleno jej pouĹľĂ­vat pro komerÄŤnĂ­ ĹˇkolenĂ­, pĹ™eprodej ani odvozenĂ© kurzy bez souhlasu Symphery.

---

Â© Symphera s.r.o. Â· metodika What a Life! â€” Martin KlusoĹ Â· [symphera.com](https://symphera.com)
