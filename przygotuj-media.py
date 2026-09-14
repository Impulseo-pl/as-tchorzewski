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
# Kopie powiększone Upscaylem (Real-ESRGAN, offline, bez kredytów) — patrz `zrodlo()`.
UPS = os.path.join(ROOT, "materialy", "upscale")
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
    ("hero.jpg",              "sypialnia-poddasze-gotowa-14.jpg", 1440, 1440/1300, 0.45, 82),
    # ── wersje @2x dla kadrów pełnoekranowych. Wchodzą do `srcset`, więc plik 1× zostaje
    #    lekki dla zwykłych ekranów, a Retina dostaje realny materiał zamiast rozciągania.
    #    ⚠️ Mają sens dopiero od kiedy `materialy/upscale/` daje źródła 2400-2880 px —
    #       wcześniej „2×" byłoby tym samym plikiem, tylko cięższym.
    ("hero@2x.jpg",           "sypialnia-poddasze-gotowa-14.jpg", 2880, 1440/1300, 0.45, 78),

    # ── otwarcia podstron: każde ma SWÓJ kadr, żeby podstrona nie zaczynała się
    #    płaskim czarnym paskiem. Pas jest niski, więc źródło tnie się do 16:7. ────
    ("otw-co-robimy.jpg",     "poddasze-belka-swiatlo-05.jpg",   1440, 16/7, 0.34, 78),
    ("otw-co-robimy@2x.jpg",     "poddasze-belka-swiatlo-05.jpg",     2880, 16/7, 0.34, 78),
    ("otw-realizacje.jpg",    "poddasze2-okna-01.jpg",           1440, 16/7, 0.30, 78),
    ("otw-realizacje@2x.jpg",    "poddasze2-okna-01.jpg",             2880, 16/7, 0.30, 78),
    ("otw-o-nas.jpg",         "poddasze-belki-01.jpg",           1200, 16/7, 0.34, 80),
    ("otw-o-nas@2x.jpg",         "poddasze-belki-01.jpg",             2400, 16/7, 0.34, 78),
    ("otw-kontakt.jpg",       "schody-beton-11.jpg",             1440, 16/7, 0.22, 78),
    ("otw-kontakt@2x.jpg",       "schody-beton-11.jpg",               2880, 16/7, 0.22, 78),

    # ── przed i po: u źródła kwadraty, więc kwadrat nie jest kadrowaniem ─────────
    # przed.jpg / po.jpg robi osobny krok `suwak_przed_po()` - patrz niżej.

    # ── kafle usług (kolejność z briefu: szpachlowanie, malowanie, łazienki,
    #    sucha zabudowa; drzwi i okna niżej) ──────────────────────────────────────
    ("u-szpachlowanie.jpg",   "poddasze-belka-swiatlo-05.jpg",   1000, 3/4,  0.5, 78),
    ("u-malowanie.jpg",       "_klatka-agregat.jpg",              720, 3/4,  0.5, 78),
    ("u-lazienki.jpg",        "lazienka-wanna-01.jpg",            739, 3/4,  0.5, 80),
    ("u-sucha-zabudowa.jpg",  "poddasze-skos-09.jpg",            1000, 3/4,  0.5, 78),
    ("u-drzwi-okna.jpg",      "pokoj-okna-rolety-15.jpg",        1000, 3/4,  0.5, 78),

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
    ("z-lazienka-01.jpg",     "lazienka-wanna-03.jpg",           1200, None, 0.5, 80),
    ("z-lazienka-02.jpg",     "lazienka-wanna-02.jpg",          1200, None, 0.5, 80),
    ("z-lazienka-03.jpg",     "lazienka-plytki-04.jpg",         1200, None, 0.5, 80),
    ("z-lazienka-04.jpg",     "lazienka-wtrakcie-podejscia-05.jpg", 1100, None, 0.5, 78),
    ("z-poddasze2-01.jpg",    "poddasze2-okna-01.jpg",           1100, None, 0.5, 78),
    ("z-poddasze2-02.jpg",    "poddasze2-wanna-wneka-05.jpg",    1100, None, 0.5, 78),
    ("z-poddasze2-03.jpg",    "poddasze2-sciana-zielen-02.jpg",  1100, None, 0.5, 78),
    ("z-schody-01.jpg",       "schody-beton-10.jpg",             1100, None, 0.5, 78),
    ("z-beton-02.jpg",        "beton-arch-jasny-02.jpg",         1200, None, 0.5, 78),
    ("z-beton-ciemny.jpg",    "beton-arch-ciemny-01.jpg",        1200, 4/3, 0.34, 78),
    # elewacja: jedyne pełne oryginały z telefonu (3072×4096) — stąd większa szerokość

    # ── zdjęcia z telefonu klienta (WhatsApp, 14.09.2026). Bez kadrowania: kadr
    #    pionowy zostaje pionowy, poziomy poziomy - `DESIGN.md`, sekcja „Zdjęcia".
    #    ⚠️ Nie ma ich w `materialy/upscale/`, więc `-duze.jpg` powstaje z oryginału
    #       (1200-2048 px) - to wystarcza powiększalnikowi, ale nie pasowi na całą szerokość.
    ("z-wejscie-01.jpg",      "wejscie-drzwi-cegla-13.jpg",          1100, None, 0.5, 78),
    ("z-hol-01.jpg",          "hol-lamele-lustro-21.jpg",            1200, None, 0.5, 78),
    ("z-hol-02.jpg",          "korytarz-lamele-20.jpg",              1200, None, 0.5, 78),
    ("z-schody-02.jpg",       "schody-kamien-gotowe-16.jpg",         1200, None, 0.5, 78),
    ("z-pokoj-01.jpg",        "pokoj-okna-rolety-15.jpg",            1200, None, 0.5, 78),
    ("z-pokoj-02.jpg",        "kacik-polki-podswietlenie-17.jpg",    1100, None, 0.5, 78),
    ("z-pokoj-03.jpg",        "belki-jodelka-19.jpg",                1100, None, 0.5, 78),
    ("z-poddasze-06.jpg",     "poddasze-belki-a-28.jpg",             1100, None, 0.5, 78),
    ("z-poddasze-07.jpg",     "pokoj-panele-belki-32.jpg",           1100, None, 0.5, 78),
    ("z-lazienka-05.jpg",     "lazienka-mala-gotowa-33.jpg",         1100, None, 0.5, 78),
    ("z-lazienka-06.jpg",     "lazienka-mala-kabina-34.jpg",         1100, None, 0.5, 78),
    ("z-lazienka-07.jpg",     "lazienka-czarna-wanna-24.jpg",        1100, None, 0.5, 78),
    ("z-lazienka-08.jpg",     "lazienka-czarna-wc-26.jpg",           1100, None, 0.5, 78),
    ("z-poddasze2-04.jpg",    "poddasze2-wneka-siedzisko-23.jpg",    1100, None, 0.5, 78),
    ("z-robota-02.jpg",       "sciana-plytki-wtrakcie-30.jpg",       1200, None, 0.5, 78),
    ("z-robota-03.jpg",       "podloga-plytki-wtrakcie-29.jpg",      1100, None, 0.5, 78),


    # ── druga para „przed i po" na głównej: wnętrze. ⛔ NIE idzie w suwak przenikający
    #    jak rozbudowa - zdjęcia robione z innego miejsca i innej ogniskowej (korelacja
    #    krawędzi 0,17), więc przy przenikaniu okno balkonowe przeskakiwałoby w bok.
    #    Stoją obok siebie, każde ze swoją etykietą. Źródło ma 900 px, więc bez @2x:
    #    kafel stoi na ~570 px, czyli gęstość i tak wychodzi powyżej 1,5.
    # 🔴 Proporcja MUSI być ta sama co u pary elewacji (OKNO_SUWAKA, 1500/1239) - od 14.09.2026
    #    obie pary stoją obok siebie w jednym rzędzie i rozjazd proporcji od razu widać.
    #    Materiał: składanka klienta miała 900 px na kadr, czyli za mało na pół szerokości
    #    rzędu - dlatego oba zdjęcia przeszły przez `upscale.sh` (1800 px, obejrzane 1:1).
    ("przedpo-pokoj-przed.jpg",    "pokoj-przed-36.jpg",         1300, 1500/1239, 0.45, 82),
    ("przedpo-pokoj-przed@2x.jpg", "pokoj-przed-36.jpg",         1800, 1500/1239, 0.45, 78),
    ("przedpo-pokoj-po.jpg",       "pokoj-po-35.jpg",            1300, 1500/1239, 0.45, 82),
    ("przedpo-pokoj-po@2x.jpg",    "pokoj-po-35.jpg",            1800, 1500/1239, 0.45, 78),

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
        im = ImageOps.exif_transpose(Image.open(zrodlo(src))).convert("RGB")
        if kadr:
            # 🔴 `kadr` zapisujemy ZAWSZE w pikselach ORYGINAŁU z `materialy/realizacje/`.
            #    Gdy `zrodlo()` poda kopię powiększoną, współrzędne trzeba przeskalować —
            #    inaczej wycinek wyląduje w lewym górnym rogu zamiast tam, gdzie go ustawiono.
            with Image.open(os.path.join(ZR, src)) as _oryg:
                skala = im.width / _oryg.width
            if skala != 1:
                kadr = tuple(int(round(v * skala)) for v in kadr)
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

    # ── Wersje `-duze.jpg` dla POWIĘKSZALNIKA. ─────────────────────────────────────
    # Kafel galerii stoi w siatce na ~577 px, ale po kliknięciu ten sam plik idzie na
    # pół ekranu — i wtedy 1100 px to gęstość ~0,46. Powiększalnik ładuje jeden plik
    # na żądanie (`data-zoom`, `rdzen.js` blok 5), więc większy rozmiar nie obciąża
    # siatki. Siatka zostaje przy swoim lekkim pliku.
    for slot, src, _szer, _prop, _pion, _jak, *_r in PLAN:
        if not slot.startswith("z-"):
            continue
        im = ImageOps.exif_transpose(Image.open(zrodlo(src))).convert("RGB")
        szer = min(2000, im.width)
        out = im.resize((szer, int(round(szer * im.height / im.width))), Image.LANCZOS)
        cel = slot.replace(".jpg", "-duze.jpg")
        p = os.path.join(IMG, cel)
        # q72, nie 76: te pliki idą TYLKO po kliknięciu i tylko jeden naraz, ale kadry
        # elewacji (z prawdziwych 3072 px, faktura tynku) puchły przy 76 do 0,8 MB.
        out.save(p, "JPEG", quality=72, optimize=True, progressive=True)
        print(f"  ✓ img/{cel:24s} {out.width}×{out.height}  "
              f"{os.path.getsize(p)//1024} KB  ← {src}")


