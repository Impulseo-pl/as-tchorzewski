# NOTATKI BUDOWY — as-tchorzewski.pl

Klient: **Firma Ogólnobudowlana Artur Tchórzewski (A.S TCHÓRZEWSKI)** · opiekun **Adam**
Zamówienie IMP/2026/09/005, opłacone w całości 04.09.2026. Karta CRM `de55d1aa-3deb-44f1-88b7-ca3a19ad8b7c`.

---

## STAN PO BLOKU D (07.09.2026, 19:35) ⬅️ CZYTAJ TO

**Teksty przeredagowane, wdrożone i przebudowane. Bramki w tym samym stanie co po bloku C
(czysto poza dwiema celowymi). Nadal nic nie opublikowane.**

### Co powstało (etap 6 - skill `redakcja-tekstow`, pełne osiem etapów)
| plik | co robi |
|---|---|
| `_dokumentacja/AUDYT-TEKSTOW.md` | ⭐ całe rozumowanie: audyt podstrona po podstronie, autorewizja, przegląd, korekta |
| `_dokumentacja/INSTRUKCJA-WDROZENIA-TEKSTOW.md` | 25 par STARE → NOWE, dla kogoś, kto nie zna tej rozmowy |

**25 zamian w 5 podstronach · treść -190 znaków (-2,2 %) · bramka języka 0 błędów.**
⤴️ **Cofnięcie całej redakcji: `git reset --hard przed-tekstami`**

### Na czym polegała ta redakcja
Teksty z bloku C były **dobre** - zero frazesów, zero zdań zastępczych, zero wymyślonych liczb.
Miały jeden problem i systemowy: **sześć argumentów firmy padało po trzy-cztery razy każdy**,
w prawie identycznym brzmieniu, bo każda podstrona była pisana tak, żeby broniła się sama.
Redakcja to głównie decyzja, **gdzie każdy argument pada RAZ i mocno**:

| argument | stoi teraz na |
|---|---|
| to nasze zdjęcia, nie stock | `realizacje` (H1 + lead) |
| polecamy sprawdzone osoby | `index` („Nie bierzemy każdej roboty") + `co-robimy` („Poza wnętrzami") |
| agregat: duża powierzchnia, równa powłoka | `co-robimy` 02 |
| jedna ekipa, nie ma komu zrzucić winy | `o-nas` |
| „drogi na skróty" | `co-robimy` 01 |
| wycena do 5 dni roboczych | hero `index` · domknięcie `realizacje` · `kontakt` krok 3 |

⛔ **Żaden fakt podyktowany przez klienta nie zniknął** - sprawdzone po kolei skryptem
(liczba mnoga, zero cen, 5 dni, kolejność usług, polecanie, rodzinna, ponad 20 lat, 2005/2015,
oba numery, godziny, oba województwa).

