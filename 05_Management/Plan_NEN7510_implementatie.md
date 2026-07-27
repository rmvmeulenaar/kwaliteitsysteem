# Implementatieplan NEN 7510 — informatiebeveiliging in de zorg

> Eigenaar: R. Meulenaar · Opgesteld: 27-07-2026 · Status: vastgesteld, uitvoering start augustus 2026
> Samenhang: [Risicoregister](Risicoregister_2026.md) (R6, R11, R13) · [SOP AVG-compliance](../02_Procedures/Administratie/SOP_AVG_compliance.md) · [Takenregister](../taken/takenregister.json) · [AI-automatiseringsplan](AI_Automatiseringsplan_2026-2027.md)

## 1. Waarom dit moet

NEN 7510 is de norm voor informatiebeveiliging in de zorg. Voor zorgaanbieders die patiëntgegevens elektronisch verwerken is **naleving** ervan het uitgangspunt van de wetgever; het is de invulling die hoort bij de beveiligingsplicht uit de AVG en de zorgwetgeving. Twee aanpalende normen horen erbij: NEN 7512 (veilige gegevensuitwisseling) en NEN 7513 (logging van toegang tot patiëntdossiers).

Belangrijk onderscheid, en dat bepaalt de aanpak hieronder: **naleving is de verplichting, certificering is een keuze.** Een praktijk van 2,5 FTE hoeft zich niet te laten certificeren om aantoonbaar te voldoen. Wat wél moet: aantoonbaar zijn. Dat betekent vastgelegd beleid, een risicoanalyse, maatregelen die je kunt laten zien, en een cyclus die controleert of ze werken.

Dat is precies de structuur die er voor ISO 9001 al staat. Daarom bouwen we geen tweede systeem.

## 2. Uitgangspunt: één systeem, twee normen

De grootste fout die kleine praktijken hier maken is een apart informatiebeveiligingssysteem optuigen naast het kwaliteitssysteem. Dat verdubbelt het onderhoud en valt binnen een jaar stil — hetzelfde patroon als de voorraadregistratie die elf maanden stillag.

Daarom:

| ISO 9001-onderdeel dat er al is | Wordt uitgebreid met |
|---|---|
| Context en scope | informatiestromen en systemen |
| Risicoregister | informatiebeveiligingsrisico's, zelfde methodiek (kans × impact) |
| SOP-structuur | SOP's toegangsbeheer, back-up, incidenten |
| Formulierenreeks F-01 t/m F-09 | registers voor autorisatie, datalekken, logcontrole |
| Takenregister + signalering + escalatie | periodieke IB-taken |
| Interne audit en directiebeoordeling | IB-paragraaf in dezelfde jaarcyclus |

Geen apart systeem, geen aparte cyclus, geen tweede set documenten die uit elkaar gaat lopen.

## 3. Wat er nu al ligt en wat ontbreekt

**Ligt er al:** een SOP AVG-compliance met datalekprocedure en meldplicht, bewaartermijnen (20 jaar, WGBO), geheimhouding in de arbeidsovereenkomst (art. 7), verwerkersovereenkomsten met de belangrijkste leveranciers (Clinicminds, VREST), en een risicoregister waarin datalek (R6), toegangsverlies (R11) en onbeheerste AI-inzet (R13) al benoemd zijn.

**Ontbreekt — en dit is de kern van het werk:**

| Wat | Waarom het moet | Fase |
|---|---|---|
| Informatiebeveiligingsbeleid (apart, vastgesteld) | het fundament van NEN 7510; nu alleen verspreide paragrafen | 1 |
| Verwerkingsregister (AVG art. 30) | wettelijk verplicht; wordt in eigen documenten als "te doen" genoemd | 1 |
| Systeem- en informatie-overzicht | je kunt niet beveiligen wat je niet in kaart hebt | 1 |
| IB-risicoanalyse | verplichte basis onder de maatregelkeuze | 2 |
| Autorisatiematrix | wordt in het kwaliteitsbeleid geclaimd maar bestaat niet | 2 |
| Logcontrole EPD-toegang (NEN 7513) | logging bestaat waarschijnlijk in Clinicminds; niemand kijkt ernaar | 2 |
| Back-up- en herstelprocedure mét teruglees-test | back-up wordt als maatregel genoemd, herstel is nooit getest | 3 |
| Datalekregister | wordt in twee documenten genoemd, bestaat niet | 3 |
| Bewijs bij geclaimde technische maatregelen | 2FA, encryptie, automatische uitlog na 15 min: geclaimd, nergens aangetoond | 3 |

## 4. Fasering

Realistisch tempo voor 2,5 FTE: zeven maanden, één blok per maand, elk blok afgerond met iets tastbaars. Niet alles tegelijk — dat is hoe het vorige keer stilviel.