def zrodlo(nazwa):
    """Ścieżka do najlepszej wersji zdjęcia: powiększona, jeśli istnieje.

    🔴 Zdjęcia wnętrz przyszły od klienta przez sociale: EXIF wycięty, 1200-1440 px,
    61-140 kB. Na Retinie stały na gęstości 0,42-0,50 — pas i hero widocznie miękły.
    Oryginały leżą na telefonie klienta (pytanie 3), ale zanim je przyśle, kopie
    z `materialy/upscale/` (Upscayl, model `high-fidelity-4x`, ×4 → redukcja do ×2)
    dają realny materiał zamiast rozciągania interpolacją.

    ⛔ `materialy/realizacje/` zostaje NIETKNIĘTE — to jest materiał od klienta.
       Kasujesz `upscale/` → wszystko dalej się buduje, tylko miękcej.
    ⚠️ Model dorysowuje mikrodetal. Na tych zdjęciach (tynk, płyta, kamień, stolarka)
       to retusz, nie zmyślanie — ale KAŻDY plik obejrzyj, zanim wejdzie na stronę.
       Skrypt wsadowy: `~/.claude/skills/strona-docelowa/upscale.sh <repo>`.
    """
    lepsza = os.path.join(UPS, os.path.splitext(nazwa)[0] + ".jpg")
    return lepsza if os.path.exists(lepsza) else os.path.join(ZR, nazwa)


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


