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

### Technisch onderzoek 27-07-2026 — wat wel en niet kan

Onderzocht is of een eigen koppeling tussen een spraaksysteem en Clinicminds te bouwen is. Uitkomst: **de ene helft kan, de andere niet — en waarschijnlijk is de koppeling helemaal niet nodig.**

**Juvoly-zijde: koppelbaar.** Er is een openbaar gedocumenteerde REST-API (V2) op `https://services.juvoly.nl/api/v2/rest`, met authenticatie via de headers `X-Juvoly-Api-Key` en `X-Juvoly-Client-Id`. Drie relevante endpoints:

| Endpoint | Wat het doet |
|---|---|
| `POST /speech/transcript?model=juvoly_v3` | audiobestand (max 100 MB) → transcript met tijdcodes per woord |
| `GET /map/template` | opvraagbare documentsjablonen, met per sjabloon de velden en parameters |
| `POST /map` | transcript + sjabloonsleutel → gestructureerd document met ingevulde velden |

Daarnaast is er een WebSocket-API voor meeluisteren in real time. De sjablonen zijn opvraagbaar en bevatten parameters, dus SOEP is niet per definitie het enige formaat — wel te verifiëren of een eigen sjabloon voor een cosmetisch behandelverslag mogelijk is.

**Clinicminds-zijde: niet schrijfbaar.** De Analytics API telt 44 endpoints en die zijn **alle 44 van het type GET**. De specificatie omschrijft zichzelf als "API for fetching reports for use with analytics tools", bedoeld voor periodieke uitvraag, niet voor realtime gebruik. Er is geen enkel endpoint om een consultverslag of dossierregel weg te schrijven. Sinds versie 5.15 zijn er twee nieuwe API's — een Booking API (afspraken en digitale intake naar binnen) en een Triggers & Actions API (gebeurtenissen naar buiten) — maar geen van beide is gedocumenteerd voor het schrijven van dossierinhoud.

Een zelfgebouwde koppeling zou dus stranden op de laatste stap: transcriberen en structureren lukt, terugschrijven in het dossier niet. Wat overblijft is kopiëren en plakken, en dan gaat de tekst buiten de logging van het EPD om — precies het NEN 7513-punt uit fase 2 van het [NEN 7510-plan](Plan_NEN7510_implementatie.md).

**En daarmee de belangrijkste vondst: Clinicminds levert deze functie zelf al.** Versie 5.15 bevat *Quinn AI Smart Summary*, dat volgens de release-aankondiging tijdens het consult meeluistert, het gesprek interpreteert en de gestructureerde velden van het medisch dossier in real time invult — dus niet alleen transcribeert, maar rechtstreeks in het dossier schrijft. Dat is exact de stap die van buitenaf niet te bouwen is.

**Conclusie voor de besluitvorming.** De volgorde is omgekeerd ten opzichte van de oorspronkelijke gedachte:

1. **Eerst Quinn AI Smart Summary in de eigen omgeving beoordelen** — beschikbaar in het abonnement, kwaliteit van het Nederlands, en of de ingevulde velden aansluiten op een cosmetisch behandelverslag inclusief informed consent, product, lot en dosering. Dit vraagt geen koppeling, geen extra verwerker en geen tweede leverancier, en het schrijft binnen de logging van het EPD.
2. **Pas als dat tekortschiet** een extern spraaksysteem overwegen. Vraag dan eerst aan Clinicminds of er een niet-openbare schrijf-API voor dossierregels bestaat; zonder die API is de koppeling niet zinvol te bouwen.
3. **Kopiëren en plakken is geen werkbaar alternatief** zolang de logging-eis uit NEN 7513 niet geregeld is.

*Nog te verifiëren: de beschrijving van Quinn komt uit de release-aankondiging van Clinicminds, niet uit eigen gebruik. Eerste stap is het in de eigen omgeving bekijken.*

### Wat er eerst beantwoord moet zijn

