# Takensysteem — hoe het werkt

> Onderdeel van het [AI-automatiseringsplan](../05_Management/AI_Automatiseringsplan_2026-2027.md) fase 2 (signalering) · Borging van risico [R2](../05_Management/Risicoregister_2026.md) · Ingericht: 26-07-2026

## Het principe

Periodieke taken hangen niet meer op "of iemand eraan denkt". Ze staan in één register, het systeem signaleert ze zelf, en de uitvoering is automatisch traceerbaar.

1. **[takenregister.json](takenregister.json)** — alle periodieke taken met frequentie, eigenaar en het formulier/document waar de registratie hoort.
2. **GitHub Action** ([taken-signalering.yml](../.github/workflows/taken-signalering.yml)) — draait elke ochtend en opent automatisch een **issue** zodra een taak aan de beurt is (maandelijks, per kwartaal, halfjaarlijks of jaarlijks). Dubbele issues worden niet aangemaakt.
3. **Issue sluiten = taak uitgevoerd.** Eerst registreren op het formulier/document, dán het issue sluiten. GitHub legt vast wie het sloot en wanneer — dat gesloten issue is zelf aantoonbaarheid (§7.5): een doorlopend, niet-antedateerbaar logboek van uitgevoerde taken.
4. **Escalatie als het níet gebeurt** ([taken-escalatie.yml](../.github/workflows/taken-escalatie.yml)) — signaleren alleen is niet genoeg, er moet ook opvolging zijn als een taak blijft liggen. Deze workflow draait elke ochtend om 06:00 UTC en mailt op vaste momenten:

| Dagen open | Mail naar | Strekking |
|---|---|---|
| 3 | eigenaar | herinnering |
| 7 | eigenaar + directeur | tweede herinnering |
| 14, daarna wekelijks | eigenaar + directeur | escalatie |

Elke verzonden mail wordt als comment op het issue gezet (met datum en ontvangers). Daardoor is achteraf te zien niet alleen dát een taak te laat was, maar ook dat erop is gerappelleerd — en door wie hij uiteindelijk is afgerond.

## Eenmalige acties met een deadline

Niet alles is terugkerend. Onderzoeks- en verbeteracties hebben een einddatum en gebeuren daarna nooit meer — en juist die vielen buiten het systeem: ze stonden alleen in de [actielijst](../03_Registraties/Actielijst.md), waar niemand een signaal van krijgt. Op 27-07-2026 bleek dat drie deadlines ongemerkt waren verstreken.

Daarom kan een taak nu ook `"frequentie": "eenmalig"` hebben met een `"deadline"` (JJJJ-MM-DD):

- het issue wordt standaard **14 dagen vóór de deadline** geopend — met `"vooraf"` is dat per actie in te stellen, bijvoorbeeld 60 dagen voor iets dat uitzoekwerk vraagt;
- in het issue staat hoeveel dagen er nog zijn, en na de deadline hoeveel dagen die verstreken is;
- de escalatie werkt er hetzelfde op als op terugkerende taken: eerst de eigenaar, daarna de directeur erbij.

Zo lopen eenmalige acties door dezelfde signalering en escalatie als de rest, in plaats van in een lijst te blijven staan die niemand op tijd naleest.

## Uitvoerders zonder GitHub-account

Niet iedereen werkt in GitHub. De escalatiemail bevat daarom een **afvinkknop**: één klik opent een vooringevulde afmelding aan de directeur met de taak, de periode en het formulier erbij. De volgorde blijft: eerst registreren op het formulier — dat is het bewijs — dan afmelden. De directeur sluit het issue.

**E-mailadressen staan bewust niet in dit register.** Per taak verwijst het veld `email_var` naar de naam van een GitHub-variabele (bijvoorbeeld `EMAIL_MOUMEN`); het adres zelf staat in de repository-instellingen. Zo staan er geen persoonsgegevens in de broncode of in de historie. Ontbreekt de variabele, dan gaat de mail naar de directeur — een taak valt dus nooit stil door een ontbrekend adres.

## Taken erin of eruit

Taak toevoegen/wijzigen = één bewerking in `takenregister.json` (met commit, dus met datum en auteur). De eerstvolgende ochtendrun pikt het op.

## Voor de auditor

De vraag "hoe borgt u dat periodieke taken gebeuren?" wordt beantwoord met: register → automatische signalering → issue → **mail naar de uitvoerder** → registratie op formulier → afmelding → gesloten issue met datum/naam. Blijft het uit, dan escaleert het systeem vanzelf naar de directeur. De volledige historie is in GitHub terug te bladeren en achteraf niet aan te passen zonder spoor.

De tweede vraag die daarop volgt — "en wat als het dan nóg niet gebeurt?" — is beantwoord met de escalatietabel hierboven: de taak blijft open staan, de herinneringen blijven komen en ze staan zichtbaar op het issue. Een taak die blijft liggen wordt daardoor zelf een bevinding, in plaats van stilletjes te verdwijnen.

*Let op: de dagelijkse run start pas zodra dit op de hoofdbranch (`main`) staat — GitHub voert geplande workflows alleen vanaf de standaardbranch uit. Tot die tijd kan de workflow handmatig gestart worden via de Actions-tab.*
