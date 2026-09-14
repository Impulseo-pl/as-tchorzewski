#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A.S TCHÓRZEWSKI - treść stron. Układ i część wspólna: `build.py`.

🔴 REGUŁY TREŚCI, których nie wolno tu złamać (źródło: `DESIGN.md`, `BRIEF-KLIENTA.md`):

1. 🔴 WSZYSTKO W LICZBIE MNOGIEJ („robimy", „malujemy", „polecamy") - wyraźne polecenie
   klienta. Łamie domyślną regułę silnika, tu wygrywa klient.
2. ⛔ ZERO cen i widełek. „W kwestii ceny trzeba się skontaktować".
3. ⛔ ZERO zdań, których klient nie powiedział: „bezpłatna wycena", „Wolsztyn i okolice",
   „bez umowy nie ruszamy", „od 20 lat", „zaczynaliśmy od murarki".
   „ponad 20 lat" - nie zaokrąglać w górę.
4. ⛔ ZERO frazesów: kompleksowo · solidnie · terminowo · indywidualne podejście · pasja ·
   profesjonalizm · najwyższa jakość · zadowolenie klienta.
5. ⛔ ZERO pustych sekcji i tekstów zastępczych. Nie ma opinii → nie ma sekcji opinii.
   Nie znamy długości gwarancji → nie piszemy o gwarancji ani słowa.
6. Kolejność usług podyktowana przez klienta: szpachlowanie, malowanie, łazienki,
   sucha zabudowa NA GÓRZE; montaż drzwi i okien niżej.
7. 🔴 KAŻDA PODSTRONA MA WŁASNY UKŁAD, nie tylko własne otwarcie:
   `co-robimy` = KATALOG (zygzak) · `realizacje` = INDEKS (galeria w grupach) ·
   `o-nas` = LIST (oś lat + narracja) · `kontakt` = DOKUMENT (karta danych).
8. Podpis pod zdjęciem mówi, CO WIDAĆ w kadrze - nie dopowiada faktów o firmie.
   Kadry „w trakcie" są podpisane jako w trakcie; to atut, nie wstyd.

⚠️ Rzeczy oznaczone `DO-POTWIERDZENIA.md` czekają na odpowiedzi klienta (10 pytań).
"""

TEL = "667 434 222"
TEL_E164 = "+48667434222"
WA = "882 832 244"
WA_LINK = "https://wa.me/48882832244"


def ikona_wa(kolor="currentColor"):
    """Znak WhatsAppa przy numerze - zamówiony przez klienta wprost (brief)."""
    return (f'<svg class="ikona-wa" width="18" height="18" viewBox="0 0 24 24" '
            f'aria-hidden="true"><path fill="{kolor}" d="M17.47 14.38c-.3-.15-1.74-.86-2-.96-.27-.1-.47'
            f'-.15-.66.15-.2.3-.76.96-.93 1.15-.17.2-.34.22-.63.08-.3-.15-1.25-.46-2.38-1.47-.88-.78'
            f'-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05'
            f'-.38-.02-.53-.08-.15-.66-1.6-.9-2.19-.24-.57-.48-.5-.66-.5h-.57c-.2 0-.52.07-.79.37'
            f'-.27.3-1.03 1.01-1.03 2.46s1.06 2.86 1.2 3.06c.15.2 2.08 3.18 5.04 4.46.7.3 1.25.48 '
            f'1.68.62.71.22 1.35.19 1.86.12.57-.09 1.74-.71 1.99-1.4.25-.69.25-1.28.17-1.4-.07-.13'
            f'-.27-.2-.57-.35M12.05 21.8h-.02a9.8 9.8 0 0 1-4.99-1.37l-.36-.21-3.71.97.99-3.62'
            f'-.23-.37a9.8 9.8 0 0 1-1.5-5.23c0-5.41 4.4-9.81 9.82-9.81a9.75 9.75 0 0 1 6.94 2.88 '
            f'9.74 9.74 0 0 1 2.87 6.94c0 5.41-4.4 9.82-9.81 9.82M20.5 3.49A11.75 11.75 0 0 0 12.05 0'
            f'C5.54 0 .25 5.29.25 11.79c0 2.08.54 4.11 1.58 5.9L.15 24l6.45-1.69a11.8 11.8 0 0 0 5.45 '
            f'1.39h.01c6.5 0 11.79-5.29 11.79-11.79 0-3.15-1.23-6.11-3.46-8.34"/></svg>')


# ── Profile w social. Oba potwierdzone: IG @a.s_tchorzewski (materiał ściągnięty
#    z 8 postów), FB 61589974670830 (baner z nowym logo). ⛔ TikToka nie ma - nie
#    dokładać ikony konta, którego nie ma.
FB_LINK = "https://www.facebook.com/profile.php?id=61589974670830"
IG_LINK = "https://www.instagram.com/a.s_tchorzewski/"


def dymki_social(sufiks=""):
    """Dwa okrągłe znaczki w prawym dolnym rogu: Facebook i Instagram.

    🔴 BEZ KAFELKA (polecenie K. 08.09.2026: „w okrągłych dymkach, bez tego białego,
    tylko same logo i ładnie podświetlone"). Wcześniej znaki siedziały w kwadratowych
    płytkach z obrysem - na papierze czytało się to jak baner doklejony do strony.

    ⚠️ OKRĄGŁOŚĆ ROBI SAM ZNAK, nie `border-radius`. Facebook jest z natury wypełnionym
    kołem; Instagram dostał koło w swoim gradiencie z białym aparatem w środku, zamiast
    dotychczasowego obrysu na przezroczystym tle. Dzięki temu zasada `border-radius: 0`
    z `DESIGN.md` zostaje NIENARUSZONA - nie ma czego zaokrąglać, bo nie ma płytki.

    🔴 KOLORY MAREK SĄ TU ŚWIADOME, mimo zasady „jeden akcent" z `DESIGN.md`.
    Ta zasada dotyczy koloru DEKORACYJNEGO; tutaj kolor niesie znaczenie - dokładnie
    tak samo jak zieleń `#25A63F` na przycisku WhatsAppa. Człowiek skanuje wzrokiem
    za niebieskim „f", nie za pomarańczowym kwadratem. (Decyzja K. 07.09.2026.)
    """
    return f'''<div class="social-dymki">
  <a class="s-fb" href="{FB_LINK}" rel="noopener" target="_blank" aria-label="A.S Tchórzewski na Facebooku">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.52 1.49-3.91 3.77-3.91 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.78-1.63 1.57v1.89h2.78l-.45 2.91h-2.33V22c4.78-.76 8.44-4.92 8.44-9.94"/></svg>
  </a>
  <a class="s-ig" href="{IG_LINK}" rel="noopener" target="_blank" aria-label="A.S Tchórzewski na Instagramie">
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <defs><linearGradient id="ig-grad{sufiks}" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FFD521"/><stop offset="25%" stop-color="#F50000"/>
        <stop offset="60%" stop-color="#B900B4"/><stop offset="100%" stop-color="#4C68D7"/>
      </linearGradient></defs>
      <circle class="ig-kolo" cx="12" cy="12" r="10"/>
      <g class="ig-aparat" transform="translate(12 12) scale(.46) translate(-12 -12)">
        <path fill="#fff" d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.3-1.46.72-2.13 1.38S.93 3.35.63 4.14C.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.3.79.72 1.46 1.38 2.13.67.66 1.34 1.08 2.13 1.38.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.3 1.46-.72 2.13-1.38.66-.67 1.08-1.34 1.38-2.13.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.3-.79-.72-1.46-1.38-2.13C21.32 1.35 20.65.93 19.86.63c-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0m0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32M12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8m7.85-10.4a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0"/>
      </g>
    </svg>
  </a>
</div>'''


def ikony_social_stopka():
    """Te same dwa znaki, ale w stopce - zamyka ostrzeżenie `brak [ikony-social]`.

    🔴 Własny sufiks gradientu jest KONIECZNY: dwa elementy o tym samym `id` to błędny
    HTML, a na telefonie dymki mają `display:none` - przeglądarka potrafi wtedy nie
    udostępnić gradientu z ukrytego poddrzewa i ikona Instagrama w stopce zrobiłaby się
    czarna. Sprawdzone przy wdrożeniu 07.09.2026.
    """
    d = dymki_social(sufiks="-stopka")
    return d.replace('class="social-dymki"', 'class="stopka-social"')


def przyciski_kontakt(duch_link="realizacje.html", duch_tekst="Zobacz realizacje",
                      trzeci=True):
    """Linia kontaktu. `trzeci=False` zdejmuje przycisk „Zobacz realizacje".

    🔴 W HERO idzie WERSJA DWUPRZYCISKOWA (K. 08.09.2026: pierwszy ekran „nie powala,
    dużo tekstu"). Trzeci przycisk konkurował z telefonem o to samo kliknięcie, a do
    realizacji i tak prowadzi menu na górze i zamknięcie strony na dole. Na pierwszym
    ekranie ma być JEDNA rzecz do zrobienia: zadzwonić.
    """
    trzeci_html = (f'\n      <a class="duch" href="{duch_link}">{duch_tekst}</a>'
                   if trzeci else "")
    return f"""<div class="kontakt-linia">
      <a class="btn" href="tel:{TEL_E164}">Zadzwoń {TEL}</a>
      <a class="duch" href="{WA_LINK}" rel="noopener">{ikona_wa()}WhatsApp {WA}</a>{trzeci_html}
      <span class="godziny">Odbieramy 8:00-20:00</span>
    </div>"""


def domkniecie_ramka(naglowek_txt, zdanie):
    """Sama ramka z wezwaniem - do wstawienia w cudzą sekcję (strona główna)."""
    return f"""<div class="domkniecie rv">
      <div>
        <h2>{naglowek_txt}</h2>
        <p>{zdanie}</p>
      </div>
      <div class="kontakt-linia">
        <a class="btn" href="tel:{TEL_E164}">Zadzwoń {TEL}</a>
        <a class="duch" href="{WA_LINK}" rel="noopener">{ikona_wa()}WhatsApp</a>
      </div>
    </div>"""


def domkniecie(naglowek_txt, zdanie):
    """Zamknięcie podstrony: jedna rzecz do zrobienia, dwa numery pod ręką."""
    return f"""<section class="sekcja">
  <div class="wrap">
    {domkniecie_ramka(naglowek_txt, zdanie)}
  </div>
</section>"""


def otwarcie(etykieta, tytul, lead, kadr=None, opis=""):
    """Otwarcie podstrony - CIEMNE, jedna rzecz na ekran (fundament „Scena").

    🔴 Po przejściu strony na jasną (droga A, 07.09.2026) to otwarcie jest na
    podstronach tym, czym scena na stronie głównej: jedynym ciemnym blokiem u góry.
    Bez niego podstrona robiła się płaskim papierem od paska do stopki. Znaku
    firmowego tu nie ma - zasada „logo tylko na jasnym" zostaje nienaruszona.

    🔴 08.09.2026 (decyzja K.): każde otwarcie dostaje WŁASNY kadr pod tekstem -
    ta sama zmiana, co na scenie strony głównej. Bez zdjęcia podstrona zaczynała
    się płaskim czarnym paskiem. `kadr=None` zostawia sam kolor (strony prawne,
    404 - tam zdjęcie robi za dużo hałasu przy błahej treści).
    """
    # `srcset` z opisem „1x/2x", nie „w": to jest dokładnie ten sam kadr w dwóch gęstościach,
    # a nie różne szerokości układu — przeglądarka wybiera po ekranie i nie potrzebuje `sizes`.
    # Plik @2x powstaje z `materialy/upscale/` (patrz `przygotuj-media.py`).
    drugi = kadr.replace(".jpg", "@2x.jpg") if kadr else ""
    tlo = (f'\n  <img class="otwarcie-tlo" data-paralaksa="200" src="img/{kadr}" '
           f'srcset="img/{kadr} 1x, img/{drugi} 2x" alt="{opis}" '
           f'decoding="async">' if kadr else "")
    klasa = "sekcja otwarcie ciemna" + (" otwarcie--kadr" if kadr else "")
    return f"""<section class="{klasa}" id="tresc">{tlo}
  <div class="wrap">
    <span class="etykieta">{etykieta}</span>
    <h1>{tytul}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>"""


# ══════════════════════════════════════════════════════════════════════════════
#  ZDJĘCIA - jedno miejsce na podpisy, żeby ten sam kadr nie opowiadał na dwóch
#  podstronach dwóch różnych historii.
#  ⛔ Podpis mówi, CO WIDAĆ. Nie dopowiada faktów o firmie (reguła 8).
# ══════════════════════════════════════════════════════════════════════════════
KADRY = {
    # klucz: (plik, szerokość, wysokość, alt, podpis)
    "poddasze-01": ("z-poddasze-01.jpg", 1100, 1467,
                    "Otwarta przestrzeń poddasza z drewnianymi belkami i oknem",
                    "Otwarta przestrzeń, belki zostawione na widoku"),
    "poddasze-02": ("z-poddasze-02.jpg", 1100, 1467,
                    "Belka konstrukcyjna i okno dachowe w wykończonym pokoju na poddaszu",
                    "Belka i okno dachowe w gotowym pokoju"),
    "poddasze-03": ("z-poddasze-03.jpg", 1100, 1467,
                    "Pokój na poddaszu po gładziach, z otwartą rozdzielnicą elektryczną na ścianie",
                    "W trakcie: pokój po gładziach, przed montażem osprzętu"),
    "poddasze-04": ("z-poddasze-04.jpg", 1100, 1467,
                    "Skos poddasza zabudowany płytą, okno dachowe, podłoga z płytek",
                    "Skos zabudowany płytą, okno dachowe"),
    "poddasze-05": ("z-poddasze-05.jpg", 1100, 1467,
                    "Łazienka na poddaszu z umywalką, muszlą i oknem dachowym",
                    "Łazienka pod skosem: umywalka, WC, okno dachowe"),

    "lazienka-01": ("z-lazienka-01.jpg", 900, 1199,
                    "Wolnostojąca wanna na podłodze z płytek drewnopodobnych, okno nad wanną",
                    "Wanna wolnostojąca, podłoga z płytek drewnopodobnych"),
    "lazienka-02": ("z-lazienka-02.jpg", 900, 1199,
                    "Wanna wolnostojąca obok wykończonej wnęki prysznicowej",
                    "Wanna i wnęka prysznicowa po wykończeniu"),
    "lazienka-03": ("z-lazienka-03.jpg", 900, 1199,
                    "Ściana wyłożona płytkami wielkoformatowymi w łazience",
                    "Płytki wielkoformatowe na całej ścianie"),
    "lazienka-04": ("z-lazienka-04.jpg", 1100, 1467,
                    "Ściana z płytek z wyprowadzonymi podejściami wodnymi w trakcie robót",
                    "W trakcie: podejścia wodne wyprowadzone w płytkach"),

    "poddasze2-01": ("z-poddasze2-01.jpg", 1100, 1467,
                     "Poddasze w trakcie robót: dwa okna dachowe i murowana obudowa wanny",
                     "W trakcie: obudowa wanny między oknami dachowymi"),
    "poddasze2-02": ("z-poddasze2-02.jpg", 1100, 1467,
                     "Wanna we wnęce pod skosem poddasza, okno dachowe nad wanną",
                     "Wanna wpuszczona we wnękę pod skosem"),
    "poddasze2-03": ("z-poddasze2-03.jpg", 1100, 1467,
                     "Ściana w ciemnym wykończeniu dekoracyjnym obok wnęki prysznicowej",
                     "Ciemna ściana dekoracyjna przy wnęce prysznicowej"),

    "schody-01": ("z-schody-01.jpg", 1100, 1467,
                  "Wykończone schody betonowe z barierką w jasnym holu",
                  "Schody po wykończeniu"),

    "beton-02": ("z-beton-02.jpg", 1200, 900,
                 "Jasna ściana z betonu architektonicznego w pokoju w trakcie robót",
                 "W trakcie: jasny beton architektoniczny na ścianie"),
    "beton-ciemny": ("z-beton-ciemny.jpg", 1200, 900,
                     "Ciemna ściana z betonu architektonicznego z czarnymi listwami w geometrycznym układzie",
                     "Ciemny beton architektoniczny z czarnymi listwami"),

    "elewacja-01": ("z-elewacja-01.jpg", 1200, 1600,
                    "Dom po wykonaniu elewacji, taras z kostki i wejście z zadaszeniem",
                    "Elewacja skończona, wejście od strony tarasu"),
    "elewacja-02": ("z-elewacja-02.jpg", 1200, 1600,
                    "Biała elewacja domu z rynną i oknem, zieleń wokół budynku",
                    "Elewacja i obróbki po robocie"),
    "elewacja-03": ("z-elewacja-03.jpg", 1200, 1600,
                    "Elewacja domu z oknem i skrzynką kwiatową, wąskie przejście wzdłuż ściany",
                    "Ściana szczytowa po wykończeniu"),
    "elewacja-04": ("z-elewacja-04.jpg", 1200, 1600,
                    "Drewniana podbitka pod okapem dachu widziana od dołu",
                    "Podbitka pod okapem"),


    # ── kadry z telefonu klienta (WhatsApp, 14.09.2026) ─────────────────────────
    "wejscie-01": ("z-wejscie-01.jpg", 1051, 1497,
                  "Czarne drzwi wejściowe w ścianie z ciemnej cegły, po bokach podłużne lampy",
                  "Wejście: drzwi w ceglanej ścianie"),
    "hol-01": ("z-hol-01.jpg", 1200, 1200,
              "Hol z drewnianą ścianą lamelową, lustrem w czarnej ramie i wideodomofonem",
              "Hol: ściana lamelowa i lustro"),
    "hol-02": ("z-hol-02.jpg", 1200, 1200,
              "Korytarz z panelami na podłodze i lamelami przy wejściu",
              "Korytarz po wykończeniu"),
    "schody-02": ("z-schody-02.jpg", 1200, 1200,
                 "Schody wyłożone ciemnym kamieniem, obraz na ścianie klatki schodowej",
                 "Schody z ciemnego kamienia"),
    "pokoj-01": ("z-pokoj-01.jpg", 1200, 1200,
                "Pokój z dwoma wysokimi oknami w czarnych ramach i opuszczonymi roletami",
                "Stolarka okienna i rolety w gotowym pokoju"),
    "pokoj-02": ("z-pokoj-02.jpg", 1100, 1588,
                "Kącik z podświetlanymi wnękami półkowymi, obrazem i ławką",
                "Wnęki z podświetleniem i miejsce do siedzenia"),
    "pokoj-03": ("z-pokoj-03.jpg", 1100, 1467,
                "Drewniane belki stropowe nad podłogą ułożoną w jodełkę",
                "Belki na widoku, podłoga w jodełkę"),
    "pokoj-05": ("z-pokoj-05.jpg", 900, 1600,
                "Zestawienie: ten sam pokój na poddaszu w stanie surowym i po wykończeniu",
                "Ten sam pokój: przed i po"),
    "poddasze-06": ("z-poddasze-06.jpg", 1100, 1467,
                   "Pokój na poddaszu z drewnianą kratownicą i podłogą z płytek wielkoformatowych",
                   "Kratownica zostawiona na widoku"),
    "poddasze-07": ("z-poddasze-07.jpg", 1100, 1467,
                   "Pomieszczenie na poddaszu z podłogą z paneli i ciemnymi belkami po bokach",
                   "Panele i belki w przejściu"),
    "lazienka-05": ("z-lazienka-05.jpg", 1100, 1467,
                   "Mała łazienka pod skosem: umywalka z szafką, WC podwieszane, okno dachowe",
                   "Łazienka pod skosem: umywalka i WC"),
    "lazienka-06": ("z-lazienka-06.jpg", 1100, 1467,
                   "Kabina prysznicowa ze szklaną ścianką obok umywalki w małej łazience",
                   "Kabina ze szklaną ścianką"),
    "lazienka-07": ("z-lazienka-07.jpg", 1100, 1467,
                   "Wanna z parawanem w czarnej ramie na tle białych płytek, ciemna podłoga",
                   "Wanna z parawanem w czarnej ramie"),
    "lazienka-08": ("z-lazienka-08.jpg", 1100, 1467,
                   "WC podwieszane i czarna szafka z umywalką w łazience z ciemną podłogą",
                   "Czarna szafka i WC podwieszane"),
    "poddasze2-04": ("z-poddasze2-04.jpg", 1100, 1467,
                    "Wnęka prysznicowa z murowanym siedziskiem obok ściany w ciemnej zieleni",
                    "Wnęka prysznicowa z siedziskiem"),
    "robota-01": ("z-robota-01.jpg", 1200, 1112,
                 "Sufit na stelażu z profili stalowych w pomieszczeniu przed zabudową płytą",
                 "W trakcie: stelaż pod sufit podwieszany"),
    "robota-02": ("z-robota-02.jpg", 1200, 900,
                 "Ściana z płytek wielkoformatowych z klinami poziomującymi w trakcie układania",
                 "W trakcie: płytki na klinach poziomujących"),
    "robota-03": ("z-robota-03.jpg", 1100, 1467,
                 "Podłoga z płytek drewnopodobnych z krzyżykami dystansowymi w trakcie układania",
                 "W trakcie: płytki drewnopodobne na podłodze"),

    # ten sam plik co w sekcji „przed i po" na stronie głównej - jeden kadr, jeden plik
    "przed": ("przed.jpg", 1100, 1100,
              "Rozbudowa w stanie surowym: mury z bloczków, stemple i otwarty otwór okienny",
              "Przed: stan surowy rozbudowy"),
    "po": ("po.jpg", 1100, 1100,
           "Ta sama rozbudowa po wykończeniu: biała elewacja, duże okno tarasowe, trawnik",
           "Po: elewacja, stolarka, uporządkowane otoczenie"),
}


def kadr_galerii(klucz, lazy=True, i=0):
    plik, w, h, alt, podpis = KADRY[klucz]
    l = ' loading="lazy" decoding="async"' if lazy else ""
    # 🔴 Powiększalnik dostaje OSOBNY, większy plik (`-duze.jpg`, 2000 px). W siatce kafel
    #    stoi na ~577 px, ale po kliknięciu idzie na pół ekranu — ten sam plik co w siatce
    #    miałby tam gęstość ~0,46. Plik `-duze` ładuje się dopiero po kliknięciu, więc
    #    siatka nie tyje. Generuje go `przygotuj-media.py` dla każdego slotu `z-*`.
    duzy = plik.replace(".jpg", "-duze.jpg")
    return (f'<figure data-zoom="img/{duzy}" data-alt="{alt}" data-cap="{podpis}" tabindex="0" '
            f'style="--i:{min(i, 4)}">'
            f'<img src="img/{plik}" alt="{alt}" width="{w}" height="{h}"{l}>'
            f'<figcaption>{podpis}</figcaption></figure>')


def grupa(tytul, licznik, klucze, lazy=True):
    """Grupa kadrów w realizacjach.

    🔴 LICZBA KOLUMN IDZIE ZA LICZBĄ ZDJĘĆ (08.09.2026, blok E - test „czy topowa
    firma dałaby to u siebie"). `.galeria` to `columns:3`, więc grupa 2- i 4-zdjęciowa
    zostawiała pusty trzeci słupek: przy 2 kadrach znikała 1/3 rzędu, przy 4 - cały
    dół prawej strony. Dwa i cztery zdjęcia idą więc na DWA słupki (2 i 2+2), trzy
    i więcej na trzy.
    ⛔ Grupa JEDNOZDJĘCIOWA nie ma dobrego układu - zdjęcie zostaje samo przy 2/3
       pustki, a rozciągnięte na całą szerokość rozmywa się (źródła to kadry z telefonu).
       Taką grupę SCALAMY z sąsiednią zamiast szukać CSS-u."""
    kadry = "\n      ".join(kadr_galerii(k, lazy, i) for i, k in enumerate(klucze))
    klasa = "galeria galeria--2" if len(klucze) in (2, 4) else "galeria"
    return f"""    <div class="grupa rv">
      <div class="grupa-tyt"><h2>{tytul}</h2><span class="licznik">{licznik}</span></div>
      <div class="{klasa} kaskada">
      {kadry}
      </div>
    </div>"""


IKONA_PLAY = ('<svg class="ikona-play" width="16" height="16" viewBox="0 0 16 16" '
              'aria-hidden="true"><path fill="currentColor" d="M3 1.6 14 8 3 14.4Z"/></svg>')


def film(plik, plakat, tytul, podpis, alt, lazy=True):
    """Kadr ożywa POD KURSOREM i pod przytrzymanym palcem (rdzeń, blok 7) - tak robią to
    strony premium. Klik zostaje dla klawiatury i dla tego, kto chce obejrzeć do końca.
    `preload="none"` nadal nie zjada transferu na telefonie.
    ⛔ Nigdzie nie piszemy „film bez dźwięku" (K. 08.09.2026): filmy z budowy dźwięku
       nie mają, ale informowanie o braku brzmi jak tłumaczenie się z wady."""
    return f"""<figure class="reel">
        <div class="reel-media">
          <img class="plakat" src="img/{plakat}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} decoding="async">
          <video preload="none" playsinline muted loop poster="img/{plakat}">
            <source src="video/{plik}" type="video/mp4">
          </video>
          <button class="reel-btn" type="button"><span>{IKONA_PLAY}{tytul}</span></button>
        </div>
        <figcaption>{podpis}</figcaption>
      </figure>"""


# ══════════════════════════════════════════════════════════════════════════════
#  STRONA GŁÓWNA - SCENA. Jedna rzecz na ekran. Strona jest JASNA (droga A,
#  07.09.2026); ciemne zostały: nagłówek sceny, ramka wezwania i pasy zdjęć.
#  Główna zapowiada, podstrony niosą treść.
# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
#  OPINIE Z GOOGLE
#  🔴 Treści PRZEPISANE Z WIZYTÓWKI 10.09.2026 (CID 0x56cbe6647684bfc8; telefon
#     667 434 222 sprawdzony, żeby nie wziąć wizytówki Tadeusza Tchórzewskiego
#     spod tego samego adresu). Ocena 5,0, sześć opinii, z czego TRZY mają treść.
#  ⛔ Nie dopisywać i nie przerabiać ani słowa. Google ucina długie opinie
#     w podglądzie - bierzemy dokładnie tyle, ile widać, kończąc na ostatnim
#     PEŁNYM zdaniu. Emotikony i podwójne spacje zdjęte, reszta bez zmian.
#  ⚠️ Liczby opinii NIE PODAJEMY (jest ich sześć) - tak każe standard plakietki
#     ze skilla `strona-docelowa` przy progu poniżej dziesięciu.
#  ⏳ Zgoda klienta na publikację z imieniem i nazwiskiem: pytanie 7
#     w `PYTANIA-DO-KLIENTA.md`, wciąż bez odpowiedzi.
# ══════════════════════════════════════════════════════════════════════════════
OPINIE = [
    ("Kinga Zielonacka",
     "Fachowcy pierwsza klasa. Panowie zrobili swoją pracę szybko i dokładnie. "
     "Bardzo mili i wszystko zostało ładnie wytłumaczone. Jestem bardzo zadowolona, "
     "bo z fachowcami w dzisiejszych czasach jest ciężko, a tutaj znalazłam swoją "
     "sprawdzoną ekipę."),
    ("Sylwia Nowicka",
     "Pełen profesjonalizm i najwyższa jakość usług. Ekipa remontowa zrealizowała "
     "projekt z dbałością o każdy, nawet najmniejszy detal. Bardzo doceniam ich "
     "punktualność, uczciwe podejście do wyceny oraz czystość podczas pracy."),
    ("Daria Jóźwikowska",
     "Z całego serca polecam tę firmę remontową. Remont został wykonany na "
     "najwyższym poziomie - wszystko dokładnie, estetycznie i z ogromną dbałością "
     "o detale. Prace przebiegały sprawnie, zgodnie z ustalonym harmonogramem."),
]

_GW = ("M9 1.6l2.2 4.46 4.92.72-3.56 3.47.84 4.9L9 12.74l-4.4 2.31.84-4.9"
       "L1.88 6.68l4.92-.72L9 1.6Z")


def _gwiazdki():
    return "".join(f'<path transform="translate({i * 18} 0)" d="{_GW}"/>' for i in range(5))


def plakietka_google(ocena="5,0"):
    """Plakietka ze standardu skilla `strona-docelowa` (rdzeń, `.g-badge`).
    Poniżej dziesięciu opinii NIE podajemy ich liczby - sama ocena i gwiazdki."""
    liczba = float(ocena.replace(",", "."))
    return f"""<span class="g-badge">
  <svg class="gb-ico" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
  </svg>
  <b class="gb-ocena">{ocena}</b>
  <svg class="gb-stars" viewBox="0 0 90 18" width="74" height="14.8" aria-hidden="true">
    <g class="gb-pusta">{_gwiazdki()}</g>
    <clipPath id="gs{int(liczba * 200)}"><rect x="0" y="0" width="{liczba / 5 * 90:.1f}" height="18"/></clipPath>
    <g class="gb-peln" clip-path="url(#gs{int(liczba * 200)})">{_gwiazdki()}</g>
  </svg>
  <span class="gb-txt">w Google</span>
</span>"""


def sekcja_opinie():
    karty = "\n".join(
        f"""        <figure class="opinia">
          <svg class="opinia-gw" viewBox="0 0 90 18" width="82" height="16.4" aria-hidden="true">
            <g>{_gwiazdki()}</g>
          </svg>
          <blockquote>{tresc}</blockquote>
          <figcaption>{autor}<span>opinia w Google</span></figcaption>
        </figure>""" for autor, tresc in OPINIE)
    return f"""<section class="sekcja sekcja--opinie">
  <div class="wrap">
    <div class="naglowek-opinie rv">
      <span class="etykieta">Opinie</span>
      <h2>Co mówią ci, u których byliśmy</h2>
      {plakietka_google()}
    </div>
  </div>
  <div class="karuzela rv" data-karuzela>
    <div class="karuzela-tor">
{karty}
    </div>
  </div>
</section>"""


def index(naglowek):
    return f"""{naglowek("index.html")}

<header class="scena">
  <img class="scena-tlo" data-paralaksa="110" src="img/hero.jpg"
    srcset="img/hero.jpg 1x, img/hero@2x.jpg 2x" width="1440" height="1300" fetchpriority="high"
    alt="Ściana z betonu architektonicznego z czarnymi liniami - z naszych realizacji">
  <div class="wrap" id="tresc">
    <div class="rv">
      <span class="etykieta">Wykończenia wnętrz · wielkopolskie i lubuskie</span>
      <h1>Wnętrze gotowe do wprowadzenia.</h1>
      <p class="lead">Szpachlowanie, malowanie, łazienki i sucha zabudowa.
        Na budowach od ponad 20 lat.</p>
      {przyciski_kontakt(trzeci=False)}
    </div>
  </div>
</header>

<section class="sekcja">
  <div class="wrap wrap--szeroki">
    <div class="naglowek-sekcji rv">
      <span class="etykieta">Przed i po</span>
      <h2>Ten sam dom. Dwa zdjęcia.</h2>
      <p class="pod">Na gotowym zdjęciu nie widać już, od czego się zaczynało.</p>
    </div>
    <figure class="przedpo rv">
      <div class="przedpo-rama" data-przedpo>
        <div class="przedpo-warstwy">
          <img class="przedpo-po" src="img/po.jpg" srcset="img/po.jpg 1x, img/po@2x.jpg 2x"
            width="1500" height="1239" decoding="async"
            alt="Ta sama rozbudowa po wykończeniu: biała elewacja, duże okno tarasowe, trawnik">
          <img class="przedpo-przed" src="img/przed.jpg" srcset="img/przed.jpg 1x, img/przed@2x.jpg 2x"
            width="1500" height="1239" decoding="async"
            alt="Ta sama rozbudowa w stanie surowym: mury z bloczków, stemple i otwarty otwór okienny">
        </div>
        <span class="znacznik przedpo-etyk przedpo-etyk--przed">Przed</span>
        <span class="znacznik po przedpo-etyk przedpo-etyk--po">Po</span>
        <button class="przedpo-przelacznik" type="button" data-przedpo-btn
          aria-pressed="false" aria-label="Pokaż stan po remoncie">
          <span class="przedpo-hint" aria-hidden="true">
            <span class="hint-mysz">Najedź lub kliknij, żeby zobaczyć efekt</span>
            <span class="hint-dotyk">Dotknij, żeby zobaczyć efekt</span>
          </span>
        </button>
      </div>
      <figcaption>Stan surowy: mury z bloczków i stemple. Po naszej robocie: elewacja,
        stolarka okienna i opaska. Ten sam narożnik tego samego domu.</figcaption>
    </figure>
  </div>
</section>

<section class="sekcja">
  <div class="wrap wrap--szeroki">
    <div class="naglowek-sekcji rv">
      <span class="etykieta">Zakres</span>
      <h2>Co robimy najczęściej</h2>
      <p class="pod">Cztery roboty, na których stoi większość naszych budów.</p>
    </div>
    <div class="kafle kaskada rv">
      <a class="kafel" href="co-robimy.html#u-01">
        <div class="obraz"><img src="img/u-szpachlowanie.jpg" width="1000" height="1333"
          alt="Światło z okna dachowego na gotowej gładzi, przy drewnianej belce" loading="lazy" decoding="async"></div>
        <div class="opis"><h3>Szpachlowanie i gładzie</h3>
          <span class="dalej">Zobacz →</span></div>
      </a>
      <a class="kafel" href="co-robimy.html#u-02">
        <div class="obraz"><img src="img/u-malowanie.jpg" width="720" height="960"
          alt="Pracownik w kombinezonie maluje ścianę agregatem natryskowym" loading="lazy" decoding="async"></div>
        <div class="opis"><h3>Malowanie</h3>
          <span class="dalej">Zobacz →</span></div>
      </a>
      <a class="kafel" href="co-robimy.html#u-03">
        <div class="obraz"><img src="img/u-lazienki.jpg" width="900" height="1200"
          alt="Łazienka z wolnostojącą wanną i płytkami drewnopodobnymi" loading="lazy" decoding="async"></div>
        <div class="opis"><h3>Łazienki</h3>
          <span class="dalej">Zobacz →</span></div>
      </a>
      <a class="kafel" href="co-robimy.html#u-04">
        <div class="obraz"><img src="img/u-sucha-zabudowa.jpg" width="1000" height="1333"
          alt="Skos poddasza zabudowany płytą gipsowo-kartonową z oknem dachowym" loading="lazy" decoding="async"></div>
        <div class="opis"><h3>Sucha zabudowa</h3>
          <span class="dalej">Zobacz →</span></div>
      </a>
    </div>
    <div class="wiersz-usluga rv">
      <h3>Montaż drzwi i okien</h3>
      <span class="spec">Wstawiamy, gdy ściany są gotowe - z obróbką ościeży.</span>
      <a class="dalej" href="co-robimy.html#u-05">Zobacz →</a>
    </div>
  </div>
</section>

<!-- ⛔ NIE USUWAJ `srcset`/`sizes` z pasów. Pas idzie przez całą szerokość okna,
     więc bez nich telefon pobiera plik 2400 px na ekran 390 px (bramka wyglądu,
     11.09.2026: „3,1× nadmiaru przy Retinie, leci tak na każdej podstronie").
     Warianty -900 i -1600 robi SAM `przygotuj-media.py` (krok `warianty_pasow`). -->
<figure class="pas pas--duzy">
  <img data-paralaksa="220" src="img/pas-elewacja.jpg"
    srcset="img/pas-elewacja-900.jpg 900w, img/pas-elewacja-1600.jpg 1600w, img/pas-elewacja.jpg 2400w"
    sizes="100vw" width="2400" height="1029" loading="lazy" decoding="async"
    alt="Skończona elewacja domu z wejściem od strony tarasu, biały tynk i ciemne obróbki">
  <figcaption>Elewacja z podbitką - po naszej robocie.</figcaption>
</figure>

<section class="sekcja">
  <div class="wrap">
    <div class="naglowek-sekcji rv">
      <span class="etykieta">Z budowy</span>
      <h2>Tak to wygląda od naszej strony</h2>
      <p class="pod">Dwa kadry prosto z roboty.
        Najedź na kadr albo przytrzymaj go palcem.</p>
    </div>
    <div class="para para--filmy rv">
      {film("agregat.mp4", "plakat-agregat.jpg", "Malowanie agregatem (37 s)",
            "Malowanie agregatem natryskowym - duża powierzchnia, powłoka bez śladów po wałku.",
            "Pracownik w kombinezonie i masce maluje ścianę agregatem natryskowym")}
      {film("ekipa.mp4", "plakat-ekipa.jpg", "Robota przy elewacji (39 s)",
            "Dzień na rusztowaniu przy elewacji - tynk, obróbki i podbitka.",
            "Ekipa przy elewacji budynku, rusztowanie ustawione wzdłuż ściany")}
    </div>
    <p class="pod-para rv"><a class="duch" href="realizacje.html">Zobacz realizacje</a></p>
  </div>
</section>

<figure class="pas pas--duzy">
  <img data-paralaksa="220" src="img/pas-lazienka.jpg"
    srcset="img/pas-lazienka-900.jpg 900w, img/pas-lazienka-1600.jpg 1600w, img/pas-lazienka.jpg 2400w"
    sizes="100vw" width="2400" height="1350" loading="lazy" decoding="async"
    alt="Wanna obudowana płytami w ciepłym beżu, we wnęce pod skosem poddasza, obok okno dachowe">
  <figcaption>Łazienka na poddaszu - wanna we wnęce pod skosem, z naszych realizacji.</figcaption>
</figure>

{sekcja_opinie()}

<section class="sekcja">
  <div class="wrap">
    <div class="dwie-kolumny rv">
      <div>
        <span class="etykieta">Uczciwie</span>
        <h2>Robimy to, na czym się znamy.</h2>
      </div>
      <div class="tekst-dlugi">
        <p>Wnętrze pod klucz prowadzi u nas jedna ekipa - od gładzi po ostatni silikon.
          Po pierwszej rozmowie wiesz, czy to coś dla nas.</p>
      </div>
    </div>
    <div class="odstep-domkniecie">
      {domkniecie_ramka("Zacznijmy od telefonu",
                        "Zadzwoń albo napisz na WhatsAppie. Umawiamy się na miejscu, "
                        "oglądamy zakres i wracamy z wyceną.")}
    </div>
  </div>
</section>"""


# ══════════════════════════════════════════════════════════════════════════════
#  CO ROBIMY - układ KATALOG: zygzak tekst/kadr, kolejność podyktowana przez klienta.
# ══════════════════════════════════════════════════════════════════════════════
def blok_uslugi(kod, numer, tytul, akapity, spec, obraz, alt, odwrocony=False, lazy=True):
    tresc = "\n        ".join(f"<p>{a}</p>" for a in akapity)
    klasa = "zygzak zygzak--odwrocony" if odwrocony else "zygzak"
    plik, w, h = obraz
    return f"""      <div class="{klasa} rv" id="{kod}">
        <div>
          <span class="kod">{numer}</span>
          <h2>{tytul}</h2>
          {tresc}
          <p class="spec-linia">{spec}</p>
        </div>
        <figure class="zygzak-obraz">
          <img src="img/{plik}" width="{w}" height="{h}" alt="{alt}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""} decoding="async">
        </figure>
      </div>"""


def co_robimy(naglowek):
    return f"""{naglowek("co-robimy.html")}

{otwarcie("Zakres robót", "Wykończenia wnętrz od gładzi po drzwi",
          kadr="otw-co-robimy.jpg",
          opis="Światło z okna dachowego na gotowej gładzi, przy odsłoniętej belce",
          lead=
          "Pięć robót, które bierzemy najczęściej - i to, co przy każdej z nich decyduje o efekcie. Ceny nie podajemy z góry - zależy od zakresu i od tego, co zastaniemy na ścianie.")}

<section class="sekcja">
  <div class="wrap">
{blok_uslugi("u-01", "01", "Szpachlowanie i gładzie", [
    "Gładź decyduje o tym, jak ściana wygląda po pomalowaniu. Każde zafalowanie widać "
    "dopiero wtedy, gdy padnie na nie światło z okna - dlatego to jest robota, przy której "
    "nie ma dróg na skróty.",
    "Robimy gładzie ręcznie i maszynowo: ściany, sufity i skosy poddaszy."],
    "gładzie ręczne i maszynowe · ściany, sufity, skosy · przygotowanie pod malowanie",
    ("u-szpachlowanie.jpg", 1000, 1333),
    "Światło z okna dachowego na gotowej gładzi, przy drewnianej belce", lazy=False)}

{blok_uslugi("u-02", "02", "Malowanie", [
    "Malujemy wałkiem i agregatem natryskowym. Agregat bierzemy tam, gdzie powierzchnia "
    "jest duża, a powłoka ma być równa - bez śladów po wałku i bez łączeń.",
    "Podłogi, stolarkę i grzejniki zaklejamy przed robotą, a nie po niej."],
    "malowanie wnętrz · agregat natryskowy · zabezpieczenie podłóg i stolarki",
    ("u-malowanie.jpg", 720, 960),
    "Pracownik w kombinezonie maluje ścianę agregatem natryskowym", odwrocony=True, lazy=False)}

{blok_uslugi("u-03", "03", "Łazienki", [
    "Łazienka to najwięcej rzemiosła na najmniejszym metrażu: podejścia wodne, płytki "
    "wielkoformatowe, zabudowa wanny albo wnęki prysznicowej, na końcu silikony.",
    "Płytka wielkoformatowa nie wybacza krzywej ściany, więc równanie podłoża jest tu "
    "połową roboty."],
    "płytki wielkoformatowe · wanny wolnostojące · zabudowa i wnęki · podejścia wodne",
    ("u-lazienki.jpg", 900, 1200),
    "Łazienka z wolnostojącą wanną i płytkami drewnopodobnymi")}

{blok_uslugi("u-04", "04", "Sucha zabudowa", [
    "Płyta gipsowo-kartonowa zamienia poddasze w pokoje: skosy, sufity, ścianki działowe, "
    "wnęki i obudowy.",
    "Zabudowę prowadzimy tak, żeby od razu szła pod gładź: równe płaszczyzny, wyprowadzone narożniki, taśmowanie na łączeniach."],
    "skosy i sufity · ścianki działowe · wnęki i obudowy",
    ("u-sucha-zabudowa.jpg", 1000, 1333),
    "Skos poddasza zabudowany płytą gipsowo-kartonową z oknem dachowym", odwrocony=True)}

{blok_uslugi("u-05", "05", "Montaż drzwi i okien", [
    "Drzwi i okna montujemy zwykle na końcu wykończenia - wtedy, gdy ściany "
    "są już gotowe i wiadomo, w co się wstawia.",
    "Po montażu sami obrabiamy ościeża i wykańczamy ścianę wokół futryny."],
    "drzwi wewnętrzne i zewnętrzne · okna · obróbka i wykończenie po montażu",
    ("u-drzwi-okna.jpg", 1000, 1333),
    "Hol z zamontowanymi drzwiami wejściowymi z matowym szkłem")}
  </div>
</section>

<section class="sekcja">
  <div class="wrap dwie-kolumny rv">
    <div>
      <span class="etykieta">Poza wnętrzami</span>
      <h2>Robimy też elewacje, podbitki i ściany dekoracyjne</h2>
    </div>
    <div class="tekst-dlugi">
      <p>Wnętrza są naszą główną robotą, ale na koncie mamy też elewacje z podbitką,
        ściany w betonie architektonicznym i wykończenia schodów. Zdjęcia z tych budów
        stoją w <a href="realizacje.html">realizacjach</a>.</p>
    </div>
  </div>
  <!-- Dwa kadry na dowód dwóch z trzech robót wymienionych obok. Trzeciej (beton
       architektoniczny) tu NIE MA: oba kadry betonu są poziome, więc w parze z tymi
       dwoma pionowymi rozbiłyby rytm, a ciemna ściana z bliska ciągnie wzrok mocniej
       niż cała reszta sekcji. Beton pokazuje tło pierwszego ekranu strony głównej
       i grupa 04 w `realizacjach` - tam jest na niego miejsce. -->
  <div class="wrap">
    <div class="para para--dowod kaskada rv">
      <figure class="klatka">
        <img src="img/z-elewacja-01.jpg" srcset="img/z-elewacja-01.jpg 1x, img/z-elewacja-01-duze.jpg 2x"
          width="1200" height="1600" loading="lazy" decoding="async"
          alt="Dom po wykonaniu elewacji: biały tynk, ciemna podbitka pod okapem i wejście od strony tarasu">
        <figcaption>Elewacja z podbitką - wejście od strony tarasu.</figcaption>
      </figure>
      <figure class="klatka">
        <img src="img/z-schody-01.jpg" srcset="img/z-schody-01.jpg 1x, img/z-schody-01-duze.jpg 2x"
          width="1100" height="1467" loading="lazy" decoding="async"
          alt="Wykończone schody betonowe z listwami ze stali i oprawami światła w ścianie">
        <figcaption>Schody po wykończeniu, z podświetleniem w ścianie.</figcaption>
      </figure>
    </div>
  </div>
</section>

{domkniecie("Powiedz, co ma być zrobione",
            "Umawiamy oględziny na miejscu i wracamy z wyceną do 5 dni roboczych.")}"""


# ══════════════════════════════════════════════════════════════════════════════
#  REALIZACJE - układ INDEKS: grupy budów, w każdej kadry w naturalnych proporcjach.
#
#  🔴 08.09.2026, blok E - test „czy topowa firma dałaby to u siebie" wyciął DWA
#     POWTÓRZENIA ze strony głównej. Podstrona była nimi zaklamrowana: otwierała się
#     tym samym, czym główna się chwali, i kończyła tym samym, czym główna się kończy.
#     ⛔ Grupa „Rozbudowa - przed i po" (`przed.jpg` + `po.jpg`) - te dwa kadry stoją
#        na GŁÓWNEJ, w sekcji „Ten sam dom. Dwa zdjęcia.", i to tam mają zostać:
#        mają tam znaczniki „Przed"/„Po" i szerszy kontener, a główna dostaje ruch
#        z wyszukiwarki. Reguła „jeden kadr nie stoi w dwóch miejscach" obowiązuje
#        tak samo dla zdjęć z galerii, jak dla kadrów w otwarciach.
#     ⛔ Sekcja „Minuta i szesnaście sekund roboty" - OBA filmy klienta (a ma tylko
#        dwa) stoją na głównej od decyzji K. z 08.09 („oba na głównej"). Tutaj zostały
#        przeoczone przy tamtej przeprowadzce - to była pozostałość, nie decyzja.
#     ⛔ Grupa „Schody" miała JEDNO zdjęcie i zostawiała 2/3 rzędu pustki. Scalona
#        z „Betonem architektonicznym" (ten sam rodzaj wykończenia, ten sam materiał)
#        w trzykadrową grupę, która wypełnia rząd co do słupka.
# ══════════════════════════════════════════════════════════════════════════════
def realizacje(naglowek):
    return f"""{naglowek("realizacje.html")}

{otwarcie("Realizacje", "Skończone wnętrza i kadry z budowy",
          kadr="otw-realizacje.jpg",
          opis="Poddasze z dwoma oknami dachowymi i zabudowaną wanną",
          lead=
          "Na gotowej łazience nie widać już, jak wyprowadzono podejścia wodne ani co siedzi pod płytką. Dlatego obok skończonych wnętrz pokazujemy kadry z samej roboty, podpisane „w trakcie”.")}

<section class="sekcja">
  <div class="wrap">
{grupa("Pokoje po wykończeniu", "01", ["pokoj-05", "pokoj-01",
                                           "pokoj-03", "pokoj-02"], lazy=False)}

{grupa("Wejście, hol i schody", "02", ["wejscie-01", "hol-01", "hol-02", "schody-02"])}

{grupa("Poddasze pod klucz", "03", ["poddasze-01", "poddasze-02", "poddasze-06",
                                    "poddasze-07", "poddasze-03", "poddasze-04",
                                    "poddasze-05"])}

{grupa("Łazienki", "04", ["lazienka-05", "lazienka-06", "lazienka-01", "lazienka-02",
                          "lazienka-03", "lazienka-04"])}

{grupa("Łazienka w czerni i bieli", "05", ["lazienka-07", "lazienka-08"])}

{grupa("Poddasze z wnęką na wannę", "06", ["poddasze2-01", "poddasze2-02",
                                           "poddasze2-04", "poddasze2-03"])}

{grupa("Beton architektoniczny i schody", "07", ["beton-02", "beton-ciemny", "schody-01"])}

{grupa("Tak to powstaje", "08", ["robota-01", "robota-02", "robota-03"])}

{grupa("Elewacja i podbitka", "09", ["elewacja-01", "elewacja-02", "elewacja-03",
                                     "elewacja-04"])}
  </div>
</section>

{domkniecie("Chcesz mieć podobnie u siebie?",
            "Zadzwoń albo napisz na WhatsAppie - umawiamy oględziny i wracamy "
            "z wyceną do 5 dni roboczych.")}"""


# ══════════════════════════════════════════════════════════════════════════════
#  O NAS - układ LIST: oś lat i narracja, na końcu film z ekipą i dane firmy.
# ══════════════════════════════════════════════════════════════════════════════
def kadr_o_nas():
    """Kadr między osią lat a narracją na podstronie „O nas".

    🔴 DECYZJA K. z 07.09.2026. Powód: na telefonie kolumny `oś lat | narracja`
    zwijają się w jedną i człowiek dostaje 104 słowa bez ani jednego obrazu -
    bramka zgłaszała to jako `sciana_tekstu`. Kadr wchodzi MIĘDZY oś a narrację,
    więc na telefonie przerywa ścianę tekstu w połowie.

    ⛔ NIE PRZENOSIĆ GO W HTML - ani do prawej kolumny, ani na koniec sekcji.
    Na telefonie wylądowałby POD całym tekstem i nie przerywał niczego.
    Kolejność w HTML jest tu treścią; położenie na laptopie robi SIATKA (CSS).

    🔴 08.09.2026 kadr jest SZEROKI i idzie przez OBIE kolumny (uwaga K.: „popraw tę
    pustą przestrzeń"). Wcześniej stał pionowo w lewej kolumnie i rozpychał ją do
    760 px przy 398 px kolumny obok - pod krótszą zostawało 400 px pustki, a im
    szerszy ekran, tym większej.
    """
    return ('<figure class="kadr-o-nas rv">'
            # ⛔ BEZ `loading="lazy"`: kadr stoi tuż nad drugim ekranem i przy
            # przewijaniu zostawiał pustą dziurę (bramka 07.09.2026).
            '<img src="img/kadr-o-nas.jpg" width="2000" height="909" '
            'alt="Rusztowanie ustawione wzdłuż ściany domu w trakcie robót elewacyjnych" '
            'decoding="async">'
            '<figcaption>Rusztowanie przy elewacji - tak wygląda nasz dzień na budowie.</figcaption>'
            '</figure>')


def o_nas(naglowek):
    return f"""{naglowek("o-nas.html")}

{otwarcie("O nas", "Firma rodzinna z Błońska",
          kadr="otw-o-nas.jpg",
          opis="Rusztowanie ustawione wzdłuż ściany domu w trakcie robót elewacyjnych",
          lead=
          "Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku "
          "pod własnym szyldem w Polsce. Pracujemy w wielkopolskiem i lubuskiem.")}

<section class="sekcja">
  <div class="wrap uklad-o-nas">
    <div class="o-nas-lata">
      <ol class="lata lata--ruch rv">
        <li style="--i:0"><b>2005</b><p>Zaczynamy pracę na budowach w Niemczech.</p></li>
        <li style="--i:1"><b>2015</b><p>Rejestrujemy własną firmę w Polsce, w Błońsku pod Rakoniewicami.</p></li>
        <li style="--i:2"><b>Dziś</b><p>Wykończenia wnętrz pod klucz - od gładzi i malowania
          po łazienki, poddasza i montaż drzwi.</p></li>
      </ol>
    </div>
    {kadr_o_nas()}
    <div class="tekst-dlugi rv">
      <h3>Co znaczy „rodzinna”</h3>
      <p>Że na budowie pracują ci sami ludzie, którzy podpisują fakturę. Firma stoi w Polsce
        od 2015 roku, a wcześniej przez dziesięć lat robiliśmy to samo na budowach w Niemczech.</p>
      <h3>Co robimy najczęściej</h3>
      <p>Szpachlowanie, malowanie, łazienki i sucha zabudowa - te cztery rzeczy wchodzą
        na niemal każdą budowę. Do tego poddasza pod klucz i montaż drzwi, a poza wnętrzami
        elewacje z podbitką, beton architektoniczny i wykończenia schodów.</p>
      <h3>Po wyschnięciu widać wszystko</h3>
      <p>Gładź, płytka wielkoformatowa i skos poddasza mają jedną wspólną cechę: efekt widać dopiero wtedy, gdy jest za późno na poprawki. Dlatego zabudowa, gładzie i malowanie idą u nas jedną ręką - nie ma komu zrzucić winy za nierówną ścianę.</p>
    </div>
  </div>
</section>


{domkniecie("Reszty dowiesz się przez telefon",
            "Zadzwoń albo napisz - umawiamy oględziny na miejscu.")}"""


# ══════════════════════════════════════════════════════════════════════════════
#  KONTAKT - układ DOKUMENT: karta danych, droga do wyceny, mapa po kliknięciu.
# ══════════════════════════════════════════════════════════════════════════════
def kontakt(naglowek):
    """Podstrona kontaktu.

    🔴 08.09.2026, blok E - test „czy topowa firma dałaby to u siebie":
    ⛔ Z ramki wezwania wyleciało „8:00-20:00, wielkopolskie i lubuskie". Godziny
       stały na tej JEDNEJ podstronie cztery razy (lead, wiersz „Godziny" w karcie,
       ramka, stopka), a obszar trzy. Ramka ma dokładać powód, żeby zadzwonić,
       nie recytować po raz czwarty to, co czytelnik ma dwa ekrany wyżej w tabelce.
    🔴 Zasłona mapy dostała adres (`.mapa-adres`) i ciemny panel z siatką w tle -
       wcześniej był to biały prostokąt na papierze, czyli coś, co czyta się jak
       element, który się nie wczytał. Wygląd siedzi w `app.css`.
    ⚠️ Prawa kolumna („Trzy kroki do ceny") kończy się ~180 px wyżej niż karta
       z danymi. Sprawdzone i ZOSTAWIONE: przy rytmie sekcji 5-10 rem to czyta się
       jak powietrze, nie jak dziura (inaczej niż 400 px pustki w „o nas").
       ⛔ Nie zapychać tego zdjęciem - wszystkie 38 kadrów klienta już gdzieś stoją,
          a jeden kadr nie może stać w dwóch miejscach.
    """
    return f"""{naglowek("kontakt.html")}

{otwarcie("Kontakt", "Zadzwoń albo napisz",
          kadr="otw-kontakt.jpg",
          opis="Bieg betonowych schodów przy gotowej, gładkiej ścianie",
          lead=
          "Telefon odbieramy od 8:00 do 20:00. Na WhatsAppie możesz od razu wrzucić "
          "zdjęcia wnętrza - to najszybszy sposób, żebyśmy wiedzieli, o czym mowa.")}

<section class="sekcja">
  <div class="wrap dwie-kolumny">
    <div class="karta rv">
      <h2>Dane kontaktowe</h2>
      <table class="dane">
        <tr><th>Telefon</th><td><a href="tel:{TEL_E164}">{TEL}</a></td></tr>
        <tr><th>WhatsApp</th><td><a href="{WA_LINK}" rel="noopener">{WA}</a></td></tr>
        <tr><th>E-mail</th><td><a href="mailto:a.s-tchorzewski@wp.pl">a.s-tchorzewski@wp.pl</a></td></tr>
        <tr><th>Godziny</th><td>8:00-20:00</td></tr>
        <tr><th>Obszar</th><td>województwo wielkopolskie i lubuskie</td></tr>
        <tr><th>Adres</th><td>Błońsko 46, 64-308 Jabłonna</td></tr>
        <tr><th>Dane firmy</th><td>Firma Ogólnobudowlana Artur Tchórzewski<br>
          NIP 995 004 44 65 · REGON 363138510</td></tr>
      </table>
      <div class="kontakt-linia" style="margin-top:26px">
        <a class="btn" href="tel:{TEL_E164}">Zadzwoń {TEL}</a>
        <a class="duch" href="{WA_LINK}" rel="noopener">{ikona_wa()}WhatsApp</a>
      </div>
    </div>

    <div class="tekst-dlugi rv">
      <span class="etykieta">Jak wygląda wycena</span>
      <h2>Trzy kroki do ceny</h2>
      <ol class="lata lata--ruch rv">
        <li style="--i:0"><b>1</b><p>Dzwonisz albo piszesz na WhatsAppie i mówisz, co ma być zrobione.</p></li>
        <li style="--i:1"><b>2</b><p>Umawiamy się na oględziny - cenę robi zakres i stan wnętrza,
          a tego nie da się ocenić przez telefon.</p></li>
        <li style="--i:2"><b>3</b><p>Wracamy z wyceną do 5 dni roboczych od oględzin.</p></li>
      </ol>
    </div>
  </div>
</section>

<section class="sekcja sekcja--mapa">
  <div class="wrap">
    <div class="naglowek-sekcji rv">
      <span class="etykieta">Gdzie nas znaleźć</span>
      <h2>Błońsko, powiat grodziski</h2>
      <p class="pod">Błońsko leży pod Rakoniewicami, w powiecie grodziskim - stąd wyjeżdżamy na budowy.</p>
    </div>
    <iframe class="mapa rv" title="Mapa: Błońsko 46, 64-308"
      src="https://maps.google.com/maps?q=B%C5%82o%C5%84sko%2046%2C%2064-308%20Jab%C5%82onna&amp;z=15&amp;output=embed"
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>

{domkniecie("Zadzwoń",
            "Jesteśmy pod telefonem od 8 do 20. Gdy nie odbierzemy, oddzwaniamy.")}"""


# ══════════════════════════════════════════════════════════════════════════════
#  DOKUMENTY
# ══════════════════════════════════════════════════════════════════════════════
def polityka(naglowek):
    return f"""{naglowek("")}

{otwarcie("Dokument", "Polityka prywatności",
          "Krótko, bo i strona jest prosta: nie zbieramy danych, nie mierzymy ruchu "
          "i nie zapisujemy ciasteczek.")}

<section class="sekcja">
  <div class="wrap tekst-dlugi">
    <p><strong>Administrator danych:</strong> Firma Ogólnobudowlana Artur Tchórzewski,
      Błońsko 46, 64-308 Jabłonna, NIP 995 004 44 65.</p>
    <p><strong>Kontakt:</strong> telefon {TEL}, WhatsApp {WA}, e-mail a.s-tchorzewski@wp.pl.</p>
    <p><strong>Formularze:</strong> na tej stronie nie ma formularza kontaktowego. Kontakt
      odbywa się telefonicznie, przez WhatsAppa albo mailem, a dane podane w rozmowie służą
      wyłącznie do przygotowania wyceny i wykonania robót.</p>
    <p><strong>Ciasteczka i statystyki:</strong> strona nie zapisuje ciasteczek, nie mierzy
      ruchu i nie ma skryptów śledzących ani reklam.</p>
    <p><strong>Mapa Google:</strong> na stronie „Kontakt” osadzona jest mapa Google.
      Przy jej wczytaniu przeglądarka łączy się z serwerami Google i obowiązują wtedy
      zasady prywatności Google.</p>
    <p><strong>Twoje prawa:</strong> dostęp do swoich danych, sprostowanie, usunięcie,
      ograniczenie przetwarzania i sprzeciw. Wystarczy telefon albo mail. Przysługuje też
      skarga do Prezesa Urzędu Ochrony Danych Osobowych.</p>
    <p><strong>Jak długo trzymamy dane:</strong> przez czas potrzebny na wycenę i wykonanie
      robót, a dokumenty księgowe przez okres wymagany przepisami podatkowymi.</p>
  </div>
</section>"""


def czterysta(naglowek):
    return f"""{naglowek("")}

{otwarcie("Błąd 404", "Tej strony nie ma",
          "Adres jest nieaktualny albo ma literówkę. Wszystko, co mamy, jest pod linkami "
          "niżej - albo po prostu zadzwoń.")}

<section class="sekcja">
  <div class="wrap">
    {przyciski_kontakt("index.html", "Strona główna")}
  </div>
</section>"""


def strony(naglowek):
    return [
        {"plik": "index.html",
         "tytul": "A.S Tchórzewski - wykończenia wnętrz, wielkopolskie i lubuskie",
         "opis": "Szpachlowanie i gładzie, malowanie, łazienki i sucha zabudowa. Rodzinna "
                 "firma, ponad 20 lat na budowach. Wycena do 5 dni roboczych od oględzin. "
                 "Tel. 667 434 222.",
         "hero": "scena",
         "tresc": index(naglowek)},
        {"plik": "co-robimy.html",
         "tytul": "Co robimy - gładzie, malowanie, łazienki, sucha zabudowa | A.S Tchórzewski",
         "opis": "Szpachlowanie i gładzie ręczne oraz maszynowe, malowanie agregatem, "
                 "łazienki z płytką wielkoformatową, sucha zabudowa poddaszy, montaż drzwi "
                 "i okien. Wielkopolskie i lubuskie.",
         "tresc": co_robimy(naglowek)},
        {"plik": "realizacje.html",
         "tytul": "Realizacje - poddasza, łazienki, elewacje | A.S Tchórzewski",
         "opis": "Zdjęcia z naszych budów: poddasza pod klucz, łazienki z wanną "
                 "wolnostojącą, beton architektoniczny, schody, elewacje z podbitką "
                 "oraz rozbudowa przed i po.",
         "tresc": realizacje(naglowek)},
        {"plik": "o-nas.html",
         "tytul": "O nas - firma rodzinna, ponad 20 lat na budowach | A.S Tchórzewski",
         "opis": "Od 2005 roku na budowach w Niemczech, od 2015 pod własnym szyldem "
                 "w Polsce. Firma rodzinna z Błońska, wykończenia wnętrz w wielkopolskiem "
                 "i lubuskiem.",
         "tresc": o_nas(naglowek)},
        {"plik": "kontakt.html",
         "tytul": "Kontakt - 667 434 222, WhatsApp 882 832 244 | A.S Tchórzewski",
         "opis": "Telefon 667 434 222, WhatsApp 882 832 244, godziny 8:00-20:00. "
                 "Wykończenia wnętrz w wielkopolskiem i lubuskiem. Wycena do 5 dni "
                 "roboczych od oględzin.",
         "tresc": kontakt(naglowek)},
        {"plik": "polityka-prywatnosci.html",
         "tytul": "Polityka prywatności | A.S Tchórzewski",
         "opis": "Kto jest administratorem danych, po co je zbieramy i jakie masz prawa. "
                 "Strona bez ciasteczek, statystyk i narzędzi zewnętrznych.",
         "tresc": polityka(naglowek)},
        {"plik": "404.html",
         "tytul": "Nie ma takiej strony | A.S Tchórzewski",
         "opis": "Tej strony nie ma pod tym adresem.",
         "noindex": True,
         "tresc": czterysta(naglowek)},
    ]
