# Auditplan 2026 — Kwaliteitssysteem PVI Clinic B.V.

> **Doel:** DEKRA-hercertificeringsaudit doorstaan én een kwaliteitssysteem dat het bedrijf (3 man) echt helpt.
> **Bron-van-waarheid:** markdown in deze repo · Word/PDF = export voor de auditor.
> **Status:** in uitvoering · **Laatst bijgewerkt:** 2026-06-15

---

## Ontwerpprincipes

1. **Markdown = bron, Word/PDF = export.** Eén bron-van-waarheid, versiebeheerd.
2. **Twee lagen.** Document-laag (beleid/SOP's — auditbaar) + operationele laag (taken, registers, monitoring — door Claude bedienbaar). Het systeem ís de borging, niet het papier erover.
3. **Minimale afhankelijkheid van anderen.** Rogier + Claude kunnen elke controle/taak draaien en bewaken; het systeem signaleert wat moet gebeuren in plaats van te vertrouwen op of personeel een reminder oppakt. Dit adresseert precies de hoofdoorzaak van beide tekortkomingen van 2025.
4. **Records = waarheid.** Registraties weerspiegelen wat er echt gebeurde. Wat gedaan is maar niet vastgelegd → leggen we naar waarheid alsnog vast. Verzinnen doen we niet.
5. **Consolideren, niet stapelen.** Bestaande documenten verbeteren; geen nieuwe versies of archieven ernaast.

---

## Audit-context (uit de DEKRA-rapporten)

| Feit | Waarde |
|---|---|
| Certificaat | 2224371 · NEN-EN-ISO 9001:2015 (NL) |
| Scope | Ambulante cosmetische behandelingen, niet-chirurgisch · 3 locaties (Nijmegen hoofd, Enschede, Sittard) · §8.3 n.v.t. |
| Laatste audits | S1 surveillance 24-02-2025 · CAO-beoordeling 08-08-2025 |
| **Volgende audit** | **27-07-2026** (audit nr. 64801) — datum bevestigd. S1 reserveerde oorspronkelijk 3 feb 2026; de audit is verschoven. |
| Lead auditor | M. Smit (DEKRA) |

### Tekortkomingen
- **JOld-48002-2** (§9.2 interne audits) — ✅ **afgesloten** 24-02-2025 (auditprogramma + planning gemaakt). *Let op: auditor toetst of de planning daadwerkelijk gevolgd wordt.*
- **MSm-55640-1** (§8.5.4 verlopen voorraad) — 🔴 **plan geaccepteerd 08-08-2025, maar NOG OPEN**. Wordt **op locatie getoetst** bij de komende audit om af te sluiten. **Dit is het hoofddoel.**

---

## De fasen — strikt één voor één

| # | Fase | Waar het komt te staan | Status |
|---|---|---|---|
| 1 | **Fundament + voorraad §8.5.4** | `02_Procedures/Administratie/SOP_Voorraadbeheer.md` + `07_Voorraad/Voorraadcontrole_register.md` | ✅ klaar |
| 2 | **Directiebeoordeling 2026** | `05_Management/Directiebeoordeling_2026.md` | ✅ klaar (ROGIER-velden ingevuld) |
| 3 | **Doelstellingen 2026** | `Directiebeoordeling_2026.md §9` · `01_Beleid/Kwaliteitsdoelstellingen.md` | ✅ klaar |
| 4 | **Interne audit 2026** | `05_Management/Interne_audit_2026.md` | ✅ klaar |
| 5 | **Verbeterregister + 7 punten** | `03_Registraties/Verbeterregister.md` | ✅ klaar |
| 6 | **SOP's actueel** | `02_Procedures/` (Behandelingen · Risicobeheer · Administratie) | 🔵 V4: afstemmen op wetenschap/Radiance loopt |
| 7 | **Apparatuur + klachten** | `03_Registraties/Apparatuuroverzicht.md` + `Verbeterregister.md` | 🔵 onderhoudsbewijs/leveranciers (A5) |
| 8 | **6 antwoorden auditor** | `06_DEKRA_Audit/Auditvragen_antwoorden_2026.md` + PDF-bijlagen | ✅ **verzonden aan auditor 15-06-2026** |
| 9 | **Eindcheck** | hele repo (document-doorloop + AVG-opschoning jun 2026) | 🔵 loopt |

**Werkwijze: per hefboom prioriteren (impact × moeite); afgeronde fasen worden vastgelegd en gecommit.**

---

## ⚠️ Kritieke consistentie-waarschuwing (§8.5.4)

Het door DEKRA **geaccepteerde** verbeterplan belofte: **maandelijkse** controle (bewijs: maart–juli 2025, 0 verlopen producten).
Maar de beoordeelde SOP heet "v1.0" met **3-maandelijkse** checklist, en de losse SOP v2 zegt **kwartaal**.
→ De auditor legt plan naast SOP. **Kies één frequentie (advies: maandelijks, want dát is geaccepteerd) en maak alles consistent.** Anders ontstaat een nieuwe tekortkoming uit de oude.

---

## De 6 auditor-vragen (vooraf aanleveren)

> ✅ **Alle zes beantwoord en verzendklaar** in [`06_DEKRA_Audit/Auditvragen_antwoorden_2026.md`](06_DEKRA_Audit/Auditvragen_antwoorden_2026.md) (+ PDF-bijlagen). Samengevat:

1. **Grote wijzigingen** afgelopen jaar? → geen structurele; wel digitalisering kwaliteitssysteem + Radiance-positionering.
2. **Calamiteiten / formele klachten / inspectiebezoek** (IGJ)? → alle drie: geen.
3. **FTE = 2,5?** → bevestigd (arts/directeur + doktersassistent + parttime administratie; schoonmaak extern).
4. **Verbetermogelijkheden vorig rapport** opgepakt? → ja, zie 7-puntenlijst hieronder.
5. **Implementatie §8.5.4** → kwartaalcontrole + FIFO + kleine voorraad; 0 verlopen producten.
6. **Management review + doelstellingen 2026** → Directiebeoordeling 2026 (+ §9 doelstellingen).

---

## 7 verbetermogelijkheden uit S1 (24-02-2025)

- [x] 1. Gebruik van lijstjes (o.a. verbeterregister) **door medewerkers** — geborgd in het systeem (PDCA-ronde)
- [x] 2. Klachten ook in een **overzicht** vastleggen (trend) — verbeter-/klachtenregister uit Clinicminds
- [x] 3. Verbeterregister: **vast moment** — PDCA-cyclus + dagelijks overleg
- [x] 4. Periodieke taken in een **kalender/actielijst** — actielijst + ritme
- [ ] 5. **ARBO** opnieuw bezien — 🔵 lichte RI&E opgesteld; maatregelen fysiek bevestigen
- [x] 6. **Apparatuuroverzicht** met controle-eisen — gemaakt; 🔵 onderhoudsbewijs/leveranciers deels
- [x] 7. **Sterilisator**: bewaartermijnen — schriftelijk vastgelegd in F-02 (per 26-07-2026); extern jaarlijks onderhoud (RIVM) nog te regelen, zie apparatuuroverzicht

---

## Eerlijk punt over bewijs

Documenten, SOP's, reviews en antwoorden kan ik opstellen. Het **bewijs** voor §8.5.4 — dat de voorraadcontroles daadwerkelijk lopen — komt uit de praktijk via het [voorraadcontrole-register](07_Voorraad/Voorraadcontrole_register.md). Eerlijk vastgelegd: de registratie was na juli 2025 stilgevallen en is per juni 2026 hervat. We documenteren naar waarheid wat er is; we verzinnen geen controles die niet zijn vastgelegd (ISO vraagt registratie, geen fotobewijs).

---

## Werkwijze
Stap voor stap per fase; Rogier keurt elke fase goed voordat de volgende start. Repo = levende infrastructuur: elke verbetering is een commit, zodat het systeem traceerbaar meegroeit met het bedrijf.
