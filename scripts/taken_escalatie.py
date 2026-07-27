#!/usr/bin/env python3
"""
Escalatie op openstaande periodieke taken.

De taken-signalering opent elke ochtend een issue zodra een taak aan de beurt is.
Dit script bewaakt wat er daarna gebeurt: blijft een taak te lang open staan, dan
krijgt de eigenaar een mail — en bij aanhoudend uitblijven ook de directeur.
Zo hangt niet alleen de signalering, maar ook de opvolging los van iemands geheugen.

Ritme (dagen na aanmaken van het issue):
  dag  3  herinnering        -> eigenaar
  dag  7  tweede herinnering -> eigenaar + directeur
  dag 14  escalatie          -> eigenaar + directeur, daarna elke 7 dagen opnieuw

Per verzonden niveau plaatst het script een markeringscomment op het issue
(<!-- escalatie:dN -->). Dat voorkomt dubbele mails en levert tegelijk een
traceerbaar spoor op: op het issue zelf is terug te zien wanneer er is gerappelleerd.

Afvinken zonder GitHub-account: de mail bevat een afvinkknop (mailto) die een
vooringevulde afmelding naar de directeur opent. Registreren op het formulier
gaat vóór; de afmelding is de melding dát het gebeurd is.

Env: GITHUB_TOKEN, GITHUB_REPOSITORY, RESEND_API_KEY,
     EMAIL_DIRECTEUR (default info@praktijkvoorinjectables.nl),
     EMAIL_* per taak zoals aangeduid met "email_var" in taken/takenregister.json,
     DRY_RUN (default 0).
"""
import os, json, datetime, urllib.request, urllib.parse, urllib.error

TOKEN     = os.environ["GITHUB_TOKEN"]
REPO      = os.environ["GITHUB_REPOSITORY"]           # "owner/repo"
RESEND    = os.environ.get("RESEND_API_KEY", "")
DIRECTEUR = os.environ.get("EMAIL_DIRECTEUR") or "info@praktijkvoorinjectables.nl"
FROM      = os.environ.get("TAKEN_FROM", "Kwaliteitssysteem PVI <info@radianceclinic.nl>")
DRY_RUN   = os.environ.get("DRY_RUN", "0") == "1"
LABEL     = "periodieke-taak"
REPO_URL  = f"https://github.com/{REPO}"
UA        = "Mozilla/5.0 (compatible; PVI-Kwaliteitssysteem/1.0)"

NIVEAUS = {
    3:  ("herinnering",        "Herinnering"),
    7:  ("tweede-herinnering", "Tweede herinnering"),
    14: ("escalatie",          "Escalatie"),
}


def api(pad, method="GET", data=None):
    url = pad if pad.startswith("http") else f"https://api.github.com{pad}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": UA,
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r) if r.status != 204 else None


def open_taakissues():
    issues, pagina = [], 1
    while True:
        blok = api(f"/repos/{REPO}/issues?labels={LABEL}&state=open&per_page=100&page={pagina}")
        if not blok:
            break
        issues += [i for i in blok if "pull_request" not in i]
        if len(blok) < 100:
            break
        pagina += 1
    return issues


def niveau_voor(leeftijd):
    """Welk escalatieniveau hoort bij deze leeftijd in dagen? None = nu niets sturen."""
    if leeftijd in NIVEAUS:
        return leeftijd
    if leeftijd >= 14 and leeftijd % 7 == 0:
        return leeftijd          # na dag 14 elke week opnieuw
    return None


def al_verstuurd(nummer, dag):
    comments = api(f"/repos/{REPO}/issues/{nummer}/comments?per_page=100")
    merk = f"<!-- escalatie:d{dag} -->"
    return any(merk in (c.get("body") or "") for c in comments)


def taak_bij_issue(register, titel):
    """Titel is '[Taak] <naam> — <periode>'; match op naam."""
    for taak in register["taken"]:
        if f"[Taak] {taak['naam']} —" in titel:
            return taak
    return None


def ontvangers(taak, dag):
    adres = ""
    if taak and taak.get("email_var"):
        adres = (os.environ.get(taak["email_var"]) or "").strip()
    naar = [adres] if adres else []
    if dag >= 7 or not naar:                 # vanaf dag 7 gaat de directeur mee
        if DIRECTEUR not in naar:
            naar.append(DIRECTEUR)
    return naar


