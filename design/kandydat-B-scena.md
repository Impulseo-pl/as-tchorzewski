# Kandydat B — „Scena"

**Fundament:** [Apple Premium Cinematic](https://designmd.app/library/apple-premium-cinematic) · biblioteka `DESIGN.md`
**Makieta:** `kierunki/kierunek-B-scena.html`
**Dla kogo gra:** ktoś, kto ma pieniądze na porządne wykończenie i porównuje wykonawców „na oko".
Ciemna strona z jednym zdjęciem na ekranie mówi „to jest droższa firma" zanim padnie jedno słowo.

## Dlaczego ten fundament dla TEJ firmy

Filozofia szablonu: **„let the product float in void" — pustka jest sceną dla przedmiotu,
każda sekcja pokazuje jedną rzecz naraz.**

Dwa powody, dla których to pasuje akurat tutaj — oba techniczne, nie gustowne:

1. ⭐ **Nowe logo klienta jest białe i żyje na czerni.** Wyciągnęliśmy je z ich banera: cienka kreska,
   biały monogram + pomarańczowa esica, wordmark rozstrzelony wersalikami na tle `#0F0F12`.
   To jest gotowy język wizualny — ten szablon go po prostu kontynuuje, zamiast z nim walczyć.
   W kierunkach A i C ten znak trzeba przemalowywać.
2. ⭐ **Wszystkie jego dobre zdjęcia są PIONOWE.** Nie mamy ani jednego ładnego kadru poziomego
   w wysokiej rozdzielczości. Ciemna scena pozwala postawić zdjęcie pionowe **bez kadrowania**,
   jako obiekt na tle — zamiast rozciągać je na szeroki pas i ucinać połowę.

## Tokeny oryginału

| co | wartość |
|---|---|
| kolory | `#000000` czerń · `#f5f5f7` jasny · `#1d1d1f` prawie czarny · `#0071e3` akcent · `#2997ff` link na ciemnym · `rgba(0,0,0,.8)` nawigacja |
| typografia | SF Pro Display/Text, Helvetica Neue (zapas), JetBrains Mono (kod) · Hero `clamp(2.5rem,5vw,4rem)` · nagłówki `line-height 1.07`, `letter-spacing −.28px` · tekst 16px/1.6, max 72ch |
| siatka | CSS Grid, max 1280px · hero split · sekcje naprzemiennie czerń ↔ jasny · zero trzech równych kolumn |
| odstępy | jednostka 8px · rytm sekcji `clamp(4rem,8vw,8rem)` |
| zaokrąglenia | CTA `980px` (pigułka) · karty 8px |
| cienie | `0 2px 8px rgba(0,0,0,.08)`, nic cięższego |
| ruch | sprężyna: sztywność 120, tłumienie 20 · wejście fade + translateY 16px→0 przez 540 ms, kaskada 120 ms · hover scale(1.03) |
| nawigacja | tło `rgba(0,0,0,.8)` + `backdrop-filter: saturate(180%) blur(20px)` |

## Do's oryginału

sekcje naprzemiennie ciemna/jasna · nawigacja półprzezroczysta z rozmyciem · **jeden akcent** ·
CTA w kształcie pigułki · przedmiot jako bohater na jednolitym tle · kinowa pustka między sekcjami

## Don'ts oryginału

zero emoji · **zero gradientów dekoracyjnych — płaski kolor** · cienie nie cięższe niż `0 2px 8px` ·
**zero czystej bieli `#FFFFFF` jako tła** · nasycenie max 80% · zero trzech równych kolumn ·
zero `h-screen` · zero klisz AI · zero lorem ipsum

## ⚠️ Odstępstwa — co odrzucamy i dlaczego

1. **🔴 Krój SF Pro — ODRZUCONY.** SF Pro to font systemowy Apple, licencyjnie nie do webu i nie
   dla nas. Zamiast tego **Jost** (nagłówki, waga 300) — szeroki, geometryczny grotesk, który
   powtarza rysunek wordmarku z logo klienta — plus **Inter** na tekst. Polskie znaki: pełne.
2. **🔴 Niebieski `#0071e3` — ODRZUCONY.** Jeden akcent, zgoda, ale ma być **jego**: `#C85C13`,
   pomarańcz odczytany z pikseli jego logo. Niebieski Apple na stronie firmy budowlanej
   z pomarańczowym znakiem byłby po prostu cudzy.
3. **🔴 Czysta czerń `#000000` — ODRZUCONA** na rzecz `#0F0F12`. To dokładnie kolor tła jego banera
   (zmierzony), a przy okazji inne pliki tej samej biblioteki czystą czerń odradzają — oryginał
   sam sobie przeczy, bo w palecie ma `#000000`, a w „don'ts" zakaz czystej czerni w innych systemach.
4. **🔴 `border-radius: 9999px` na KARTACH — ODRZUCONE.** To śmieć w pliku źródłowym (karty
   z zaokrągleniem 9999px zamieniają się w pigułki). Pigułka zostaje wyłącznie na przyciskach CTA;
   karty i zdjęcia mają 8px.
5. **Radialna poświata pod hero** — szablon zakazuje gradientów dekoracyjnych. Zostawiamy jedną,
   bardzo słabą (10% krycia, pomarańcz), bo płaska czerń przy zdjęciach z budowy robi się martwa.
   ⚠️ To świadome złamanie zasady, nie przeoczenie — do skasowania, jeśli K. uzna, że widać.
6. **„Przedmiot na jednolitym tle"** czytamy jako **realizacja na jednolitym tle**. Sekcja „przed
   i po" gra tu rolę, którą u Apple gra produkt.

## Ryzyko

⚠️ Ciemna strona **wybacza mniej przy słabych zdjęciach** — szumy i przepalenia widać od razu.
Zdjęcia łazienki i poddasza mamy dziś tylko w wersji ~1200 px z Instagrama. Jeśli klient nie przyśle
oryginałów z telefonu (pytanie 3), ten kierunek trzeba zbudować na mniejszych kadrach albo odpuścić.
