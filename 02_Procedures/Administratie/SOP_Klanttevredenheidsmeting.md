# SOP Klanttevredenheidsmeting
**Praktijk voor Injectables / Radiance Clinic**

> Documentcode: SOP_009 · Versie: 1.1 · 2026-07-27 · Norm: NEN-EN-ISO 9001:2015 §9.1.2 (klanttevredenheid)
> *Wijziging v1.0 → v1.1 (27-07-2026): NPS als aanvullende maatstaf toegevoegd, met rekenwijze, rapportageritme en de omgang met kleine aantallen. Responspercentage toegevoegd als meetpunt.*

---

## Doel
Structureel en aantoonbaar de tevredenheid van behandelde patiënten meten, zodat de zorg continu verbeterd wordt en de directie over actuele cijfers beschikt.

## Werkwijze (geautomatiseerd)
- **Frequentie:** per kwartaal.
- **Doelgroep:** patiënten die het afgelopen kwartaal een behandeling hadden en het formulier nog niet invulden.
- **Dedup:** wie al invulde wordt herkend aan een verborgen patiëntcode (`pid`) en krijgt geen nieuwe uitnodiging.
- **Afzender per locatie:** Enschede/Sittard → *Praktijk voor Injectables* (`praktijkvoorinjectables@radianceclinic.nl`); overige → *Radiance Clinic* (`info@radianceclinic.nl`).
- **Uitvoering:** automatisch via GitHub Actions (kwartaal-cron). Geen handmatige actie nodig — dit borgt dat de meting niet afhankelijk is van een persoon.

## Wat wij meten

Drie maatstaven naast elkaar. Ze meten verschillende dingen en vervangen elkaar niet.

| Maatstaf | Vraag | Waarvoor |
|---|---|---|
| **Aanbevelingspercentage** | beveelt u ons aan? (ja/nee) | doorlopende trendlijn sinds januari 2025; doelstelling 3 (≥ 90%) |
| **Gemiddelde waardering** | rapportcijfer / sterren | hoe tevreden, ongeacht aanbeveling |
| **NPS** *(nieuw per 27-07-2026)* | 0–10-schaal, zie hieronder | vergelijkbaarheid met de sector en gevoeligheid voor ontevredenheid |
| **Responspercentage** *(nieuw)* | ingevuld ÷ uitgenodigd | zegt of de andere drie cijfers iets betekenen |

De bestaande twee blijven ongewijzigd. Ze vormen de trendlijn sinds januari 2025 en die breek je niet door halverwege van maatstaf te wisselen. NPS komt erbij.

## NPS — Net Promoter Score

**De vraag, letterlijk zo te stellen:**

> Hoe waarschijnlijk is het dat je onze praktijk aanbeveelt aan familie of vrienden?
> *0 = zeer onwaarschijnlijk · 10 = zeer waarschijnlijk*

De schaal moet 0 tot en met 10 zijn — elf punten. Een schaal van 1–5 of 1–10 levert géén NPS op en is niet vergelijkbaar met sectorcijfers. Dit is de enige plek in deze SOP waar de exacte vorm van de vraag ertoe doet.

**Rekenwijze:**

| Groep | Score | Betekenis |
|---|---|---|
| Promoters | 9–10 | bevelen actief aan |
| Passief tevredenen | 7–8 | tellen niet mee in de uitkomst |
| Criticasters | 0–6 | risico op negatieve mond-tot-mondreclame |

**NPS = % promoters − % criticasters.** De uitkomst ligt tussen −100 en +100 en is geen percentage; noteer hem als getal zonder procentteken. Passief tevredenen tellen niet mee in de teller, wél in de noemer.

*Rekenvoorbeeld:* 40 reacties, 26 promoters (65%), 9 passief (22,5%), 5 criticasters (12,5%) → NPS = 65 − 12,5 = **+52,5**, afgerond **+53**.

