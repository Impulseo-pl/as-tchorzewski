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
V_CSS = 13
V_RDZEN = 12

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
    # 🔴 Skrypt wejścia idzie TUŻ ZA `</header>`, nie na koniec dokumentu i nie do
    # `rdzen.js`: rdzeń rusza ~300 ms później, a przy budżecie 1,5 s to jest różnica
    # między „płynnie" a „ospale". Wcześniej się nie da - pomiar potrzebuje <header>.
    # ⛔ Tylko strona główna; na podstronach wejścia nie ma.
    wejscie_js = ("\n" + WEJSCIE_JS) if biezaca == "index.html" else ""
    # 🔴 `nav` obok `nawigacja`: pod klasą `.nav` szuka jej wspólny `rdzen.js`
    # (rozwijanie menu na telefonie, Escape, zamknięcie po kliknięciu w pozycję).
    # Bez niej przycisk jest martwy. Napis „Menu" przy kreskach jest CELOWY -
    # sama ikona bywa czytana jako ozdoba (uwaga K. z 02.09.2026, SPECBUD).
    return f"""<header class="top">
  <div class="wrap">
    <a class="znak" href="index.html" aria-label="{MARKA} - strona główna"><img
      src="img/logo.png" width="240" height="177" alt="{MARKA} - {PODPIS}"></a>
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
</header>{wejscie_js}"""


def stopka():
    linki = "\n".join(f'          <a href="{h}">{e}</a>' for h, e in MENU)
    return f"""<footer>
  <div class="wrap">
    <div class="stopka">
      <div>
        <img src="img/logo.png" width="240" height="177" alt="{MARKA} - {PODPIS}"
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


# ══════════════════════════════════════════════════════════════════════════════
#  WEJŚCIE NA STRONĘ (kurtyna z logo) — TYLKO strona główna.
#  Wygląd i uzasadnienie: `assets/app.css`, sekcja „WEJŚCIE NA STRONĘ".
#  Procedura i pułapki: skill `wejscie-na-strone`.
# ══════════════════════════════════════════════════════════════════════════════

# Zapalarka klasy. 🔴 Siedzi w <head> BEZ `defer` i celowo NIE robi pomiaru:
# z `defer` przez ułamek sekundy widać stronę, a dopiero potem kurtynę - wygląda
# jak błąd. Pomiaru tu nie da się zrobić, bo <header> jeszcze nie istnieje.
WEJSCIE_ZAPALARKA = """<script>(function(){
 try{
  var h=document.documentElement, a=location.search.indexOf('intro')>-1;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if(!a && sessionStorage.getItem('as-wejscie')) return;
  sessionStorage.setItem('as-wejscie','1');
  h.classList.add('intro-on','bez-wejscia-tla');
 }catch(e){}
})();</script>"""

WEJSCIE_HTML = """<div class="wejscie" aria-hidden="true">
  <div class="wejscie-plyta"></div>
  <div class="wejscie-znak-box">
    <img class="wejscie-znak" src="img/logo-duze.png" width="640" height="472" alt="">
    <i class="wejscie-kreska"></i>
  </div>
