# SOP Klanttevredenheidsmeting
**Praktijk voor Injectables / Radiance Clinic**

> Documentcode: SOP_009 · Versie: 1.0 · 2026-06-15 · Norm: NEN-EN-ISO 9001:2015 §9.1.2 (klanttevredenheid)

---

## Doel
Structureel en aantoonbaar de tevredenheid van behandelde patiënten meten, zodat de zorg continu verbeterd wordt en de directie over actuele cijfers beschikt.

## Werkwijze (geautomatiseerd)
- **Frequentie:** per kwartaal.
- **Doelgroep:** patiënten die het afgelopen kwartaal een behandeling hadden en het formulier nog niet invulden.
- **Dedup:** wie al invulde wordt herkend aan een verborgen patiëntcode (`pid`) en krijgt geen nieuwe uitnodiging.
- **Afzender per locatie:** Enschede/Sittard → *Praktijk voor Injectables* (`praktijkvoorinjectables@radianceclinic.nl`); overige → *Radiance Clinic* (`info@radianceclinic.nl`).
- **Uitvoering:** automatisch via GitHub Actions (kwartaal-cron). Geen handmatige actie nodig — dit borgt dat de meting niet afhankelijk is van een persoon.

## Verantwoordelijkheden
- **Directeur:** bewaakt dat de meting draait en bespreekt de uitkomst in de directiebeoordeling.
- **Systeem (kwaliteitssysteem):** voert de mailing uit en houdt bij wie al reageerde.

## Bronnen & registratie
- **Vragenlijst:** Typeform "Klanttevredenheid 2026–2027"
- **Techniek:** `scripts/tevredenheidsmail.py` + GitHub Action `tevredenheidsmail.yml` (zie repo)
- **Resultaten/KPI:** verwerkt in de [Directiebeoordeling](../../05_Management/Directiebeoordeling_2026.md) (aanbevelingspercentage + rapportcijfers)
- **Laatste meting:** 2020/21 — 95% aanbeveling, gemiddeld rapportcijfer 8,8

## Privacy (AVG)
Alleen geaggregeerde cijfers worden vastgelegd; geen individuele reacties of persoonsgegevens in het kwaliteitssysteem. Elke mail bevat een afmeldlink.
