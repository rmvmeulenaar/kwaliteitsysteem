# Takensysteem — hoe het werkt

> Onderdeel van het [AI-automatiseringsplan](../05_Management/AI_Automatiseringsplan_2026-2027.md) fase 2 (signalering) · Borging van risico [R2](../05_Management/Risicoregister_2026.md) · Ingericht: 26-07-2026

## Het principe

Periodieke taken hangen niet meer op "of iemand eraan denkt". Ze staan in één register, het systeem signaleert ze zelf, en de uitvoering is automatisch traceerbaar.

1. **[takenregister.json](takenregister.json)** — alle periodieke taken met frequentie, eigenaar en het formulier/document waar de registratie hoort.
2. **GitHub Action** ([taken-signalering.yml](../.github/workflows/taken-signalering.yml)) — draait elke ochtend en opent automatisch een **issue** zodra een taak aan de beurt is (maandelijks, per kwartaal, halfjaarlijks of jaarlijks). Dubbele issues worden niet aangemaakt.
3. **Issue sluiten = taak uitgevoerd.** Eerst registreren op het formulier/document, dán het issue sluiten. GitHub legt vast wie het sloot en wanneer — dat gesloten issue is zelf aantoonbaarheid (§7.5): een doorlopend, niet-antedateerbaar logboek van uitgevoerde taken.

## Taken erin of eruit

Taak toevoegen/wijzigen = één bewerking in `takenregister.json` (met commit, dus met datum en auteur). De eerstvolgende ochtendrun pikt het op.

## Voor de auditor

De vraag "hoe borgt u dat periodieke taken gebeuren?" wordt beantwoord met: register → automatische signalering → issue → registratie op formulier → gesloten issue met datum/naam. De volledige historie is in GitHub terug te bladeren en achteraf niet aan te passen zonder spoor.

*Let op: de dagelijkse run start pas zodra dit op de hoofdbranch (`main`) staat — GitHub voert geplande workflows alleen vanaf de standaardbranch uit. Tot die tijd kan de workflow handmatig gestart worden via de Actions-tab.*
