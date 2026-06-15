#!/usr/bin/env python3
"""
Kwartaal-tevredenheidsmailing — PVI / Radiance Clinic.

Wat het doet:
  1. Haalt uit Clinicminds de patiënten op die het afgelopen kwartaal een behandeling hadden (met e-mail + locatie).
  2. Haalt uit Typeform op wie al heeft ingevuld (via verborgen veld 'pid' = patiëntnummer).
  3. Mailt via Resend de rest een persoonlijke tevredenheidslink — met de juiste afzender per locatie.

Veiligheid (cost-/privacy-guards):
  - DRY_RUN=1 (STANDAARD): verstuurt NIETS, logt alleen geaggregeerde aantallen.
  - TEST_SEND=1: stuurt één testmail naar TEST_TO (eigen adres), niet naar patiënten.
  - LIVE pas bij DRY_RUN=0. MAX_MAILS begrenst het aantal per run.
  - Logt nooit e-mailadressen/namen — alleen aantallen.

Env: CLINICMINDS_API_TOKEN, TYPEFORM_TOKEN, RESEND_API_KEY,
     TYPEFORM_FORM_KLANTTEVREDENHEID (default Eb1d7tgh),
     DRY_RUN (default 1), TEST_SEND (default 0), TEST_TO, MAX_MAILS (default 300), QUARTER_DAYS (default 95).
"""
import os, json, sys, datetime, urllib.request, urllib.parse, urllib.error

CM_TOKEN = os.environ["CLINICMINDS_API_TOKEN"]
CM_BASE  = os.environ.get("CLINICMINDS_API_BASE", "https://app.clinicminds.com/api/analytics")
TF_TOKEN = os.environ["TYPEFORM_TOKEN"]
FORM_ID  = os.environ.get("TYPEFORM_FORM_KLANTTEVREDENHEID", "Eb1d7tgh")
RESEND   = os.environ["RESEND_API_KEY"]

DRY_RUN   = os.environ.get("DRY_RUN", "1") != "0"
TEST_SEND = os.environ.get("TEST_SEND", "0") == "1"
TEST_TO   = os.environ.get("TEST_TO", "info@praktijkvoorinjectables.nl")
MAX_MAILS = int(os.environ.get("MAX_MAILS", "300"))
QUARTER_DAYS = int(os.environ.get("QUARTER_DAYS", "95"))

FORM_URL = f"https://form.typeform.com/to/{FORM_ID}"
PVI_LOCATIES = ("enschede", "sittard")  # -> Praktijk voor Injectables; rest -> Radiance
UNSUB = "mailto:info@radianceclinic.nl?subject=afmelden%20tevredenheid"
UA = "Mozilla/5.0 (compatible; PVI-Kwaliteitssysteem/1.0)"  # Cloudflare blokkeert de default Python-useragent

def _get(url, headers):
    headers = {"User-Agent": UA, **headers}
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60))

def cm(path):
    return _get(f"{CM_BASE}/{path}&format=json", {"X-Api-Key": CM_TOKEN})

def rows(d):
    if isinstance(d, list): return d
    if isinstance(d, dict): return d.get("data") or next((v for v in d.values() if isinstance(v, list)), [])
    return []

def reeds_ingevuld():
    """Patiëntnummers (pid) die het formulier al invulden."""
    d = _get(f"https://api.typeform.com/forms/{FORM_ID}/responses?page_size=1000",
             {"Authorization": f"Bearer {TF_TOKEN}"})
    return {str(it.get("hidden", {}).get("pid")) for it in d.get("items", []) if it.get("hidden", {}).get("pid")}

def afzender(locatie):
    loc = (locatie or "").lower()
    if any(x in loc for x in PVI_LOCATIES):
        return "Praktijk voor Injectables", "praktijkvoorinjectables@radianceclinic.nl"
    return "Radiance Clinic", "info@radianceclinic.nl"

