# Zwakke-plekken-scan kwaliteitssysteem — 27-07-2026

> Uitgevoerd: 27-07-2026, dag van de DEKRA-audit · Eigenaar: R. Meulenaar
> Methode: consistentiecontrole over alle 62 documenten van het kwaliteitssysteem — gezocht naar maatregelen die worden geclaimd zonder bewijs, documenten waarnaar verwezen wordt maar die niet bestaan, en interne tegenstrijdigheden tussen registers.
> Deze scan is bewust vóór publicatie van bevindingen door derden uitgevoerd. Bevindingen gaan naar het [verbeterregister](../03_Registraties/Verbeterregister.md).

## Waarom deze scan

Het patroon achter beide eerdere tekortkomingen was hetzelfde: iets stond op papier als geregeld, maar het bewijs erachter ontbrak of was verlopen. Deze scan zoekt gericht naar dat patroon in plaats van te controleren of documenten bestaan.

Drie categorieën, oplopend in ernst:

1. **Verwezen maar niet bestaand** — een document noemt een register of formulier dat er niet is.
2. **Geclaimd zonder bewijs** — een maatregel staat als feit beschreven, maar er is niets dat aantoont dat hij werkt.
3. **Intern tegenstrijdig** — twee documenten zeggen iets anders over dezelfde werkelijkheid.

---

## Categorie 3 — Intern tegenstrijdig (eerst oplossen)

### Z1. Risicoregister R6 waardeert een datalek als onwaarschijnlijk, terwijl er in 2025 een datalek wás

Het risicoregister geeft R6 (datalek/AVG-incident) kans **1** — onwaarschijnlijk — met eindscore 3, waardoor er volgens de eigen methodiek (score ≥ 6 vereist een beheersmaatregel met eigenaar) geen maatregel verplicht is.

Twee andere documenten spreken dat tegen. R13 in datzelfde register noemt expliciet het **AI-mailbot-incident van 2025** als reden voor het risico onbeheerste AI-inzet. En het verbeterregister noemt in de correctie op de klachtentabel over 2025 onder meer **"een datalek"** als geregistreerd kwaliteitsincident.

Een risico dat zich in de meetperiode heeft voorgedaan kun je niet op kans 1 laten staan. Kans 2 × impact 3 = **score 6**, en daarmee valt R6 in de categorie die volgens het eigen register een benoemde beheersmaatregel met eigenaar vereist.

**Actie — uitgevoerd 27-07-2026:** R6 herwaardeerd naar kans 2, score 6; beheersmaatregel en eigenaar ingevuld; het incident van 2025 als onderbouwing opgenomen in de toelichting bij de hoogste risico's. Dit is de belangrijkste bevinding van de scan — niet omdat het risico groot is, maar omdat het register hier zichzelf tegenspreekt en dat de geloofwaardigheid van álle andere scores raakt.

### Z2. Takenregister vraagt een maandafsluiting die op het formulier niet bestaat

De taak *Maandafsluiting hygiënecontrolelijst (F-06)* draagt op "de maand af te sluiten", maar F-06 heeft geen maandafsluitingsblok. F-01 heeft dat wel (aantal dagen geregistreerd, aantal afwijkingen, paraaf arts). De taak kan dus wel worden uitgevoerd maar nergens worden vastgelegd.

**Actie:** maandafsluitingsblok toevoegen aan F-06, naar het model van F-01.

---

## Categorie 2 — Geclaimd zonder bewijs

### Z3. Technische beveiligingsmaatregelen staan als feit in het kwaliteitsbeleid

Het kwaliteitsbeleid noemt onder technische maatregelen: tweefactorauthenticatie, encryptie van gegevens, **automatische uitlogfunctie na 15 minuten**, firewall en virusbescherming. Geen van deze vier is ergens vastgelegd, gecontroleerd of aangetoond. De sessietimeout van 15 minuten is het meest kwetsbaar: dat is een concrete instelling die of wel of niet zo staat, en het is nooit nagekeken.

Dit is precies het type groene vinkje dat bij doorvragen sneuvelt — hetzelfde mechanisme als bij de sterilisator, waar "geregeld" alleen de interne controle dekte.

**Actie:** in fase 2 van het [NEN 7510-plan](Plan_NEN7510_implementatie.md) per maatregel vastleggen wat de werkelijke instelling is, met datum van controle. Wat niet aanstaat: aanzetten of de claim schrappen.

### Z4. Back-up wordt als beheersmaatregel genoemd maar is nooit teruggezet

R11 noemt back-ups als beheersmaatregel tegen verlies van toegang tot systemen. Er is geen back-upprocedure en geen enkel bewijs dat een herstel ooit is getest. Een back-up waarvan nooit iets is teruggezet is geen aantoonbare maatregel.

