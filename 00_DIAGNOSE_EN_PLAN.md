# Diagnose & Opschoonplan — Kwaliteitssysteem PVI

> **Status:** concept ter goedkeuring · **Datum:** 2026-06-15 · **Auteur:** Claude (in opdracht R. Meulenaar)
> **Vangnet:** lokale git-repo aangemaakt (snapshot-commit vóór elke wijziging). **Geen remote** — dit systeem bevat arbeidscontracten, AVG-/patiëntdata en personeelsgegevens; niets gaat online zonder expliciet akkoord.

---

## 0. Conclusie eerst

Het kwaliteitssysteem is **niet kapot — het is een half-afgemaakte migratie.** De structuur (`01_Beleid` … `07_Voorraad`) is een logische, audit-bestendige indeling. De wanorde zit in vier dingen, die ik allemaal heb teruggebracht tot concrete beslissingen in §4:

1. **Versie-wildgroei** — dezelfde SOP in 2–5 afwijkende kopieën, zonder dat één "de geldende" is.
2. **Verdwaalde bestanden** — `06_DEKRA_Audit` is een vergaarbak met inhoud die in `02`/`07` hoort.
3. **Stubs & lege pointers** — uit Drive meegekopieerde verwijsbestandjes zonder eigen inhoud.
4. **md/docx door elkaar** — geen afspraak over wat de bron is en wat de export.

Daarbovenop ontbreekt een **masterindex** en is de **DEKRA-tekortkoming (§8.5.4)** het scharnierpunt waar alles om draait — dat verhoogt de inzet van het voorraad-dossier.

**Aanpak:** vier fasen (§5). Fase 1 (dit document) is af. Fase 2 (opschonen) kan direct, want elke stap is via git terug te draaien. **Embedden + monitoren is bewust geparkeerd** (§6).

---

## 1. Wat er staat (feiten)

- **64 bestanden** in de nieuwe structuur (`01`–`07`), **77 bestanden** in `_Archief_oude_structuur` (grotendeels een 1-op-1 Google Drive-export met diepe nesting).
- Formaten: 127 × `.md`, 13 × `.docx`, 1 × `.pdf`.
- De nieuwe structuur is een **herordening + hernoeming** van de Drive-export. De migratie heeft documenten gekopieerd **inclusief** stubs, lege docs en dubbele varianten — zonder de "welke versie geldt"-beslissingen te nemen. Dát is de puinhoop.

---

## 2. De vier probleemclusters (bewijs)

### 2.1 Versie-wildgroei
| Onderwerp | Kopieën aangetroffen | Welke geldt | Bewijs |
|---|---|---|---|
| **Voorraadbeheer SOP** | `02/SOP_Voorraadbeheer.md` (v1, maandelijks) · `02/SOP_Voorraadbeheer_v2.md` (kwartaal) · `06/SOP_Voorraadbeheer_v2.md` (kwartaal + Drive-metadata) · + 3 varianten in archief | **v2 (kwartaal)** | v1-header zegt zelf: *"oudere maandelijkse variant, zie 5) SOP voor de actuele kwartaalversie."* v2 is het product van het §8.5.4-correctieplan. |
| **AVG** | `02/Administratie/SOP_AVG_compliance.md` (93 r, 12 ISO-hoofdstukken) · `02/SOP_AVG_patientgegevens.md` (43 r, kort stappenplan) | **compliance-versie** (lang), korte versie samenvoegen | Headings vergeleken: de lange dekt alles van de korte + datalekken, bewaartermijnen, verwerkers, monitoring. |

### 2.2 Verdwaalde bestanden in `06_DEKRA_Audit`
| Bestand | Hoort in | Reden |
|---|---|---|
| `Voorraad_inventarisatie.md` (212 r) | `07_Voorraad` | Is een register, geen auditcorrespondentie. |
| `Lijst_injectables.md` (27 r) | `07_Voorraad` | Idem. |
| `SOP_Voorraadbeheer_v2.md` | `02_Procedures` | Duplicaat van de geldende SOP. |
| `INDEX_oud.md` (189 r) | *verwijderen* | Verouderd; vervangen door `00_INDEX.md`. |

### 2.3 Stubs & lege pointers
| Bestand | Wat het is | Actie |
|---|---|---|
| `01_Beleid/Kernprotocollen.md` (7 r) | Pointer: *"woordelijk identiek aan H8–12 van Kwaliteitsbeleid.md"* | Verwijderen; vervangen door een verwijzing in de index. |
| `01_Beleid/PVI_methode_actueel.md` (4 r) | Pointer naar een **leeg** Google Doc | Vervangen door de echte actuele PVI-methode uit het archief (`PVI-methode_23-02-2025.md`). |

### 2.4 md/docx-dualiteit
Patroon: de **definitieve/verstuurde stukken staan als `.docx`** in de nieuwe structuur, maar hun **`.md`-bronnen liggen nog in het archief** (`02_Directiebeoordeling_2026_voorzet.md`, `03_Interne_audit_2026_werkdocument.md`, `04_Risicoregister_2026.md`, `05_Voorraadcontrole_register.md`). Daardoor weet niemand wat de bron is.

**Aanbeveling (architectuurbeslissing — zie §3):** **Markdown = bron** voor alle levende documenten; **docx/pdf = export** voor wat naar buiten gaat.

---

## 3. Doelstructuur & formaatprincipe

