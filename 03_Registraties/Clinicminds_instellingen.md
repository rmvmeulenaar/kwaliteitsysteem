# Instellingen Clinicminds-export

> Bron: Google Drive fileId: 1_QejHcwiaertwvSV-y4TbM8ium5emVcjn-BnfDoKmlU
> Type: Google Doc — Stappenplan voor configureren van Clinicminds-exports t.b.v. maandelijkse statistieken en ISO9001-compliance

---

Dit stappenplan beschrijft hoe de Clinicminds-export wordt ingericht om automatisch maandelijkse statistieken te kunnen genereren, data te koppelen aan andere systemen, trends inzichtelijk te maken en te voldoen aan ISO9001-richtlijnen.

## 1. Export-instellingen configureren in Clinicminds

**Frequentie:**
- Stel een automatische, periodieke export in (indien beschikbaar in Clinicminds) of plan een terugkerende handmatige export in op een vaste dag na het einde van elke maand.

**Formaat:**
- Voorkeur voor **CSV** bij geautomatiseerde koppelingen, **XLSX** als de data handmatig wordt verwerkt of als men in Excel draaitabellen gebruikt.

**Datavelden:**

- Patiëntinformatie (geanonimiseerd):
  - Unieke (pseudonieme) patiënt-ID
  - Geslacht (indien nodig voor statistische analyse)
  - Geboortejaar (i.p.v. volledige geboortedatum, t.b.v. privacy)

- Afspraak- en behandelgegevens:
  - Datum en tijd van afspraak
  - Behandeltype
  - Behandeldatum
  - Naam of ID van behandelaar/medewerker
  - Locatie (bij meerdere vestigingen)

- Uitkomst- en kwaliteitsindicatoren:
  - Complicaties (ja/nee + type)
  - Follow-up afspraken (ja/nee + datum)
  - Afgebroken behandelingen (reden)

- Financiële gegevens (optioneel):
  - Tarief/behandelbedrag
  - Betaalstatus

**Configuratie:** Stel velden in onder Settings > Export en kies voor "All records" of "Filtered records" (bv. per maand). Bestandsnaam met tijdsaanduiding: `clinicminds_export_YYYY-MM.csv`.

## 2. Automatisering en beveiliging van de export

1. **Automatisch versturen naar beveiligde locatie (SFTP/FTPS)** — minimaliseer kans op datalekken en voldoe aan ISO9001-eisen rond data-integriteit.
2. **Rechten en toegangen beperken** — enkel geautoriseerde medewerkers toegang; toegangslogboek bijhouden.
3. **Versiebeheer** — archiveer alle maandelijkse exports in versiebeheerstructuur (SharePoint of mappenstructuur met tijdstempels).

## 3. Verwerkingsstappen voor maandelijkse statistieken

1. **Import in BI/rapportagetool** — Microsoft Power BI, Qlik Sense, Tableau of Excel. Gebruik ETL-proces om data te schonen.
2. **Data modelleren:**
   - Tabel Patiënten (geanonimiseerd)
   - Tabel Behandelingen
   - Tabel Financiën

3. **Kernstatistieken:**
   - Volume van behandelingen per behandeltype per maand
   - Complicatieratio: complicaties / totaal behandelingen
   - Doorlooptijden: gemiddelde tijd intake → behandeling → follow-up
   - Declaraties/betalingen
   - Klanttevredenheid (NPS-score)

4. **Visualisatie:** Dashboardoverzichten met trendlijnen, staafdiagrammen per complicatietype, gemiddelde doorlooptijden per behandelaar.

5. **Maandelijks (automatisch) rapport** in PDF-vorm naar kwaliteitsfunctionaris of directie. PDCA-cyclus.

## 4. Koppelen aan andere systemen

1. **CRM/Patient Relationship Management** — synchroniseer patiënt-ID's. Let op AVG/GDPR.
2. **Financiële administratie** — koppeltabel met factuurnummers en patiënt-ID's naar boekhoudsoftware (Exact, AFAS).
3. **Agenda- en planningssysteem** — real-time koppeling behandeldata en patiëntgegevens.

## 5. ISO9001-compliance

1. **Documentatie van processen** — leg het gehele proces vast in kwaliteitsmanagementhandboek. Definieer verantwoordelijkheden (wie exporteert, controleert, accordeert).
2. **Audit-trail** — logboek van elke maandelijkse export (datum, door wie, welke data, eventuele correcties).
3. **Beveiliging & vertrouwelijkheid** — versleutelde omgeving (Secure drive, SharePoint met MFA). Retentieperioden 5-7 jaar conform nationale regelgeving.
4. **Continu verbeteren** — statistieken gebruiken voor verbeterplannen (PDCA-cirkel).

## Samenvatting

- **Exportinstellingen:** Periodieke export CSV/XLSX met essentiële velden (patiënt-ID, behandelingstype, complicaties).
- **Automatisering en beveiliging:** SFTP/FTPS, beperkte rechten, archivering en versiebeheer.
- **Verwerking:** BI-omgeving met dashboards voor kernstatistieken.
- **Koppelingen:** Synchronisatie met CRM, financiële systemen, EPD/agenda.
- **ISO9001-compliance:** Processen, audit-trails en beveiliging geborgd in kwaliteitsmanagementsysteem.

---

*Bijlage: API endpoint-tabel (leeg sjabloon)*

| Datum | Rapport type | URL/Endpoint | Headers | Response format | Opmerkingen |
|-------|-------------|-------------|---------|-----------------|-------------|
| | | | | | |