# ══════════════════════════════════════════════════════════════════════════════
#  SUWAK PRZED/PO — dopasowanie kadrów homografią
#  ──────────────────────────────────────────────────────────────────────────────
#  K. 10.09.2026: „zdjęcia muszą być dopasowane PERFEKCYJNIE, tak żeby przy
#  przesuwaniu użytkownik miał wrażenie, że to dosłownie IDENTYCZNY kadr".
#
#  Obie fotki są z ręki, z innego miejsca i pod innym kątem, więc samo przycięcie
#  i przesunięcie NIE WYSTARCZY - pokrywa się wtedy albo dół, albo góra, nigdy oba.
#  Rozwiązanie: elewacja z otworem drzwiowym leży w JEDNEJ PŁASZCZYŹNIE, więc
#  wystarczy homografia z czterech rogów tego otworu, żeby ustawić zdjęcie „po"
#  dokładnie w układzie zdjęcia „przed". Płaszczyzna elewacji (mur, parapet, linia
#  opaski) pokrywa się wtedy co do piksela; rzeczy poza nią (żywopłot, boczna
#  ściana) lekko się przesuwają - to niewidoczne, bo i tak ich nie ma na „przed".
#
#  ⛔ Rogi są mierzone RĘCZNIE na zdjęciach z siatką współrzędnych (skala 0-1000
#     niezależna od rozdzielczości pliku). Zmieniasz zdjęcie w parze → mierzysz od
#     nowa, inaczej suwak rozjedzie się bardziej niż przed poprawką.
#  ⛔ Kolejność rogów: lewy górny, prawy górny, prawy dolny, lewy dolny.
# ══════════════════════════════════════════════════════════════════════════════
# ── PUNKTY ODNIESIENIA (skala 0-1000, niezależna od rozdzielczości pliku) ──────
# 🔴 Pierwsze podejście brało WYŁĄCZNIE cztery rogi otworu drzwiowego i to był błąd:
#    po wykończeniu ościeże jest o kilka centymetrów mniejsze niż surowy otwór
#    w murze, więc przyklejenie ich do siebie co do piksela rozciągało całe zdjęcie
#    „po" o ~2 % i wypychało resztę elewacji w pionie (K.: „mam wrażenie, że przed
#    jest niżej niż po"). Teraz kotwicą są NAROŻNIKI ELEWACJI PRZY GRUNCIE - tych
#    wykończenie nie rusza - a rogi otworu wchodzą jako wskazówka o mniejszej wadze.
#    Dopasowanie liczy się najmniejszymi kwadratami, więc błąd rozkłada się po całym
#    kadrze zamiast siedzieć w jednym miejscu.
# ⛔ Zmieniasz zdjęcie w parze → mierzysz punkty od nowa na zrzutach z siatką.
PARY_SUWAKA = [
    # (punkt na PRZED, ten sam punkt na PO)
    ((52, 755), (100, 900)),      # lewy narożnik elewacji przy gruncie
    ((981, 661), (858, 731)),     # prawy narożnik elewacji przy gruncie
    ((300, 253), (377, 367)),     # otwór: lewy górny
    ((800, 250), (719, 400)),     # otwór: prawy górny
    ((800, 672), (719, 757)),     # otwór: prawy dolny
    ((300, 693), (377, 800)),     # otwór: lewy dolny
]
WAGI_SUWAKA = [3.0, 3.0, 1.0, 1.0, 1.0, 1.0]

