# Risicoregister 2026 — PVI Clinic B.V.

> Eigenaar: R. Meulenaar · Vorige versie: 2020 (vervangen) · Norm: ISO 9001:2015 §6.1
> Methodiek: kans (1–3) × impact (1–3) = score; **score ≥ 6 vereist een beheersmaatregel met eigenaar**.
> Bijgewerkt: 2026-07-26 (R13 toegevoegd; status R6, R9 geactualiseerd)

| # | Risico | Kans | Impact | Score | Beheersmaatregel | Status |
|---|---|:--:|:--:|:--:|---|---|
| R1 | Verlopen producten in voorraad (herhaling tekortkoming §8.5.4) | 2 | 3 | **6** | Kwartaalcontrole + FIFO + kleine voorraad + SOP Voorraadbeheer | hervat per jun 2026 |
| R2 | Periodieke taken vallen stil bij drukte/afwezigheid (wortel-oorzaak 2025) | 3 | 3 | **9** | Borging in systeem (GitHub-cron, signalering) i.p.v. personen | in uitvoering |
| R3 | Interne audit/directiebeoordeling niet uitgevoerd (herhaling §9.2) | 2 | 3 | **6** | Vaste jaarcyclus + dit register + actielijst | loopt |
| R4 | Complicatie bij behandeling (medisch) | 1 | 3 | 3 | Protocollen, noodtas, bekwaamheid arts, verwijsafspraken | actueel houden |
| R5 | Verkeerde verwachtingen klant → ontevredenheid/klacht | 2 | 2 | 4 | Vectra/Faceapp, informed consent, nabellen | doorlopend |
| R6 | Datalek / AVG-incident (patiëntgegevens, Clinicminds) | 1 | 3 | 3 | SOP AVG, toegangsbeheer, verwerkersovereenkomsten | gecheckt 26-07-2026: Clinicminds-DPA van kracht (abonnement; bewijsmail 06-11-2025), VREST getekend 27-03-2024; Typeform/Resend via standaardvoorwaarden, kopieën nog downloaden |
| R7 | **Sleutelpersoon-risico: alles hangt op één arts/directeur** | 3 | 3 | **9** | Taken delen + documentatie + AI/systeemborging (dit systeem) | structureel aandachtspunt |
| R8 | Apparatuur niet onderhouden → uitval/onveilig | 2 | 2 | 4 | Apparatuuroverzicht + onderhoudsschema | opgesteld, deels te regelen |
| R9 | Koelketen-falen medicatiekoelkast | 1 | 3 | 3 | Wekelijkse temperatuurregistratie (digitaal formulier) + dagelijkse visuele check bij opening | registratie 2025 aangeleverd 26-07-2026; loopt door via formulier |
| R10 | Diensten buiten certificaatscope (TRT, GLP-1, BHT) | 2 | 2 | 4 | Intern beoordeeld: buiten certificaat gehouden, niet als ISO-gecertificeerd geclaimd; geen proactieve DEKRA-melding | beoordeeld jun 2026 |
| R11 | Verlies toegang systemen (Clinicminds, repo, Drive) | 1 | 2 | 2 | Wachtwoordbeheer, back-ups, leverancierafspraken | laag |
| R12 | Financieel: cashflow/verlies raakt kwaliteit | 2 | 2 | 4 | Betaalkalender vaste verplichtingen; groei + kostenbesparing (zie doelstellingen) | aandacht (verlies 2024) |
| R13 | **Onbeheerste AI-inzet**: datalek (AI-mailbot-incident 2025), output zonder menselijke controle, registraties buiten het kwaliteitssysteem om | 2 | 3 | **6** | Elke automatiseringsstap als beheerste wijziging (§6.3): eigenaar per proces, vastlegging in het kwaliteitssysteem, arts eindverantwoordelijk; zie [AI-automatiseringsplan](AI_Automatiseringsplan_2026-2027.md) | toegevoegd 26-07-2026 |

## Toelichting hoogste risico's (score ≥ 6)
- **R2 & R7 (score 9):** beide gaan over afhankelijkheid van personen / één persoon. Dit is precies waarom de strategische richting (AI + systeemborging, minder afhankelijk van mensen) ook een **risicobeheersmaatregel** is — niet alleen een ambitie.
- **R1 & R3 (score 6):** herhalingsrisico van de twee eerdere tekortkomingen; beheerst via vaste cyclus + systeemsignalering.
- **R13 (score 6):** AI is tegelijk de belangrijkste beheersmaatregel voor R2/R7 én een eigen risico. De kans (efficiency, borging, minder persoonsafhankelijkheid) wordt alleen benut als de inzet beheerst gebeurt — daarom loopt elke automatisering via het AI-automatiseringsplan en niet ad hoc.

## Kansen (§6.1)
- **AI/automatisering** — grootste kans: routineprocessen, registraties, interne audits en werkbesprekingen stapsgewijs via agents, met de arts als eindverantwoordelijke. Zie [AI-automatiseringsplan 2026–2027](AI_Automatiseringsplan_2026-2027.md).
- **Peptiden en regeneratieve geneeskunde** — mogelijke nieuwe behandeldomeinen; introductie pas na scope- en regelgevingsbeoordeling (koppeling R10).
- **Eigen software i.p.v. abonnementen** — lagere kosten en minder leveranciersafhankelijkheid.

## Besluit directie
Vastgesteld op 15-06-2026 · volgende herziening: jaarlijks bij de directiebeoordeling.