**Wat een uitkomst betekent.** Boven 0 zijn er meer promoters dan criticasters. In de cosmetische en particuliere zorg liggen goed presterende praktijken doorgaans ruim boven de +50. Wij stellen pas een streefwaarde vast ná vier kwartalen meten — een doel zonder nulmeting is een gok, en dat is precies het soort claim dat dit kwaliteitssysteem wil vermijden.

**Kleine aantallen: de belangrijkste beperking.** Met ongeveer 45 reacties over anderhalf jaar is een kwartaal-NPS onbetrouwbaar. Bij 20 reacties in een kwartaal verschuift één criticaster de score al met 5 punten. Daarom:

- rapporteer NPS **voortschrijdend over twaalf maanden**, niet per los kwartaal;
- vermeld **altijd het aantal reacties (n)** bij het cijfer — een NPS zonder n is betekenisloos;
- beschouw een verschil van minder dan 10 punten bij n < 50 als ruis en niet als trend;
- kijk bij weinig reacties naar de **losse criticasters** in plaats van naar de score: bij deze aantallen is één toelichting van een ontevreden patiënt informatiever dan het gemiddelde.

**Opvolging.** Elke criticaster (0–6) is een signaal: beoordelen of er een klacht of complicatie achter zit volgens de definitie op [F-03](../../03_Registraties/Formulieren/F-03_Complicatieregistratieformulier.md), en zo ja registreren. Terugkerende thema's gaan naar het [verbeterregister](../../03_Registraties/Verbeterregister.md). Dit is de koppeling die van een cijfer een verbetering maakt.

## Responspercentage

Van de kwartaalmailing wordt vastgelegd: aantal uitgenodigd, aantal ingevuld, responspercentage. Zonder dat getal is niet te beoordelen of de uitkomst representatief is of alleen de mening van de meest tevreden of juist de meest ontevreden patiënten weergeeft. Het aantal uitgenodigden is bekend uit de mailing; het aantal reacties uit het formulier.

## Rapportage

- **Per kwartaal** bij de taak *Kwartaalreview klanttevredenheid*: aanbevelingspercentage, gemiddelde waardering, NPS voortschrijdend twaalf maanden met n, responspercentage, en de losse toelichtingen van criticasters.
- **Jaarlijks** in de directiebeoordeling (§9.1.2), met de trend over de voorgaande jaren.

## Verantwoordelijkheden
- **Directeur:** bewaakt dat de meting draait en bespreekt de uitkomst in de directiebeoordeling.
- **Systeem (kwaliteitssysteem):** voert de mailing uit en houdt bij wie al reageerde.

## Bronnen & registratie

> **Openstaand punt (27-07-2026):** deze SOP noemt Typeform als vragenlijst, terwijl de directiebeoordeling 2026 de lopende meting sinds januari 2025 aan Google Forms toeschrijft — en dáár komen de circa 45 reacties en het aanbevelingspercentage van 87% vandaan. Twee bronnen voor één cijfer. Vast te stellen welke leidend is en de andere te beëindigen of expliciet als aparte meting te beschrijven. Zolang dat niet is beslecht, moet bij elk gerapporteerd cijfer staan uit welk formulier het komt. Zie [zwakke-plekken-scan](../../05_Management/Zwakke_plekken_scan_2026-07-27.md) Z10.

- **Vragenlijst:** Typeform "Klanttevredenheid 2026–2027"
- **Techniek:** `scripts/tevredenheidsmail.py` + GitHub Action `tevredenheidsmail.yml` (zie repo)
- **Resultaten/KPI:** verwerkt in de [Directiebeoordeling](../../05_Management/Directiebeoordeling_2026.md) (aanbevelingspercentage + rapportcijfers)
- **Laatste meting:** 2020/21 — 95% aanbeveling, gemiddeld rapportcijfer 8,8

## Privacy (AVG)
Alleen geaggregeerde cijfers worden vastgelegd; geen individuele reacties of persoonsgegevens in het kwaliteitssysteem. Elke mail bevat een afmeldlink.