# Wspólne okno kadru, też w skali 0-1000. 🔴 K.: „nie ucinaj tak zdjęcia, ma być całe
# widoczne, tylko dopasowane najlepiej jak się da". Po dopasowaniu „po" pokrywa ~90 %
# kwadratu „przed"; to jest największy prostokąt mieszczący się w OBU - policzony maską
# pokrycia, nie na oko. Odpada tylko dolny pas trawnika ze znakiem wodnym klienta.
# Proporcja 998/826 = 1,208 MUSI stać w `aspect-ratio` ramki w `app.css`
# i w atrybutach width/height w `pages.py`.
OKNO_SUWAKA = (4, 4, 994, 822)

# -- OKNO SZERSZE DLA "PO" (K. 11.09.2026 i znow 14.09: "mozemy oddalic kadr tego
#    zdjecia efektu po?") ---------------------------------------------------------
# Wspolne okno wyzej jest przecieciem dwoch kadrow i dlatego "po" wychodzilo z niego
# przycietym zblizeniem na sam mur z oknem - nie bylo widac ANI dachu, ANI narozzika,
# ANI trawnika, czyli tego, co klient sprzedaje. Powiekszyc wspolnego okna sie nie da:
# "przed" po prostu nie ma tam pikseli (zmierzone - pokrycie 61 %).
#
# 🔴 14.09.2026: to okno wolno bylo przywrocic dopiero wtedy, kiedy z klocka zniknela
#    PRZESUWANA LINIA. Przy linii oba zdjecia musialy siedziec w jednym oknie, bo po jej
#    obu stronach ten sam mur stalby w innym miejscu. Strzalka przeskakuje cale kadry,
#    wiec kazdy moze miec swoje pole widzenia.
# ⛔ Wracasz do suwaka z linia -> "po" MUSI wrocic do OKNO_SUWAKA.
#
# Liczby nie sa dobrane na oko: `maks-okno.py` (sumy prefiksowe na masce pikseli) szukal
# NAJWIEKSZEGO prostokata o proporcji pary, ktory w calosci lezy na prawdziwych pikselach
# zdjecia po homografii. Wyszlo 1165 jednostek szerokosci (OKNO_SUWAKA ma 990, czyli
# o 18 % wiecej kadru), lewy gorny rog (70, -130). Poza te granice wychodza juz czarne rogi
# po prostowaniu. Proporcja MUSI zostac 1500/1239 - obie pary stoja obok siebie w rzedzie.
OKNO_PO = (70, -130, 1235, 832.3)

