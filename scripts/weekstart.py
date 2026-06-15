#!/usr/bin/env python3
"""
Wekelijkse weekstart-briefing — maandagochtend per mail naar de directeur.
Leest de actielijst (open taken), haalt een Clinicminds-signaal op, en mailt het overzicht via Resend.
Het systeem brieft jou: 's maandags ligt klaar wat er moet.

Env: CLINICMINDS_API_TOKEN, RESEND_API_KEY, WEEKSTART_TO (default info@praktijkvoorinjectables.nl),
     DRY_RUN (default 0 — mail gaat naar de directeur zelf, geen patiënten).
"""
import os, json, re, datetime, urllib.request, urllib.error

CM_TOKEN = os.environ["CLINICMINDS_API_TOKEN"]
CM_BASE  = os.environ.get("CLINICMINDS_API_BASE", "https://app.clinicminds.com/api/analytics")
RESEND   = os.environ["RESEND_API_KEY"]
TO       = os.environ.get("WEEKSTART_TO", "info@praktijkvoorinjectables.nl")
FROM     = os.environ.get("WEEKSTART_FROM", "Kwaliteitssysteem PVI <info@radianceclinic.nl>")
DRY_RUN  = os.environ.get("DRY_RUN", "0") == "1"
REPO_URL = "https://github.com/rmvmeulenaar/kwaliteitsysteem"
UA = "Mozilla/5.0 (compatible; PVI-Kwaliteitssysteem/1.0)"

def get(url, headers):
    headers = {"User-Agent": UA, **headers}
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60))

def open_acties(pad="03_Registraties/Actielijst.md", maxn=15):
    acties = []
    try:
        for line in open(pad, encoding="utf-8"):
            if "⬜" in line:
                acties.append(re.sub(r"^[\s\-]*⬜\s*", "", line).strip())
    except FileNotFoundError:
        pass
    return acties[:maxn]

def cm_signaal():
    """Nieuwe patiënten afgelopen 7 dagen — kort praktijksignaal."""
    eind = datetime.date.today()
    start = eind - datetime.timedelta(days=7)
    try:
        d = get(f"{CM_BASE}/number-of-patients?date_from={start}&date_to={eind}&format=json", {"X-Api-Key": CM_TOKEN})
        return d["Totaal"][0].get("Nieuwe patiënten", "—")
    except Exception:
        return "—"

def verstuur(html):
    body = {"from": FROM, "to": [TO], "subject": f"🗓️ Weekstart {datetime.date.today():%d-%m-%Y} — Kwaliteitssysteem PVI", "html": html}
    req = urllib.request.Request("https://api.resend.com/emails", data=json.dumps(body).encode(),
            method="POST", headers={"Authorization": f"Bearer {RESEND}", "Content-Type": "application/json", "User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=30))

def main():
    acties = open_acties()
    nieuw = cm_signaal()
    weeknr = datetime.date.today().isocalendar()[1]
    acties_html = "".join(f"<li>{a}</li>" for a in acties) or "<li>Geen open acties 🎉</li>"
    html = f"""<p>Goedemorgen Rogier — hier is je weekstart (week {weeknr}).</p>
<h3>🔁 Deze week (vast ritme)</h3>
<ul><li>Salarisstrook + reiskostenvergoeding Moumen</li><li>Schoonmaak alle locaties</li></ul>
<h3>📌 Open acties</h3>
<ul>{acties_html}</ul>
<h3>📈 Praktijksignaal</h3>
<p>Nieuwe patiënten afgelopen 7 dagen: <b>{nieuw}</b></p>
<hr><p style="font-size:12px;color:#888">Volledige cockpit: <a href="{REPO_URL}/blob/main/03_Registraties/Actielijst.md">actielijst</a> · <a href="{REPO_URL}">kwaliteitssysteem</a></p>"""
    print(f"Weekstart week {weeknr}: {len(acties)} open acties | nieuwe patiënten 7d: {nieuw}")
    if DRY_RUN:
        print("DRY-RUN — niet verstuurd."); return
    verstuur(html)
    print(f"✓ Weekstart verstuurd naar {TO}")

if __name__ == "__main__":
    main()