| Vraag | Waarom het bepalend is |
|---|---|
| Doet **Quinn AI Smart Summary** wat wij nodig hebben? | Zit al in Clinicminds, schrijft binnen het EPD en dus binnen de logging. Als dit volstaat vervalt de hele koppelingsvraag |
| Is het **uitvoerformaat** passend? | Bij Juvoly is de standaard SOEP, dat is huisartsgeneeskunde. Een cosmetisch behandelverslag heeft een andere vorm: anamnese, informed consent, product met lot en dosering, foto's. Bij Quinn is de vraag of de dossiervelden van Clinicminds correct worden gevuld |
| **Verwerkersovereenkomst** en verwerkingslocatie | Gesprekken over gezondheid zijn bijzondere persoonsgegevens. Verwerking binnen de EU, geen modeltraining op eigen data, en helder wat er na transcriptie met de gegevens gebeurt. Volgens de leverancier wordt het gesprek niet opgenomen maar meegeluisterd, getranscribeerd en samengevat, waarna terugluisteren niet mogelijk is — te verifiëren en vast te leggen |
| **Patiëntinformatie en bezwaar** | De patiënt moet weten dat er wordt meegeluisterd. Opnemen in de intake en de privacyverklaring, met een vastgelegde mogelijkheid om het te weigeren |
| **Nauwkeurigheid bij doseringen en productnamen** | Een verkeerd getranscribeerde eenheid botulinetoxine is een patiëntveiligheidskwestie, geen administratieve fout. Vraagt een expliciete controlestap door de arts vóór vaststelling |

### Onder welke voorwaarden

Spelregel 3 en 4 hierboven gelden onverkort: het transcript is een **concept**, de arts controleert en stelt vast, en er gaan geen patiëntgegevens naar de tooling zonder verwerkersovereenkomst en AVG-toets. Dit valt onder risico **R13** (onbeheerste AI-inzet) — een systeem dat consultgesprekken verwerkt zit in dezelfde risicocategorie als de AI-mailbot van 2025, maar zwaarder. Dat is geen reden het niet te doen; het is de reden om het als beheerste wijziging (§6.3) te doen, met de vijf vragen hierboven vooraf beantwoord en vastgelegd.

**Vervolgstap — belegd, niet vrijblijvend.** Quinn AI Smart Summary in de eigen Clinicminds-omgeving beoordelen. Pas als dat tekortschiet de externe route onderzoeken, en dan eerst bij Clinicminds navragen of er een schrijf-API voor dossierregels bestaat. Antwoorden vastleggen en het besluit voorleggen bij de directiebeoordeling 2027.

Dit onderzoek staat als eenmalige actie met deadline 31-12-2026 in het [takenregister](../taken/takenregister.json) (`onderzoek-quinn-dossiervoering`). Het issue opent zestig dagen vooraf en escaleert daarna per mail — hetzelfde mechanisme als de terugkerende taken. Daarmee is dit geen voornemen in een plan maar een gesignaleerde en bewaakte actie.

### Bijvangst van het onderzoek: wat de Analytics API wél biedt

De 44 leesbare endpoints bevatten data die nu handmatig wordt bijgehouden. Drie zijn direct bruikbaar voor bestaande verbeterpunten:

- **`/product-stock`, `/product-stock-adjustments`, `/treatment-material-stock`** — voorraadstanden en mutaties. Dit maakt het vervaldatum-overzicht mogelijk waar F-08 de gegevens al voor vastlegt: maanden vooruit weten wat er afloopt in plaats van het te ontdekken bij de kwartaalrondgang. Preventief in plaats van opsporend.
- **`/complications` en `/side-effects`** — complicatie- en bijwerkingsregistratie. Voedt de trendtabel in het verbeterregister rechtstreeks, in plaats van handmatig samenstellen.
- **`/records`, `/forms`, `/checklist-questions`** — dossier- en formulierdata voor de KPI's in de directiebeoordeling.

Deze drie vallen onder fase 5 (administratie) en vragen geen nieuwe leverancier: de API-koppeling en de sleutel bestaan al en worden gebruikt door de weekstart- en tevredenheidsscripts.

## Wat dit betekent voor het kwaliteitssysteem

Automatisering verandert *hoe* processen draaien, niet *dat* ze aan de norm moeten voldoen. Bij elke fase wordt beoordeeld welke SOP's en formulieren aangepast moeten worden, en die aanpassing wordt met datum en versie vastgelegd. Zo wordt "het hele bedrijf automatiseren" geen project naast ISO 9001, maar de manier waarop het systeem zichzelf gaat dragen.

*Evaluatie: jaarlijks bij de directiebeoordeling; eerstvolgende toets van fase 1–2 bij de kwartaalcyclus Q4 2026.*