SUWAK = [("przed.jpg", 1500, 82, OKNO_SUWAKA), ("przed@2x.jpg", 2400, 76, OKNO_SUWAKA),
         ("po.jpg", 1500, 82, OKNO_PO), ("po@2x.jpg", 2400, 76, OKNO_PO)]


def _homografia(pary, wagi, skala):
    """Macierz przenosząca PO w układ PRZED, z najmniejszych kwadratów.
    `skala` przelicza punkty ze skali 0-1000 na piksele przestrzeni roboczej."""
    import numpy as np
    A, B, W = [], [], []
    for ((xd, yd), (xs, ys)), w in zip(pary, wagi):
        xd, yd, xs, ys = xd * skala, yd * skala, xs * skala, ys * skala
        A.append([xs, ys, 1, 0, 0, 0, -xd * xs, -xd * ys]); B.append(xd); W.append(w)
        A.append([0, 0, 0, xs, ys, 1, -yd * xs, -yd * ys]); B.append(yd); W.append(w)
    W = np.sqrt(np.array(W, float))
    h, *_ = np.linalg.lstsq(np.array(A, float) * W[:, None], np.array(B, float) * W, rcond=None)
    M = np.array([[h[0], h[1], h[2]], [h[3], h[4], h[5]], [h[6], h[7], 1.0]])
    # PIL chce przekształcenia ODWROTNEGO: piksel wyjściowy → piksel wejściowy
    odw = np.linalg.inv(M).ravel()
    return (odw / odw[8])[:8]


