# PDCA-logboek — Kwaliteitssysteem PVI

> De verbetercyclus van de praktijk. **Werkwijze:** Rogier logt periodiek in → Claude bekijkt de repo-stand en noteert de voortgang (Check) → samen Check + Act (beslissen/bijsturen) → vastleggen. Zo is het kwaliteitssysteem een levende PDCA-cyclus (ISO 9001 §10).
>
> **Plan** = doelen/acties (auditplan + actielijst) · **Do** = uitvoeren (Claude + Rogier) · **Check** = voortgang beoordelen (hieronder) · **Act** = bijsturen/besluiten.

---

## Ronde 2026-06-15 — opzet kwaliteitssysteem

**Check (stand):**
- ✅ Fases 1–3 af: voorraad §8.5.4 · directiebeoordeling 2026 · interne audit 2026 · risicoregister 2026
- ✅ Operationele laag draait: Clinicminds live · klanttevredenheidsmeting (kwartaal, dry-run) · weekstart-cron
- ✅ Cockpit + wegwijzer + afvink-issue
- ✅ A1 beleid · A2 risicoregister · A4 verbeter-/klachtenregister · interne scope-check (R10, besluit hieronder)
- 🔵 In uitvoering (fysieke uitvoering Rogier): A3 voorraadcontrole · A5 apparatuurbewijs · A6 RI&E-maatregelen bevestigen · A7 nascholing (GAIA)

**Act (besluiten/bijsturen):**
- Werkwijze vastgesteld: PDCA via inlog-sessies. **Per ronde prioriteren op hefboom (impact × moeite)** — de grootste hefboom eerst, geen mechanische afvinklijst.
- **Scope-check ingebracht als prioriteit** (zie onder) → besluit aan directie.

**Hefbomen nu (slimste eerst):**
| Hefboom | Impact | Moeite | Wie |
|---|---|---|---|
| Interne scope-check (R10) — besloten: buiten certificaat houden | hoog | laag | Rogier ✅ |
| A4 verbeter-/klachtenregister automatiseren (Clinicminds) | midden-hoog | midden | Claude |
| Tevredenheidsmailing live zetten | midden | laag | Rogier |
| A6 RI&E-notitie | midden | laag | Claude |
| A1 beleid actualiseren | midden | midden | samen |

---

## Ronde 2026-07-26 — auditvoorbereiding + softwareprojecten als vast punt

**Check (stand):**
- ✅ Directiebeoordeling 2026 aangevuld: §6 risico's en kansen (§9.3.2e), actuele klanttevredenheidscijfers, adrescorrectie
- ✅ Risicoregister: R13 (onbeheerste AI-inzet) toegevoegd, R6 gesloten, R9 gedekt
- ✅ Koelkasttemperatuurregistratie 2025 aangeleverd en geregistreerd (52 wekelijkse controles); doorlopende registratie live via Google-formulier
- ✅ Takensysteem live: takenregister + dagelijkse signalering via issues (AI-plan fase 2)
- ✅ Formulieren F-01 t/m F-09 + overzicht; auditdossier compleet (simulatie, navigator, ophaallijst)
- 🔵 Open richting audit: originele koelkastlijsten 2025 bijleggen, fysieke voorraadrondgang, servicerapporten 4 apparaten

**Act (besluiten):**
- **Softwareprojecten zijn vanaf nu een vast punt in elke PDCA-ronde.** De eigen ontwikkeling (automatisering, agents, vervanging abonnementen) is een kwaliteitsproces als elk ander: elk project heeft een doel, een status en een evaluatiemoment, en wijzigingen lopen als beheerste wijziging (§6.3) — kader in het [AI-automatiseringsplan](AI_Automatiseringsplan_2026-2027.md), risicokant in R13.
- Gefabriceerd ogende registraties worden niet in het dossier opgenomen; herkomst van digitale overzettingen wordt altijd expliciet vermeld (besluit n.a.v. auditvoorbereiding 26-07).

### Vast punt: softwareprojecten & automatisering (stand 26-07-2026)

| Project | Doel | Status | Volgende Check |
|---|---|---|---|
| Kwaliteitsysteem-repo (GitHub) | één bron, versiebeheer §7.5 | **live** | Q4 2026 |
| Taken-signalering (cron + issues) | borging R2, periodieke taken | **live 26-07** — activeert op main na merge | Q4 2026 |
| Digitale registraties (Google Forms) | koelkast ✅ · klanttevredenheid ✅ · voorraad/hygiëne volgen | deels live | Q4 2026 |
| Werkbesprekings-agent (agenda + verslag) | overlegverslagen structureel (ophaalpunt 12) | plan (fase 3) | Q4 2026 |
| Interne-audit-agent | documentcontrole + consistentiechecks, arts stelt vast | plan (fase 4, 2027) | bij audit 2027 |
| AI-mailbot | klantcommunicatie | **stilgelegd na datalek 2025** — herstart alleen onder R13-spelregels | bij herstart |
| Eigen software i.p.v. abonnementen | kostenverlaging, minder leveranciersafhankelijkheid | plan (fase 5, doelstelling 8) | 2027 |

---

## ⚠️ Bevinding: certificaatscope vs. dienstenaanbod (R10 / A1)

**Situatie:** het certificaat (2224371) dekt *"het uitvoeren van ambulante cosmetische behandelingen, niet-chirurgisch"*. De praktijk biedt echter ook **TRT** (testosteronvervangende therapie), **GLP-1 / gewichtsverlies** en **bio-identieke hormonen (BHT)** aan — dat zijn *medische/endocriene* behandelingen, geen puur cosmetische.

**Beoordeling:** deze diensten vallen waarschijnlijk **buiten** de huidige gecertificeerde scope. Twee mogelijkheden:
1. Ze blijven **buiten** het ISO-certificaat (toegestaan, mits je niet claimt dat ze ISO-gecertificeerd zijn).
2. De **scope wordt verbreed** en aan DEKRA gemeld.

**Besluit directie (Rogier, jun 2026):** de scope wordt **intern beheerd** (risico R10) — er wordt **niet proactief** contact opgenomen met DEKRA hierover. De medische/endocriene diensten (TRT, GLP-1, BHT) blijven vooralsnog **buiten** het ISO-certificaat (optie 1); ze worden niet als ISO-gecertificeerd geclaimd. Komt het op de auditdag ter sprake, dan lichten we het transparant toe. Verbreding van de scope is een latere, aparte afweging.
