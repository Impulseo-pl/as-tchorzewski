#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Składa stronę A.S TCHÓRZEWSKI z części wspólnych. Treść siedzi w `pages.py`.

    python3 build.py

Wygląd: `assets/app.css` - pisany pod `DESIGN.md`, które jest JEDYNYM źródłem prawdy
o wyglądzie (kierunek B „Scena", `border-radius: 0` wszędzie).
Mechanika i dostępność: `assets/rdzen.*` - wspólne dla wszystkich stron docelowych,
wgrywane przez `~/.claude/skills/strona-docelowa/rdzen.py`.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from typografia import twarde_spacje                                   # noqa: E402
import pages                                                           # noqa: E402

SITE = "https://as-tchorzewski.pl"
FIRMA = "Firma Ogólnobudowlana Artur Tchórzewski"
MARKA = "A.S Tchórzewski"
PODPIS = "Usługi ogólnobudowlane"
TEL = pages.TEL
TEL_E164 = pages.TEL_E164
WA = pages.WA
WA_LINK = pages.WA_LINK
MAIL = "a.s-tchorzewski@wp.pl"          # ⚠️ trzy zapisy w ich materiałach - pytanie 9
ULICA = "Błońsko 46"
KOD = "64-308"
# ✅ ROZSTRZYGNIĘTE 07.09.2026 (nie pytanie do klienta - sprawdzony fakt):
# kod 64-308 to POCZTA Jabłonna, obejmująca m.in. Błońsko. Rejestr VAT zapisuje
# miejscowość (Błońsko), faktura zapisuje pocztę (Jabłonna) - oba są prawdziwe,
# a poprawna forma adresowa łączy jedno z drugim: „Błońsko 46, 64-308 Jabłonna".
# ⛔ „64-308 Błońsko" (nasz poprzedni zapis) jest po prostu błędne.
MIASTO = "Jabłonna"
NIP = "995 004 44 65"
REGON = "363138510"

# 🔄 Podbij przy KAŻDEJ zmianie pliku, inaczej klient zostanie na starej wersji.
V_CSS = 5
V_RDZEN = 10

# 🔴 PODGLĄD ROBOCZY. Strona stoi na zdjęciach klienta, na które NIE MAMY jeszcze
# jego pisemnej zgody (pytanie 3 w `PYTANIA-DO-KLIENTA.md`), a domena nie jest
# jeszcze wpięta. Do tego czasu każda podstrona ma `noindex`, a `robots.txt`
# zamyka całość. ⛔ Przestawić na False dopiero razem ze: zgodą na zdjęcia,
# odpowiedziami na 10 pytań, domeną i CNAME.
PODGLAD_ROBOCZY = True

MENU = [
    ("co-robimy.html", "Co robimy"),
    ("realizacje.html", "Realizacje"),
    ("o-nas.html", "O nas"),
    ("kontakt.html", "Kontakt"),
]


def adres_publiczny(plik):
    """Adres KOŃCOWY, bez `.html` - serwer i tak przekierowuje `.html` (308), a mapa
    strony z przekierowaniami wypycha podstrony z indeksu Google.
    ⚠️ Linki WEWNĄTRZ stron zostają z `.html`, żeby działał podgląd z dysku."""
    if plik == "index.html":
        return SITE + "/"
    return SITE + "/" + plik[:-5]


def menu_html(biezaca):
    poz = []
    for href, etykieta in MENU:
        cur = ' aria-current="page"' if href == biezaca else ""
        poz.append(f'        <li><a href="{href}"{cur}>{etykieta}'
                   f'<span class="strzalka-poz" aria-hidden="true">→</span></a></li>')
    return "\n".join(poz)


# Klasa `js` NA POCZĄTKU, nie z `rdzen.js` z końca strony: zwinięte menu telefonu
# wisi na `.js`, a rdzeń rusza dopiero po wczytaniu dokumentu - przez ułamek sekundy
# byłaby widoczna rozwinięta lista, która potem znika. Bez JS menu zostaje otwarte,
# więc zawsze da się wejść na podstronę.
JS_FLAGA = """<script>document.documentElement.classList.add('js')</script>"""


def naglowek(biezaca):
    # 🔴 `nav` obok `nawigacja`: pod klasą `.nav` szuka jej wspólny `rdzen.js`
    # (rozwijanie menu na telefonie, Escape, zamknięcie po kliknięciu w pozycję).
    # Bez niej przycisk jest martwy. Napis „Menu" przy kreskach jest CELOWY -
    # sama ikona bywa czytana jako ozdoba (uwaga K. z 02.09.2026, SPECBUD).
    return f"""<header class="top">
  <div class="wrap">
    <a class="znak" href="index.html" aria-label="{MARKA} - strona główna"><img
      src="img/logo.png" width="704" height="154" alt="{MARKA} - {PODPIS}"></a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="menu-glowne">
      <span class="burger-kreski" aria-hidden="true"><i></i><i></i><i></i></span>
      <span>Menu</span>
    </button>
    <nav class="nawigacja nav" id="menu-glowne" aria-label="Główne">
      <ul>
{menu_html(biezaca)}
      </ul>
    </nav>
    <a class="tel-gora" href="tel:{TEL_E164}">{TEL}</a>
  </div>
</header>"""


def stopka():
    linki = "\n".join(f'          <a href="{h}">{e}</a>' for h, e in MENU)
    return f"""<footer>
  <div class="wrap">
    <div class="stopka">
      <div>
        <img src="img/logo.png" width="704" height="154" alt="{MARKA} - {PODPIS}"
          loading="lazy" decoding="async">
        <p>Szpachlowanie, malowanie, łazienki i sucha zabudowa.
          Wykończenia wnętrz w wielkopolskiem i lubuskiem.</p>
      </div>
      <div>
        <h2>Na stronie</h2>
{linki}
      </div>
      <div>
        <h2>Kontakt</h2>
        <a href="tel:{TEL_E164}">{TEL}</a>
        <a href="{WA_LINK}" rel="noopener">WhatsApp {WA}</a>
        <a href="mailto:{MAIL}">{MAIL}</a>
        <p>Odbieramy 8:00-20:00</p>
        <p>{FIRMA}<br>{ULICA}<br>{KOD} {MIASTO}</p>
        <p>NIP {NIP}<br>REGON {REGON}</p>
        {pages.ikony_social_stopka()}
      </div>
    </div>
    <div class="stopka-dol">
      <span>© <span data-year>2026</span> {FIRMA}</span>
      <span><a href="polityka-prywatnosci.html">Polityka prywatności</a></span>
      <span>Projekt strony: <a href="https://impulseo.pl" rel="noopener">Impulseo</a></span>
    </div>
  </div>
</footer>
<div class="pasek-dolny">
  <a class="a-tel" href="tel:{TEL_E164}">Zadzwoń {TEL}</a>
  <a class="a-wa" href="{WA_LINK}" rel="noopener">{pages.ikona_wa("#fff")}WhatsApp</a>
</div>
{pages.dymki_social()}"""


# ⚠️ Bez godzin otwarcia: klient podał 8-20, ale wizytówka Google mówi 18:00 i nie
# wiemy, których dni to dotyczy (pytanie 8). Sprzeczne godziny w danych strukturalnych
# Google karze mocniej niż ich brak.
DANE_FIRMY = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",
"name":"{FIRMA}","alternateName":"{MARKA}","url":"{SITE}/",
"telephone":"{TEL_E164}","email":"{MAIL}",
"description":"Wykończenia wnętrz: szpachlowanie i gładzie, malowanie, łazienki, sucha zabudowa oraz montaż drzwi i okien. Rodzinna firma, ponad 20 lat doświadczenia.",
"address":{{"@type":"PostalAddress","streetAddress":"{ULICA}","postalCode":"{KOD}","addressLocality":"{MIASTO}","addressCountry":"PL"}},
"areaServed":["województwo wielkopolskie","województwo lubuskie"],
"vatID":"PL9950044465","foundingDate":"2015"}}
</script>"""


def szkielet(strona):
    plik = strona["plik"]
    kanon = adres_publiczny(plik)
    wstepne = ""
    if strona.get("hero") == "scena":
        wstepne = '\n<link rel="preload" as="image" href="img/hero.jpg" fetchpriority="high">'
    noindex = ('\n<meta name="robots" content="noindex, nofollow">'
               if PODGLAD_ROBOCZY or strona.get("noindex") else "")
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{strona['tytul']}</title>
<meta name="description" content="{strona['opis']}">{noindex}
<link rel="canonical" href="{kanon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="{MARKA}">
<meta property="og:title" content="{strona['tytul']}">
<meta property="og:description" content="{strona['opis']}">
<meta property="og:url" content="{kanon}">
<meta property="og:image" content="{SITE}/img/hero.jpg">
<meta name="theme-color" content="#0F0F12">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="assets/fonty/jost-latin-ext-300-normal.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="assets/fonty/jost-latin-300-normal.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="assets/fonty/inter-latin-ext-400-normal.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="assets/fonty/inter-latin-400-normal.woff2">{wstepne}
<link rel="stylesheet" href="assets/rdzen.css?v={V_RDZEN}">
<link rel="stylesheet" href="assets/app.css?v={V_CSS}">
{DANE_FIRMY}{JS_FLAGA}
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
{strona['tresc']}
{stopka()}
<div class="lb" hidden>
  <button class="lb-x" type="button" aria-label="Zamknij powiększenie">&times;</button>
  <button class="lb-p" type="button" aria-label="Poprzednie zdjęcie">&#8249;</button>
  <button class="lb-n" type="button" aria-label="Następne zdjęcie">&#8250;</button>
  <img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt="">
  <p class="lb-cap"></p>
</div>
<script src="assets/rdzen.js?v={V_RDZEN}"></script>
</body>
</html>
"""


def main():
    mapa = []
    for strona in pages.strony(naglowek=naglowek):
        html = twarde_spacje(szkielet(strona))
        with open(os.path.join(ROOT, strona["plik"]), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ {strona['plik']:28s} ({len(html)//1024} KB)")
        if not strona.get("noindex"):
            mapa.append(adres_publiczny(strona["plik"]))

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for adres in mapa:
            f.write(f"  <url><loc>{adres}</loc></url>\n")
        f.write("</urlset>\n")
    print(f"  ✓ sitemap.xml                 ({len(mapa)} adresów, bez .html)")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        if PODGLAD_ROBOCZY:
            f.write("# PODGLĄD ROBOCZY - strona czeka na zgodę klienta na publikację jego\n"
                    "# zdjęć i na domenę. Zdjąć razem z PODGLAD_ROBOCZY w build.py.\n"
                    "User-agent: *\nDisallow: /\n")
        else:
            f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("  ✓ robots.txt" + ("                  (PODGLĄD: Disallow /)" if PODGLAD_ROBOCZY else ""))


if __name__ == "__main__":
    main()
