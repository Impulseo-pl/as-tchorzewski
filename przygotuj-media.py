#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A.S TCHÓRZEWSKI — przygotowanie zdjęć i filmów do `img/` oraz `video/`.

    python3 przygotuj-media.py            # wszystko
    python3 przygotuj-media.py zdjecia    # tylko zdjęcia (szybkie)

Źródło: `materialy/` (38 zdjęć z ich IG/FB, 2 filmy, logo odzyskane z banera).
⛔ Zero stocku — `DESIGN.md`, sekcja „Zdjęcia".

🔴 Nazwa pliku w `img/` opisuje MIEJSCE NA STRONIE, nie pochodzenie. Gdy klient przyśle
   oryginały z telefonu (pytanie 3), podmienia się wpis w PLANIE i przebudowuje — HTML
   i CSS zostają nietknięte.

🔴 Kadry PIONOWE zostają pionowe (`DESIGN.md`: „bez kadrowania, jako obiekt na scenie").
   Kadrujemy wyłącznie tam, gdzie slot z natury jest inny niż zdjęcie: kwadraty „przed
   i po" (są kwadratowe u źródła) i jeden pas 21:9 z jedynego poziomego materiału.
"""
import os
import subprocess
import sys

from PIL import Image, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
ZR = os.path.join(ROOT, "materialy", "realizacje")
WID = os.path.join(ROOT, "materialy", "wideo")
IMG = os.path.join(ROOT, "img")
VIDEO = os.path.join(ROOT, "video")

# slot                     źródło                              szer.  proporcja  pion  jakość
PLAN = [
    # ── hero: PEŁNOEKRANOWY kadr sceny (decyzja K. 08.09.2026). Ściana z betonu
    #    architektonicznego - najmocniejsza rzecz w jego portfolio i jedyne zdjęcie
    #    wnętrza, które niesie tekst na sobie. Kadr NIE jest cięty do proporcji
    #    ekranu: oddajemy 1440×1300, a wycinek dobiera `object-fit:cover` - inaczej
    #    na telefonie (kadr pionowy) zostałby pasek. Bierzemy GÓRĘ, bo u dołu stoją
    #    wiadra i deska.
    ("hero.jpg",              "beton-arch-ciemny-01.jpg",        1440, 1440/1300, 0.10, 82),

    # ── otwarcia podstron: każde ma SWÓJ kadr, żeby podstrona nie zaczynała się
    #    płaskim czarnym paskiem. Pas jest niski, więc źródło tnie się do 16:7. ────
    ("otw-co-robimy.jpg",     "poddasze-belka-swiatlo-05.jpg",   1440, 16/7, 0.34, 78),
    ("otw-realizacje.jpg",    "poddasze2-okna-01.jpg",           1440, 16/7, 0.30, 78),
    ("otw-o-nas.jpg",         "poddasze-belki-01.jpg",           1200, 16/7, 0.34, 80),
    ("otw-kontakt.jpg",       "schody-beton-11.jpg",             1440, 16/7, 0.22, 78),

    # ── przed i po: u źródła kwadraty, więc kwadrat nie jest kadrowaniem ─────────
    ("przed.jpg",             "PRZED-rozbudowa.jpg",             1100, 1/1,  0.5, 80),
    ("po.jpg",                "PO-rozbudowa.jpg",                1100, 1/1,  0.5, 80),

    # ── kafle usług (kolejność z briefu: szpachlowanie, malowanie, łazienki,
    #    sucha zabudowa; drzwi i okna niżej) ──────────────────────────────────────
    ("u-szpachlowanie.jpg",   "poddasze-belka-swiatlo-05.jpg",   1000, 3/4,  0.5, 78),
    ("u-malowanie.jpg",       "_klatka-agregat.jpg",              720, 3/4,  0.5, 78),
    ("u-lazienki.jpg",        "lazienka-wanna-01.jpg",            739, 3/4,  0.5, 80),
    ("u-sucha-zabudowa.jpg",  "poddasze-skos-09.jpg",            1000, 3/4,  0.5, 78),
    ("u-drzwi-okna.jpg",      "hol-drzwi-12.jpg",                1000, 3/4,  0.5, 78),

    # ── pas na stronie głównej: ŁAZIENKA NA PODDASZU (wanna we wnęce).
    #
    # 🔴 10.09.2026, trzy podejścia i jedna nauka (K.: „dalej zdjęcie wygląda kiepsko —
    #    obejrzyj je sam przed wstawieniem"). Dwa pierwsze liczyły ostrość i proporcję,
    #    a nie sprawdziły, CO WIDAĆ. Metoda, która to naprawiła:
    #
    #    ⛔ PAS POKAZUJE TYLKO ŚRODKOWE ~52% PLIKU (420 px z 810 px ramki). Kadrowanie do
    #       16:9 i oglądanie całego pliku KŁAMIE — na stronie widać z niego pasek
    #       o proporcji 1440/420 = 3,43:1. Zanim cokolwiek wstawisz, wytnij ze źródła
    #       dokładnie ten pasek i obejrzyj GO, a nie plik.
    #       Skrypt do tego: `scratchpad/strip-*.jpg` (kandydaci × trzy wysokości).
    #
    #    Odrzucone po obejrzeniu paska, nie po liczbach:
    #      · `beton-arch-jasny-04` — ostre (×1,83), ale pasek to ciemna cętkowana plama
    #        z przepaloną smugą; wygląda jak zawilgocona ściana, nie jak wykończenie.
    #      · `poddasze2-sciana-zielen-02` — w pasku wychodzi przepalone okno po lewej,
    #        pusta płyta w środku i podejścia wodne (czerwone/niebieskie) na zieleni.
    #      · `lazienka-wanna-03` — pasek to sam brzuch wanny i kosz na śmieci.
    #      · `schody-beton-11` — dobry pasek, ale to nagłówek podstrony „kontakt".
    #
    #    Wybrane: wanna we wnęce, kamień w ciepłym beżu, świetlik z zielenią drzew po prawej.
    #    Kadr `y 338-1013` ustawiony tak, żeby widoczny pasek trafił dokładnie w y 500-850.
    #    Powiększenie ×2,0 z 1200 px — sprawdzone na żywej stronie przy DPR 2, trzyma się.
    ("pas-lazienka.jpg",      "poddasze2-wanna-wneka-05.jpg",    2400, 1440/810, 0.5, 84, True,
     (0, 338, 1200, 1013)),

    # ── DRUGI pas 21:9, tym razem SZEROKI I OSTRY. Elewacja to jedyny materiał
    #    z pełnych oryginałów (3072×4096), więc jako jedyna wytrzymuje wycięcie
    #    pasa 2400 px bez powiększania. Zmierzone 07.09.2026: przy 21:9 zostaje
    #    32 % kadru i nadal jest ostre. Kadr bierze ŚRODEK - u góry samo niebo,
    #    u dołu kostka brukowa.
    ("pas-elewacja.jpg",      "elewacja-po-taras-04.jpg",        2400, 21/9, 0.46, 80),

    # ── kadr na „O nas": rusztowanie ekipy, SZEROKI. Wchodzi 08.09.2026 w miejsce
    #    kadru pionowego - to on rozpychał lewą kolumnę i zostawiał 400 px pustki
    #    pod krótszą prawą (uwaga K.). Szeroki kadr idzie przez obie kolumny.
    ("kadr-o-nas.jpg",        "elewacja-rusztowanie-09.jpg",     2000, 2.2,  0.34, 80),

    # ── galeria realizacji: naturalne proporcje, bez kadrowania ─────────────────
    ("z-poddasze-01.jpg",     "poddasze-belki-02.jpg",           1100, None, 0.5, 78),
    ("z-poddasze-02.jpg",     "poddasze-belki-03.jpg",           1100, None, 0.5, 78),
    ("z-poddasze-03.jpg",     "poddasze-pokoj-07.jpg",           1100, None, 0.5, 78),
    ("z-poddasze-04.jpg",     "poddasze-skos-08.jpg",            1100, None, 0.5, 78),
    ("z-poddasze-05.jpg",     "poddasze-lazienka-04.jpg",        1100, None, 0.5, 78),
    ("z-lazienka-01.jpg",     "lazienka-wanna-03.jpg",            900, None, 0.5, 80),
    ("z-lazienka-02.jpg",     "lazienka-wanna-02.jpg",           900, None, 0.5, 80),
    ("z-lazienka-03.jpg",     "lazienka-plytki-04.jpg",           900, None, 0.5, 80),
    ("z-lazienka-04.jpg",     "lazienka-wtrakcie-podejscia-05.jpg", 1100, None, 0.5, 78),
    ("z-poddasze2-01.jpg",    "poddasze2-okna-01.jpg",           1100, None, 0.5, 78),
    ("z-poddasze2-02.jpg",    "poddasze2-wanna-wneka-05.jpg",    1100, None, 0.5, 78),
    ("z-poddasze2-03.jpg",    "poddasze2-sciana-zielen-02.jpg",  1100, None, 0.5, 78),
    ("z-schody-01.jpg",       "schody-beton-10.jpg",             1100, None, 0.5, 78),
    ("z-beton-02.jpg",        "beton-arch-jasny-02.jpg",         1200, None, 0.5, 78),
    ("z-beton-03.jpg",        "beton-arch-jasny-04.jpg",         1200, None, 0.5, 78),
    # elewacja: jedyne pełne oryginały z telefonu (3072×4096) — stąd większa szerokość
    ("z-elewacja-01.jpg",     "elewacja-po-taras-04.jpg",        1200, None, 0.5, 72),
    ("z-elewacja-02.jpg",     "elewacja-po-01.jpg",              1200, None, 0.5, 72),
    ("z-elewacja-03.jpg",     "elewacja-po-03.jpg",              1200, None, 0.5, 72),
    ("z-elewacja-04.jpg",     "elewacja-wtrakcie-06.jpg",        1200, None, 0.5, 72),
]

# Filmy: `preload="none"` + odtwarzanie po kliknięciu (rdzeń, blok 7). Dźwięku nie ma —
# to hałas budowy, a bez ścieżki plik chudnie i nic nie zaskakuje klienta w słuchawkach.
FILMY = [
    ("agregat.mp4",  "malowanie-agregatem.mp4",  "plakat-agregat.jpg", "00:00:22"),
    ("ekipa.mp4",    "elewacja-ekipa.mp4",       "plakat-ekipa.jpg",   "00:00:03"),
]


def klatka_z_filmu(zrodlo, cel, czas):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", czas,
                    "-i", zrodlo, "-frames:v", "1", "-q:v", "3", cel], check=True)


def zdjecia():
    os.makedirs(IMG, exist_ok=True)
    # klatka z filmu służy jako kafel „malowanie" — człowiek przy pracy jest mocniejszy
    # niż pusta pomalowana ściana, a innego zdjęcia z ludźmi nie mamy
    klatka = os.path.join(ZR, "_klatka-agregat.jpg")
    if not os.path.exists(klatka):
        klatka_z_filmu(os.path.join(WID, "malowanie-agregatem.mp4"), klatka, "00:00:06")
    for slot, src, szer, prop, pion, jakosc, *reszta in PLAN:
        # 7. pole (nieobowiązkowe): wyostrzenie po powiększeniu. Włączaj TYLKO tam, gdzie
        # plik wychodzi szerszy niż źródło — LANCZOS przy powiększaniu zawsze zmiękcza,
        # a maska wyostrzająca oddaje krawędziom kontrast, którego interpolacja nie ma
        # skąd wziąć. ⛔ Nie włączaj przy pomniejszaniu: tam robi obwódki wokół krawędzi.
        wyostrz = bool(reszta and reszta[0])
        # 8. pole (nieobowiązkowe): KADR ZE ŹRÓDŁA `(x0, y0, x1, y1)` wycinany PRZED
        # dopasowaniem. `ImageOps.fit` umie przesuwać kadr tylko w jednej osi i zawsze
        # zostawia pełną szerokość źródła — a bywa, że interesuje nas wycinek w środku
        # (np. sama płaszczyzna ściany, bez sufitu, folii i bałaganu przy krawędziach).
        kadr = reszta[1] if len(reszta) > 1 else None
        im = ImageOps.exif_transpose(Image.open(os.path.join(ZR, src))).convert("RGB")
        if kadr:
            im = im.crop(kadr)
        if prop:
            wys = int(round(szer / prop))
            out = ImageOps.fit(im, (szer, wys), method=Image.LANCZOS, centering=(0.5, pion))
        else:                                   # bez kadrowania — samo przeskalowanie
            szer = min(szer, im.width)
            out = im.resize((szer, int(round(szer * im.height / im.width))), Image.LANCZOS)
        if wyostrz:
            out = out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=110, threshold=3))
        p = os.path.join(IMG, slot)
        out.save(p, "JPEG", quality=jakosc, optimize=True, progressive=True)
        print(f"  ✓ img/{slot:24s} {out.width}×{out.height}  "
              f"{os.path.getsize(p)//1024} KB  ← {src}")


def logo():
    """Logo do `img/` — w DWÓCH rozmiarach: pasek (240 px) i kurtyna wejścia (640 px).

    🔴 ŹRÓDŁEM JEST LOGO **STARE** (`logo-stare-przezroczyste.png`, czarny napis
       „TCHÓRZEWSKI"). Klient potwierdził je 07.09.2026 i to ono wywróciło całą stronę
       na jasną — patrz `DESIGN.md`, droga A.
    ⛔ NIE podstawiać `logo-nowe-przezroczyste.png`: nowy znak ma BIAŁY napis, a na
       jasnym pasku znika. Do 08.09.2026 ta funkcja robiła dokładnie to i po każdym
       uruchomieniu `przygotuj-media.py` logo w pasku stawało się niewidzialne
       (a plik puchł z 14 kB do 109 kB, bo szedł w oryginalnym rozmiarze).
    🔴 Paleta zamiast pełnego koloru: 558 kB → 14 kB przy tym samym wyglądzie.
    """
    src = os.path.join(ROOT, "materialy", "logo", "logo-stare-przezroczyste.png")
    im = Image.open(src).convert("RGBA")
    # ⚠️ Wysokości są WPISANE, nie liczone: `build.py` podaje je w atrybutach
    #    width/height (240×177, 640×472). Zaokrąglenie dawało 178 i 473, czyli obrazek
    #    o innych proporcjach niż deklaruje HTML — przeglądarka rezerwuje wtedy złe
    #    miejsce i znak drga przy ładowaniu.
    for cel, szer, wys in (("logo.png", 240, 177), ("logo-duze.png", 640, 472)):
        maly = im.resize((szer, wys), Image.LANCZOS).quantize(colors=255, method=Image.FASTOCTREE)
        p = os.path.join(IMG, cel)
        maly.save(p, "PNG", optimize=True)
        print(f"  ✓ img/{cel:24s} {szer}×{wys}  {os.path.getsize(p)//1024} KB  ← logo STARE")


def filmy():
    os.makedirs(VIDEO, exist_ok=True)
    for cel, src, plakat, czas in FILMY:
        zr = os.path.join(WID, src)
        wy = os.path.join(VIDEO, cel)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", zr,
                        "-an", "-vf", "scale=-2:960", "-c:v", "libx264", "-crf", "28",
                        "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", wy], check=True)
        klatka_z_filmu(zr, os.path.join(IMG, plakat), czas)
        print(f"  ✓ video/{cel:16s} {os.path.getsize(wy)//1024} KB  "
              f"(było {os.path.getsize(zr)//1024} KB)   + img/{plakat}")


if __name__ == "__main__":
    co = sys.argv[1] if len(sys.argv) > 1 else "wszystko"
    zdjecia()
    logo()
    if co != "zdjecia":
        filmy()