</div>"""

# 🔴 Ten skrypt MUSI stać tuż za </header>, nie w rdzen.js z końca strony:
# rdzeń rusza ~300 ms później, a przy budżecie 1,5 s to jest różnica między
# „płynnie" a „ospale". Pomiar potrzebuje <header>, więc wcześniej się nie da.
WEJSCIE_JS = """<script>(function(){
 var h=document.documentElement;
 if(!h.classList.contains('intro-on')) return;
 var obraz=document.querySelector('.znak img');
 var lecacy=document.querySelector('.wejscie-znak');
 if(!obraz||!lecacy){h.classList.remove('intro-on');return;}

 /* 🔴 SKALUJEMY W DÓŁ, NIGDY W GÓRĘ. Znak dostaje na kurtynie swój docelowy
    rozmiar naprawdę (width/height), a do paska wraca `scale()` mniejszym od 1.
    Powiększanie `transform`em rasteryzuje warstwę w rozmiarze bazowym i na
    telefonie (DPR 3) daje rozmyty znak - zrzut na Macu tego nie pokaże.
    Sufit liczy się z PIKSELI PLIKU podzielonych przez gęstość ekranu. */
 var PLIK_W=640, PLIK_H=472;
 var r=obraz.getBoundingClientRect();
 var sufit=PLIK_W/Math.min(window.devicePixelRatio||1,3);
 var cel=(innerWidth<680)?Math.min(innerWidth*0.72,320):Math.min(innerWidth*0.42,480);
 cel=Math.max(r.width, Math.min(cel, sufit));
 h.style.setProperty('--i-w', Math.round(cel)+'px');
 h.style.setProperty('--i-h', Math.round(cel*PLIK_H/PLIK_W)+'px');
 h.style.setProperty('--i-zmniejsz', (r.width/cel).toFixed(4));
 h.style.setProperty('--i-px', Math.round(r.left+r.width/2-innerWidth/2)+'px');
 h.style.setProperty('--i-py', Math.round(r.top+r.height/2-innerHeight/2)+'px');

 /* Po dodaniu stanu startowego potrzebne są DWIE klatki, inaczej przeglądarka
    sklei start z końcem i przejścia w ogóle nie widać. */
 requestAnimationFrame(function(){requestAnimationFrame(function(){
   h.classList.add('intro-gra');
 });});

 var start=Date.now(), MIN=560, SUFIT=900, zaladowane=false, zrobione=false;

 /* Zasłona schodzi, gdy gotowe jest HERO - nie po sztywnym timerze i NIE po
    `window.load`. Sztywny timer zasłania treść, która już się narysowała;
    `load` czeka na WSZYSTKIE zdjęcia strony i trzyma kurtynę dwa razy za długo.
    Pod zasłoną liczy się jedna rzecz: kadr hero. */
 function heroGotowe(){
   var im=document.querySelector('.scena-tlo');
   return !!(im && im.complete && im.naturalWidth>0);
 }
 function koniec(){
   if(zrobione) return; zrobione=true;
   h.classList.add('intro-out');
   /* Znak w pasku odsłaniamy DOKŁADNIE gdy lecący ląduje na jego miejscu -
      oba rysują to samo w tym samym rozmiarze, więc podmiany nie widać. */
   setTimeout(function(){ h.classList.remove('intro-on','intro-gra','intro-out'); }, 1100);
 }
 function moze(){
   if(Date.now()-start>=MIN && (heroGotowe()||zaladowane)) koniec();
   else setTimeout(moze,70);
 }
 window.addEventListener('load',function(){zaladowane=true;moze();});
 moze();
 setTimeout(koniec, SUFIT);                                  /* sufit z budżetu */
 setTimeout(function(){                                      /* twardy bezpiecznik */
   h.classList.remove('intro-on','intro-gra','intro-out');
 }, 3000);
 ['click','wheel','touchstart','keydown','scroll'].forEach(function(z){
   window.addEventListener(z, koniec, {once:true, passive:true});
 });
})();</script>"""


def szkielet(strona):
    plik = strona["plik"]
    kanon = adres_publiczny(plik)
    wstepne = ""
    if strona.get("hero") == "scena":
        wstepne = '\n<link rel="preload" as="image" href="img/hero.jpg" fetchpriority="high">'
    noindex = ('\n<meta name="robots" content="noindex, nofollow">'
               if PODGLAD_ROBOCZY or strona.get("noindex") else "")
    # ⛔ Wejście TYLKO na stronie głównej - nigdy na podstronach (reguła skilla).
    wejscie = strona.get("hero") == "scena"
    zapalarka = ("\n" + WEJSCIE_ZAPALARKA) if wejscie else ""
    kurtyna = ("\n" + WEJSCIE_HTML) if wejscie else ""
    if wejscie:
        wstepne += ('\n<link rel="preload" as="image" href="img/logo-duze.png" '
                    'fetchpriority="high">')
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
<meta name="theme-color" content="#F3F1ED">
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
{DANE_FIRMY}{JS_FLAGA}{zapalarka}
</head>
<body>{kurtyna}
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
