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

## Wat dit betekent voor het kwaliteitssysteem

Automatisering verandert *hoe* processen draaien, niet *dat* ze aan de norm moeten voldoen. Bij elke fase wordt beoordeeld welke SOP's en formulieren aangepast moeten worden, en die aanpassing wordt met datum en versie vastgelegd. Zo wordt "het hele bedrijf automatiseren" geen project naast ISO 9001, maar de manier waarop het systeem zichzelf gaat dragen.

*Evaluatie: jaarlijks bij de directiebeoordeling; eerstvolgende toets van fase 1–2 bij de kwartaalcyclus Q4 2026.*