def suwak_przed_po():
    import numpy as np
    N = 2500                                   # przestrzeń robocza dopasowania
    # Okno „po" wychodzi poza kwadrat (ujemne y), więc obie warstwy renderujemy na
    # płótnie z zapasem - inaczej `crop` dokleiłby czarny pas zamiast pikseli zdjęcia.
    M = 1400

    przed = ImageOps.exif_transpose(Image.open(zrodlo("PRZED-rozbudowa.jpg")))
    przed = przed.convert("RGB").resize((N, N), Image.LANCZOS)
    po = ImageOps.exif_transpose(Image.open(zrodlo("PO-rozbudowa.jpg")))
    po = po.convert("RGB").resize((N, N), Image.LANCZOS)

    H = _homografia(PARY_SUWAKA, WAGI_SUWAKA, N / 1000)          # PIL: wyjście → wejście
    Hm = np.array(list(H) + [1.0]).reshape(3, 3)
    przes = np.array([[1, 0, -M], [0, 1, -M], [0, 0, 1]], float)  # płótno → kwadrat PRZED
    Hp = (Hm @ przes).ravel(); Hp = (Hp / Hp[8])[:8]
    po = po.transform((N + 2 * M, N + 2 * M), Image.PERSPECTIVE, tuple(Hp), Image.BICUBIC)

    plotno = Image.new("RGB", (N + 2 * M, N + 2 * M), (12, 12, 14))
    plotno.paste(przed, (M, M))
    przed = plotno

    for cel, szer, jakosc, okno in SUWAK:
        zr = przed if cel.startswith("przed") else po
        box = tuple(int(round(v * N / 1000)) + M for v in okno)
        prop = (okno[2] - okno[0]) / (okno[3] - okno[1])
        wys = int(round(szer / prop))
        out = zr.crop(box).resize((szer, wys), Image.LANCZOS)
        out = out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=3))
        sciezka = os.path.join(IMG, cel)
        out.save(sciezka, "JPEG", quality=jakosc, optimize=True, progressive=True)
        print(f"  ✓ img/{cel:24s} {szer}×{wys}  {os.path.getsize(sciezka)//1024} KB  "
              f"← {'kadr wspólny' if cel.startswith('przed') else 'kadr szeroki'}, homografia")


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


# ══════════════════════════════════════════════════════════════════════════════
#  WARIANTY PASÓW — jeden plik na każdą klasę ekranu
# ══════════════════════════════════════════════════════════════════════════════
# Pasy 21:9 idą przez CAŁĄ szerokość okna, więc ich rozmiar zależy od szerokości
# ekranu, a nie od stałego miejsca w układzie. Stąd `srcset` w jednostkach `w`
# + `sizes="100vw"`, a NIE konwencja `@2x` używana w reszcie tego pliku: `@2x`
# rozstrzyga o gęstości pikseli, ale nie wie nic o szerokości okna, więc telefon
# przy DPR 2-3 i tak brałby plik 2400 px.
#
# 🔴 Powód wprowadzenia (bramka wyglądu, telefon 390×844, 11.09.2026):
#    „pas-elewacja.jpg 2400 px / 330 kB w miejscu 390 px (3,1× nadmiaru przy
#    Retinie) — leci tak na każdej podstronie". Klient na telefonie płacił
#    transferem za piksele, których jego ekran nie umie pokazać.
#
# ⛔ Nie twórz tych plików ręcznie. Powstają TUTAJ, z gotowego pasa 2400 px,
#    więc kadr jest ten sam co w pliku bazowym i nie rozjedzie się przy
#    następnym `przygotuj-media.py`.
SZEROKOSCI_PASOW = (900, 1600)


def warianty_pasow():
    for nazwa in sorted(os.listdir(IMG)):
        if not nazwa.startswith("pas-") or not nazwa.endswith(".jpg"):
            continue
        if any(f"-{w}." in nazwa for w in SZEROKOSCI_PASOW):
            continue                      # to już jest wariant, nie rób wariantu z wariantu
        zr = os.path.join(IMG, nazwa)
        im = Image.open(zr)
        for szer in SZEROKOSCI_PASOW:
            if im.width <= szer:
                continue                  # nie powiększamy - to by dodało wagi bez treści
            cel = os.path.join(IMG, nazwa.replace(".jpg", f"-{szer}.jpg"))
            wys = int(round(szer * im.height / im.width))
            im.resize((szer, wys), Image.LANCZOS).save(
                cel, "JPEG", quality=80, optimize=True, progressive=True)
            print(f"  ✓ img/{os.path.basename(cel):24s} {szer}×{wys}  "
                  f"{os.path.getsize(cel)//1024} KB  ← {nazwa}")


if __name__ == "__main__":
    co = sys.argv[1] if len(sys.argv) > 1 else "wszystko"
    zdjecia()
    suwak_przed_po()
    warianty_pasow()
    logo()
    if co != "zdjecia":
        filmy()
