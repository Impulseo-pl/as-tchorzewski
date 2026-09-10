---
name: "A.S TCHÓRZEWSKI"
opis: "Wykończenia wnętrz — Błońsko k. Rakoniewic, wielkopolskie i lubuskie"
fundament: "Apple Premium Cinematic (designmd.app) — kierunek B „Scena”, ODWRÓCONY NA JASNY"
wybrany: "2026-09-07 przez Krzysztofa, z dwoma poleceniami: BEZ ZAOKRĄGLONYCH RAMEK
  oraz (21:15) STRONA NA JASNĄ — droga A z sekcji o logo"
kolory:
  tlo: "#F3F1ED"
  tlo_ciemne: "#0F0F12"
  tekst: "#1B1B1E"
  akcent: "#C85C13"
typografia:
  naglowki: "Jost 300"
  tekst: "Inter 400"
  etykiety: "Inter 500, letter-spacing .2em"
zaokraglenia: "0 — wszędzie, bez wyjątku"
---

# DESIGN.md — A.S TCHÓRZEWSKI

> 🔒 **To jest jedyne źródło prawdy o wyglądzie tej strony.** Zmiana wyglądu = zmiana w TYM pliku,
> nie kolejny pomysł w trakcie budowy. Każda sekcja strony ma być z nim zgodna.
>
> **Fundament:** [Apple Premium Cinematic](https://designmd.app/library/apple-premium-cinematic)
> — gotowy szablon z biblioteki `DESIGN.md`.
> **Dlaczego ten:** filozofia *„let the product float in void" — pustka jest sceną, każda sekcja
> pokazuje jedną rzecz naraz.* Wybrane z dwóch powodów; ⚠️ **07.09.2026 pierwszy z nich upadł:**
> ~~(1) nowe logo klienta jest białe i żyje na czerni~~ — klient potwierdził, że aktualne jest
> **STARE** logo, z czarnym napisem (patrz sekcja „LOGO"). Powód (2) stoi dalej i to on utrzymał
> ten kierunek przy życiu: **wszystkie jego dobre zdjęcia są pionowe**, a scena pozwala postawić
> kadr pionowy bez kadrowania.
> 🔴 **Dlatego od 07.09.2026 pustka jest z PAPIERU, nie z czerni.** Filozofia nietknięta —
> jedna rzecz na ekran, kadr jako przedmiot na scenie — zmienił się kolor sceny.
> Czerń została akcentem: nagłówek strony głównej, otwarcia podstron, ramka wezwania,
> podpisy na pasach zdjęć i zasłona przy powiększeniu zdjęcia.
> **Makieta źródłowa:** `design/_kierunki/kierunek-B-scena.html` · uzasadnienie: `design/kandydat-B-scena.md`

---

## 🔴 Polecenie Krzysztofa, które nadpisuje szablon

> **„Możemy zrobić B, ale bez zaokrąglonych ramek?"** (07.09.2026)

**`border-radius: 0` na WSZYSTKIM.** Przyciski, karty, zdjęcia, etykiety, pola formularza, ramki
sekcji — zero zaokrągleń, bez wyjątków. To unieważnia najbardziej charakterystyczny element
oryginału (pigułki `980px`) i jest świadome: ostra krawędź pasuje do cienkiej, prostej kreski
w jego logo i do branży budowlanej lepiej niż zaokrąglenia Apple'a.

⛔ Jeżeli w trakcie budowy pojawi się gdziekolwiek `border-radius` inny niż `0` — to jest błąd,
nie decyzja. Kontrola: `grep -n "border-radius" assets/app.css | grep -v ":0"` musi zwrócić pustkę.
(Arkusz strony leży w `assets/`, nie w korzeniu — `*.css` w korzeniu nie sprawdza niczego.)

---

## Kolory

| Nazwa | Wartość | Zastosowanie |
|---|---|---|
| **papier** | `#F3F1ED` | **tło główne całej strony** (od 07.09.2026, droga A) |
| papier 2 | `#FFFFFF` | karty i pola na papierze |
| papier 3 | `#E9E5DE` | stopka — ton głębszy od papieru, oddziela ją bez rysowania kreski |
| noc | `#0F0F12` | **akcent**: scena, otwarcia podstron, ramka wezwania, zasłona zdjęcia · **zmierzone z jego banera**, nie wymyślone |
| noc jaśniejsza | `#18161A` | karty i pola wewnątrz bloku ciemnego |
| atrament | `#1B1B1E` | **tekst podstawowy** (na papierze) |
| przygaszony jasny | `#6B6259` | tekst drugiego planu na papierze · kontrast 5,29 |
| biel | `#F5F5F7` | tekst wewnątrz bloku ciemnego |
| przygaszony | `#A39A93` | tekst drugiego planu na ciemnym · kontrast 6,93 |
| **akcent** | `#C85C13` | **jedyny kolor akcentu** — odczytany z pikseli jego logo. Kreski, obrysy, hover |
| akcent — przycisk | `#A34A0F` | tło przycisków (biel na `#C85C13` daje 4,20 — poniżej progu 4,5) |
| akcent — mały tekst na ciemnym | `#E2762A` | etykiety i „Zobacz →" na kaflu `#17171B` |
| akcent — mały tekst na jasnym | `#8F3F0A` | etykiety i numery na sekcji `#F3F1ED` |
| WhatsApp | `#25A63F` | wyłącznie tło przycisku WhatsApp (znaczeniowe, nie dekoracyjne) |
| linia | `rgba(27,27,30,.22)` | obrysy i ramki **na papierze** (domyślne) |
| linia słaba | `rgba(27,27,30,.12)` | podziały i cienkie kreski na papierze |
| linia na ciemnym | `rgba(255,255,255,.16)` | to samo, ale wewnątrz bloku `.ciemna` |

🔴 **Domyślna linia jest CIEMNA.** Białe warianty obsługują wyłącznie bloki `.ciemna`;
biała linia na papierze znika bez śladu i tak się właśnie gubi ramki po odwróceniu palety.

⛔ **Jeden akcent i nic więcej.** Zero drugiego koloru „dla ożywienia". Trzy warianty wyżej
to ten SAM pomarańcz przyciemniony albo rozjaśniony pod próg kontrastu 4,5 — zmierzone bramką
07.09.2026, nie dobrane na oko. Zero gradientów
dekoracyjnych poza jedną wskazaną niżej. Zero wielkich płaszczyzn pomarańczu — akcent to kreska,
przycisk, mała etykieta, **nigdy tło sekcji**.

## Typografia

| Rola | Krój | Ustawienia |
|---|---|---|
| nagłówki | **Jost 300** | `line-height:1.08`, `letter-spacing:-.015em` · szeroki geometryczny grotesk, powtarza rysunek wordmarku z logo |
| tekst | **Inter 400** | 17px/1.65, maksimum 72 znaki w wierszu |
| etykiety nad nagłówkiem | Inter 500 | 12px, `letter-spacing:.2em`, wersaliki, kolor akcentu |
| liczby w kolumnach | Inter + `font-variant-numeric: tabular-nums` | |

⛔ **Zero nagłówków wersalikami.** Wersaliki wolno wyłącznie na małych etykietach (12 px)
i w samym znaku graficznym logo — tam są częścią znaku.
Oba kroje mają pełne polskie znaki. 🔴 Ładowane **z naszego serwera** (`assets/fonty/*.woff2`,
latin + latin-ext, `font-display:swap`), nie z Google Fonts — dzięki temu strona nie łączy się
z obcym serwerem i nie potrzebuje banera cookies (reguła silnika stron docelowych).

## Układ

- Siatka CSS Grid, `max-width: 1240px`, padding boczny 32px (20px na telefonie).
- Rytm sekcji: `clamp(4rem, 8vw, 8rem)`.
- 🔴 **Sekcje są JASNE, czerń jest gościem** (od 07.09.2026). Ciemny blok dostają dokładnie
  cztery rzeczy: **nagłówek strony głównej** (`.scena`), **otwarcie każdej podstrony**
  (`.otwarcie.ciemna`), **ramka wezwania do kontaktu** (`.domkniecie`) i **zasłona przy
  powiększeniu zdjęcia** (`.lb`). Do tego pasy zdjęć na całą szerokość, które ciemne są
  z natury. ⛔ Nie dokładać piątego ciemnego bloku bez decyzji K. — dwa ciemne bloki obok
  siebie i papier przestaje być tłem, a zaczyna być przerwą.
- 🔒 **LOGO STOI WYŁĄCZNIE NA JASNYM** — górny pasek i stopka, nigdzie indziej. To nie jest
  preferencja, tylko powód, dla którego cała strona jest jasna: znak ma czarny napis
  i czarne wieżowce, na `#0F0F12` zostaje z niego biały dach i srebrna kielnia.
- Hero: tekst po lewej, **jeden kadr pionowy po prawej**, w cienkiej ramce odsuniętej o 26px.
- ⛔ **Zero trzech równych kolumn** (zakaz szablonu). Cztery kafle wolno, zygzak wolno.
- ⛔ Zero `h-screen` — `min-h:100dvh`.
- Telefon: **przycisk „Menu"**, nie pasek pozycji + **przyklejony na dole pasek**
  „Zadzwoń 667 434 222" / „WhatsApp".
- 🔴 **PIERWSZY EKRAN JEST ODCHUDZONY** (K. 08.09.2026: „nie powala, dużo tekstu").
  Zdjęte: podpis pod kadrem hero (8 słów — treść siedzi w `alt`), trzeci przycisk
  „Zobacz realizacje" (konkurował z telefonem o to samo kliknięcie; do realizacji prowadzi
  menu i zamknięcie strony), połowa leadu. Z ~54 słów zostało ~38, z trzech wezwań — jedno:
  **zadzwonić**. Zwolnione miejsce poszło na kadr: 624 → 708 px wysokości na laptopie.
  ⛔ Nie dokładać tu nic bez przeliczenia sumy w `.kadr-scena img`.
- 🔴 **Kadr hero MIEŚCI SIĘ W PIERWSZYM EKRANIE, zawsze i wszędzie** (reguła K. 07.09.2026).
  Na laptopie `max-height: calc(100dvh - 192px)`, na telefonie `44vh`. ⚠️ Limit szerokości
  `min(44vw,560px)` obowiązuje TYLKO na dużym ekranie - na telefonie musi być skasowany,
  bo 44 % z 390 px to 172 px. Bramka: `hero_poza_ekranem`.
- 🔴 **Znaczki social (FB, IG) w prawym dolnym rogu - tylko na dużym ekranie.** Na telefonie
  ikony idą do stopki; dolny róg należy do „Zadzwoń” i „WhatsApp”.
  🔴 **BEZ KAFELKA** (K. 08.09.2026): same znaki, okrągłe, w barwach marek, z poświatą
  i podniesieniem na najechanie. Okrągłość robi SAM ZNAK (Facebook jest kołem z natury,
  Instagram dostał koło w swoim gradiencie) — **nie `border-radius`**, więc zasada
  „zero zaokrągleń" zostaje nienaruszona. Poświata jest funkcją, nie ozdobą: znak bez tła
  przejeżdża i po papierze, i po ciemnej scenie, więc ma dwie słabe poświaty naraz.
- 🔴 **Kadr hero na telefonie ma limit wysokości: `max-height: 44vh`.** Bez niego zdjęcie
  1200×1600 zjadało 531 z 844 px pierwszego ekranu i spychało H1 pod przyklejony pasek -
  nagłówek był przecięty na 60 px (zmierzone 07.09.2026). Skalujemy CAŁE zdjęcie, **nie
  kadrujemy** - kadry pionowe bez kadrowania to sens tego kierunku. Ramka `::before` idzie
  za figurą dzięki `width: fit-content`. Bramka pilnuje tego testem `zaslona_fixed`.

## Ruch

- Wejście: fade + `translateY(16px → 0)`, 540 ms ease-out, kaskada 120 ms.
- Hover: `scale(1.03)` + delikatny cień, 200 ms.
- **Tylko `transform` i `opacity`.** Żadnych właściwości uruchamiających przeliczanie układu.
- `@media (prefers-reduced-motion: reduce)` wyłącza wszystko.
- ⛔ Zero animowanych liczników. Liczby stoją statycznie (REMPERFEKT ma na żywej stronie
  liczniki pokazujące „0 +" — to jest bramka, nie anegdota).

## Komponenty

- **Przycisk główny:** prostokąt, tło `#C85C13`, tekst biały, waga 500. Hover: tło ciemniej
  o 8% **+ ukośna smuga światła przelatująca przez przycisk w 0,75 s + uniesienie o 2 px
  i cień pod spodem**; `active` wraca na `translateY(0)`.
  🔴 10.09.2026, prośba K.: „hover ma wyglądać jak na demie, tam ładniej się podświetla".
  Sama zmiana tła czytała się jak przełącznik, nie jak reakcja. Efekt jest przeniesiony
  1:1 z silnika dem (`~/.claude/skills/strona-klienta/recipes/multipage/motion.css`).
  To dalej **zero poświat** — żadnej łuny dookoła krawędzi; smuga leci WEWNĄTRZ prostokąta,
  jest przezroczysta i nie rusza kontrastu napisu (5,89). Krawędź zostaje ostra.
- **Przycisk drugi („duch"):** obrys 1,5px, tło przezroczyste. Na papierze `rgba(27,27,30,.3)`,
  wewnątrz bloku ciemnego `rgba(255,255,255,.22)`. Hover: obrys pełny + delikatne wypełnienie
  (4,5% czerni na papierze / 9% bieli na ciemnym) + ta sama smuga i uniesienie co wyżej.
  ⚠️ Smuga bierze kolor z `currentColor` — na papierze jest ciemna, w bloku ciemnym jasna.
  Biała smuga na przezroczystym przycisku na papierze byłaby niewidoczna.
- **Kafel/karta:** obrys 1px, tło `#FFFFFF` na papierze (`#18161A` w bloku ciemnym),
  **krawędź ostra**, cień nie cięższy niż `0 2px 8px rgba(0,0,0,.08)`.
- **Pole formularza:** etykieta NAD polem, obrys 1px, focus ring 2px w kolorze akcentu z offsetem 2px,
  błąd pod polem. Zero floating labels.
- **Nawigacja:** tło `rgba(243,241,237,.86)` + `backdrop-filter: saturate(180%) blur(20px)`.
  🔴 **Jasna, bo stoi w niej logo.** Wysokość **96 px** (70 → 76 px na telefonie), bo znak
  urósł z 34 na **60 px** (46 px na telefonie): stare logo jest rysunkiem w proporcji 4:3,
  nie poziomym wordmarkiem, i przy 34 px napis „TCHÓRZEWSKI" robił się nieczytelną kreską.
  ⚠️ Zmieniasz wysokość paska → popraw też odjęcie w `.kadr-scena img`
  (`calc(100dvh - 276px)`), inaczej hero wyjdzie poza pierwszy ekran.

---

## ⚠️ Odstępstwa od oryginału — co odrzucamy i dlaczego

1. **🔴 Wszystkie zaokrąglenia (`980px` na CTA, `8px` na kartach) → `0`.** Polecenie K. z 07.09.
   To najgłębsze odstępstwo od tego szablonu; opis wyżej.
2. **🔴 Krój SF Pro — ODRZUCONY.** Font systemowy Apple, licencyjnie nie do webu.
   Zamiast: **Jost** + **Inter**.
   ⛔ I nigdy „System UI stack" — to jest dokładnie błąd, za który dostaliśmy zwrot.
3. **🔴 Niebieski `#0071e3` — ODRZUCONY** na rzecz `#C85C13` z jego logo. Jeden akcent, zgoda,
   ale ma być JEGO.
4. **🔴 Czysta czerń `#000000` — ODRZUCONA** na rzecz `#0F0F12`, zmierzonego z tła jego banera.
5. **🔴 `border-radius: 9999px` na KARTACH — ODRZUCONE jako śmieć w pliku źródłowym**
   (karty zamieniłyby się w pigułki). I tak bezprzedmiotowe, bo wszędzie mamy `0`.
6. **Radialna poświata pod hero (10% krycia, pomarańcz)** — szablon zakazuje gradientów
   dekoracyjnych. Zostawiamy jedną, bardzo słabą, bo płaska czerń przy zdjęciach z budowy robi się
   martwa. ⚠️ Świadome złamanie zasady, nie przeoczenie — do skasowania, jeśli będzie widać.
7. **„Przedmiot na jednolitym tle"** czytamy jako **realizacja na jednolitym tle**. Sekcja
   „przed i po" gra tu rolę, którą u Apple gra produkt.

---

## ✅ LOGO — ROZSTRZYGNIĘTE 07.09.2026 21:15: IDZIEMY DROGĄ A

**Klient potwierdził Adamowi, że aktualne jest STARE logo** (domki, młotek, klucz, pędzel,
kielnia, czarny napis „TCHÓRZEWSKI"), a nie monogram A+S z banera na Facebooku.

⚠️ **To nie jest podmiana pliku.** Ten kierunek („Scena", ciemny) został wybrany **dlatego**,
że nowe logo jest białe i żyje na czerni — to jest dosłownie zapisane wyżej w tym pliku jako
powód nr 1. Stare logo ma czarny napis i czarne wieżowce: **na tle `#0F0F12` znika.**

### ✅ Decyzja K. (07.09.2026 21:15): **droga A — strona przechodzi na jasną.**

Wykonane w tej samej pracy: paleta odwrócona (`assets/app.css`), pasek i stopka jasne,
znak podmieniony na stary (`img/logo.png`, 240×177, 14 kB — przycięty z przezroczystego
oryginału i skwantowany do 128 kolorów, bo pełny plik ważył 558 kB na każdej podstronie).
Czerń została **akcentem**, nie zniknęła: scena, otwarcia podstron, ramka wezwania, zasłona
przy powiększeniu zdjęcia, pasy zdjęć.

⚠️ **Co za to zapłaciliśmy** — dla uczciwości zapisu: „drogi" nastrój, dla którego kierunek B
wygrał, jest teraz słabszy niż w makiecie. Nie zniknął (kadry pionowe nadal stoją na czerni
w scenie i w otwarciach podstron), ale strona czyta się jaśniej i lżej niż `kierunek-B-scena.html`.
To był świadomy koszt drogi A, nie wpadka.

🔵 Droga **C** (poprosić klienta o wersję znaku na ciemne tło) **jest nadal warta pytania** —
jeśli kiedyś przyśle wektor (pytanie 2), można rozważyć powrót ciemnej stopki. ⛔ Ale nie
odwracamy dla tego całej strony drugi raz.

**Tabela, z której wybieraliśmy** (zostaje jako zapis, dlaczego nie poszliśmy B ani D):

| | droga | co kosztuje | ryzyko |
|---|---|---|---|
| **A** | **Strona przechodzi na JASNĄ** (`#F3F1ED` jako tło główne, ciemne jako akcent sekcji) | przepisanie palety i kontrastów, ~pół dnia; teksty i zdjęcia zostają | traci się „drogi" nastrój, dla którego kierunek B wygrał; ciemne zdjęcia z budowy wyglądają na jasnym inaczej |
| **B** | Zostaje ciemna, logo dostaje **jasną płytkę** w nagłówku | godzina | prawie zawsze wygląda jak naklejka; to jest ten wygląd, którego unikamy |
| **C** | Prosimy klienta o **wersję na ciemne tło** (biały napis) | jeden telefon + czekanie | najlepszy efekt, ale znów stoimy na kliencie |
| **D** | **Przemalowujemy** czarne elementy na białe u siebie | godzina | ⛔ wymaga jego wyraźnej zgody — to ingerencja w znak |

Rekomendacja brzmiała „C, a jeśli nie chce czekać — A". K. wybrał **A** — i była to trafna
poprawka: klient dosłał logo JPG-iem przez WhatsAppa i nie odpowiedział na 15 pytań obiecanych
na 07.09, więc C oznaczałoby czekanie na coś, czego najpewniej nie ma.
Płytka (B) psuje to, za co zapłacił; przemalowanie (D) bez jego zgody jest poza naszą rolą.

**Plik jest u nas i nie trzeba nic dosyłać:** `materialy/logo/logo-stare-przezroczyste.png`
(1018×753, przezroczyste tło) — lepszy niż kopia, która przyszła WhatsAppem.

---

## Logo klienta — STARE, potwierdzone przez klienta 07.09.2026

**Idzie STARE logo:** rysunek z wieżowcami, trzema domkami, młotkiem, kluczem, pędzlem
i kielnią, pomarańczowe „A.S" i **czarny napis „TCHÓRZEWSKI"** pod spodem. Klient potwierdził
to Adamowi. ⛔ NIE monogram A+S z banera na Facebooku — mimo że to nim firma znakuje zdjęcia.

**Plik:** `img/logo.png` (240×177, 14 kB), źródło `materialy/logo/logo-stare-przezroczyste.png`
(1018×753, przezroczyste). Poprzedni znak leży w `materialy/logo/logo-nowe-*` — nie kasować,
gdyby klient jeszcze raz zmienił zdanie.

**Czego wolno:** stawiać na jasnym tle w oryginalnych kolorach; skalować proporcjonalnie.
**Czego NIE wolno:**
- 🔒 **stawiać na ciemnym tle** — 59 % widocznych pikseli znaku jest ciemnych; na `#0F0F12`
  zostaje z niego biały dach i srebrna kielnia. To jest powód, dla którego cała strona jest jasna.
- przemalowywać (droga D — wymagałaby wyraźnej zgody klienta, której nie mamy),
- podkładać jasnej płytki pod znak na ciemnym (droga B — czyta się jak naklejka),
- dodawać poświat i cieni, rozciągać,
- schodzić w pasku poniżej **60 px wysokości** (46 px na telefonie): przy 34 px napis
  „TCHÓRZEWSKI" robi się nieczytelną kreską.

⚠️ **Nadal nie mamy wektora.** Znak jest rastrem odzyskanym z pliku od klienta; przy 60 px
w pasku to bez znaczenia, ale do druku i do dużych formatów będzie potrzebny oryginał —
pytanie 2 w `PYTANIA-DO-KLIENTA.md`. Po otrzymaniu **podmienić i skasować raster**.

**Przepis do odtworzenia** `img/logo.png` (gdyby plik zginął):
```
źródło: materialy/logo/logo-stare-przezroczyste.png     (1018×753, przezroczyste)
1. przytnij do zawartości po kanale alfa (próg 8)       → 1006×742
2. przeskaluj LANCZOS do szerokości 240 px              → 240×177
3. skwantuj do 128 kolorów (FASTOCTREE) + optimize      → 14 kB
```
🔴 Krok 3 nie jest kosmetyką: bez niego plik waży **558 kB i leci na KAŻDEJ podstronie**
(bramka „pliki wielokrotnie cięższe niż miejsce, w którym stoją", 07.09.2026).
240 px to 2,7× miejsca, w którym znak stoi — z zapasem na ekran Retina.

---

## ✅ „O NAS" NA TELEFONIE — ROZSTRZYGNIĘTE 07.09.2026 21:15

**Problem:** podstrona `o-nas` ma układ LIST — dwie kolumny `oś lat | narracja`. Na telefonie
zwijają się w jedną i człowiek dostaje **104 słowa bez ani jednego obrazu** pod nagłówkiem.
Bramka zgłaszała to jako `sciana_tekstu`.

**Decyzja K.: wpuszczamy kadr** (a nie: uznajemy za świadome odstępstwo).

Kadr `z-schody-01.jpg` („Schody po wykończeniu") wchodzi **między oś lat a narrację**,
wewnątrz LEWEJ kolumny. Dwa zyski naraz:
- na telefonie przerywa ścianę tekstu **w połowie**, nie na końcu,
- na laptopie wypełnia pustkę pod krótką osią — trzy pozycje kontra pięć akapitów obok
  zostawiały pół kolumny pustego papieru.

⛔ **Nie przenosić kadru do prawej kolumny ani na koniec sekcji.** Na telefonie wyląduje wtedy
POD całym tekstem i nie przerwie niczego — kolejność w HTML jest tu treścią, nie układem.
⛔ **Bez `loading="lazy"`** — kadr stoi 1023 px od góry, czyli tuż nad drugim ekranem,
i z leniwym ładowaniem zostawiał przy przewijaniu pustą dziurę (bramka, 07.09.2026).

Kod: `pages.py`, funkcja `kadr_o_nas()`. Wygląd: `.kadr-o-nas` w `assets/app.css`.

---

## 🎬 WEJŚCIE NA STRONĘ — kurtyna z logo (08.09.2026, polecenie K.)

**Tylko strona główna.** Kod: `build.py` (`WEJSCIE_ZAPALARKA` / `WEJSCIE_HTML` / `WEJSCIE_JS`),
wygląd: `assets/app.css`, sekcja „WEJŚCIE NA STRONĘ". Procedura: skill `wejscie-na-strone`.

**Co opowiada:** ekran jest świeżo wykończoną ŚCIANĄ w kolorze papieru. Spod pociągnięcia
wychodzi znak firmy (maska w prawo + z rozmycia do ostrości), pod nim zostaje ślad w kolorze
akcentu, znak odlatuje na swoje miejsce w pasku, a dopiero potem ściana schodzi i odsłania
gotowe wnętrze. To jest dosłownie to, co ta firma robi — a nie „fade z logo", który umie
zrobić każdy szablon.

**Takty:** znak 0,52 s → ślad 0,46 s (opóźnienie 0,14 s) → przelot znaku 0,72 s →
ściana 0,62 s **z opóźnieniem 0,42 s**. Zasłona rusza najwcześniej w 560 ms, najpóźniej
w 900 ms; twardy bezpiecznik zdejmuje wszystko po 3 s.

### 🔴 Dwie rzeczy, których nie wolno tu ruszyć
1. **NAJPIERW LECI ZNAK, DOPIERO POTEM SCHODZI ŚCIANA** (`transition-delay: .42s` na
   `.wejscie-plyta`). Zmierzone na stopklatce: przy jednoczesnym starcie ściana wygrywa
   wyścig (0,62 s kontra 0,72 s znaku), odsłania ciemną scenę pod lecącym znakiem
   i **czarny napis „TCHÓRZEWSKI" znika w czerni jak naklejka**. Sama krzywa z wolnym
   startem tego nie ratowała. ⛔ Nie skracać poniżej ~0,4 s bez ponownego sprawdzenia.
2. **Znak dostaje na kurtynie swój rozmiar naprawdę** (`width`/`height` z pomiaru),
   a do paska wraca `scale()` **mniejszym od 1**. Powiększanie `transform`em rasteryzuje
   warstwę w rozmiarze bazowym i na telefonie (DPR 3) daje rozmyty znak — zrzut na Macu
   tego nie pokaże. Sufit = 640 px pliku ÷ gęstość ekranu.

**Plik:** `img/logo-duze.png` (640×472, 58 kB) — osobny od `img/logo.png`, bo znak w pasku
ma 240 px i na kurtynie byłby miękki. Ładuje się TYLKO na stronie głównej.

**Jak to obejrzeć:** zwykły zrzut pokazuje już gotową stronę — animacja jest szybsza niż
zrzut. Zrób stopklatkę: kopia `index.html` w `_makiety/wejscie/` (katalogi `_*` bramki
pomijają) z `MIN`/`SUFIT` ustawionymi na `999000`, wyciętymi twardymi timerami i pustą listą
zdarzeń przerywających, plus dowiązania do `assets/`, `img/`, `video/`. Do adresu dopisz
`?intro`, żeby zagrać ponownie. ⛔ Po obejrzeniu skasuj `_makiety` — to kopia, która rdzewieje.

**Bezpieczniki (wszystkie obowiązkowe):** zasłona jest `display:none`, dopóki nie włączy jej
skrypt · twardy limit 3 s zdejmuje ją niezależnie od wszystkiego · klik/scroll/dotyk/klawisz
przerywa natychmiast · `prefers-reduced-motion` pomija całość · gra RAZ NA WIZYTĘ
(`sessionStorage`), powrót z podstrony jej nie odtwarza.

---

## Zdjęcia

- **Wyłącznie z `materialy/realizacje/`** (38 kadrów z ich IG i FB). ⛔ Zero stocku.
  16 plików `img/` z dema (hero, about, g1–g14) to Pexels — na tej stronie nie ma dla nich miejsca.
- 🔴 **Kadr w hero musi pokazywać wnętrze SKOŃCZONE.** Nagłówek mówi „zostawiamy wnętrze gotowe
  do wprowadzenia" — kadr z odkrytymi puszkami elektrycznymi zaprzecza mu w tej samej sekundzie.
  (Pierwsza wersja makiety miała ten błąd; poprawione na `poddasze-belki`.)
- Kadry pionowe stawiamy **bez kadrowania**, jako obiekt na scenie. To jest sens tego kierunku.
- ⚠️ Elewacja jest w pełnych 3072×4096; łazienka, poddasze i schody tylko w ~1200 px — te ostatnie
  **nie nadają się na duży kadr**, dopóki klient nie przyśle oryginałów (pytanie 3).
- 🔴 **Pas przez całą szerokość okna chce ~2400 px pliku.** Żadne zdjęcie wnętrza od klienta
  tyle nie ma, a Google Flow oddaje ok. 1584 px — więc taki pas budujemy z **faktury, nie
  z pomieszczenia**: powiększenie widać na prostych liniach (skos sufitu, framuga), na cętkowanym
  betonie nie ma go gdzie zobaczyć. Wyjątek: elewacja, która ma pełne oryginały.
  ⛔ Do pasa nie wchodzą narożniki ścian — na krawędzi ekranu robią pionowy ciemny pasek.
- ⛔ Do czasu pisemnej zgody klienta (pytanie 3) **żadne zdjęcie nie idzie na produkcję**.
- Zdjęcia mają własny znak wodny klienta — zostaje, to jego znak.

---

## Czego NIE wolno napisać

**Ustalenia z klientem — twarde:**
- 🔴 **Wszystko w LICZBIE MNOGIEJ.** Firma mówi o sobie „my / robimy / polecamy / wyceniamy",
  na każdej podstronie. To łamie domyślną regułę silnika — tu wygrywa klient.
- ⛔ **Zero cen i widełek.** „W kwestii ceny trzeba się skontaktować".
- „**ponad** 20 lat" — nie zaokrąglać w górę, nie pisać „od 20 lat".
- Kolejność usług: szpachlowanie, malowanie, łazienki, sucha zabudowa NA GÓRZE;
  montaż drzwi i okien niżej.
- WhatsApp **882 832 244** z ikoną WA przy numerze. Telefon główny **667 434 222**. Godziny 8–20.

**Zdania z dema, których klient NIGDY nie powiedział — nie przenosić:**
- „Bezpłatna wycena", „za obejrzenie placu nie bierzemy pieniędzy" (5 wystąpień w demie),
- „Wolsztyn i okolice" + lista miast (zawęża lejek o całe lubuskie),
- „Bez podpisanej umowy nie ruszamy", „robota idzie etapami z odbiorami", „płacisz za to, co już stoi",
- „od 20 lat", „zaczynaliśmy od murarki".

**Frazesy zakazane** (żaden nie padł od klienta — w całej checkliście nie ma słów „najlepsi",
„profesjonalizm", „pasja", „jakość", „zadowolenie klienta"): kompleksowo · solidnie · terminowo ·
indywidualne podejście · pasja · profesjonalizm · najwyższa jakość · zadowolenie klienta ·
Elevate / Seamless / Unleash / Next-Gen.

**Bramki wyciągnięte z błędów konkurencji:**
- ⛔ **Zero tekstów zastępczych** (LUX-DOM ma na żywej stronie opinie „Jane Anderson" i „James Head"
  o firmie „Earthly Elegance").
- ⛔ **Zero pustych sekcji** (PK FLIZ ma sekcję „Opinie klientów napawają nas dumą!" bez ani
  jednej opinii). Albo mamy zgodę na przepisanie opinii, albo nie robimy sekcji.
- ⛔ **Zero sekcji „certyfikaty"** — klient nie ma żadnych papierów ani autoryzacji producenckich.
- ⛔ Zero ikony TikToka w stopce — konta nie ma.

**Miejsca, w których czeka liczba od klienta** (nie zaklejać ogólnikiem):
gwarancja (ile lat, na co) · czas reakcji na telefon · liczba osób w ekipie · pięć miast z zasięgu.

---

## HERO I OTWARCIA PODSTRON (K. + Marceli, 08.09.2026)

🔴 **Scena strony głównej jest PEŁNOEKRANOWA**: zdjęcie na całą szerokość, tekst na
przyciemnieniu. Poprzedni układ - pionowy kadr w odsuniętej ramce OBOK tekstu - został
odrzucony wprost („kompletnie mi się nie podoba"). ⛔ Nie wracać do `.kadr-scena`.

- Zdjęcie hero: **ściana z betonu architektonicznego**, jedyny kadr w portfolio, który
  niesie tekst na sobie. Plik jest WYSOKI (1440×1300), nie docięty do proporcji ekranu -
  wycinek dobiera `object-fit:cover`, więc ten sam plik działa na laptopie i na telefonie.
- **Każda podstrona ma własny kadr w otwarciu.** Bez zdjęcia podstrona zaczynała się
  płaskim czarnym paskiem. Strony prawne i 404 zostają bez zdjęcia.
- 🔴 **Przyciemnienie jest liczone, nie dobrane na oko.** Na 1440 px idzie ukośnie
  (ciemniej tam, gdzie stoi tekst), na telefonie pionowo. Zmieniasz zdjęcie w scenie albo
  w otwarciu → **przemierz bramką**: lead na jasnym niebie w oknach dachowych dał 4,20:1
  przy progu 4,5 i bramka to złapała.
- ⛔ Ten sam kadr nie może stać w dwóch miejscach naraz (hero + pas, otwarcie + galeria) -
  przy 39 zdjęciach powtórka od razu widać. Wchodzi na hero → wypada z galerii.

## FILMY Z BUDOWY (K. 08.09.2026)

Klient ma **dwa** filmy i tylko dwa: malowanie agregatem (37 s) i robota przy elewacji (39 s).
Oba są pionowe i oba realnie **nie mają ścieżki dźwiękowej**.

- 🔴 **Oba stoją na STRONIE GŁÓWNEJ**, obok siebie, w sekcji „Z budowy". To najlepsze, co
  klient ma z ruchu — nie chowamy tego na podstronie. Powtórka na `realizacje` zostaje.
- 🔴 **Kadr ożywa pod kursorem i pod przytrzymanym palcem** (rdzeń, blok 7), tak jak na stronach
  premium. Klik zostaje dla klawiatury i dla obejrzenia do końca; palec ma 120 ms zwłoki, żeby
  przewijanie strony nie budziło filmu przy każdym machnięciu.
- ⛔ **Nigdzie nie piszemy „film bez dźwięku"** — informowanie o braku brzmi jak tłumaczenie się
  z wady. Podpis mówi, co widać, nie czego nie słychać.
- 🔴 **Jeden kadr 4:5 dla wszystkich filmów** (`.reel-media{aspect-ratio:4/5}`, `object-fit:cover`).
  Filmy mają różne proporcje (9:16 i 3:4); puszczone „jak są" dawały dwa kafle różnej wysokości
  i pod niższym zostawała martwa dziura — dokładnie to, co K. wytknął w układzie `film-obok`.
- ⛔ Układ `.film-obok` (film z lewej, sam tekst z prawej) **skasowany**: przy krótkim tekście
  zostawiał pół ekranu pustki.

⚠️ **Rozszerzenie Claude-in-Chrome blokuje ładowanie wideo** — w karcie sterowanej przez
rozszerzenie film stoi na `readyState=0` i w sieci nie widać nawet zapytania o `.mp4`.
To NIE jest błąd strony. Sprawdzaj odtwarzanie w czystym Chromie (headless przez `cdp.mjs`).

## Kontrola przed każdym pokazaniem i każdym wypchnięciem

```bash
python3 ~/.claude/skills/bramki/sprawdz.py ~/Developer/impulseo-klienci/as-tchorzewski
grep -rn "border-radius" ~/Developer/impulseo-klienci/as-tchorzewski/*.css | grep -v ":0"   # musi być pusto
```
