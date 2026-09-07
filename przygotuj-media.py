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

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
ZR = os.path.join(ROOT, "materialy", "realizacje")
WID = os.path.join(ROOT, "materialy", "wideo")
IMG = os.path.join(ROOT, "img")
VIDEO = os.path.join(ROOT, "video")

# slot                     źródło                              szer.  proporcja  pion  jakość
PLAN = [
    # ── hero: jedyny duży kadr na scenie. Wnętrze SKOŃCZONE (DESIGN.md) ──────────
    ("hero.jpg",              "poddasze-belki-01.jpg",           1200, None, 0.5, 80),

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

    # ── pas 21:9: jedyny poziomy materiał w komplecie. Kadr bierze GÓRNĄ część,
    #    bo u dołu stoją wiadra i pace (bałagan budowlany) ────────────────────────
    ("pas-beton.jpg",         "beton-arch-ciemny-01.jpg",        1440, 21/9, 0.30, 78),

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
    ("z-schody-02.jpg",       "schody-beton-11.jpg",             1100, None, 0.5, 78),
    ("z-beton-01.jpg",        "beton-arch-ciemny-01.jpg",        1100, None, 0.5, 78),
    ("z-beton-02.jpg",        "beton-arch-jasny-02.jpg",         1200, None, 0.5, 78),
    ("z-beton-03.jpg",        "beton-arch-jasny-04.jpg",         1200, None, 0.5, 78),
    # elewacja: jedyne pełne oryginały z telefonu (3072×4096) — stąd większa szerokość
    ("z-elewacja-01.jpg",     "elewacja-po-taras-04.jpg",        1200, None, 0.5, 72),
    ("z-elewacja-02.jpg",     "elewacja-po-01.jpg",              1200, None, 0.5, 72),
    ("z-elewacja-03.jpg",     "elewacja-po-03.jpg",              1200, None, 0.5, 72),
    ("z-elewacja-04.jpg",     "elewacja-wtrakcie-06.jpg",        1200, None, 0.5, 72),
    ("z-elewacja-05.jpg",     "elewacja-rusztowanie-09.jpg",     1200, None, 0.5, 72),
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
    for slot, src, szer, prop, pion, jakosc in PLAN:
        im = ImageOps.exif_transpose(Image.open(os.path.join(ZR, src))).convert("RGB")
        if prop:
            wys = int(round(szer / prop))
            out = ImageOps.fit(im, (szer, wys), method=Image.LANCZOS, centering=(0.5, pion))
        else:                                   # bez kadrowania — samo przeskalowanie
            szer = min(szer, im.width)
            out = im.resize((szer, int(round(szer * im.height / im.width))), Image.LANCZOS)
        p = os.path.join(IMG, slot)
        out.save(p, "JPEG", quality=jakosc, optimize=True, progressive=True)
        print(f"  ✓ img/{slot:24s} {out.width}×{out.height}  "
              f"{os.path.getsize(p)//1024} KB  ← {src}")


def logo():
    """Logo do `img/`: plik odzyskany z banera (704×154, biały znak na przezroczystym).
    ⚠️ Podmienić na oryginał od grafika, gdy przyjdzie (pytanie 2)."""
    src = os.path.join(ROOT, "materialy", "logo", "logo-nowe-przezroczyste.png")
    cel = os.path.join(IMG, "logo.png")
    Image.open(src).save(cel, "PNG", optimize=True)
    print(f"  ✓ img/logo.png             ← materialy/logo/logo-nowe-przezroczyste.png")


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