```
00_INDEX.md                  ← masterindex (nieuw): wat geldt, waar, welke versie, status
00_DIAGNOSE_EN_PLAN.md       ← dit stuurdocument
01_Beleid/                   ← beleid & fundament (Kwaliteitsbeleid H1–12, doelstellingen, methode…)
02_Procedures/               ← SOP's, in submappen Behandelingen / Administratie / Risicobeheer
03_Registraties/             ← levende registers (KPI, verbeterregister, incidenten, controles)
04_Personeel/                ← contracten, functiebeschrijvingen, sjablonen (_Archief = oud-team)
05_Management/               ← directiebeoordeling, interne audit, risicoregister (per jaar)
06_DEKRA_Audit/              ← uitsluitend auditcorrespondentie + tekortkoming + bewijs
07_Voorraad/                 ← voorraadregisters & inventarisaties (NIET de SOP)
_Archief_oude_structuur/     ← bevroren; bronbewijs en historie, wordt niet meer bewerkt
```

**Formaatprincipe (single source of truth):**
- **Markdown is de bron** — versiebeheerbaar (git), leesbaar, en straks direct embedbaar voor zoeken/monitoren.
- **docx/pdf zijn exports** — alleen voor externe communicatie (auditbrieven) of een nette uitdraai. De `.md`-bron leeft mee; de export wordt opnieuw gegenereerd wanneer nodig.
- **Scheiding procedure ↔ registratie:** een *SOP* (hoe het hoort) staat in `02`; het *register/de uitvoering* (wat er gedaan is) staat in `03` of `07`.

---

## 4. Beslissingenregister (opschoonacties)

Legenda: ✅ = veilig, voer ik uit · 🟡 = vraagt jouw akkoord (inhoud/oordeel) · 📦 = archiveren (niets gaat verloren)

| # | Actie | Type |
|---|---|---|
| 1 | Voorraad: **v2 wordt de enige** `SOP_Voorraadbeheer.md` (in `02/.../`), met de rijke metadata-header van de 06-kopie. | ✅ |
| 2 | Voorraad v1 (maandelijks) → 📦 archief als *bewijs van de "was"-situatie* vóór de §8.5.4-correctie. | ✅📦 |
| 3 | Voorraad-kopie in `06` → verwijderen (duplicaat van #1). | ✅ |
| 4 | `Voorraad_inventarisatie.md` + `Lijst_injectables.md` → verplaatsen naar `07_Voorraad`. | ✅ |
| 5 | AVG: lange compliance-SOP wordt leidend; korte versie eerst checken op uniek stappenplan, dan 📦. | 🟡 (ik check inhoud) |
| 6 | Losse SOP's in `02`-root naar submappen: Klachten→Risicobeheer, AVG→Administratie, Intake→Behandelingen. | ✅ |
| 7 | `Kernprotocollen.md` (stub) → verwijderen, vervangen door verwijzing in `00_INDEX.md`. | ✅ |
| 8 | `PVI_methode_actueel.md` (leeg) → vervangen door actuele methode uit archief. | ✅ |
| 9 | `INDEX_oud.md` → verwijderen na bouw `00_INDEX.md`. | ✅ |
| 10 | `Tekortkoming_ISO854.md` → hernoemen naar `Tekortkoming_8.5.4_verlopen_producten.md`. | ✅ |
| 11 | md/docx: `.md`-bronnen van de 2026-managementdocs uit archief naar `05`; docx als export behandelen. | 🟡 (hangt aan §3) |
| 12 | `00_INDEX.md` bouwen: tabel met document, locatie, versie/datum, status, ISO-koppeling. | ✅ |

---

## 5. Fasering

| Fase | Inhoud | Status |
|---|---|---|
| **1. Diagnose & plan** | Dit document + git-vangnet | ✅ klaar |
| **2. Opschonen & herordenen** | Beslissingen §4 uitvoeren + masterindex | ▶ klaar om te starten |
| **3. DEKRA-compleetheid** | Inhoudelijke gap-check tegen ISO 9001 / DEKRA-eisen; is de §8.5.4-correctie aantoonbaar? Openstaand punt: **maandelijks vs. kwartaal** controle — verdedigbaar? | gepland |
| **4. Beter maken** | Inhoudelijke kwaliteit van SOP's/beleid verhogen; consistentie, volledigheid, versiebeheer-discipline | gepland |
| *(later)* **5. Embedden + monitoren** | Zie §6 — bewust geparkeerd | geparkeerd |

---

## 6. Geparkeerd: embedden & monitoren (later)

Rogier's wens: *"zaken embedden … en monitoren van alle zaken, door embedden (dit moet later)."*

Dit wordt pas zinvol **ná** fase 2–4, omdat embedden op een rommelige bron rommel oplevert. Richting (nog niet uitvoeren):
- Markdown-bron → vector-embeddings → doorzoekbaar/bevraagbaar kwaliteitssysteem ("wat is onze SOP bij datalek?").
- Monitoring: KPI's en registers (incidenten, voorraadcontroles, verbeterregister) automatisch volgen en signaleren bij afwijking/achterstand.
- Hoort thuis in een aparte repo/pipeline (conform projectregels), niet in deze documentenmap.

---

## 7. Beperkingen van deze diagnose (eerlijkheid)

- **`.docx`/`.pdf`-inhoud is niet gelezen** (binformaat) — alleen bestandsnamen/locaties beoordeeld. Inhoudelijke beoordeling daarvan volgt in fase 3/4 of na conversie naar md.
- Het **archief** is op bestandsnaam-niveau geïnventariseerd, niet elk bestand inhoudelijk. Voor migratie-volledigheid (staat er nog iets uniek in het archief?) is een gerichte vergelijking nodig — opgenomen in fase 2.
- "Welke versie geldt" is bepaald op basis van **expliciete aanwijzingen in de documenten zelf** (headers, datums, het §8.5.4-correctieplan), niet op een externe bron. Waar twijfel: gemarkeerd 🟡.
