# Toetsingskader Digitale Zorg (IGJ) — zelftoets en implementatie

> Eigenaar: R. Meulenaar · Opgesteld: 27-07-2026 · Bron: [IGJ Toetsingskader Digitale Zorg](https://www.igj.nl/documenten/2024/05/06/toetsingskader-digitale-zorg-uitgebreide-versie), in gebruik sinds mei 2024
> Samenhang: [NEN 7510-implementatieplan](Plan_NEN7510_implementatie.md) · [AI-automatiseringsplan](AI_Automatiseringsplan_2026-2027.md) · [Risicoregister](Risicoregister_2026.md) R13

## Waarom dit kader van toepassing is

De IGJ toetst hiermee hoe zorgaanbieders digitale zorg **organiseren, beheersen en borgen** — niet welke techniek er gebruikt wordt, maar of de verantwoordelijkheden belegd zijn, de risico's beheerst en de werking aantoonbaar. PVI Clinic valt als zorgaanbieder onder dit toezicht, en de praktijk zet actief digitale middelen in: een EPD, geautomatiseerde patiëntmailings, AI-ondersteuning bij documentbeheer, en mogelijk vanaf 2027 spraakondersteunde dossiervoering.

Dit kader is dus niet vrijblijvend, en het overlapt sterk met wat er al loopt. **Thema 5 is letterlijk NEN 7510.** Daarom wordt het niet als apart traject opgezet maar ondergebracht bij het bestaande NEN 7510-plan; alleen wat het kader daarbovenop vraagt, krijgt eigen acties.

## Zelftoets per thema (stand 27-07-2026)

### Thema 1 — Goed bestuur en verantwoord innoveren
*IGJ verwacht: taken, verantwoordelijkheden en besluitvorming helder belegd bij digitale toepassingen die de zorg wezenlijk veranderen.*

**Aanwezig.** [Organisatiestructuur](../01_Beleid/Organisatiestructuur.md) §5 legt vast dat AI-ondersteuning een hulpmiddel is, geen functionaris, en dat elke inhoudelijke keuze, goedkeuring en medische beslissing bij de arts ligt. Het [AI-automatiseringsplan](AI_Automatiseringsplan_2026-2027.md) bevat vijf spelregels waaronder de eis dat elke automatisering als beheerste wijziging (§6.3) wordt doorgevoerd met een eigenaar. R13 benoemt onbeheerste AI-inzet als risico met score 6.

**Ontbreekt.** Een vastgelegd besluitvormingspad: wie besluit over invoering van een digitale toepassing, op basis van welke afweging, en waar dat besluit wordt vastgelegd. Nu is dat impliciet (de directeur besluit), maar niet beschreven.

**Beoordeling:** grotendeels op orde. Fase 6 van het AI-plan is er het levende voorbeeld van — een toepassing die onderzocht, besloten en pas daarna ingevoerd wordt, met alle drie de stappen afzonderlijk belegd.

### Thema 2 — Invoering en gebruik van digitale zorg
*IGJ verwacht: een gestructureerd invoerproces met aandacht voor behoeften, risico-afweging, training, testen en onderhoud.*

**Aanwezig.** Het AI-plan werkt gefaseerd met per fase een tastbare oplevering en een evaluatie na één cyclus in het PDCA-logboek. Voor fase 6 is de invoering uitgeschreven tot op het niveau van verwerkersovereenkomst, patiëntinformatie, controlestap en SOP-aanpassing.

**Ontbreekt.**
- Een **overzicht van alle digitale toepassingen** die nu al in gebruik zijn: Clinicminds, VREST, Google Workspace, Typeform, Resend, GitHub, Nmbrs en de eigen scripts. Zonder dat overzicht is niet te beoordelen of ze allemaal beheerst zijn. Dit valt samen met het systeemoverzicht uit fase 1 van het NEN 7510-plan.
- Een **generiek invoerproces** dat voor elke nieuwe toepassing geldt, niet alleen voor fase 6.

**Beoordeling:** deels. Het proces bestaat in de praktijk maar is niet als procedure vastgelegd.

### Thema 3 — Informeren, betrekken en ondersteunen van patiënten
*IGJ verwacht: patiënten krijgen voldoende informatie en ondersteuning om digitale zorg te kunnen gebruiken, inclusief nazorg.*

**Ontbreekt vrijwel geheel — dit is het grootste gat.** Patiënten worden nergens geïnformeerd over welke digitale middelen bij hun zorg worden ingezet en wat dat voor hen betekent. De privacyverklaring dekt de AVG-kant (welke gegevens, welke rechten), maar niet de zorgkant: dat het dossier digitaal is, dat er geautomatiseerde tevredenheidsmailings uitgaan, dat er AI-ondersteuning wordt gebruikt bij documentbeheer, en straks mogelijk bij dossiervoering tijdens het consult.

Dit weegt zwaarder zodra fase 6 doorgaat: meeluisteren tijdens een consult *moet* aan de patiënt worden uitgelegd, met de mogelijkheid het te weigeren. Dat staat al als voorwaarde in fase 6, maar het onderliggende gat is breder dan die ene toepassing.

**Beoordeling:** niet op orde. Vraagt een patiëntgerichte toelichting op digitale zorg, gekoppeld aan intake en website.

### Thema 4 — Samenwerken in het netwerk en elektronisch uitwisselen van gegevens
*IGJ verwacht: heldere afspraken intern en met ICT-partners over gegevensdeling en -uitwisseling.*

**Aanwezig.** Verwijsafspraken met ziekenhuizen liggen vast in [SOP Calamiteiten](../02_Procedures/Risicobeheer/SOP_Calamiteiten.md). Er is een leverancierslijst en er zijn verwerkersovereenkomsten met de partijen die patiëntgegevens verwerken.

**Ontbreekt.** Een expliciete vastlegging van de **scope**: PVI wisselt geen patiëntgegevens elektronisch uit met andere zorgaanbieders — geen LSP-aansluiting, geen koppeling met huisartsinformatiesystemen, geen medicatieoverdracht. Dat is een legitieme beperking gezien de aard van de praktijk, maar hij moet vastgelegd zijn in plaats van stilzwijgend. NEN 7512 (veilige uitwisseling) is daarmee grotendeels niet van toepassing; ook dat hoort onderbouwd te staan.

**Beoordeling:** deels — vooral een kwestie van vastleggen wat níet van toepassing is en waarom.

### Thema 5 — Informatiebeveiliging en continuïteit
*IGJ verwacht: informatiebeveiliging conform NEN 7510, onafhankelijke verificatie van de maatregelen, en voorbereiding op uitval.*

**Loopt.** Het volledige [NEN 7510-implementatieplan](Plan_NEN7510_implementatie.md) van 27-07-2026 dekt dit thema: nulmeting, informatiebeveiligingsbeleid, verwerkingsregister, autorisatiematrix, logcontrole, back-up met herstel-test, datalekregister en awareness.

**Ontbreekt — twee punten die het toetsingskader toevoegt boven op NEN 7510 zelf:**
- **Onafhankelijke verificatie** van de beveiligingsmaatregelen. Dat staat niet in het NEN-plan. Bij een praktijk van 2,5 FTE is een volledige audit onevenredig, maar iets van externe toetsing — een beveiligingsscan, een externe review van de nulmeting — is wel de verwachting. Vast te stellen wat passend is bij deze omvang, en die afweging vastleggen.
- **Continuïteit bij uitval.** Er is geen uitwijkprocedure voor het geval Clinicminds langdurig onbereikbaar is: hoe wordt er dan behandeld, waar komen de gegevens vandaan, hoe wordt achteraf geregistreerd. R11 noemt verlies van toegang als risico maar zonder procedure.

**Beoordeling:** op koers voor de NEN-kant, twee eigen acties erbij.

## Samenvatting

| Thema | Stand | Waar belegd |
|---|---|---|
| 1 · Goed bestuur en verantwoord innoveren | grotendeels op orde | AI-plan spelregels; besluitvormingspad toevoegen |
| 2 · Invoering en gebruik | deels | fase 1 NEN-plan (systeemoverzicht) + invoerprocedure |
| 3 · Informeren en ondersteunen van patiënten | **niet op orde** | eigen actie — grootste gat |
| 4 · Netwerk en gegevensuitwisseling | deels | scope-beperking vastleggen |
| 5 · Informatiebeveiliging en continuïteit | op koers | NEN 7510-plan + onafhankelijke toetsing + uitwijkprocedure |

**Conclusie.** Vier van de vijf thema's raken werk dat al loopt; het kader vraagt vooral om vastleggen wat in de praktijk al gebeurt, plus expliciet maken wat niet van toepassing is en waarom. Eén thema staat er los van en is echt open: patiënten informeren over de inzet van digitale zorg.

Dat laatste is geen papieren kwestie. Zodra er tijdens het consult wordt meegeluisterd, is patiëntinformatie geen randvoorwaarde meer maar de kern — en dan moet het al staan, niet nog bedacht worden.

## Acties

| # | Actie | Waar belegd | Termijn |
|---|---|---|---|
| 1 | Zelftoets afronden met de volledige normtekst van het kader ernaast | eenmalige actie in het [takenregister](../taken/takenregister.json) | 30-09-2026 |
| 2 | Overzicht digitale toepassingen (valt samen met systeemoverzicht) | fase 1 NEN 7510-plan | sep 2026 |
| 3 | **Patiëntinformatie digitale zorg via QR-code** — zie hieronder | eenmalige actie in het takenregister, A27 | 31-10-2026 |
| 4 | Besluitvormingspad en invoerprocedure digitale toepassingen vastleggen | AI-plan, aanvulling op de spelregels | 31-12-2026 |
| 5 | Scope elektronische gegevensuitwisseling vastleggen (incl. waarom NEN 7512 beperkt van toepassing is) | fase 1 NEN 7510-plan | sep 2026 |
| 6 | Vorm van onafhankelijke toetsing bepalen die past bij 2,5 FTE | fase 5 NEN 7510-plan | jan 2027 |
| 7 | Uitwijkprocedure bij uitval Clinicminds | fase 3 NEN 7510-plan | nov 2026 |

## De QR-code: drie eisen in één artefact

Thema 3 vraagt om patiënten informeren. Dat kan met een folder, maar één QR-code op de nazorgkaart, in de behandelkamer en in de afsprakenbevestiging dekt tegelijk drie dingen die nu los van elkaar openstaan:

1. **Informatie over de inzet van digitale zorg** — digitaal dossier, geautomatiseerde tevredenheidsuitvraag, AI-ondersteuning bij documentbeheer, en straks mogelijk spraakondersteunde dossiervoering met de mogelijkheid dat te weigeren. Dat is thema 3, en het is de randvoorwaarde onder fase 6 van het AI-plan.
2. **Directe toegang tot het tevredenheidsformulier.** De meting levert nu circa 45 reacties in anderhalf jaar, te weinig voor een betekenisvolle NPS. Een code die de patiënt scant terwijl hij nog in de stoel of bij de balie staat, werkt aantoonbaar beter dan een mail een week later. Dit raakt dus ook het responspercentage uit [SOP Klanttevredenheidsmeting](../02_Procedures/Administratie/SOP_Klanttevredenheidsmeting.md) v1.1.
3. **De klachtenprocedure laagdrempelig bereikbaar**, zoals de Wkkgz vraagt. Nu staat die in documenten; met een scan is hij in twee tikken vindbaar.

Eén artefact, drie eisen — en het is het soort maatregel dat je aan een auditor kunt laten zien in plaats van beschrijven.

**Aandachtspunt:** de pagina mag geen persoonsgegevens uitvragen buiten wat het tevredenheidsformulier al doet, en moet zonder inloggen bereikbaar zijn. De koppeling met de patiëntcode (`pid`) die de tevredenheidsmailing gebruikt voor deduplicatie werkt bij een QR-code niet — daar staat tegenover dat een scan anoniem is, wat de drempel juist verlaagt. Bij invoering vastleggen hoe dubbeltellingen worden voorkomen.

*Herziening: jaarlijks bij de directiebeoordeling, samen met het NEN 7510-plan.*