**Actie:** opgenomen als halfjaarlijkse taak *Back-up herstel-test*, eerste uitvoering oktober 2026.

### Z5. Logging van toegang tot patiëntdossiers gebeurt waarschijnlijk wel, maar niemand kijkt

Het overzicht van regelgeving noemt een beveiligd EPD "met toegangsbeveiliging en logging" als verplicht. Clinicminds logt vrijwel zeker, maar er is geen procedure die die logs periodiek beoordeelt. Loggen zonder ernaar kijken voldoet niet aan NEN 7513.

**Actie:** opgenomen als kwartaaltaak *Logcontrole toegang patiëntdossiers*, eerste uitvoering augustus 2026.

### Z7. Jaarlijkse privacytraining is toegezegd maar nooit gegeven

SOP AVG-compliance §9 belooft een jaarlijkse training over privacy en gegevensbescherming, instructie bij indiensttreding, en bewustwording rond phishing. Er is geen enkel bewijs dat die instructie ooit is gegeven, en het bekwaamheidsoverzicht F-07 had in de scholingstabel geen regel waarop het vastgelegd kon worden.

Dat weegt zwaarder dan een gemiste administratieve handeling: het datalek van 2025 ontstond door een AI-mailbot, dus door een systeem dat werd ingezet zonder te overzien wat eruit kon komen. Geen technische maatregel had dat tegengehouden; bewustwording wel. De maatregel die op papier al bestond, is precies de maatregel die het incident had kunnen voorkomen.

**Actie:** vier onderwerpen toegevoegd aan de scholingstabel van F-07 (privacy/AVG, informatiebeveiliging, datalekken en phishing herkennen, veilig gebruik van AI-hulpmiddelen) en belegd als jaarlijkse taak, uit te voeren in fase 4 van het NEN 7510-plan (december 2026).

---

## Categorie 1 — Verwezen maar niet bestaand

### Z6. Vijf genoemde documenten bestaan niet

Vijf documenten worden in het systeem genoemd — deels als wettelijk verplicht — maar bestaan niet:

| Ontbrekend document | Waar het wordt genoemd | Status |
|---|---|---|
| **Verwerkingsregister (AVG art. 30)** | overzicht regelgeving, tweemaal, als wettelijke verplichting | wettelijk verplicht, ontbreekt |
| **Autorisatiematrix** | kwaliteitsbeleid, organisatorische maatregelen | geclaimd, ontbreekt |
| **Autorisatielogboek gegevensverwerking** | SOP AVG §11, als registratieformulier | genoemd, ontbreekt |
| **Datalekregister / logboek datalekken** | kwaliteitsbeleid én SOP AVG §11 | genoemd, ontbreekt — terwijl er in 2025 een datalek wás (zie Z1) |
| **Privacyverklaring patiënt + verzoekformulier inzage/correctie/verwijdering** | SOP AVG §11, als registratieformulieren | genoemd, niet in de F-reeks F-01 t/m F-09 |

Het datalekregister weegt het zwaarst: het wordt in twee documenten genoemd als de plek waar datalekken worden vastgelegd, en er heeft zich in 2025 een datalek voorgedaan dat daar dus niet in staat.

**Actie:** alle vijf belegd in fase 1 en fase 3 van het NEN 7510-plan. Het verwerkingsregister en het datalekregister eerst — die zijn wettelijk het meest hard.

---

## Nog open uit eerdere ronden

- **Verwerkersovereenkomsten Typeform en Resend** — lopen via standaardvoorwaarden, kopieën nog te downloaden (R6, openstaand sinds 26-07-2026).
- **Extern jaarlijks onderhoud sterilisator** inclusief sensorkalibratie — als open punt benoemd, nog niet geregeld.
- **Servicerapporten apparatuur** — overzicht compleet, onderliggende rapporten deels.
- **ARBO-maatregelen** — lichte RI&E opgesteld, maatregelen lopen.

## Samenvatting

Zeven bevindingen (Z1 t/m Z7, waarbij Z6 vijf ontbrekende documenten bundelt), plus vier punten die al openstonden. Eén heeft voorrang: de tegenstrijdigheid rond R6. Geen van de bevindingen raakt de patiëntveiligheid direct; ze raken allemaal de aantoonbaarheid. Dat is consistent met het beeld uit beide eerdere tekortkomingen — het handelen is in orde, de vastlegging loopt erachteraan.

De opvolging loopt via het [NEN 7510-implementatieplan](Plan_NEN7510_implementatie.md) en het [verbeterregister](../03_Registraties/Verbeterregister.md). Volgende scan: bij de interne audit 2027.
