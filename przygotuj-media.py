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

# 🔴 JEDNA proporcja dla WSZYSTKICH czterech kadrow "przed i po" - stoja obok siebie
#    w jednym rzedzie i rozjazd od razu widac. Musi zgadzac sie z `aspect-ratio` w
#    `.duet-rama` (app.css) i z width/height w `pages.py`.
PARA = 1500 / 1322

# slot                     źródło                              szer.  proporcja  pion  jakość
PLAN = [
    # ── hero: PEŁNOEKRANOWY kadr sceny (decyzja K. 08.09.2026). Od 14.09.2026 to
    #    SYPIALNIA NA PODDASZU po wykończeniu (wcześniej ściana z betonu architektonicznego
    #    - przy masce przyciemnienia była prawie czarna). Kadr NIE jest cięty do proporcji
    #    ekranu: oddajemy 1440×1300, a wycinek dobiera `object-fit:cover` - inaczej
    #    na telefonie (kadr pionowy) zostałby pasek.
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
    # 🔴 30.09.2026: tło Kontaktu to już NIE schody (`schody-beton-11`) - klient kazał zdjąć
    #    ze strony WSZYSTKIE zdjęcia schodów („nie chcą, żeby one były na stronie").
    #    Zamiast nich okno dachowe z niebem, kadr dotąd nieużyty nigdzie (jeden kadr = jedno
    #    miejsce). Okno stoi PO PRAWEJ, czyli tam, gdzie przyciemnienie jest najsłabsze -
    #    tekst leży na ciemnej, gładkiej ścianie po lewej. Źródło 1200 px → `upscale.sh`.
    ("otw-kontakt.jpg",       "poddasze2-pokoj-03.jpg",          1440, 16/7, 0.25, 78),
    ("otw-kontakt@2x.jpg",       "poddasze2-pokoj-03.jpg",            2880, 16/7, 0.25, 78),

    # 🔴 B4 (naprawione 30.09.2026): commit `52fc09e` (14.09) przy wycinaniu homografii
    #    skasował z PLAN-u wszystkie wpisy od kafli usług do galerii - pliki w `img/`
    #    zostały, ale kolejne uruchomienie tego skryptu już by ich nie odtworzyło
    #    (a `-duze.jpg` galerii nie powstawały dla żadnego nowego kadru). Przywrócone
    #    1:1 z `52fc09e^`. ⛔ Wycinasz wpisy z PLAN-u → `git diff` tego pliku przed commitem.

    # ── kafle usług (kolejność z briefu: szpachlowanie, malowanie, łazienki,
    #    sucha zabudowa; drzwi i okna niżej) ──────────────────────────────────────
    ("u-szpachlowanie.jpg",   "poddasze-belka-swiatlo-05.jpg",   1000, 3/4,  0.5, 78),
    ("u-malowanie.jpg",       "_klatka-agregat.jpg",              720, 3/4,  0.5, 78),
    ("u-lazienki.jpg",        "lazienka-wanna-01.jpg",            739, 3/4,  0.5, 80),
    ("u-sucha-zabudowa.jpg",  "poddasze-skos-09.jpg",            1000, 3/4,  0.5, 78),
    ("u-drzwi-okna.jpg",      "pokoj-okna-rolety-39.jpg",        1000, 3/4,  0.5, 78),

    # ── bloki podstrony „Co robimy" - zdjęcia WSKAZANE PRZEZ KLIENTA 29.09.2026 (podpisy
    #    „Do 1" … „Do 5" pod zdjęciami na WhatsAppie). Ta sama proporcja 3:4 co kafle, żeby
    #    w blokach z DWOMA kadrami oba stały równo obok siebie.
    #    ⚠️ Kafle na GŁÓWNEJ (`u-szpachlowanie`, `u-malowanie`) zostają przy swoich kadrach -
    #       klient zmieniał podstronę, nie stronę główną.
    ("cr-szpachlowanie.jpg",  "poddasze-belki-a-28.jpg",         1000, 3/4,  0.5, 78),   # „Do 1"
    ("cr-malowanie.jpg",      "poddasze-jodelka-belki-37.jpg",   1000, 3/4,  0.5, 78),   # „Do 2"
    ("cr-lazienki.jpg",       "poddasze2-wneka-siedzisko-23.jpg", 1000, 3/4, 0.5, 78),   # „Do 3"
    ("cr-sucha-zabudowa.jpg", "poddasze-jodelka-skos-38.jpg",    1000, 3/4,  0.5, 78),   # „Do 4"
    # „Do 5" = `u-drzwi-okna` wyżej; drugi kadr bloku: te same okna w trakcie montażu
    ("cr-drzwi-okna-montaz.jpg", "okna-montaz-cegla-46.jpg",     1000, 3/4,  0.5, 78),
    # 06 Podłogi (nowa pozycja od klienta): korytarz z panelami. Kadr klienta jest wyższy
    # niż 3:4 - bierzemy DÓŁ, bo w tej sekcji treścią jest podłoga, nie sufit.
    ("cr-podlogi.jpg",        "korytarz-panele-40.jpg",          1000, 3/4,  0.8, 78),

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
    #      · `schody-beton-11` — dobry pasek, ale był nagłówkiem podstrony „kontakt";
    #        od 30.09.2026 schody są na stronie ZAKAZANE (polecenie klienta).
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
    ("z-lazienka-01.jpg",     "lazienka-wanna-03.jpg",           1200, None, 0.5, 80),
    ("z-lazienka-02.jpg",     "lazienka-wanna-02.jpg",          1200, None, 0.5, 80),
    ("z-lazienka-03.jpg",     "lazienka-plytki-04.jpg",         1200, None, 0.5, 80),
    ("z-lazienka-04.jpg",     "lazienka-wtrakcie-podejscia-05.jpg", 1100, None, 0.5, 78),
    ("z-poddasze2-01.jpg",    "poddasze2-okna-01.jpg",           1100, None, 0.5, 78),
    ("z-poddasze2-02.jpg",    "poddasze2-wanna-wneka-05.jpg",    1100, None, 0.5, 78),
    ("z-poddasze2-03.jpg",    "poddasze2-sciana-zielen-02.jpg",  1100, None, 0.5, 78),
    ("z-beton-02.jpg",        "beton-arch-jasny-02.jpg",         1200, None, 0.5, 78),
    ("z-beton-ciemny.jpg",    "beton-arch-ciemny-01.jpg",        1200, 4/3, 0.34, 78),
    # elewacja: jedyne pełne oryginały z telefonu (3072×4096) — stąd większa szerokość

    # ── zdjęcia z telefonu klienta (WhatsApp, 14.09.2026). Bez kadrowania: kadr
    #    pionowy zostaje pionowy, poziomy poziomy - `DESIGN.md`, sekcja „Zdjęcia".
    #    ⚠️ Nie ma ich w `materialy/upscale/`, więc `-duze.jpg` powstaje z oryginału
    #       (1200-2048 px) - to wystarcza powiększalnikowi, ale nie pasowi na całą szerokość.
    ("z-wejscie-01.jpg",      "wejscie-drzwi-cegla-13.jpg",          1100, None, 0.5, 78),
    ("z-hol-02.jpg",          "korytarz-lamele-20.jpg",              1200, None, 0.5, 78),
    ("z-pokoj-01.jpg",        "pokoj-okna-rolety-39.jpg",            1200, None, 0.5, 78),
    ("z-pokoj-02.jpg",        "kacik-polki-podswietlenie-17.jpg",    1100, None, 0.5, 78),
    ("z-pokoj-03.jpg",        "belki-jodelka-19.jpg",                1100, None, 0.5, 78),
    ("z-poddasze-06.jpg",     "poddasze-belki-a-28.jpg",             1100, None, 0.5, 78),
    ("z-poddasze-07.jpg",     "pokoj-panele-belki-32.jpg",           1100, None, 0.5, 78),
    ("z-lazienka-05.jpg",     "lazienka-mala-gotowa-33.jpg",         1100, None, 0.5, 78),
    ("z-lazienka-07.jpg",     "lazienka-czarna-wanna-zywsza-44.jpg",        1100, None, 0.5, 78),
    ("z-lazienka-08.jpg",     "lazienka-czarna-wc-zywsza-41.jpg",           1100, None, 0.5, 78),
    ("z-poddasze2-04.jpg",    "poddasze2-wneka-siedzisko-23.jpg",    1100, None, 0.5, 78),
    ("z-robota-02.jpg",       "sciana-plytki-wtrakcie-30.jpg",       1200, None, 0.5, 78),
    ("z-robota-03.jpg",       "podloga-plytki-wtrakcie-29.jpg",      1100, None, 0.5, 78),

    # ── runda poprawek 29.09.2026 (WhatsApp od klienta przez Adama) ────────────────
    #    „A w zakładce realizacje można już pododawać zdjęcia wcześniej, które Sandro
    #    wysłał. Przesyłam jeszcze parę zdjęć w żywszych kolorach". Z paczki 14.09 („Sandro")
    #    dochodzą kadry, które wtedy pominęliśmy (trawertyn w trakcie, belki z jodełką - B1,
    #    wanna = żywsza wersja z 29.09); z 29.09 - nowe.
    #    ⛔ `poddasze-belka-swiatlo-27` NIE wchodzi: bramka (dHash 0/64) i oko potwierdzają,
    #       że to TO SAMO ujęcie co `poddasze-belka-swiatlo-05` - wisi już 2× (otwarcie
    #       „Co robimy" i kafel na głównej). Trzecie miejsce = ten sam kadr trzy razy.
    #    `z-lazienka-07/08` i `z-pokoj-01` wyżej mają już źródła z 29.09 (żywsze / 2048 px).
    ("z-hol-03.jpg",          "hol-lamele-ciemne-45.jpg",            1100, None, 0.5, 78),
    ("z-lazienka-09.jpg",     "lazienka-czarna-wanna-zywsza-42.jpg", 1100, None, 0.5, 78),
    ("z-lazienka-10.jpg",     "lazienka-czarna-dluga-43.jpg",        1100, None, 0.5, 78),
    ("z-wtrakcie-04.jpg",     "okna-montaz-cegla-46.jpg",            1100, None, 0.5, 78),
    ("z-wtrakcie-05.jpg",     "poddasze-belki-wtrakcie-47.jpg",      1100, None, 0.5, 78),
    ("z-wtrakcie-06.jpg",     "lazienka-trawertyn-wtrakcie-31.jpg",  1100, None, 0.5, 78),


    # ── druga para „przed i po" na głównej: wnętrze. ⛔ NIE idzie w suwak przenikający
    #    jak rozbudowa - zdjęcia robione z innego miejsca i innej ogniskowej (korelacja
    #    krawędzi 0,17), więc przy przenikaniu okno balkonowe przeskakiwałoby w bok.
    #    Stoją obok siebie, każde ze swoją etykietą. Źródło ma 900 px, więc bez @2x:
    #    kafel stoi na ~570 px, czyli gęstość i tak wychodzi powyżej 1,5.

    # ── przed i po: OBA kadry prosto z oryginalu, bez prostowania ────────────────
    # 🔴 K. 14.09.2026: "teraz jest za bardzo przesuniete w lewo przez co ucina lewa
    #    krawedz, nie mozesz po prostu wstawic tam oryginalnego zdjecia albo nie
    #    przerabiac az tak formatu?". Zdjecie "po" bylo prostowane homografia, zeby
    #    nakladalo sie na "przed" co do piksela - to bylo potrzebne WYLACZNIE pod suwak
    #    z przesuwana linia i pod przenikanie. Klocek przelacza dzis cale kadry strzalka,
    #    wiec prostowanie tylko zabieralo krawedzie i wyginalo sciane. Wylecialo.
    # ⛔ Wraca suwak z linia -> wraca homografia (kod w historii gita, commit 033e481).
    #
    # Proporcja PARA (1500/1322 = 1,135) jest kompromisem miedzy czterema kadrami i JEDNA
    # rzecza, ktorej nie wolno zostawic: znakiem wodnym klienta wgranym w zdjecie.
    #   · "przed": logo w PRAWYM DOLNYM rogu od y=1120 (oryginal 1254 px) -> kadr z GORY,
    #   · "po":    logo w PRAWYM GORNYM rogu do y=117                     -> kadr z DOLU,
    #   · oba kadry wnetrza maja u zrodla ~1,125, wiec tu prawie nic nie odpada.
    # ⛔ Zmieniasz proporcje w dol (kadr wyzszy) -> znak wodny wraca do kadru. Zmierz od nowa.
    ("przed.jpg",    "PRZED-rozbudowa.jpg", 1500, PARA, 0.0, 82),
    ("przed@2x.jpg", "PRZED-rozbudowa.jpg", 2400, PARA, 0.0, 76),
    ("po.jpg",       "PO-rozbudowa.jpg",    1500, PARA, 1.0, 82),
    ("po@2x.jpg",    "PO-rozbudowa.jpg",    2400, PARA, 1.0, 76),

    ("przedpo-pokoj-przed.jpg",    "pokoj-przed-36.jpg",         1300, PARA, 0.45, 82),
    ("przedpo-pokoj-przed@2x.jpg", "pokoj-przed-36.jpg",         1800, PARA, 0.45, 78),
    ("przedpo-pokoj-po.jpg",       "pokoj-po-35.jpg",            1300, PARA, 0.45, 82),
    ("przedpo-pokoj-po@2x.jpg",    "pokoj-po-35.jpg",            1800, PARA, 0.45, 78),

    ("z-elewacja-01.jpg",     "elewacja-po-taras-04.jpg",        1200, None, 0.5, 72),
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
    warianty_pasow()
    logo()
    if co != "zdjecia":
        filmy()
