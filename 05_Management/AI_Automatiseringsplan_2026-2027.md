# AI-automatiseringsplan 2026–2027 — PVI Clinic B.V.

> Eigenaar: R. Meulenaar · Opgesteld: 26-07-2026 · Koppeling: directiebeoordeling 2026 §6 en §10, risicoregister R2/R7 (kans) en R13 (risico)
> Uitgangspunt: **de hele bedrijfsvoering wordt stapsgewijs geautomatiseerd — binnen het kwaliteitssysteem, niet erlangs.**

## Waarom

De twee hoogste risico's in het register (R2 en R7, beide score 9) zijn hetzelfde probleem: alles hangt op personen die eraan moeten denken. De onderbroken voorraadregistratie 2025 is daarvan het bewijs. AI-borging is dus geen ambitie naast het kwaliteitssysteem — het **is** de beheersmaatregel. Tegelijk is onbeheerste AI-inzet zelf een risico (R13): het datalek door de AI-mailbot in 2025 laat zien wat er gebeurt als automatisering buiten de kaders loopt.

## Spelregels (borging §6.3 — geldt voor elke stap)

1. Elke automatisering wordt doorgevoerd als **beheerste wijziging**: vooraf beschreven (wat, waarom, welk proces), met eigenaar.
2. Elke geautomatiseerde processtap **registreert in het kwaliteitssysteem** (repo/formulieren) — geen schaduwadministratie.
3. **De arts blijft eindverantwoordelijk**: AI bereidt voor, signaleert en registreert; besluiten met medische of kwaliteitsimpact worden door de arts genomen of bekrachtigd.
4. Geen patiëntgegevens in AI-tooling zonder verwerkersovereenkomst en AVG-check (les van het mailbot-incident).
5. Per stap wordt de werking na één cyclus geëvalueerd (PDCA-logboek).

## Fasering