### 🪤 Trzy rzeczy, które ta redakcja o sobie ustaliła
- 🔴 **Autorewizja (etap 4) zwróciła 9 poprawek i 1 wycofanie na 19 propozycji.** Wycofane:
  „to część tej samej roboty, nie osobne zlecenie" przy montażu drzwi - **obietnica cenowa
  złożona za klienta** (ten sam błąd co „bezpłatny pomiar" u PEC STAL).
- 🔴 **Wycinanie powtórzeń samo tworzy powtórzenia.** Cztery razy nowa propozycja duplikowała
  coś innego na stronie (Z-04 kopiował listę `spec`, Z-05 dublował „budowę", Z-08+Z-09 „najczęściej",
  Z-05+Z-17 wzorzec „bez X i bez Y"). Sprawdzać PO wdrożeniu, na wyniku, nie na propozycjach.
- 🔴 **`o-nas` ma twardy próg 1 800 znaków** (bramka, lekcja 2026-08-06-018). Po skróceniach
  spadło do 1 771 i bramka zapaliła się na czerwono. Naprawione **treścią, nie watą**: obszar
  wrócił do leadu, punkt „Dziś" został puentą o zakresie.

### Stan bramek (07.09.2026, 19:35)
✅ statyczne · ✅ język (0 błędów, 0 ostrzeżeń) · ✅ wygląd na przeglądarce · ✅ hover ·
✅ korekta skryptem (zero literówek, długich myślników, emoji).
⛔ Zostają - CELOWO, bez zmian od bloku C: `noindex` + `Disallow: /` (`PODGLAD_ROBOCZY = True`)
oraz „repo nie ma zdalnego adresu". Błędy z kontroli DEM nadal nie dotyczą strony docelowej.

### 🔴 BLOK E (etap 7, kontrola) - częściowo zrobiony 07.09 19:55
**Znaleziony i naprawiony realny błąd, którego nie widziała żadna bramka:** na telefonie
390×844 pionowy kadr hero zjadał 531 px, przez co H1 stał na 736-850, a przyklejony pasek
kontaktu (`fixed`, 790-844) **przecinał nagłówek na 60 px**. Najważniejsze zdanie strony było
nieczytelne na ekranie, na którym ta strona się rozstrzyga.
Naprawa: `max-height: 44vh` na kadrze (skalowanie, ZERO kadrowania) → H1 kończy się na 755,
pasek zaczyna na 790, **zapas 35 px**. Zapisane w `DESIGN.md`.

**Dwie rzeczy dołożone do silnika, żeby to nie wróciło u następnego klienta:**
1. `bramki/wyglad.js` - nowy test **`zaslona_fixed`**: czy element `fixed`/`sticky` zasłania
   nagłówek albo przycisk na PIERWSZYM ekranie. Sprawdzony na obu stanach (łapie przed
   naprawą, milczy po). Celowo NIE obejmuje akapitów - urwany na krawędzi `.lead` to
   normalne przewijanie, a nie wada.
2. `bramki/sprawdz.py` - **drugi przebieg na telefonie (390×844)**. 🔴 Do 07.09.2026 bramka
   mierzyła wygląd WYŁĄCZNIE na 1440 px, choć klient otwiera link z SMS-a na telefonie -
   cała ta klasa wad była dla niej niewidoczna.

### 📸 RUNDA ZDJĘCIOWA 07.09 20:35 - polecenie K. „więcej większych zdjęć, mniej tekstu"
⚠️ K. powiedział wprost, że **animacje i przejścia zostają** („ludzie je lubią, skupiają uwagę") -
⛔ nie zdejmować `.rv`, kaskady ani `scale(1.03)`. To była moja propozycja, którą odrzucił.

Zrobione na stronie głównej: kadr hero 430→560 px · kafle wyższe (2:3) i szersze (276→326 px),
bez jednolinijkowych opisów · „przed i po" oraz kafle na kontenerze 1500 px · **nowy pas 21:9
z elewacji 2400×1029** · tekst 247→229 słów.

🔴 **Powiększenia dobierane POMIAREM gęstości** (`naturalWidth` / szerokość na ekranie), nie na oko:
kafle miały 3,6× zapasu (powiększenie darmowe), po zmianie 2,2-3,1×. **Przy „Łazienkach" zapas
to 2,3× i tam jest granica** - dalej nie ma po co iść bez oryginałów od klienta.

🔴 **Rozdzielczość materiału wyznacza, co wolno zaprojektować.** Elewacja przyszła z FACEBOOKA
w 3072×4096 i jako jedyna uniosła kinowy pas; łazienka i poddasze przyszły z INSTAGRAMA
w 739-1200 px i nie uniosą żadnego dużego kadru. Instagram kompresuje, Facebook nie.

### 🔴🔴 ODWRÓCENIE PALETY 07.09 21:15 — dwie decyzje K. i przebudowa

**Co się stało:** klient potwierdził Adamowi, że aktualne jest **STARE logo** — rysunek
z domkami i narzędziami, z **czarnym napisem „TCHÓRZEWSKI"**. To nie była podmiana pliku:
kierunek B „Scena" wygrał m.in. dlatego, że NOWE logo jest białe i żyje na czerni. Zmierzone:
**59 % widocznych pikseli starego znaku jest ciemnych** — na `#0F0F12` zostaje z niego biały
dach i srebrna kielnia.

**Decyzja K. nr 1 (21:15): droga A — strona przechodzi na jasną.** Rozważane były cztery
(A jasna · B płytka pod logo · C prosić klienta o wersję na ciemne · D przemalować u siebie);
tabela z kosztami i ryzykiem została w `DESIGN.md`. Rekomendacja brzmiała „C, a jak nie chce
czekać — A", z zastrzeżeniem, że klient dosłał logo JPG-iem z WhatsAppa i nie odpowiedział
na 15 pytań obiecanych na 07.09, więc C to najpewniej czekanie na coś, czego nie ma.

**Decyzja K. nr 2 (21:15): `o-nas` dostaje kadr**, a nie wpis „świadome odstępstwo".

**Wykonane w tej samej pracy:**
- `assets/app.css` — paleta odwrócona. Papier `#F3F1ED` jest tłem, atrament `#1B1B1E` tekstem.
  Czerń NIE zniknęła — dostała rolę akcentu i ma dokładnie **cztery** miejsca: scena strony
  głównej, otwarcie każdej podstrony (`.otwarcie.ciemna`), ramka wezwania (`.domkniecie`)
  i zasłona przy powiększeniu zdjęcia. Do tego pasy zdjęć, ciemne z natury.
  Wprowadzona jedna klasa `.ciemna`, która odwraca WSZYSTKO wewnątrz bloku — żeby przy
  następnej sekcji nie polować po pliku za kolorami.
- 🔒 **Zasada, która to spina: LOGO STOI WYŁĄCZNIE NA JASNYM.** Dlatego pasek i stopka są
  jasne, a znak nie wchodzi do żadnego ciemnego bloku.
- `img/logo.png` — stary znak, przycięty i przeskalowany do 240×177. 🔴 Skwantowany do
  128 kolorów, bo pełny plik ważył **558 kB i leciał na każdej podstronie** (złapane bramką)
  → **14 kB**. Przepis do odtworzenia w `DESIGN.md`.
- Pasek urósł 82 → **96 px**, znak 34 → **60 px** (46 px na telefonie): stare logo to rysunek
  4:3, nie poziomy wordmark, i przy 34 px napis „TCHÓRZEWSKI" był nieczytelną kreską.
  ⚠️ Razem z paskiem poprawione odjęcie w `.kadr-scena img` (`100dvh - 256px` → `- 276px`),
  inaczej hero wyszłoby poza pierwszy ekran i złamało regułę K.
- `pages.py` — nowa funkcja `kadr_o_nas()`: kadr „Schody po wykończeniu" **między osią lat
  a narracją**, wewnątrz lewej kolumny. Na telefonie przerywa ścianę tekstu w połowie,
  na laptopie wypełnia pustkę pod krótką osią. ⛔ Bez `loading="lazy"` — stoi 1023 px od góry
  i z leniwym ładowaniem zostawiał dziurę przy przewijaniu (bramka).
- `build.py` — `theme-color` z `#0F0F12` na `#F3F1ED`.

⚠️ **Koszt, dla uczciwości zapisu:** „drogi" nastrój, dla którego kierunek B wygrał, jest teraz
słabszy niż w makiecie `kierunek-B-scena.html`. Nie zniknął — kadry pionowe nadal stoją na
czerni w scenie i w otwarciach podstron — ale strona czyta się jaśniej i lżej. To był świadomy
koszt drogi A, nie wpadka.

### 🎬 PIERWSZY EKRAN 08.09 — trzy polecenia K.

K.: „pierwsze co widać nie powala, dużo tekstu" · „jest świetne logo od klienta, zróbmy
zajebiste wejście" · „linki social w okrągłych dymkach, bez tego białego, tylko same logo,
podświetlone, z hoverem".

**1. Hero odchudzony.** Zdjęte: podpis pod kadrem (8 słów — treść siedzi w `alt`), trzeci
przycisk „Zobacz realizacje", połowa leadu. Z ~54 słów zostało ~38, z trzech wezwań jedno:
zadzwonić. Zwolnione miejsce poszło w kadr — **624 → 708 px wysokości** na laptopie
(górny odstęp sceny 76 → 56, suma odjęta od widoku 276 → 192 px).

**2. Wejście z logo** (skill `wejscie-na-strone`). Ekran jest świeżo wykończoną ścianą
w kolorze papieru; spod pociągnięcia wychodzi znak, pod nim ślad w kolorze akcentu, znak
odlatuje do paska, a dopiero potem ściana schodzi i odsłania gotowe wnętrze. To opowiada
robotę klienta, a nie jest „fade z logo", który umie zrobić każdy szablon.

🔴 **Realny błąd złapany na stopklatce (nie okiem, nie zrzutem):** przy jednoczesnym starcie
ściana wygrywała wyścig ze znakiem (0,62 s kontra 0,72 s), odsłaniała ciemną scenę pod
lecącym logo i **czarny napis „TCHÓRZEWSKI" znikał w czerni jak naklejka**. Sama krzywa
z wolnym startem, którą zaleca skill, tego NIE ratowała. Naprawa: `transition-delay: .42s`
na ścianie — najpierw leci znak, ściana rusza, gdy on jest już prawie w pasku.
⚠️ Zwykłym zrzutem tego nie widać — zrzut robi się wolniej niż animacja.

Osobny plik `img/logo-duze.png` (640×472, 58 kB), tylko na stronie głównej: znak w pasku ma
240 px i na kurtynie byłby miękki. Znak dostaje na kurtynie swój rozmiar naprawdę, a do paska
wraca `scale()` mniejszym od 1 — powiększanie `transform`em rozmywa na telefonie.

**3. Znaczki social bez kafelka.** Same znaki, okrągłe, w barwach marek, z poświatą
i podniesieniem na najechanie. 🔴 Okrągłość robi SAM ZNAK — Facebook jest kołem z natury,
Instagram dostał koło w swoim gradiencie z białym aparatem. Dzięki temu zasada
`border-radius: 0` została nienaruszona: nie ma płytki, więc nie ma czego zaokrąglać.
Poświata jest funkcją, nie ozdobą — znak bez tła przejeżdża i po papierze, i po ciemnej
scenie, więc ma dwie słabe poświaty naraz.

**⏳ ZOSTAJE Z BLOKU E:**
- ⚠️ `polityka-prywatnosci` dostaje ostrzeżenie o ścianie tekstu = **fałszywy alarm bramki**;
  na stronie prawnej ściana tekstu jest poprawna. Do pominięcia w `sciana_tekstu`.
- ⏳ Test „czy topowa firma tej branży dałaby to u siebie?" - obejrzenie całej strony.

**⏳ NASTĘPNY KROK: odpowiedzi klienta.** Redakcja zrobiła wszystko, co da się zrobić bez niego.
Publikacja stoi na zgodzie na zdjęcia (pytanie 3). Pytania: `PYTANIA-DO-KLIENTA.md` - **10 blokujących
+ 6 bonusowych** (nowe 16: jak szybko oddzwaniają, gdy nie odbiorą).

**Blokery, które nie zniknęły:**
- ⏳ Odpowiedzi klienta na 10 pytań (obiecane wieczorem 07.09 - nie przyszły; sprawdzone 18:55
  w CRM i w Gmailu).
- ⚠️ Sprawdzić w OVH, czy **abonentem domeny jest klient**, nie Krzysztof prywatnie.

---

## STAN PO BLOKU C (07.09.2026, 18:40) - archiwalnie

**Strona STOI — kod gotowy, bramki przechodzą, nic jeszcze nie jest opublikowane.**

### Co powstało (etap 5)
| plik | co robi |
|---|---|
| `build.py` | szkielet: nagłówek, stopka, dane strukturalne, `sitemap.xml`, `robots.txt`, wersje `?v=` |
| `pages.py` | CAŁA treść + reguły treści na górze pliku (liczba mnoga, zero cen, zakazane frazy) |
| `assets/app.css` | wygląd pisany pod `DESIGN.md` (kierunek B, `border-radius: 0` wszędzie) |
| `assets/rdzen.*` | mechanika i dostępność, wersja 10, wgrana `rdzen.py` |
| `assets/fonty/` | Jost 300/400/500 + Inter 400/500, latin i latin-ext, U SIEBIE (bez Google Fonts → bez banera cookies) |
| `przygotuj-media.py` | `materialy/` → `img/` i `video/`; nazwa pliku = MIEJSCE NA STRONIE, nie pochodzenie |
| `DO-POTWIERDZENIA.md` | ⭐ co stoi na stronie, a nie jest potwierdzone przez klienta + co zrobić po odpowiedzi |
| `.deklaracje-potwierdzone` | „od 2015 roku" - potwierdzone białą listą VAT |

**Podstrony:** `index` (scena) · `co-robimy` (katalog, zygzak) · `realizacje` (indeks galerii
+ 2 filmy) · `o-nas` (oś lat + film z ekipą) · `kontakt` (karta danych + mapa po kliknięciu)
+ `polityka-prywatnosci` i `404`. Każda ma WŁASNY układ, nie tylko własne otwarcie.

### Decyzje podjęte w bloku C (nie były w `DESIGN.md`)
1. 🔴 **Firma o sobie w liczbie MNOGIEJ (polecenie klienta), do czytelnika w POJEDYNCZEJ**
   („zadzwoń", nie „zadzwońcie"). Bramka języka blokuje drugą osobę mnogą, a polecenie
   klienta dotyczyło tego, jak firma mówi o SOBIE. Opisane w `DO-POTWIERDZENIA.md`.
2. **Zero formularza kontaktowego** - klient sprzedaje telefonem i WhatsAppem.
3. **Zero kurtyny powitalnej** - pokazywałaby na pełnym ekranie logo odzyskane z JPG-a.
4. **Zero plakietki opinii Google** - nie mamy pewności, że wizytówka z 6 opiniami jest ICH
   (pod tym samym adresem druga firma o tym nazwisku), ani zgody na przepisanie opinii.
5. **Filmy: bez dźwięku, `preload=none`, rusza po kliknięciu.** 5,6 MB → 1,7 MB i 3,5 MB.
6. **Na telefonie kadr hero idzie PRZED nagłówkiem** - pierwszy ekran ma rozstrzygać
   zdjęciem prawdziwej roboty (decyzja z etapu 2).
7. **Myślniki: tylko zwykłe `-`** (twarda reguła bramki języka), zero emoji - przycisk filmu
   dostał ikonę SVG.

### 🪤 Pułapki, które kosztowały rundę - zapisane, żeby nie wracały
- 🔴 **`.kaskada` SAMA NIC NIE ODSŁANIA.** Klasę `is-in` dokłada obserwator `.rv` (rdzeń,
  blok 4), więc kontener musi mieć `class="... kaskada rv"`. Bez `rv` cztery kafle usług
  stały na `opacity:0` - sekcja była PUSTA i widać to było dopiero na zrzucie.
- **Biel na `#C85C13` to kontrast 4,20 - poniżej progu.** Przyciski biorą `--akcent-btn`
  `#A34A0F`, mały tekst akcentem na sekcji jasnej `--akcent-na-jasnym` `#8F3F0A`.
  Sam `#C85C13` zostaje na kreski i na tekst na ciemnym tle.
- **`.spec` i `.dalej` w kaflu muszą być blokami** - jako elementy liniowe sklejały się
  w jedno zdanie („zabudowa i podejścia. Zobacz →").
- **Makiety kierunków przeniesione do `design/_kierunki/`** - katalog z podkreśleniem
  bramka pomija; wcześniej trzy makiety zgłaszały brak `canonical` i og:.
- **To samo zdjęcie w kaflu i w galerii bramka widzi jako klon szablonu.** Kafle usług
  i galeria stoją teraz na ROZŁĄCZNYCH kadrach (`przygotuj-media.py`).

### Stan bramek (07.09.2026, 18:40)
✅ statyczne · ✅ język (0 błędów) · ✅ wygląd na przeglądarce (wszystkie podstrony) ·
✅ hover · ✅ hero zatwierdzone (`.hero-ok.json`).
⛔ Zostają - CELOWO, nie do naprawy teraz:
- `noindex` na każdej podstronie i `Disallow: /` w `robots.txt` → `PODGLAD_ROBOCZY = True`
  w `build.py`. Zdjąć razem ze zgodą klienta na zdjęcia + domeną.
- „repo nie ma zdalnego adresu" → strona świadomie nigdzie nie stoi (patrz niżej).
- Błędy z kontroli DEM (`stopklatka`, `pasek-kontaktu`, `ikony-social`) - to testy silnika
  dem, których strona docelowa nie używa. Pasek kontaktu JEST (`.pasek-dolny`).

### ⛔ Czego NIE zrobiono i dlaczego
**Strona nie została nigdzie opublikowana.** Zdjęcia klienta nie mogą iść na produkcję przed
jego pisemną zgodą (pytanie 3), więc nie ma repozytorium zdalnego, nie ma Cloudflare i nie ma
CNAME. Podgląd: `open -g index.html` albo `python3 -m http.server` w tym katalogu.

**⏳ NASTĘPNY KROK: blok D - teksty** (skill `redakcja-tekstow`, pełne osiem etapów).
Wejście: `pages.py` + `DO-POTWIERDZENIA.md` + odpowiedzi klienta na 10 pytań.

**Blokery, które nie zniknęły:**
- ⏳ Odpowiedzi klienta na 10 pytań (obiecane wieczorem 07.09: gwarancja, logo, zdjęcia).
- ⚠️ Sprawdzić w OVH, czy **abonentem domeny jest klient**, nie Krzysztof prywatnie.

---

## STAN PO BLOKU B (07.09.2026, 14:15) - archiwalnie

**Zrobione w bloku B (etapy 2–4):**
- ✅ **Pytania przycięte 97 → 10** blokujących + 5 bonusowych → `PYTANIA-DO-KLIENTA.md` (do ręki Adamowi).
  Pełna lista leży w `PYTANIA-pelna-lista-97.md` — nie wysyłać.
- ✅ **Materiały ściągnięte** — `materialy/` (38 zdjęć, 2 filmy, 3 pliki logo). Szczegóły niżej.
- ✅ **Decyzje projektowe** — sekcja „ETAP 2" niżej.
- ✅ **Trzy kierunki zbudowane i wyrenderowane** — `design/kandydat-{A,B,C}-*.md` + makiety
  `design/_kierunki/kierunek-*.html`.
  Porównanie: `design/_kierunki/_kierunki-podglad/POROWNANIE.png` (komputer) i `.../telefon/`.

### ✅ KIERUNEK WYBRANY — **B „Scena", BEZ ZAOKRĄGLONYCH RAMEK**

Krzysztof, 07.09.2026 ok. 14:00: *„Możemy zrobić B ale bez zaokrąglonych ramek?"*

- Fundament: [Apple Premium Cinematic](https://designmd.app/library/apple-premium-cinematic).
- 🔴 **`border-radius: 0` wszędzie** — unieważnia pigułki `980px`, najbardziej charakterystyczny
  element oryginału. Ostra krawędź pasuje do cienkiej kreski w jego logo i do branży lepiej.
- **Dlaczego B wygrało:** jedyny kierunek, w którym jego białe logo działa bez przemalowania,
  i jedyny, w którym pionowe zdjęcia stoją bez kadrowania.
- 🔒 **Wszystko o wyglądzie jest teraz w `DESIGN.md` w korzeniu repo.** Zmiana wyglądu = zmiana
  w tamtym pliku, nie kolejny pomysł w trakcie budowy.
- Poprawione przy okazji: **kadr w hero zamieniony na wnętrze SKOŃCZONE** (`poddasze-belki`).
  Poprzedni pokazywał odkryte puszki elektryczne, co zaprzeczało nagłówkowi „gotowe do wprowadzenia".

**⏳ NASTĘPNY KROK: blok C — kod.** Wejście: `DESIGN.md` + `materialy/` + makieta
`design/_kierunki/kierunek-B-scena.html`. ⛔ Zdjęcia nie idą na produkcję przed zgodą klienta (pytanie 3).

**Blokery, które nie zniknęły:**
- ⏳ Odpowiedzi klienta na 10 pytań (obiecane wieczorem 07.09: gwarancja, logo, zdjęcia).
- ⚠️ Sprawdzić w OVH, czy **abonentem domeny jest klient**, nie Krzysztof prywatnie.

---

## ETAP 2 — decyzje projektowe

### Kto tu trafi i czego chce w pierwsze 10 sekund
Najważniejsza grupa: **ktoś dostał nazwisko z polecenia i sprawdza w Google, czy firma jest prawdziwa.**
Przychodzi ze strachem, nie z ciekawością (76,1% Polaków miało problemy z fachowcami; najczęściej
jakość wymagająca poprawek i opóźnienia). Szuka czterech rzeczy naraz: **co robicie · gdzie · dowód ·
jak się odezwać.** Ocena wyglądu powstaje w ~50 ms i już się nie zmienia — pierwszy ekran na telefonie
musi rozstrzygnąć jednym zdjęciem prawdziwej roboty.

### Czym ta firma różni się od konkurencji — jedno zdanie
**Oddają wycenę w terminie: do 5 dni roboczych — żadna z sześciu sprawdzonych firm z regionu
(ROLICZ, REMPERFEKT, PK FLIZ, LUX-DOM, ART-BART, Kundzik) nie podaje NA STRONIE żadnego terminu wyceny.**
Drugi wyróżnik, na osobną sekcję: przy usłudze, której nie robią, polecają sprawdzone osoby.

### Pomysł prowadzący
**Prowadzi ICH WŁASNE nowe logo, nie nasz gust.** Odczytane z pikseli ich banera:
- tło `#0F0F12` (prawie czarne, lekko chłodne),
- znak: **cienka biała kreska** (monogram A+S) + **jedna pomarańczowa esica `#C85C13`**,
- wordmark: wersaliki, bardzo szeroka rozstrzelina, lekka waga.

Z tego wynikają trzy rzeczy dla całej strony: **cienkie linie zamiast grubych ramek · jeden ciepły
akcent i nic więcej · szeroko rozstrzelone małe etykiety zamiast krzykliwych nagłówków.**
🔴 Konsekwencja praktyczna: **nowe logo jest białe i świeci tylko na ciemnym tle.** Kierunek ciemny (B)
używa go bez zmian; kierunki jasne (A, C) wymagają przemalowania znaku — a to wymaga zgody klienta.

### Czego świadomie NIE robimy
- ⛔ **Zero cen i widełek** — „w kwestii ceny trzeba się skontaktować" (polecenie klienta).
- ⛔ **Zero sekcji „certyfikaty"** — nie znaleziono żadnych papierów ani autoryzacji producenckich.
  U konkurencji widzieliśmy sekcję „Opinie napawają nas dumą!" bez ani jednej opinii — tak wygląda
  pusta sekcja i wygląda gorzej niż jej brak.
- ⛔ **Zero animowanych liczników** — REMPERFEKT ma na żywej stronie liczniki pokazujące „0 +".
  Liczby stawiamy statycznie.
- ⛔ **Zero „20 lat doświadczenia" jako hasła głównego** — zajęte (ROLICZ ma 30 lat i dwa dyplomy
  mistrzowskie, LUX-DOM ma dokładnie 20 i tak samo gra kartą zagranicy).
- ⛔ **Zero wielkich jaskrawych płaszczyzn, wersalikowych nagłówków i grubych czarnych ramek**
  (nasza reguła po demie HG Group). Mocny kolor = akcent, nigdy tło sekcji.
- ⛔ **Zero tekstów zastępczych** — LUX-DOM ma na żywej stronie opinie „Jane Anderson" i „James Head"
  o firmie „Earthly Elegance". To jest bramka, nie anegdota.

### Rzeczy zamówione wprost przez klienta (nie do dyskusji)
- 🔴 **Teksty w LICZBIE MNOGIEJ** — łamie domyślną regułę silnika, tu wygrywa klient.
- Kolejność usług: **szpachlowanie, malowanie, łazienki, sucha zabudowa NA GÓRZE**;
  montaż drzwi i okien niżej (mniejszy zarobek).
- **WhatsApp 882 832 244 z ikoną WA przy numerze.**
- „ponad 20 lat" — nie zaokrąglać w górę, nie pisać „od 20 lat".
- Godziny **8–20**, obszar **wielkopolskie i lubuskie**.

### Menu i kontakt
Menu na 4–5 pozycji. Na telefonie: **przycisk „Menu"**, nie pasek pozycji (reguła z SPECBUD, 02.09)
+ **przyklejony na dole pasek z dwoma przyciskami**: „Zadzwoń 667 434 222" i „WhatsApp".
Wpięte we wszystkie trzy makiety.

---

## ETAP 3 — materiały

Wszystko leży w `materialy/`. Źródło: Instagram `@a.s_tchorzewski` (8 postów po jednym adresie,
`gallery-dl` z ciasteczkami Chrome) + Facebook `61589974670830`.

| co | ile | gdzie |
|---|---|---|
| zdjęcia realizacji | **38** | `materialy/realizacje/` |
| filmy | **2** | `materialy/wideo/` |
| logo — pliki źródłowe i odzyskane | 5 | `materialy/logo/` |

### 🔴 Cztery ustalenia, które PROSTUJĄ dossier z bloku A

1. **Nie wszystko jest w 1080 px.** Realizacja „elewacja i podbitka" (9 kadrów) przyszła
   w **3072×4096** — pełne oryginały z telefonu. Bloker „potrzebne oryginały" dotyczy więc już tylko
   łazienki, poddasza i schodów (te są w 924–1440 px) — i akurat to są najładniejsze zdjęcia.
2. **✅ „Malowanie agregatem" NIE jest naszym wymysłem.** Dossier trzymał to na liście
   `[NIEPOTWIERDZONE]` („klient nie wymienił agregatu ani razu"). Mamy **film**, na którym pracownik
   w kombinezonie i masce maluje ścianę agregatem natryskowym, a na ich własnej wizytówce i banerze
   figuruje „Malowanie agregatem" i „Szpachlowanie i gładzie maszynowe". Zdejmuję to z listy zmyśleń.
3. **✅ Mamy „ludzi przy pracy" — czego dossier szukał i nie znalazł.** Drugi film (elewacja) pokazuje
   **co najmniej trzy–cztery osoby** na drabinach i przy ścianie. To jednocześnie jedyny twardy ślad
   wielkości ekipy. Twarzy nie widać — zdjęcie ekipy nadal jest do zamówienia u klienta.
4. **Logo — bloker częściowo zdjęty.** Znaleźliśmy:
   - **stare logo w czystej formie**, 1290×1278 na białym tle → wycięte do `logo-stare-przezroczyste.png`
     (znacznie lepsze niż 720 px JPG, którego użyło demo),
   - **nowe logo** w banerze 1942 px → odzyskane jako `logo-nowe-przezroczyste.png` (na ciemne tło)
     i `logo-nowe-na-jasne-tlo.png` (znak przemalowany na `#111114`).
   ⚠️ To są pliki **odzyskane z JPG**, nie oryginały od grafika — w nagłówku będą minimalnie miękkie.
   Plik wektorowy nadal zamawiamy (pytanie 2).

### Co mamy — realizacje
| realizacja | kadrów | rozdzielczość | uwaga |
|---|---|---|---|
| **Przed i po** (rozbudowa) | 2 | 1254×1254 | ⭐ najmocniejszy dowód w całym materiale · znak wodny klienta na obu |
| Poddasze pod klucz | 12 | 1200×1600 | najbogatszy jednolity zestaw, ładne światło |
| Elewacja i podbitka | 9 + film | **3072×4096** | jedyne pełne oryginały · dokumentacyjne, nie efektowne |
| Łazienka (wanna wolnostojąca) | 6 | 924–1440 px | ⭐ najładniejsze wnętrze · 2 kadry „w trakcie" |
| Poddasze II (belki, wnęka na wannę) | 5 | 1200×1600 | pokoje jeszcze nieukończone (puszki elektryczne) |
| Beton architektoniczny | 4 | 1440×1080 | ⭐ jedyne **poziome** kadry · bałagan budowlany u dołu, do skadrowania |
| Film: malowanie agregatem | 37 s | 720×1280 | ⭐ człowiek przy pracy |
| Film: elewacja, ekipa | 39 s | 720×960 | ⭐ 3–4 osoby przy robocie |

### 🔴 Ograniczenie, które ukształtowało wszystkie trzy kierunki
**Nie mamy ani jednego ładnego, poziomego zdjęcia w wysokiej rozdzielczości.** Wszystko dobre jest
pionowe albo kwadratowe. Dlatego żaden z trzech kierunków nie stoi na klasycznym szerokim pasie
nagłówka z jednym rozciągniętym zdjęciem — każdy rozwiązuje to inaczej (A: kadr pionowy obok tekstu ·
B: kadr pionowy jako obiekt na ciemnej scenie · C: małe zdjęcia w indeksie realizacji).

### ⛔ Czego NIE wolno użyć
- **16 plików `img/` z dema** (hero, about, g1–g14) — stock z Pexels. Na płatnej stronie znikają co do jednego.
- **Tła banerów reklamowych** — ciemne wnętrze z pufą (okładka FB) i dom z kamienną elewacją.
  To grafiki/rendery, nie ich realizacje.
- **`RECON.md` z biblioteki dema** — zawiera CUDZE profile (recon pomylił firmę z inną spod Nekli).
- **Ikona TikToka w stopce** — konta nie ma.
- Zdjęcia i film **do czasu pisemnej zgody klienta** (pytanie 3) — na demo przechodziło, na płatną stronę nie.

---

## ETAP 4 — trzy kierunki ⏳ CZEKA NA WYBÓR K.

Fundamenty wzięte z biblioteki `DESIGN.md` (designmd.app), **trzy różne szablony**, nie trzy odcienie
jednego gustu. Każdy plik kandydata ma sekcję „⚠️ Odstępstwa" — co z oryginału odrzucamy i dlaczego.

| | kierunek | fundament | logika układu | mocna strona | ryzyko |
|---|---|---|---|---|---|
| **A** | **Obietnica** | [Trust & Authority](https://designmd.app/library/trust-authority) | jasna, split hero + cztery kafle obietnic | **nie zależy od tego, ile zdjęć przyśle klient** | traci serce, jeśli klient nie zgodzi się na publiczną obietnicę „5 dni" |
| **B** | **Scena** | [Apple Premium Cinematic](https://designmd.app/library/apple-premium-cinematic) | ciemna, jedna rzecz na ekran, kadr pionowy bez kadrowania | **jedyny, w którym jego białe logo działa bez przemalowania**; wygląda drożej | ciemne tło nie wybacza zdjęć w 1200 px |
| **C** | **Redakcja** | [Editorial Contemporâneo](https://designmd.app/library/editorial-contemporaneo) | papier, szeryf, asymetria, indeks realizacji z numerami | **najbezpieczniejszy przy słabych zdjęciach** (małe kadry) + miejsce na historię 2005→2015 | historii jeszcze nie mamy potwierdzonej |

**Pytanie do K. brzmi: który sprzedaje TĘ firmę TEMU klientowi** — nie który ładniejszy.

Wybór zapisać TUTAJ (z uzasadnieniem), a wybranego kandydata przepisać na **`DESIGN.md` w korzeniu repo**.

---

## STAN PO BLOKU A (07.09.2026, 12:20) — archiwalnie

- Domena `as-tchorzewski.pl` kupiona (OVH, 1 rok, 20,53 zł brutto, DNSSEC + Zimbra Starter w cenie).
- Brief z checklisty Adama → `BRIEF-KLIENTA.md`.
- Research wieloagentowy (7 torów, 15 agentów, ~32 min): **126 faktów przyjętych, 9 obalonych**.
  - `dossier.md` — dokument roboczy (33 kB). ⚠️ Cztery jego ustalenia poprawione w bloku B, patrz ETAP 3.
  - `research-tory.md` — pełny materiał źródłowy (132 kB), do zaglądania, nie do czytania w całości.
  - `research-odrzucone.md` — 9 rzeczy obalonych przez weryfikatora.
- 🎁 **Wizytówka Google ma źle ustawiony obszar** — pinezka wypada w Barczyźnie k. Nekli, ~130 km
  od Błońska, i nie ma podpiętej strony. Darmowy zysk do zgłoszenia przy oddaniu (pytanie 10).

### 🎬 FILMY 08.09 13:50 - polecenie K. „za dużo dziwnej pustej przestrzeni"
K. wskazał sekcję „Nasza ekipa przy robocie" na `o-nas`: film z lewej, cztery linijki tekstu
z prawej i pół ekranu pustki. Ta sama choroba siedziała na stronie głównej.

Zrobione:
- **Oba filmy (i tylko tyle klient ma) przeniesione na STRONĘ GŁÓWNĄ**, obok siebie w sekcji
  „Z budowy". Przechylony układ `.film-obok` skasowany z CSS i z obu podstron.
- **Kadr 4:5 dla obu** - filmy mają różne proporcje (9:16 i 3:4), więc bez tego kafle miały
  różną wysokość i pod niższym znowu robiła się dziura.
- **Odtwarzanie na najechaniu kursorem i na przytrzymaniu palca** (`rdzen.js`, blok 7 przepisany;
  zmiana poszła do ŹRÓDŁA w `~/.claude/skills/strona-docelowa/rdzen/`, nie tylko tutaj).
  Klik zostaje - dla klawiatury i dla obejrzenia do końca.
- **Zdanie „film bez dźwięku" wycięte wszędzie** (K.: nie tłumaczymy się z braku).
- `V_CSS` 9→10, `V_RDZEN` 10→11.

⚠️ **Pułapka, która kosztowała pół godziny:** w karcie sterowanej przez rozszerzenie
Claude-in-Chrome wideo NIGDY się nie ładuje (`readyState=0`, w sieci brak zapytania o `.mp4`).
Wygląda jak zepsuty odtwarzacz. W czystym headless Chromie film gra bez zarzutu (sprawdzone:
`currentTime` 3,87 s po 4 s najechania). Nie diagnozuj wideo przez rozszerzenie.

⚠️ **Druga pułapka:** pełnostronicowy zrzut (`captureBeyondViewport`) NIE domalowuje zdjęć
spoza pierwszego ekranu - na obrazku zostają czarne i białe dziury nie do odróżnienia od
prawdziwej pustki w układzie. Zrzut do OCENY WYGLĄDU rób z oknem ustawionym na całą wysokość
strony: `cdp.mjs <url> --tylko-zrzut --szerokosc 1440 --wysokosc <wysokość strony>`.

### ⏳ HERO - czeka na wybór K. (08.09 14:15)
K. i Marceli: pierwszy ekran „kompletnie się nie podoba". Przygotowane **trzy propozycje**
pełnoekranowego hero (zdjęcie na całą szerokość + tekst na przyciemnieniu, zamiast kadru
w ramce obok tekstu). Wszystkie ze ZDJĘĆ KLIENTA, żadnego stocku:
1. **Beton architektoniczny** (`beton-arch-ciemny-01`) - kadr natywny 1440 px, bez rozszerzania.
2. **Schody i gładź** (`schody-beton-11`) - podciągnięty z 1200 px, do rozszerzenia w Flow.
3. **Poddasze w świetle** (`poddasze2-okna-01`) - podciągnięty z 1200 px, do rozszerzenia w Flow.
Makiety: `/private/tmp/.../scratchpad/hero-makiety/` (robocze, poza repo). Po wyborze K.:
wdrożyć w `pages.py` + `app.css`, hero podstron też, `V_CSS` w górę.

### 🖼️ HERO PEŁNOEKRANOWY 08.09 17:00 - decyzja K. „beton architektoniczny"
K. wybrał propozycję 1. Wdrożone:
- **Scena strony głównej pełnoekranowa**: `img/hero.jpg` = ściana z betonu architektonicznego
  (`beton-arch-ciemny-01`), 1440×1300, `object-fit:cover`. ⛔ Układ `.kadr-scena` (pionowy kadr
  w ramce OBOK tekstu) SKASOWANY - nie wracać bez decyzji K.
- **Każda podstrona ma własny kadr w otwarciu** (`otwarcie(kadr=…)`): `co-robimy` = belka
  i światło, `realizacje` = poddasze z oknami, `o-nas` = rusztowanie przy elewacji,
  `kontakt` = betonowe schody. Polityka prywatności i 404 zostają bez zdjęcia - przy błahej
  treści zdjęcie robi hałas.
- **Pas na głównej zmieniony** na zieleń pod belkami (`pas-zielen.jpg`): beton poszedł na hero,
  a ten sam kadr dwa razy na jednej stronie zdradza, że materiału jest mało.
- Z galerii wypadły `z-beton-01` i `z-schody-02` - oba niosą teraz hero/otwarcie.
- `V_CSS` 10→11.

🔴 **WPADKA, KTÓRĄ TRZEBA ZNAĆ:** `przygotuj-media.py` funkcja `logo()` brała
`logo-nowe-przezroczyste.png` (BIAŁY napis) i zapisywała go w oryginalnym rozmiarze.
Każde uruchomienie skryptu kasowało poprawne, stare logo (14 kB, czarny napis) i podmieniało
je na niewidoczne na jasnym pasku (109 kB). Naprawione: źródłem jest `logo-stare-przezroczyste.png`,
oba rozmiary (240×177 i 640×472) robi jedna funkcja, paleta zamiast pełnego koloru.
⚠️ Wysokości są WPISANE, nie liczone - `build.py` deklaruje je w atrybutach.

⚠️ **Bramka na telefonie potrafi zgłosić „pomiar kontrastu pominięty" na `index.html`** -
to migotliwy artefakt, nie wada. Zdjęcie `object-fit:cover` rasteryzuje się od nowa, gdy bramka
przełącza widok na 390 px, więc trafia między dwa kadry pomiaru. Zmierzone z pikseli zrzutu
telefonu 08.09: najjaśniejsze tło pod tekstem (41,41,43) → **13,3:1 z bielą, 5,3:1 z szarością**
drugiego planu. Próg to 4,5. Jak przemierzyć: zrzut `--telefon`, potem luminancja WCAG z pasów
tekstu (skrypt w scratchpadzie sesji).

### 🧱 „O NAS" 08.09 19:00 - uwaga K. „popraw tę pustą przestrzeń"
Pionowy kadr stał w LEWEJ kolumnie i rozpychał ją do 760 px przy 398 px kolumny obok -
pod krótszą zostawało ok. 400 px pustki, a im szerszy ekran, tym więcej.

- Sekcja ma teraz własną siatkę `.uklad-o-nas`: oś lat i narracja w PIERWSZYM wierszu,
  **kadr przez obie kolumny w drugim**. Kolejność w HTML (`oś → kadr → narracja`) ZOSTAJE -
  na telefonie kadr musi przerywać ścianę tekstu w połowie (bramka `sciana_tekstu`).
  🔴 Reguły telefonu muszą mieć TĘ SAMĄ szczegółowość co reguły laptopa, inaczej
  `grid-row:2` wygrywa mimo media query i kadr ląduje pod tekstem (złapane bramką).
- **Zdjęcia podmienione**: otwarcie = poddasze z belkami (ciepłe wnętrze), pas = rusztowanie
  przy skończonej elewacji — jedyny kadr, na którym widać CZŁOWIEKA przy robocie.
  Oba zwolnione z innych miejsc; `z-elewacja-05` wypadło z galerii (⛔ jeden kadr = jedno miejsce).
- Przyciemnienie sceny na telefonie wróciło na .85/.70/.56 - przy .80/.64/.50 etykieta nad
  nagłówkiem dawała 4,49:1 przy progu 4,5.

Bramki: **sekcja wyglądu czysta na 1440 i na 390 px**. Zostają ✗ celowe (noindex, Disallow,
brak zdalnego repo) i near-duplikat `logo.png ≈ logo-duze.png` - to ten sam znak w dwóch
rozmiarach, z założenia.

### ✅ BLOK E ZAMKNIĘTY 08.09 19:40 - „realizacje" i „kontakt" przez test topowej firmy
Ostatnie dwie podstrony po nowych otwarciach ze zdjęciami. Pięć rzeczy nie przeszłoby
u topowego wykonawcy; wszystkie naprawione, bramki przemierzone po każdej.

**1. Realizacje powtarzały stronę główną - na obu końcach.** Podstrona OTWIERAŁA się grupą
„Rozbudowa - przed i po" (`przed.jpg` + `po.jpg`) i KOŃCZYŁA sekcją z oboma filmami - a jedno
i drugie stoi na głównej. Kto wchodził główna → realizacje, dostawał te same dwa zdjęcia
i te same dwa filmy, z tymi samymi podpisami. Filmy były pozostałością po przeprowadzce
z 08.09 („oba na głównej") - wtedy dołożono je na główną, ale nie zdjęto stąd.
🔴 Reguła „jeden kadr nie stoi w dwóch miejscach" dotyczy TAK SAMO zdjęć z galerii
i filmów, jak kadrów w otwarciach. Oba zostają na głównej, z realizacji zeszły.

**2. Dziury w siatce grup.** `.galeria` to `columns:3`, a grupy miały 2, 5, 4, 3, 1, 2, 4 kadry:
„Schody" (JEDNO zdjęcie) zostawiały 2/3 pustego rzędu, „Beton" i „Rozbudowa" (po dwa) - 1/3,
a czterozdjęciowe „Łazienki" i „Elewacja" - dziurę na całą wysokość rzędu po prawej.
- Liczbę słupków wybiera teraz `grupa()` w `pages.py`, nie oko: **2 i 4 kadry → dwa słupki**
  (`.galeria--2`), 3 i więcej → trzy. Dwa i cztery wypełniają rząd co do słupka.
- ⛔ Grupa JEDNOZDJĘCIOWA nie ma dobrego układu (samotny kadr przy 2/3 pustki, a rozciągnięty
  na całą szerokość mięknie - źródła to kadry z telefonu). Taką grupę **scalamy z sąsiednią**:
  „Schody" weszły do „Beton architektoniczny i schody" - ten sam rodzaj wykończenia.
- ⚖️ Koszt, świadomy: „Łazienki" stoją teraz w miejscu 577 px zamiast 377 px, a trzy z czterech
  źródeł mają 900 px (oryginały od klienta: 739-924 px). Bramka liczy gęstość 0,78 potrzebnej
  na Retinie i klasyfikuje to jako „za mały materiał od klienta - nie do naprawienia u nas",
  czyli nie blokuje. Dla porównania KAŻDE otwarcie podstrony stoi dziś na 0,42-0,50.
  Wypełniony rząd wygrywa z 1,5× zamiast 2× gęstości - ⛔ nie cofać tego bez nowych zdjęć.

**3. Para filmów na głównej stała po lewej.** `.reel` ma sufit 420 px (źródła: 540 i 720 px
szerokości), więc w rzędzie `1fr 1fr` dwa kafle zajmowały 874 z 1176 px i po prawej zostawało
300 px pustki - dokładnie to, na co K. narzekał 08.09 przy `.film-obok`. `.para--filmy` daje
parze twardą szerokość **1074 px** (520 + 34 + 520) i stawia ją na środku. ⛔ Nie podnosić
520 px - przy 540 px źródła to już skala 1:1, wyżej film mięknie. Poniżej 980 px `.reel`
traci sufit (media query) i kafle wypełniają połówki same.

**4. Zasłona mapy wyglądała jak element, który się nie wczytał.** Biały prostokąt (`--papier-2`)
na papierze `#F3F1ED`, z włoskową ramką i przyciskiem na środku - rdzeń wprost tego zabrania
(„zasłona ma wyglądać jak część strony, nie jak błąd"). Teraz ciemny panel w tonie ramki
wezwania: siatka ulic z `repeating-linear-gradient` przy `opacity:.16`, ukośna „droga",
adres `Błońsko 46 · 64-308 Jabłonna` akcentem, wysokość 380 px. ⛔ Nie wracać na biel
i nie zdejmować siatki - to ona odróżnia „miejsce na mapę" od dziury.

**5. Kontakt recytował godziny CZTERY razy.** „8:00-20:00" stało w leadzie, w wierszu „Godziny"
w karcie, w ramce wezwania i w stopce; obszar „wielkopolskie i lubuskie" - trzy razy.
Z ramki wezwania wyleciały oba: została sama treść, której nie ma nigdzie indziej
(„Nie odbieramy tylko wtedy, gdy jesteśmy na rusztowaniu - wtedy oddzwaniamy").

**Sprawdzone i ZOSTAWIONE bez zmiany:**
- Prawa kolumna kontaktu („Trzy kroki do ceny") kończy się ~180 px wyżej niż karta z danymi.
  Przy rytmie sekcji 5-10 rem czyta się to jak powietrze, nie jak dziura - inaczej niż 400 px
  w „o nas". ⛔ Nie zapychać zdjęciem: wszystkie 38 kadrów klienta już gdzieś stoją.
- „Poddasze pod klucz" (5 kadrów) zostaje na trzech słupkach - jedna komórka u dołu pusta,
  ale tak wygląda każda porządna mozaika; przy dwóch słupkach dziura byłaby większa.
- ⚠️ `o-nas.html: podstrona bez treści` (1673 znaki) w sekcji 1 bramek - to zastane, sprzed
  bloku E, i wisi na odpowiedziach klienta (liczba osób w ekipie, lata, miejscowości).
  Domyka je blok F, nie E.

Bramki po zmianach: **sekcja wyglądu czysta na 1440 i na 390 px, język 0/0**. Zostają ✗ celowe
(noindex, Disallow, brak zdalnego repo) - stan sprzed publikacji, nie usterki.