### Fase 0 — Nulmeting (augustus 2026)
Gap-analyse tegen NEN 7510-2: per beheersmaatregel vastleggen of die aanwezig, deels of afwezig is. Levert de werkelijke startpositie en meteen de prioriteitsvolgorde. **Oplevering:** `Nulmeting_NEN7510.md`.

### Fase 1 — Fundament (september 2026)
Informatiebeveiligingsbeleid opstellen en vaststellen (scope, rollen, uitgangspunten, wie waarvoor tekent). Rolverdeling expliciet: de directeur is eindverantwoordelijk en vervult zelf de rol van security officer — bij 2,5 FTE is dat onvermijdelijk en dat benoemen we, net als bij de interne audit. Verwerkingsregister (AVG art. 30) opstellen. Systeemoverzicht: welk systeem bevat welke gegevens, wie heeft toegang, waar staat het. **Oplevering:** `01_Beleid/Informatiebeveiligingsbeleid.md`, `03_Registraties/Verwerkingsregister.md`, `03_Registraties/Systeem_en_informatieoverzicht.md`.

### Fase 2 — Toegang en logging (oktober 2026)
IB-risico's toevoegen aan het bestaande risicoregister, met dezelfde kans × impact-methodiek. Autorisatiematrix opstellen: per systeem per persoon welke rechten, plus de procedure bij in- en uitdiensttreding. Toegangsbeheer aantoonbaar maken: 2FA aan, sessietimeout gecontroleerd, accounts opgeschoond. Logcontrole inrichten volgens NEN 7513: nagaan wat Clinicminds logt en een kwartaalcontrole op die logs beleggen. **Oplevering:** `F-10 Autorisatiematrix`, `SOP_Toegangsbeheer.md`, kwartaaltaak logcontrole.

### Fase 3 — Continuïteit en incidenten (november 2026)
Back-up- en herstelprocedure vastleggen én een echte teruglees-test uitvoeren — een back-up die nooit is teruggezet is geen back-up. Datalekregister inrichten (`F-11`), gekoppeld aan de bestaande VIM-melding F-04. Leveranciersbeheer afronden: alle verwerkersovereenkomsten binnen, inclusief de kopieën van Typeform en Resend die uit R6 nog openstaan. **Oplevering:** `SOP_Backup_en_herstel.md` met testverslag, `F-11 Datalekregister`, complete DPA-map.

### Fase 4 — Mensen (december 2026)
Bewustwording en training: phishing, wachtwoorden, clean desk, wat te doen bij een vermoed datalek. Voor twee mensen is dat geen cursus maar een vastgelegde instructie met aftekening. Aansluiten op het bekwaamheidsoverzicht F-07. **Oplevering:** instructie + aftekening in F-07.

### Fase 5 — Aantonen (januari–februari 2027)
Interne audit met een informatiebeveiligingsblok, in dezelfde ronde als de ISO-audit. Uitkomsten naar het verbeterregister. IB-paragraaf toevoegen aan de directiebeoordeling 2027. Vanaf dat moment is naleving aantoonbaar en loopt het mee in de jaarcyclus. **Oplevering:** IB-blok in `Interne_audit_2027.md` en `Directiebeoordeling_2027.md`.

## 5. Borging na oplevering

Zonder terugkerende taken zakt dit binnen een jaar weg. Daarom zijn vijf taken toegevoegd aan het [takenregister](../taken/takenregister.json), met dezelfde signalering en escalatie als de rest:

| Taak | Frequentie | Eigenaar |
|---|---|---|
| Logcontrole toegang patiëntdossiers (NEN 7513) | per kwartaal | Rogier |
| Toegangs- en autorisatiecontrole | halfjaarlijks | Rogier |
| Back-up herstel-test | halfjaarlijks | Rogier |
| Verwerkersovereenkomsten en leveranciers-IB nalopen | jaarlijks | Rogier |
| Informatiebeveiligingsbeleid en IB-risico's herzien | jaarlijks | Rogier |

## 6. Wat dit kost

Vooral tijd, weinig geld. De systemen die de praktijk gebruikt (Clinicminds, Google Workspace) hebben de technische maatregelen al aan boord — 2FA, encryptie, logging, back-up. Het werk zit in aanzetten wat uit staat, vastleggen wat er is, en periodiek controleren of het nog klopt. Schatting: twee tot vier uur per fase, plus de terugkerende taken van ongeveer een uur per kwartaal.

Certificering is een aparte afweging en niet nodig om te voldoen. Pas overwegen wanneer een opdrachtgever of samenwerkingspartner erom vraagt.

## 7. Besluit

Vastgesteld 27-07-2026. Eerste ijkmoment: de directiebeoordeling van 2027, waarin de voortgang van dit plan een vast agendapunt is.