| Fase | Wat | Status |
|---|---|---|
| **1. Registraties digitaal** (2026 H2) | Google-formulieren voor terugkerende registraties: koelkasttemperatuur ✅ (live 26-07), klanttevredenheid ✅ (live sinds jan 2025), voorraadcontrole en hygiëne volgen | gestart |
| **2. Signalering** (2026 H2) | Vaste taken (kwartaalcontrole, interne audit, verlengingen, onderhoud) door het systeem laten signaleren i.p.v. door personen — cron/agenda-gestuurd vanuit de repo | **live 26-07-2026**: [takenregister](../taken/takenregister.json) + dagelijkse GitHub Action opent issues per taak; gesloten issue = traceerbare uitvoering ([uitleg](../taken/LEESMIJ_takensysteem.md)) |
| **3. Werkbesprekingen via agents** (2026 H2–2027) | Het dagelijks/wekelijks overleg krijgt een vaste, door een agent voorbereide agenda (openstaande acties, afwijkingen, registratie-status) en een automatisch vastgelegd verslag — daarmee is ook ophaallijst-punt 12 (geen overlegverslagen) structureel opgelost | plan |
| **4. Interne audits agent-ondersteund** (2027) | Een agent voert de documentcontrole en consistentiechecks van de interne audit uit (zoals de slotcontrole van 26-07-2026 al liet zien); de arts beoordeelt, weegt en stelt vast. De audit blijft een directiebesluit — de agent is het gereedschap | plan |
| **5. Administratie & inkoop** (2027) | Koppeling Clinicminds/boekhouding, voorraadsignalering, eigen software vervangt abonnementen (doelstelling 8) | plan |
| **6. Dossiervoering tijdens het consult** (2027, kandidaat) | Een meeluisterend spraaksysteem (bijvoorbeeld [Juvoly](https://juvoly.nl/)) zet het consultgesprek automatisch om in dossiertekst, die de arts controleert en vaststelt. Zie de uitwerking hieronder | **te beoordelen — geen besluit** |

## Fase 6 nader: registratie die samenvalt met de handeling

*Toegevoegd 27-07-2026 als verbetermogelijkheid, nog niet besloten.*

### Waarom dit meer is dan tijdwinst

Onder beide eerdere tekortkomingen ligt hetzelfde patroon: de handeling gebeurde wél, de vastlegging was een aparte taak die iemand moest onthouden. Dat gold voor de voorraadcontrole, de koelkasttemperatuur, de hygiënecontrole — en het geldt ook voor dossiervoering, die na het consult moet gebeuren, onder tijdsdruk, aan het eind van de dag.

Fase 2 loste dit op door te signaleren *dat* er geregistreerd moet worden. Deze fase gaat een stap verder: de registratie ontstaat uit de handeling zelf. Het consult produceert het verslag.

**De concrete aanleiding is een gedocumenteerd incident.** Het incidentenlog over 2025 bevat "onvolledige informed consent bij meerdere patiënten". Het gesprek is gevoerd; de vastlegging schoot tekort. Een systeem dat het consultgesprek omzet in dossiertekst grijpt precies daarop aan. Daarmee is dit een corrigerende maatregel op een vastgesteld kwaliteitsincident, niet alleen een efficiencymaatregel.

### Wat er eerst beantwoord moet zijn

| Vraag | Waarom het bepalend is |
|---|---|
| Sluit het aan op **Clinicminds**? | De bekende integraties lopen op huisartsinformatiesystemen (CGM, HealthConnected). Clinicminds is een EPD voor cosmetische klinieken. Zonder koppeling wordt het kopiëren en plakken — en dan gaat de tekst buiten de logging van het EPD om, wat botst met NEN 7513 (fase 2 van het [NEN 7510-plan](Plan_NEN7510_implementatie.md)) |
| Is het **uitvoerformaat** aanpasbaar? | De uitvoer is SOEP-gestructureerd, dat is huisartsgeneeskunde. Een cosmetisch behandelverslag heeft een andere vorm: anamnese, informed consent, product met lot en dosering, foto's. Past dat niet, dan levert het gesprekstekst maar geen dossierstructuur |
| **Verwerkersovereenkomst** en verwerkingslocatie | Gesprekken over gezondheid zijn bijzondere persoonsgegevens. Verwerking binnen de EU, geen modeltraining op eigen data, en helder wat er na transcriptie met de gegevens gebeurt. Volgens de leverancier wordt het gesprek niet opgenomen maar meegeluisterd, getranscribeerd en samengevat, waarna terugluisteren niet mogelijk is — te verifiëren en vast te leggen |
| **Patiëntinformatie en bezwaar** | De patiënt moet weten dat er wordt meegeluisterd. Opnemen in de intake en de privacyverklaring, met een vastgelegde mogelijkheid om het te weigeren |
| **Nauwkeurigheid bij doseringen en productnamen** | Een verkeerd getranscribeerde eenheid botulinetoxine is een patiëntveiligheidskwestie, geen administratieve fout. Vraagt een expliciete controlestap door de arts vóór vaststelling |

### Onder welke voorwaarden

Spelregel 3 en 4 hierboven gelden onverkort: het transcript is een **concept**, de arts controleert en stelt vast, en er gaan geen patiëntgegevens naar de tooling zonder verwerkersovereenkomst en AVG-toets. Dit valt onder risico **R13** (onbeheerste AI-inzet) — een systeem dat consultgesprekken verwerkt zit in dezelfde risicocategorie als de AI-mailbot van 2025, maar zwaarder. Dat is geen reden het niet te doen; het is de reden om het als beheerste wijziging (§6.3) te doen, met de vijf vragen hierboven vooraf beantwoord en vastgelegd.

**Vervolgstap:** leverancier benaderen met deze vijf vragen, antwoorden vastleggen, en op basis daarvan een besluit voorleggen bij de directiebeoordeling 2027.

## Wat dit betekent voor het kwaliteitssysteem

Automatisering verandert *hoe* processen draaien, niet *dat* ze aan de norm moeten voldoen. Bij elke fase wordt beoordeeld welke SOP's en formulieren aangepast moeten worden, en die aanpassing wordt met datum en versie vastgelegd. Zo wordt "het hele bedrijf automatiseren" geen project naast ISO 9001, maar de manier waarop het systeem zichzelf gaat dragen.

*Evaluatie: jaarlijks bij de directiebeoordeling; eerstvolgende toets van fase 1–2 bij de kwartaalcyclus Q4 2026.*