def mail_html(naam, link):
    hi = f"Beste {naam}," if naam else "Beste cliënt,"
    return f"""<p>{hi}</p>
<p>Je bent recent bij ons geweest voor een behandeling. We willen onze zorg continu verbeteren en horen graag hoe je je ervaring vond — het invullen duurt ongeveer 1 minuut.</p>
<p><a href="{link}">Klik hier om de korte vragenlijst in te vullen</a></p>
<p>Hartelijk dank!<br>Met vriendelijke groet</p>
<hr><p style="font-size:12px;color:#888">Geen tevredenheidsmails meer ontvangen? <a href="{UNSUB}">Afmelden</a>.</p>"""

def verstuur(to, sender_name, sender_email, html):
    body = {"from": f"{sender_name} <{sender_email}>", "to": [to],
            "subject": "Hoe was je ervaring bij ons? (1 minuut)",
            "html": html, "headers": {"List-Unsubscribe": f"<{UNSUB}>"}}
    req = urllib.request.Request("https://api.resend.com/emails", data=json.dumps(body).encode(),
            method="POST", headers={"Authorization": f"Bearer {RESEND}", "Content-Type": "application/json", "User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=30))

def main():
    vandaag = datetime.date.today()
    d_from = (vandaag - datetime.timedelta(days=QUARTER_DAYS)).isoformat()
    d_to = vandaag.isoformat()
    print(f"== Tevredenheidsmailing == periode {d_from} t/m {d_to} | "
          f"modus: {'DRY-RUN' if DRY_RUN else ('TEST' if TEST_SEND else 'LIVE')}")

    behandeld = rows(cm(f"treatments?date_from={d_from}&date_to={d_to}"))
    patienten = rows(cm(f"patients-with-treatment?date_from={d_from}&date_to={d_to}"))
    locatie_van = {}
    for t in behandeld:
        locatie_van.setdefault(t.get("Patiëntnummer"), t.get("Locatie", ""))
    al_gedaan = reeds_ingevuld()

    doelgroep = []
    overgeslagen_ingevuld = geen_email = 0
    for p in patienten:
        pid = p.get("Patiëntnummer"); email = (p.get("E-mailadres") or "").strip()
        if not email or "@" not in email: geen_email += 1; continue
        if str(pid) in al_gedaan: overgeslagen_ingevuld += 1; continue
        sn, se = afzender(locatie_van.get(pid))
        link = f"{FORM_URL}?pid={urllib.parse.quote(str(pid))}"
        doelgroep.append({"pid": pid, "email": email, "naam": p.get("Voornaam", ""),
                          "sender_name": sn, "sender_email": se, "html": mail_html(p.get("Voornaam", ""), link)})

    pvi = sum(1 for d in doelgroep if d["sender_email"].startswith("praktijkvoor"))
    print(f"  behandeld: {len(patienten)} | al ingevuld (overgeslagen): {overgeslagen_ingevuld} | "
          f"zonder e-mail: {geen_email}")
    print(f"  DOELGROEP: {len(doelgroep)}  (PVI: {pvi} | Radiance: {len(doelgroep)-pvi})")

    if DRY_RUN:
        print("  DRY-RUN — niets verstuurd. Zet DRY_RUN=0 (of TEST_SEND=1) om te versturen."); return
    if len(doelgroep) > MAX_MAILS:
        print(f"  STOP: doelgroep ({len(doelgroep)}) > MAX_MAILS ({MAX_MAILS}). Verhoog MAX_MAILS bewust."); sys.exit(1)

    if TEST_SEND:
        d = doelgroep[0] if doelgroep else {"sender_name": "Radiance Clinic",
            "sender_email": "info@radianceclinic.nl", "html": mail_html("Test", f"{FORM_URL}?pid=TEST")}
        verstuur(TEST_TO, d["sender_name"], d["sender_email"], d["html"])
        print(f"  TEST: één voorbeeldmail verstuurd naar {TEST_TO}."); return

    verzonden = 0
    for d in doelgroep:
        try:
            verstuur(d["email"], d["sender_name"], d["sender_email"], d["html"]); verzonden += 1
        except urllib.error.HTTPError as e:
            print(f"  fout bij 1 mail (pid {d['pid']}): HTTP {e.code}")
    print(f"  LIVE: {verzonden}/{len(doelgroep)} mails verstuurd.")

if __name__ == "__main__":
    main()