def mail_html(taak, issue, dag, label):
    naam     = taak["naam"] if taak else issue["title"]
    eigenaar = taak.get("eigenaar", "—") if taak else "—"
    doc      = f"{REPO_URL}/blob/main/{taak['link']}" if taak else REPO_URL
    onderwerp_afvink = urllib.parse.quote(f"AFGEVINKT: {issue['title']}")
    body_afvink = urllib.parse.quote(
        f"Deze taak is uitgevoerd en geregistreerd.\n\n"
        f"Taak: {issue['title']}\n"
        f"Uitgevoerd door: \nDatum: \n"
        f"Geregistreerd op: {taak['link'] if taak else '—'}\n\n"
        f"Issue: {issue['html_url']}\n"
    )
    afvink = f"mailto:{DIRECTEUR}?subject={onderwerp_afvink}&body={body_afvink}"
    omschrijving = taak.get("omschrijving", "") if taak else ""
    return f"""<p>Hallo {eigenaar},</p>
<p><b>{label}</b> — deze periodieke taak staat sinds {dag} dagen open:</p>
<h3 style="margin-bottom:4px">{naam}</h3>
<p style="margin-top:0;color:#555">{omschrijving}</p>
<p><b>Zo werk je hem af:</b></p>
<ol>
  <li>Voer de taak uit en <b>registreer het resultaat</b> op het formulier:
      <a href="{doc}">{taak['link'] if taak else 'kwaliteitssysteem'}</a></li>
  <li>Klik daarna op de knop hieronder om af te melden.</li>
</ol>
<p style="margin:24px 0">
  <a href="{afvink}" style="background:#0e8a16;color:#fff;padding:12px 22px;
     border-radius:6px;text-decoration:none;font-weight:bold">✅ Afgevinkt — melden</a>
</p>
<p style="font-size:13px;color:#666">Registreren gaat vóór afmelden: het formulier is het bewijs,
de afmelding is het signaal dat het gebeurd is.</p>
<hr>
<p style="font-size:12px;color:#888">
  Taak uit het <a href="{REPO_URL}/blob/main/taken/takenregister.json">takenregister</a> ·
  <a href="{issue['html_url']}">issue {issue['number']}</a> ·
  automatische bewaking van het kwaliteitssysteem (ISO 9001 §7.5)
</p>"""


def verstuur(naar, onderwerp, html):
    payload = {"from": FROM, "to": naar, "subject": onderwerp, "html": html}
    req = urllib.request.Request("https://api.resend.com/emails", data=json.dumps(payload).encode(),
        method="POST", headers={"Authorization": f"Bearer {RESEND}",
                                "Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    register = json.load(open("taken/takenregister.json", encoding="utf-8"))
    vandaag = datetime.datetime.now(datetime.timezone.utc)
    issues = open_taakissues()
    print(f"{len(issues)} open taak-issue(s) gevonden.")

    verzonden = 0
    for issue in issues:
        aangemaakt = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ") \
                       .replace(tzinfo=datetime.timezone.utc)
        dag = (vandaag - aangemaakt).days
        niveau = niveau_voor(dag)
        if niveau is None:
            continue
        if al_verstuurd(issue["number"], dag):
            continue

        taak = taak_bij_issue(register, issue["title"])
        _, label = NIVEAUS.get(dag, ("escalatie", "Escalatie"))
        naar = ontvangers(taak, dag)
        onderwerp = f"[{label}] {issue['title']} — staat {dag} dagen open"
        html = mail_html(taak, issue, dag, label)

        print(f"→ {label} (dag {dag}) voor issue #{issue['number']} naar {', '.join(naar)}")
        if DRY_RUN:
            continue
        if not RESEND:
            raise SystemExit("RESEND_API_KEY ontbreekt — escalatiemail kon niet worden verstuurd.")
        verstuur(naar, onderwerp, html)
        api(f"/repos/{REPO}/issues/{issue['number']}/comments", "POST", {
            "body": f"<!-- escalatie:d{dag} -->\n"
                    f"📬 **{label} verstuurd** op {vandaag:%d-%m-%Y} naar: {', '.join(naar)}. "
                    f"Taak staat {dag} dagen open."
        })
        verzonden += 1

    print(f"✓ Klaar — {verzonden} escalatiemail(s) verstuurd." if not DRY_RUN
          else "DRY-RUN — niets verstuurd.")


if __name__ == "__main__":
    main()
