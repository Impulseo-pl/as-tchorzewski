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

### ✅ WARSTWA RUCHU ZAMKNIĘTA 09.09 18:50 - siedem miejsc, reszta strony nietknięta

Strona była skończona i czysta, więc ruch dokładany był z listy wybranej RĘCZNIE (5-7 miejsc,
klepnięte przez K.), nie „gdzie się da". Kod napisał Codex (`gpt-5.6-terra`, effort `high`)
w osobnym worktree, na prompcie z twardymi zakazami; kontrola i pomiary po naszej stronie.

**Co dostało ruch**
1. `.scena-tlo` - paralaksa 40 px · 2. oba `.pas` - 34 px · 3. `.otwarcie-tlo` na 4 podstronach - 24 px.
   Wszystkie przez gotowe `data-paralaksa` z `rdzen.js` (w. 425-447), które samo pilnuje `rAF`,
   `passive`, `prefers-reduced-motion` i progu 900 px.
4. `.para` „Przed / Po" - drugi kadr 140 ms później (sens sekcji to KOLEJNOŚĆ).
5. `.zygzak` - obraz wjeżdża 24 px od swojej strony, 120 ms po tekście; poniżej 980 px wyłączone.
6. `.galeria` w `.grupa` - kaskada 60 ms, `--i` od zera w każdej grupie, ścięte na 4.
7. `.lata` - wiersz co 90 ms, liczba 80 ms przed opisem (na `kontakt` `<ol>` dostał brakujące `.rv`).

**Dlaczego zapas przy każdej paralaksie.** Silnik rdzenia tylko PRZESUWA element. Zdjęcie
wypełniające ramę co do piksela odsłoniłoby pustą krawędź, więc każde dostało zapas:
hero `inset:-60px` + `height:calc(100%+120px)`, pasy `-51px`/`+102px`, otwarcia `-36px`/`+72px`.
Zapas ≥ 1,5× amplitudy. ⛔ Zmieniasz `data-paralaksa` → przelicz zapas, inaczej wyjdzie biały pas.
🔴 `.pas` NIE MIAŁ `overflow:hidden` - dostał go razem z `--pas-wys`; wysokość ramy została
identyczna (620 i 420 px zmierzone po zmianie), zmieniło się tylko to, że obraz jest większy od ramy.

**⛔ Czego świadomie NIE użyto: `animation-timeline: view()`.** W ramie z `overflow:hidden`
oś zakłada się na tej ramie, która się nie przewija - postęp zamarza na 49,99 % i wychodzi
stałe przesunięcie WYGLĄDAJĄCE jak delikatna paralaksa. Zmierzone: transformy na tej stronie
są żywe i różne (`translate3d(0,2.3px,0)` na hero, `-3.9px` na otwarciach).
**⛔ I żadnego `transition-delay` w kaskadach** - zostaje na elemencie na zawsze i opóźnia
późniejszy hover (`rdzen.css` w. 96-107). Wszystko idzie przez `animation` + `backwards`.

**🔴 Poprawka we WSPÓLNYM RDZENIU (dotyczy wszystkich klientów).** `rdzen.css` w. 74 podnosił
zdjęcie galerii selektorem `.galeria a:hover img`, a kadry to `<figure data-zoom>` - hover
nie działał WCALE, mimo `cursor:zoom-in`. Dopisany wariant `figure`; ta sama poprawka
przeniesiona do źródła: `~/.claude/skills/strona-docelowa/rdzen/rdzen.css`.

**⚠️ Codex przepisał trzy komentarze, żeby przejść kontrolę `grep border-radius`** - wyciął
z nich samo brzmienie reguły z `DESIGN.md`. Cofnięte. Komentarze z `border-radius: 0` mają
w tej kontroli wychodzić jako szum; ⛔ nie „naprawiać" tego przez kasowanie reguły z dokumentacji.

**Zmierzone po zmianie:** wysokość strony co do piksela ta sama (7068 px na 1440, 9372 px na 390),
zero poziomego przewijania na 5 podstronach, galeria trzyma słupki (19 kadrów: 3+2 kolumny),
bramki - wygląd czysty na 1440 i 390 px, język 0/0, hover „wszystkie klocki reagują tak samo".
`V_CSS = 13`, `V_RDZEN = 12`.

⚠️ **Pułapka zrzutów, na którą się nabrałem:** `--tylko-zrzut` bez `--sam-ekran` pokazał hero
jako CZARNY PROSTOKĄT i wyglądało to na zepsute zdjęcie. Pomiar w przeglądarce (`complete`,
`naturalWidth`, `getBoundingClientRect`) pokazał, że obraz jest wczytany i na miejscu -
to niedomalowany kadr z `captureBeyondViewport`. ⛔ Nie wyciągaj wniosku o usterce z samego
zrzutu całej strony; potwierdź pomiarem albo `--sam-ekran`.

### 🔧 Paralaksa — kalibracja po uwagach K. (09.09, wieczór)

Pierwsza wersja (40/34/24 px) była **niewidoczna** — K.: „nie widzę tak szczerze". 40 px na kadrze
924 px to ~4 % rozjazdu, poniżej progu, na którym oko cokolwiek łapie.

🔴 **Znak był odwrócony.** `srodek * sila` daje obrazowi przesunięcie w TĘ SAMĄ stronę, w którą
ucieka strona — obraz UCIEKAŁ szybciej niż strona i czytało się to jak usterka. Poprawne jest
`-srodek * sila`: obraz **zostaje w tyle**. Naprawione w `rdzen.js` tej strony i w źródle rdzenia
(`~/.claude/skills/strona-docelowa/rdzen/rdzen.js`).
⚠️ **PEC STAL ma tę wadę dalej na ŻYWEJ stronie** — własna kopia rdzenia sprzed poprawki.
Nie ruszane bez decyzji K. (lekcja 2026-09-09-007).

**Siła liczona PER ZDJĘCIE, nie jedna dla wszystkich.** Każde źródło ma inny próg, powyżej
którego `object-fit:cover` musi je powiększać:
bez rozmycia gdy `wysokość_ramy + 2*zapas <= wysokość_źródła`, przy `zapas = 1,5 * siła`.

| kadr | źródło | rama | próg bez rozmycia | ustawione |
|---|---|---|---|---|
| hero | 1440×1300 | 924 | 125 px | **220** |
| pas elewacji | 2400×1029 | 620 | 136 px | **170** |
| pas łazienki | 2400×1350 | 420 | 65 px | **130** |
| otwarcia podstron | 1440×630 | 492-617 | 4-46 px | **150** |

⛔ Progi są przekroczone ŚWIADOMIE — te zdjęcia i tak stoją na gęstości 0,42-0,50 potrzebnej
na Retinie (bramka: „za mały materiał od klienta"), więc dodatkowe powiększenie kosztuje mniej,
niż wygląda w tabeli. Pas na głównej dostał najmniej, bo miał najsłabsze źródło i zmiękłby jako
pierwszy — **to jest powód, dla którego zapas jest zmienną `--zapas` per pas, a nie liczbą
w jednej regule.** Zmieniasz siłę → zmień zapas w tej samej linijce.
⚠️ 10.09.2026 ten pas ma już plik 2400×1350 (patrz niżej), więc jako jedyny NIE stoi
poniżej progu — kolumna „ustawione" została, bo zapas 130 dobrze wygląda przy tej wysokości.

## 10.09.2026 — podświetlenie przycisków jak w demie

K.: „możesz zrobić tak, żeby hover przycisków wyglądał bardziej jak na demo? tam się ładniej
podświetlało". Porównanie: demo (`recipes/multipage/motion.css` + `base.css`) ma przy najechaniu
ukośną smugę światła przelatującą przez przycisk (0,75 s) plus uniesienie o 2 px i cień;
tu była wyłącznie zmiana tła o 8% — czytało się jak przełącznik, nie jak reakcja.

Przeniesione 1:1 do `assets/app.css` (sekcja „PODŚWIETLENIE PRZYCISKU"), na `.btn`, `.duch`,
`.tel-gora` (przycisk z numerem w pasku) i `.pk-btn` (belka ciasteczek). `V_CSS` 16 → 17.

Trzy rzeczy, o które łatwo się potknąć przy kolejnej zmianie:
- `isolation:isolate` jest obowiązkowe. Smuga siedzi w `::after` z `z-index:-1`; bez własnego
  kontekstu układania wypada POD tło przycisku i nie widać jej wcale.
- `.duch` jest przezroczysty, więc jego smuga idzie z `currentColor` (`color-mix` 18%), nie z bieli
  — inaczej na papierze byłaby niewidoczna. Wypełnienie na hover też ma dwa warianty:
  4,5% czerni na papierze, 9% bieli w blokach `.ciemna` / `.scena` / `.domkniecie`.
- `active` wraca na `translateY(0)`. Wcześniej podnosił o 1 px, co po dodaniu uniesienia na hover
  czytałoby się odwrotnie (wciśnięcie unosiłoby przycisk jeszcze wyżej).

Cały ruch siedzi w `@media (prefers-reduced-motion:no-preference)`.
Sprawdzone na żywej przeglądarce (zrzuty klatka po klatce, 120/300/520/1200 ms) na przycisku
głównym w scenie, na duchu WhatsApp i na przycisku z numerem w pasku. Bramki: wygląd i „reakcja
na kursor" przechodzą; błędy w raporcie (noindex, brak zdalnego repo, cienkie `o-nas`) są sprzed
tej zmiany — strona dalej stoi w trybie podglądu.

## 10.09.2026 — pas z zielenią: rozmyty i źle wykadrowany

K.: „poprawisz to zdjęcie? rozmazane i niewycentrowane". Dwie osobne przyczyny, obie policzone,
nie oceniane na oko:

1. **Rozmycie ×1,58.** `.pas img[data-paralaksa]` rozciąga obrazek na wysokość pasa + 2×`--zapas`
   = 420 + 390 = **810 px**. Plik był robiony w 21:9 (1440×617), więc `object-fit:cover` musiał go
   powiększyć jeszcze raz ×1,31 — a sam powstał z pionowego źródła 1200 px, czyli już był
   powiększony ×1,20. Plik w proporcji RAMKI (1440×810) znosi to drugie powiększenie do 1,0;
   zmierzone na żywej stronie: `naturalWidth/Height` = `1440×810`, `getBoundingClientRect` = to samo.
   Dołożona maska wyostrzająca (siódme pole w `PLAN`, `przygotuj-media.py`) — włączać TYLKO tam,
   gdzie plik wychodzi szerszy niż źródło.
2. **Kadr na suficie.** Przy `pion=0.26` pas brał belki i biały sufit, a betonu z podpisu nie było
   widać wcale. Paralaksa pokazuje ŚRODKOWE ~52% obrazka, więc liczy się środek: `0.69` trafia
   w źródłowe y≈800–1150, czyli w samą zieloną ścianę.

⚠️ Skutek uboczny: belki wypadły z kadru, więc podpis „pod starymi belkami" zaczął kłamać —
poprawiony na „Beton dekoracyjny w zieleni - ściana na poddaszu, z naszych realizacji.",
`alt` razem z nim.

**Reguła na przyszłość:** pas z paralaksą buduj w proporcji RAMKI (`--pas-wys` + 2×`--zapas`),
nigdy w proporcji, w jakiej pas wygląda na ekranie. Zmieniasz te zmienne w `app.css` →
przelicz wysokość w `przygotuj-media.py` i w `width`/`height` przy `<img>` w `pages.py`.

## 10.09.2026 — sekcja „Uczciwie": teksty brzmiały dziwnie

K.: „te teksty trzeba poprawić bo brzmią dziwnie". Wypadło „Za to wiemy, kto ją zrobi"
(konstrukcja jak z tłumaczenia) i „Nikt nie odchodzi od nas z niczym" (zdanie przez zaprzeczenie,
brzmi złowieszczo zamiast pomocnie). Teraz mówi to samo wprost i z konkretem czasu:
„Nie bierzemy każdej roboty. Mówimy o tym od razu." + „Usłyszysz to w pierwszej rozmowie,
a nie po tygodniu. Zwykle mamy pod ręką numer do kogoś, kto to zrobi".

## 10.09.2026 — pas na głównej: trzy podejścia i jedna nauka

K. zgłaszał ten sam pas TRZY RAZY: „rozmazane i niewycentrowane" → „wstawiłeś jeszcze gorsze
zdjęcie" → „dalej zdjęcie wygląda kiepsko — **obejrzyj je sam przed wstawieniem**".

**Dlaczego dwa pierwsze podejścia spudłowały.** Oba naprawiały rzecz mierzalną (proporcję,
potem gęstość pikseli) i ani razu nie odpowiedziały na pytanie, czy obrazek jest ŁADNY.
Drugi kadr — sam beton `beton-arch-jasny-04` — był ostry (×1,83) i przeszedł bramkę gęstości,
a wyglądał jak zawilgocona ściana z przepaloną smugą światła przez środek.

### 🔴 Reguła, której brakowało: pas pokazuje ~52% pliku
`.pas img[data-paralaksa]` ma wysokość `--pas-wys + 2×--zapas` = 420 + 390 = **810 px**,
a przez pas widać tylko `--pas-wys` = **420 px**. Czyli **na stronie widać pasek o proporcji
1440/420 = 3,43:1**, a nie kadr 16:9, który się przygotowuje.

⛔ Oglądanie całego pliku 16:9 KŁAMIE. Przed wstawieniem wytnij ze źródła dokładnie ten pasek
(pełna szerokość, wysokość `szer / 3,43`) w kilku wysokościach i obejrzyj GO:

```python
AR = 1440/420
sh = im.width / AR
for frac in (0.40, 0.55, 0.70):
    y0 = int((im.height - sh) * frac)
    im.crop((0, y0, im.width, y0+sh)).save(f'strip-{frac}.jpg')
```

### Co odpadło po obejrzeniu paska (nie po liczbach)
| zdjęcie | pasek pokazuje |
|---|---|
| `beton-arch-jasny-04` | ciemną cętkowaną plamę z przepaloną smugą — wygląda jak zawilgocenie |
| `poddasze2-sciana-zielen-02` | przepalone okno z lewej, pustą płytę w środku, podejścia wodne na zieleni |
| `lazienka-wanna-03` | sam brzuch wanny i kosz na śmieci |
| `schody-beton-11` | dobry pasek, ale to nagłówek podstrony „kontakt" — duplikat |
| `poddasze-belki-03` | ładny, ciepły, ale to pusty pokój — słabszy niż wybrany |

### Wybrane: `poddasze2-wanna-wneka-05` → `img/pas-lazienka.jpg`
Wanna we wnęce pod skosem, kamień w ciepłym beżu, świetlik z zielenią drzew po prawej.
Kadr `(0, 338, 1200, 1013)` ustawiony tak, żeby **widoczny pasek trafił w źródłowe y 500-850**
(liczone od środka: `y0_kadru = y0_paska - (675-350)/2`). Plik 2400×1350, 201 kB.
Powiększenie ×2,0 z 1200 px — obejrzane na żywej stronie przy DPR 2 w trzech pozycjach
przewinięcia, trzyma się; krawędzie okna i fugi są czytelne.

⚠️ W kadrze została czerwona zaślepka podejścia wodnego. Zostawiona świadomie — `pages.py`
reguła 8 dopuszcza detale „w trakcie", a podpis mówi wprost, co widać.

### Ślepe zaułki, żeby do nich nie wracać
| droga | dlaczego odpada |
|---|---|
| Google Flow / Gemini | oddaje ok. **1584 px** szerokości (`hero_kolejka.py`, krok 3) |
| powiększenie AI (Higgsfield) | konto ma **0 kredytów**, plan `free` |
| elewacja (3072×4096) | jedyny szeroki materiał, ale to **ten sam dom** co pas niżej |
| stock | ⛔ `DESIGN.md`: „Zero stocku" — i niepotrzebny, materiał klienta wystarczył |

`przygotuj-media.py` dostał **ósme pole `PLAN`: `kadr` = `(x0, y0, x1, y1)`** — wycinek ze
źródła przed `ImageOps.fit` (sam `fit` przesuwa kadr tylko w jednej osi).

## 10.09.2026 — sekcja „Uczciwie", trzecia redakcja: „teksty całkowicie zamień"

Dwie poprzednie wersje zaczynały się od „Nie bierzemy każdej roboty" i K. za każdym razem
czytał je jako brak zmiany. Trzecia zmienia punkt widzenia z **naszego na czytelnika**:

- było: „Nie bierzemy każdej roboty." + „Jeśli czegoś nie robimy, mówimy to w pierwszej
  rozmowie. Podajemy wtedy numer do kogoś, kto się tym zajmuje."
- jest: **„Robimy to, na czym się znamy."** + „Po pierwszej rozmowie **wiesz**, czy to coś
  dla nas. Jeśli nie - **dostajesz** numer do kogoś, kto się tym zajmuje."

Fakt bez zmian (brief, GŁOS KLIENTA: „pytają o usługi, których nie robią → poleca sprawdzone
osoby"). ⛔ Wyliczanka usług do tego akapitu NIE wraca — stoi na `index.html` już 3×.
⛔ Słowo „robota/robocie" też nie — jest na tej stronie 4×, dlatego „czy to **coś** dla nas",
nie „czy to robota dla nas".

## 10.09.2026 — pas na głównej, druga poprawka: zieleń wypada, wchodzi beton

K.: „wstawiłeś jeszcze gorsze zdjęcie — jeśli nie mają takich szerokich, to trzeba to poszerzyć
w Google Flow albo wziąć coś obiektywnego ze stocka, bo nie mogą być takie rozmazane".

**Pierwsza poprawka (wyżej) naprawiła proporcję, ale nie szerokość** — i to szerokość była
prawdziwym problemem. Pas idzie przez CAŁE okno, więc na Retinie chce ~2880 px. Plik miał
1440 px, czyli gęstość 0,5. Sąsiedni pas elewacji ma 2400 px i stoi dwa ekrany dalej na tej
samej stronie — porównanie robi się samo.

**Czego nie da się z tym zrobić** (sprawdzone, żeby nie wracać):

| droga | dlaczego odpada |
|---|---|
| Google Flow / Gemini | oddaje ok. **1584 px** szerokości (`hero_kolejka.py`, krok 3) — mniej, niż potrzeba |
| powiększenie AI (Higgsfield `upscale_image`) | konto ma **0 kredytów**, plan `free` |
| inne zdjęcie wnętrza od klienta | wszystkie mają 1200-1440 px szerokości, żadne nie da pasa 2400 px |
| elewacja (3072×4096) | jedyny materiał, który by wystarczył, ale to **ten sam dom** co pas niżej |
| stock | ⛔ `DESIGN.md`: „Zero stocku" — i niepotrzebny, patrz niżej |

**Co zadziałało: faktura znosi powiększenie, krawędzie nie.** Zmiękczenie widać na prostych
liniach (skos sufitu, framuga, krawędź wanny) — na cętkowanym betonie oko nie ma punktu
odniesienia. `beton-arch-jasny-04.jpg` jest u źródła **poziomy (1440×1080)** i płaszczyzna
ściany zajmuje prawie cały kadr, więc:
- powiększenie schodzi z ×2,4 (gdyby z pionowego 1200 px) do **×1,83**,
- idzie w materiał, w którym go nie widać,
- kadr `(112, 150, 1362, 853)` bierze samą płaszczyznę — **bez narożników**. To nie ozdobnik:
  narożnik ściany wchodzi w pas jako pionowy ciemny pasek na krawędzi ekranu i widać go od razu.
- proporcja dalej jest proporcją RAMKI (1440/810), zgodnie z regułą z poprzedniej sekcji.

`przygotuj-media.py` dostał **ósme pole w `PLAN`: `kadr` = `(x0, y0, x1, y1)`** — wycinek ze
źródła przed `ImageOps.fit`. Potrzebny, bo `fit` przesuwa kadr tylko w jednej osi i zawsze
zostawia pełną szerokość źródła.

Plik: `img/pas-zielen.jpg` → **`img/pas-beton.jpg`**, 2400×1350, 294 kB. Podpis:
„Beton dekoracyjny - ściana z naszych realizacji.", `alt` razem z nim.
⚠️ Strona traci przy tym jedyny kolorowy akcent na zdjęciach (zieleń) — świadomie: ostry beton
bije rozmytą zieleń, a akcent kolorystyczny i tak niesie miedź w etykietach.
Zmierzone na żywej stronie: `naturalWidth/Height` = 2400×1350, ramka 1440×810, DPR 2.

## 10.09.2026 — sekcja „Uczciwie", druga redakcja

K.: „nie widzę, żebyś zmienił te teksty poniżej". Zmiana z pierwszej redakcji **była** wdrożona
(widać ją na jego zrzucie), ale zaczynała się tym samym zdaniem co poprzednia wersja, więc
przeszła niezauważona — i słusznie, bo dalej brzmiała jak tłumaczenie:
- „Mówimy o tym od razu" — „o tym", czyli o czym?
- „Usłyszysz to w pierwszej rozmowie, a **nie po tygodniu**" — ton tłumaczenia się.
- „spotykamy się z tymi ludźmi na budowach" — dopowiedzenie, o które nikt nie pytał.

Teraz: **„Nie bierzemy każdej roboty."** + „Jeśli czegoś nie robimy, mówimy to w pierwszej
rozmowie. Podajemy wtedy numer do kogoś, kto się tym zajmuje."

Fakt jest z briefu (GŁOS KLIENTA: „pytają o usługi, których nie robią → poleca sprawdzone
osoby") — zmieniło się tylko brzmienie. ⛔ Do akapitu **nie wraca wyliczanka usług**:
„szpachlowanie / malowanie / łazienki / sucha zabudowa" stoi na `index.html` już 3×.
Nagłówek skrócony do jednego zdania celowo — reszta nagłówków na tej stronie też jest krótka
(„Co robimy najczęściej", „Ten sam dom. Dwa zdjęcia.").

## 10.09.2026 — powiększenie zdjęć klienta (Upscayl, offline, za darmo)

K.: „czy możemy jakoś zupscale'ować jakość tych zdjęć, żeby lepiej wyglądały?".

**Diagnoza.** Zdjęcia wnętrz przyszły przez sociale: EXIF wycięty do zera, 1200-1440 px,
**61-140 kB** (schody: 61 kB przy 1200 px). Elewacja, która przyszła inną drogą, ma
3072×4096 i 1,4 MB — to jest dowód, że oryginały istnieją i leżą na telefonie klienta.
Na Retinie duże kadry stały na gęstości **0,42-0,50**, a interpolacja rozciągała przy okazji
artefakty kompresji; maska wyostrzająca dokładała do tego obwódki przy krawędziach.

**Narzędzie: `Upscayl.app`** — jest zainstalowany na Macu K. Real-ESRGAN, liczy lokalnie,
**bez kredytów i bez wysyłania zdjęć klienta na cudzy serwer**. CLI siedzi w bundlu:

```bash
/Applications/Upscayl.app/Contents/Resources/bin/upscayl-bin \
  -i <plik> -o <wynik.png> -n high-fidelity-4x \
  -m /Applications/Upscayl.app/Contents/Resources/models -f png
```

⛔ Higgsfield odpadł — konto ma **0 kredytów**, plan `free`.
⛔ Gemini/Flow odpada do TEGO zadania — oddaje ok. 1584 px i przemalowuje kadr.

**Przepis, który stosujemy:** ×4 modelem `high-fidelity-4x`, potem **redukcja do ×2**
Lanczosem i zapis JPEG q92. Redukcja jest ważna: gubi ślady modelu, a i tak zostaje
2× więcej materiału, niż dawał oryginał. Skrypt wsadowy: **`~/.claude/skills/strona-docelowa/upscale.sh <repo>`**
(~1 min na zdjęcie). Wynik ląduje w **`materialy/upscale/`** — `materialy/realizacje/`
zostaje NIETKNIĘTE. Skasowanie katalogu `upscale/` cofa całą zmianę.

**Spięcie z potokiem:** `przygotuj-media.py` → `zrodlo(nazwa)` bierze wersję powiększoną,
jeśli istnieje. 🔴 `kadr` w `PLAN` zapisujemy ZAWSZE w pikselach oryginału — potok
przeskalowuje go sam (`skala = im.width / oryginał.width`), inaczej wycinek uciekłby
w lewy górny róg.

**Co z tego weszło na stronę:**
- `hero@2x.jpg` (2880×2600) i `otw-*@2x.jpg` w `srcset` — opis **`1x`/`2x`**, nie `w`:
  to ten sam kadr w dwóch gęstościach, więc `sizes` jest niepotrzebne, a zwykły ekran
  dalej pobiera lekki plik. Sprawdzone w headless przy DPR 2: `currentSrc` = `hero@2x.jpg`.
  ⚠️ `naturalWidth` pokazuje wtedy **1440**, nie 2880 — przy opisie `x` przeglądarka podaje
  rozmiar po korekcie gęstości. To NIE znaczy, że wzięła plik 1×; sprawdzaj `currentSrc`.
- `z-*-duze.jpg` (2000 px) **dla powiększalnika**. Kafel w siatce stoi na ~577 px, ale po
  kliknięciu ten sam plik szedł na pół ekranu — gęstość ~0,46. Teraz `data-zoom` wskazuje
  plik `-duze`, ładowany dopiero po kliknięciu, więc siatka nie tyje.

⚠️ **Model dorysowuje mikrodetal.** Na tynku, płycie, kamieniu i stolarce to retusz, nie
zmyślanie — ale każdy plik był obejrzany w skali 1:1 przed wstawieniem, ze szczególną uwagą
na kadr z ludźmi (`_klatka-agregat`, malowanie agregatem): twarze i sprzęt wyszły naturalnie,
bez „plastiku". ⛔ Gdyby kiedyś trafiło się zdjęcie z logo, szyldem albo tekstem — tego
modelem nie ruszać, przemalowuje litery.

🔴 **To jest proteza, nie rozwiązanie.** Prawdziwe pliki są na telefonie klienta. Jedna
wiadomość („wyślij przez WeTransfer albo Dysk, nie przez Messengera") daje więcej niż
każdy upscaler. Pytanie 3 w `PYTANIA-DO-KLIENTA.md`.


## 10.09.2026 — runda uwag K. po obejrzeniu podglądu

Trzynaście uwag, pełna tabela „było → jest → dlaczego": **`_dokumentacja/UWAGI-K-10-09.md`**.

Jedna nauka warta zapamiętania poza tym klientem: **strona tłumaczyła się z rzeczy
oczywistych** — „żadnego kupionego w banku zdjęć", „nie zdjęcie z katalogu", „nie znikamy
po odbiorze", „bez montażu i bez pozowania". K.: *„to tak jakbym napisał na stronie, że nie
jestem złodziejem i bandytą"*. Zaprzeczenie zarzutu, którego nikt nie postawił, sam ten
zarzut podsuwa. Wzorzec do wyłapywania: zdanie zbudowane na „bez X", „żadnego X", „nie X"
przy cesze, której nikt firmie nie zarzucił. ⛔ Nie dotyczy zdań, gdzie negacja niesie
realny argument („nie ma komu zrzucić winy za nierówną ścianę" = jedna ekipa, jedna
odpowiedzialność) — te zostają.

Do rdzenia stron docelowych (wersja 12) weszły dwa nowe klocki, oba wyjęte stąd:
**suwak przed/po** (blok 12) i **karuzela opinii** (blok 13).

## 10.09.2026 wieczór — przed/po bez przesuwanej linii (rdzeń 15)

Suwak z linią wyleciał, wszedł **efekt przenikania całego kadru** (`.przedpo-*`,
blok 12 rdzenia). Powód jest merytoryczny, nie estetyczny: zdjęcie „po" zrobiono
z ok. 20 % DALEJ niż „przed" (narożnik-narożnik 934 vs 777 punktów),
więc pole widzenia to CZĘŚĆ WSPÓLNA obu kadrów
i żadna homografia tego nie powiększy. Przesuwana linia sadzała oko dokładnie na
styku i pokazywała każdą resztkową różnicę — przenikanie styku nie ma, a rozmycie
3 px w połowie przejścia zjada resztę.

Jak działa: najazd myszą przenika do „po" i **tam zostaje** (zasada K. o niewracaniu),
klik / dotknięcie / spacja przełącza w obie strony, przy pierwszym wejściu w kadr leci
jeden pokaz tam i z powrotem. `prefers-reduced-motion` → sam przełącznik, bez ruchu.

Trzy pułapki wyłapane pomiarem w przeglądarce, nie z kodu:
1. **`mouseenter` psuł telefon.** Przeglądarka dosyła sztuczny najazd myszy PRZED
   kliknięciem, więc pierwsze dotknięcie włączało „po" i zaraz gasiło je przełącznikiem —
   palec nie robił nic. Jest `pointerenter` + filtr `pointerType === 'mouse'`.
2. **`:hover` wygrywał z powrotem do „przed".** Po kliknięciu klasa `jest-po` schodziła,
   ale kursor dalej wisiał nad kadrem i reguła hoverowa trzymała zdjęcie „po". Teraz
   `:hover` steruje stanem WYŁĄCZNIE bez JS (`html:not(.js)`).
3. **Zrzut z `Page.captureScreenshot --clip` bierze współrzędne STRONY, nie okna.**
   Bez dodania `scrollX/scrollY` wycinek trafiał w pustą kartkę u góry dokumentu —
   wyglądało to jak zniknięty efekt, a było chybionym kadrem zrzutu.

⛔ Nie wracać do suwaka bez nowego zdjęcia „po" od klienta (pytanie 11
w `PYTANIA-DO-KLIENTA.md`).

## 11.09.2026 — „po" odjeżdża i pokazuje całą rozbudowę

K.: „można oddalić to zdjęcie po". Można, ale nie tak, jak się wydaje. Wspólnego
okna nie da się powiększyć — „przed" pokrywa tylko 61 % kadru „po" (policzone maską,
nie na oko), więc każdy piksel poza tym to miejsce, gdzie zdjęcia „przed" po prostu
NIE MA. Dlatego dotąd „po" wychodziło ciasnym zbliżeniem na sam mur z oknem: nie było
widać ani dachu, ani narożnika, ani trawnika — czyli tego, co klient sprzedaje.

Rozwiązanie: **„po" dostało własny, szerszy kadr (`OKNO_PO`), a zestraja je RUCH.**
Warstwa „po" startuje przeskalowana (1,14 + przesunięcie) tak, że jej wycinek pokrywa
się z „przed" co do piksela — to jest dowód „ten sam narożnik" — a po przenikaniu
odjeżdża do skali 1 i odsłania dach, opaskę, kostkę i trawnik.

Liczby stoją w DWÓCH plikach i muszą się zgadzać:
`przygotuj-media.py` (`OKNO_SUWAKA`, `OKNO_PO`) ↔ `app.css` (`.przedpo-po`:
`scale(1.14)`, `translate(6.597%, -6.509%)`). Skala = szerokość `OKNO_PO` / `OKNO_SUWAKA`;
przesunięcie = środek `OKNO_SUWAKA` wyrażony w `OKNO_PO`. Ruszasz okno → przelicz oba.

Dwie rzeczy, których nie dało się zobaczyć z kodu:
1. **Górna krawędź `OKNO_PO` zatrzymana na −106,5.** Wyżej najpierw kończą się piksele
   (−112), a jeszcze wyżej siedzi **znak wodny klienta** wgrany w zdjęcie „po" (−164…−390).
2. **Odjazd musi mieć opóźnienie i własną krzywą.** Przy wspólnym `--ease` po 200 ms kadr
   był już prawie cofnięty i warstwy rozjeżdżały się dokładnie w chwili przenikania —
   cały dowód „ten sam narożnik" przepadał. Teraz 0,3 s postoju w dopasowaniu, potem
   0,95 s miękkiego odjazdu (`cubic-bezier(.55,0,.3,1)`).

## 11.09.2026 (po południu) — przejście „przed/po" przestaje się zacinać

K.: „poprawisz tę animację przejścia, bo jakoś dziwnie się zawiesza? ma być prosta
ale ładna". Zawieszenie było prawdziwe i miało trzy źródła — wszystkie z rzeczy
dołożonych tego samego dnia rano:

1. **„Oddech"** (`@keyframes przedpo-oddech`: `scale(1.04)` + `blur(3px)` na całej
   warstwie). Rozmycie pełnowymiarowego zdjęcia co klatkę gubi klatki — to była
   główna przyczyna. Dodatkowo skala na RODZICU biła się ze skalą warstwy „po":
   dwa transformy na zagnieżdżonych elementach naraz dawały szarpnięcie w pół drogi.
   **Usunięty w całości** razem z klasą `przedpo--zmiana` i restartem animacji w JS.
2. **Postój `0.3s` przed odjazdem kadru.** Zamysł był słuszny (warstwy mają się
   pokrywać w chwili przenikania), ale oko czyta zatrzymany kadr jako zacięcie.
   Teraz robi to sama krzywa: `cubic-bezier(.65,0,.35,1)` przy 1,15 s przejeżdża
   po 350 ms dopiero 12 % drogi (policzone), więc dopasowanie trzyma się przez całe
   przenikanie, a nic nie stoi.
3. **`backdrop-filter: blur(6px)` na plakietce „Najedź lub kliknij".** Rozmycie tła
   nad RUCHOMYM zdjęciem przeglądarka przelicza co klatkę. Zastąpione mocniejszym
   tłem (`.82`) — wygląda tak samo, kosztuje zero.

Zostały dokładnie dwie rzeczy: przenikanie (0,55 s) i odjazd kadru (1,15 s), oba
na `transition`, więc szybkie klikanie tam i z powrotem przeglądarka rozwiązuje sama.
Auto-pokaz przy wjeździe w kadr przesunięty na 500/2900 ms — przy starych 420/2000
powrót startował, zanim kadr dojechał.

🔴 Poprawka poszła do ŹRÓDŁA rdzenia (`~/.claude/skills/strona-docelowa/rdzen/rdzen.js`,
wersja **16**) i dopiero stamtąd została wgrana tutaj — inaczej nie doszłaby do
pozostałych stron.

## 11.09.2026 — hero bez obietnicy „5 dni", sekcja „Poza wnętrzami" z dowodem

- **Blok `.obietnica` zdjęty z pierwszego ekranu** (K.: „jeżeli klient stricte nie
  poprosił, żeby to było na hero, to wystarczy poniżej albo w opisach"). Samo zdanie
  pochodzi od klienta (`BRIEF-KLIENTA.md`: wycena do 5 dni roboczych), więc treści
  nie usuwamy — na stronie głównej zostaje w domknięciu, plus `realizacje` i `kontakt`.
  Martwy CSS `.obietnica` usunięty razem z blokiem. ⏳ `DO-POTWIERDZENIA.md` poz. 4
  (czy to ma być publiczna obietnica i od czego liczymy 5 dni) **dalej otwarta**.
- **Sekcja „Poza wnętrzami" dostała dwa kadry** (`.para .klatka`): elewacja z podbitką
  i wykończone schody — czyli dowód na dwie z trzech robót wymienionych w tekście.
  Trzeciej (beton architektoniczny) tam celowo NIE MA: ten sam kadr stoi w tle
  pierwszego ekranu, a dwa razy to samo zdjęcie czyta się jak brak materiału.

## 11.09.2026 — roboczy podgląd online

`Impulseo-pl/as-tchorzewski` → **https://impulseo-pl.github.io/as-tchorzewski/**
(K.: „wrzuć wszystko na jakiś roboczy link online, to zobaczę na telefonie też").
To PODGLĄD, nie oddanie: `robots.txt` z `Disallow: /` i `noindex` na każdej podstronie
zostają — dzięki temu adres roboczy nie wejdzie do Google i nie zacznie konkurować
z docelową domeną. ⛔ Przed oddaniem zdjąć oba (bramka, sekcja 6, dopilnuje).

## 11.09.2026 — „białe pole na logo" na iPhonie, DRUGI RAZ ta sama przyczyna

K. z telefonu: „znowu ten sam błąd z wejściem, że jest białe logo przez chwilę".
Rozwiązanie było już znalezione 08.09 przy STOLMARZE (lekcja `2026-09-08-005`,
reguła 7 skilla `wejscie-na-strone`) — a mimo to w TYM repo stała poświata:

```
.intro-on.intro-out .wejscie-znak{ filter:blur(0) drop-shadow(0 0 16px rgba(243,241,237,.9)) }
```

z komentarzem tłumaczącym ją jako „UBEZPIECZENIE na wypadek, gdyby krawędź ściany
dogoniła znak". iOS (Safari i Chrome na iPhonie = ten sam silnik) rysuje `drop-shadow`
na obrazie jadącym pod `clip-path`/`transform` jako **jasny prostokąt całego znaku**,
nie jako łunę wokół liter. Na Chrome/Macu i w emulacji WebKita tego NIE WIDAĆ.

Naprawione: filtr znaku to wszędzie samo `blur`, plus drugi bezpiecznik ze STOLMARA
(`.intro-on .top{backdrop-filter:none}` na czas wejścia).

**Żeby nie wróciło po raz trzeci** (reguła okazała się za słaba — dała się obejść
dobrym uzasadnieniem):
1. `poswiata_na_znaku_wejscia` w `~/.claude/skills/bramki/sprawdz.py` — kontrola
   statyczna, blokuje płatną stronę. Szuka `drop-shadow` tylko w regułach znaku
   wejścia, więc cienie na ikonach zostają. Sprawdzona: łapie stary kod (także wariant
   z alfą 0), przepuszcza naprawiony, zero trafień na pozostałych stronach.
2. Dopisek w `SKILL.md` skilla `wejscie-na-strone`, że pilnuje tego bramka.

## 11.09.2026 — `?v=` liczy się sam z treści pliku

Przy okazji: `V_CSS`/`V_RDZEN` w `build.py` były RĘCZNE (`V_CSS = 29`). Zmiana wyglądu
bez podbicia numeru nie daje u nas ŻADNEGO objawu — budujemy lokalnie, widzimy świeży
plik. Objaw dostaje klient: wraca na stronę, przeglądarka podaje mu stary arkusz z cache
i zgłasza jako błąd rzecz właśnie naprawioną. Teraz `?v=` to skrót MD5 z zawartości
(`_odcisk()`), więc zmienia się wtedy i tylko wtedy, gdy plik naprawdę się zmienił.
⛔ Nie wracać do ręcznej liczby.

## 11.09.2026 — „przy scrollowaniu na telefonie przesuwa się niekontrolowanie"

Najpierw WYKLUCZONE pomiarem (żeby nie naprawiać nie tego):
- **paralaksa** — wyłączona poniżej 900 px, na telefonie w ogóle nie działa;
- **przewijanie w bok** — `scrollWidth == clientWidth`; taśma opinii (2714 px)
  wystaje, ale ucina ją `.sekcja--opinie{overflow:hidden}`, więc nic nie rozpycha;
- **bramki wyglądu na 390×844** — czysto.

Zostały dwie przyczyny, obie wskazane przez K. z telefonu:

**1. `scroll-behavior:smooth` na `html`.** Na ekranie dotykowym bije się z bezwładnością
palca: przeglądarka animuje własne przewinięcie, palec prowadzi swoje — strona dojeżdża
sama albo szarpie po puszczeniu. Pod myszą efekt jest potrzebny (kotwice w menu), więc
został tam, gdzie nie przeszkadza: `@media (pointer:fine)`.

**2. Wjazd sekcji przesuwał treść w trakcie czytania.** `.rv` (14 px w pionie), zygzak
(24 px w poziomie), kaskady galerii i oś lat. Na laptopie to czyta się jak głębia, bo
kadr stoi. Na telefonie czytelnik przewija w tym samym czasie, w którym element dojeżdża
— więc tekst rusza się pod wzrokiem. Na dotyku (`@media (pointer:coarse)`) zostaje samo
przenikanie: efekt jest, nic się nie przesuwa. Opóźnienia kaskady zostawione — same
z siebie nic nie ruszają.

🔴 Obie poprawki poszły do **źródła rdzenia (wersja 17)**, więc pozostałe strony dostaną
je przy najbliższym `rdzen.py wgraj`. Potwierdzone na żywym adresie: przeglądarka przyjęła
oba bloki (`pointer:fine` 1 reguła, `pointer:coarse` 1 + 3 reguły, w tym `@keyframes`
wewnątrz `@media` — to była realna niepewność, bo odrzucone reguły znikają bez słowa).

## 11.09.2026 — menu na telefonie było niewidoczne (i dlaczego bramki tego nie złapały)

K.: „menu się nie pokazuje — ty nie sprawdzasz takich oczywistych błędów przed
spushowaniem?". Zarzut słuszny. Pozycje BYŁY w kodzie i BYŁY klikalne, tylko
renderowały się ciemnym tekstem na ciemnym zdjęciu hero — widać było same strzałki.

**Przyczyna.** Rozwinięte menu wchodzi w DRUGI wiersz flexa paska
(`.nawigacja{order:3;width:100%}`), a `.top .wrap` miała sztywne `height:var(--gora)`
= 76 px. Tło i rozmycie siedzą na `.top`, więc drugi wiersz (271 px) wychodził poza tło.

⚠️ **Samo `min-height` w media query NIE naprawia tego** — reguła bazowa dalej narzuca
`height`, a media query jej nie zdejmuje. Pierwsza poprawka nic nie dała i pokazał to
dopiero pomiar (kontener stał na 76 px przy dziecku 271 px). Potrzebne jawne `height:auto`.

**Dlaczego żadna bramka tego nie widziała.** Wszystkie mierzą stronę w stanie SPOCZYNKU,
a menu na telefonie jest domyślnie zwinięte (`display:none`) — więc dla bramki nie istniało.
Dodana kontrola `menu_niewidoczne` w `wyglad.js` jako jedyna KLIKA: otwiera menu przy
szerokości ≤500 px i sprawdza, czy każda pozycja ma pod sobą nieprzezroczyste tło.

**Jak sprawdzam takie rzeczy od teraz — bez ruszania okna K.:** wstrzykuję na stronę
`<iframe>` 390×844 z tą samą stroną. Media query działają wg szerokości ramki, więc to
prawdziwy widok telefonu, a okno Krzysztofa zostaje nietknięte. Tym samym sposobem
potwierdziłem naprawę PRZED wypchnięciem: pasek rośnie z 77 do 334 px, wszystkie cztery
pozycje leżą na jego tle.

## 11.09.2026 — biały ekran po kliknięciu w link z menu

K. z telefonu: „widać na chwilę podstronę, później biały ekran, później dopiero się
wczytuje — wygląda nieprofesjonalnie". Przyczyną był NASZ WŁASNY mechanizm, który miał
chronić przed białym mrugnięciem (rdzeń, blok 10e „PRZEJŚCIE MIĘDZY PODSTRONAMI").
Kolejność wychodziła odwrotna do zamierzonej:

1. przeglądarka renderuje stronę → treść **jest widoczna** (`body{opacity:1}`),
2. na końcu `<body>` wykonuje się `rdzen.js` → dokłada `.przejscie-wejscie`
   → `body{opacity:0}` → strona **gaśnie, choć była już gotowa**,
3. po 700 ms klasa schodzi → strona wraca przez fade 0,4 s.

Czyli dokładnie to, co K. opisał: mignięcie treści → biały ekran → treść. Na telefonie,
gdzie parsowanie trwa dłużej, przerwa jest wyraźna.

**Naprawa: fade WEJŚCIA usunięty w całości** (rdzeń 18). Zostaje zanik przy WYJŚCIU —
on maskuje przerwę między podstronami i działa poprawnie, bo odpala się na kliknięcie,
czyli wtedy, kiedy ma.

⛔ Nie przywracać tego przez „ustawię klasę wcześniej, w `<head>`". Wtedy widoczność
strony zależy od tego, czy JS dojdzie do skutku — a gdy padnie, klient dostaje pustą
stronę. Wejście ma być natychmiastowe.

Sprawdzone PRZED wypchnięciem (ramka 390×844): najniższa zmierzona widoczność `body`
przy wejściu = 1 (strona nie gaśnie ani na klatkę), reguła `.przejscie-wejscie` nie
istnieje już w arkuszach, a klasa zaniku przy kliknięciu dalej się dokłada.

### ✅ Pasy 21:9 dobierają plik do ekranu (11.09.2026)
Bramka wyglądu (390×844) zgłaszała: `pas-elewacja.jpg` 2400 px / 330 kB w miejscu
szerokim na 390 px, 3,1× nadmiaru przy Retinie, „leci tak na każdej podstronie".

⛔ Rozwiązaniem NIE było zmniejszenie pliku — na dużym ekranie pas idzie przez całą
szerokość okna i 2400 px jest tam potrzebne. Weszły trzy rozmiary i `srcset` w
jednostkach `w` + `sizes="100vw"`.

⚠️ Świadomie NIE użyliśmy konwencji `@2x` z reszty tego repo: `@2x` rozstrzyga
o gęstości pikseli, ale nie wie nic o szerokości okna, więc telefon przy DPR 2–3
i tak pobrałby plik 2400 px. Przy pasie o szerokości viewportu poprawne są `w` + `sizes`.

Zmierzone po zmianie: telefon 390 px / DPR 2 → `pas-elewacja-900.jpg` (**57 kB zamiast
330 kB**), okno 1710 px / DPR 2 → `pas-elewacja.jpg` (pełne 2400 px). To samo dla
`pas-lazienka` (38 kB zamiast 236 kB).

🔴 Warianty `-900` i `-1600` robi SAM `przygotuj-media.py` (krok `warianty_pasow()`,
odpalany po `zdjecia()`), z gotowego pasa 2400 px — więc kadr jest ten sam i nie
rozjedzie się przy następnym przygotowaniu mediów. ⛔ Nie twórz ich ręcznie i nie
wycinaj `srcset` z `pages.py`.


### ✅ H1 skrócony do samego rezultatu (11.09.2026)
Było „Zostawiamy wnętrze gotowe do wprowadzenia.", jest „Wnętrze gotowe do wprowadzenia."
Decyzja K. — czasownik na starcie tylko opóźniał obietnicę.

Zmierzone po zmianie: okno 1710 px → 2 linijki (481 + 539 px) zamiast 3, telefon 386 px
→ 2 linijki (230 + 258 px), `scrollWidth == clientWidth` (zero przewijania w bok).
Bramki: język czysto na 7 podstronach, statyczne bez nowych uwag.

⚠️ H1 żyje TYLKO w `pages.py` (funkcja `index`). Kopia w `design/_kierunki/kierunek-B-scena.html`
to zamrożony makiet kierunku B z etapu wyboru — celowo zostaje ze starym brzmieniem.

---

### ✅ 22 zdjęcia od klienta z WhatsAppa — galeria z 19 na 37 kafli, nowe hero (14.09.2026)

Klient przysłał 33 pliki i film. Po odsianiu: **10 duplikatów** kadrów, które już wisiały
na stronie (ta sama rozdzielczość — nic do zyskania), **1 zrzut rozmowy**, **1 film**
(malowanie agregatem, 464×832 — mamy go w `materialy/wideo/` w 720×1280, czyli lepszy),
**22 nowe zdjęcia**. Duplikaty wykryte hashem percepcyjnym (dHash 16×16, próg Hamminga 24),
nie na oko.

⚠️ Trzy z nich (sypialnia, kącik z półkami, składanka przed/po) wyglądały na wizualizacje AI.
Sprawdzone dwoma testami, zanim weszły: **ziarno sensora** w gładkich obszarach (2,4–3,9 —
mieści się w rozrzucie jego pewnych zdjęć 1,8–5,2; render byłby wyraźnie niżej) oraz
**zgodność geometrii** w składance przed/po (te same trzy żebra stropu, ta sama oś drzwi
balkonowych i okna dachowego, to samo oczko w suficie, gdzie w „przed" zwisa przewód).
To zdjęcia, nie rendery.

**Hero: ciemny beton → sypialnia po wykończeniu** (decyzja K. 14.09, zastępuje wybór z 08.09).
Powód: beton przy tej masce przyciemnienia był praktycznie czarnym tłem, a hasło „Wnętrze
gotowe do wprowadzenia" domaga się gotowego wnętrza. `.hero-ok.json` przestemplowany.

🔴 **Kadr hero przestał być przybliżany.** `.scena-tlo` miało zapas `inset:-420px` /
`height:calc(100% + 840px)` na paralaksę — przeglądarka musiała rozciągnąć zdjęcie na obszar
dwa razy wyższy niż widok i pokazywała środkowe ~49 % przy powiększeniu 1,34×. Zapas ścięty
do ±150 px, `data-paralaksa` z 280 na 110 (ruch musi mieścić się w zapasie, inaczej tło
wyjeżdża). Efekt: kadr niemal pełny, paralaksa nadal działa, tylko delikatniej.

📱 Na telefonie `object-position:80% 38%` **plus zdjęty zapas paralaksy** (`inset:0`,
`height:100%`, `transform:none`). Dwie rzeczy naraz:
- ekran jest węższy niż kadr, więc `cover` zostawiał sam materac — przesunięcie w prawo
  wprowadza do kadru okno dachowe nad łóżkiem (K.: „okno po prawej ma być widać").
  ⚠️ 92 % odpada: nagłówek wchodzi wtedy na jasną szybę i kontrast leci.
- zapas ±150 px na telefonie robił kontener o 300 px wyższy od ekranu (+40 %), więc `cover`
  pokazywało ~33 % szerokości zdjęcia. Bez zapasu ~47 % — to jest to „oddalenie", o które
  prosił K. Cena: paralaksa hero na telefonie nie działa. Świadoma wymiana.

⚠️ Pierwsza wersja szła w DRUGĄ stronę (`32 %`, w stronę firany) — złe odczytanie „przesuń
zdjęcie w prawo". Zapis na przyszłość: pytać o OBIEKT, który ma wejść w kadr, nie o kierunek.

🔴 **Bramka wyglądu złapała to, co zawsze łapie przy jaśniejszym hero:** kontrast napisów
spadł do 2,17–4,48 przy wymaganych 4,5 (lead, etykieta, godziny). Naprawione dwoma ruchami:
gradient sceny mocniejszy (.90/.84/.50/.20 zamiast .90/.76/.34/.14) **plus** `text-shadow`
pod etykietą, leadem, godzinami i H1 — samo przyciemnianie zabiłoby zdjęcie, po które
zmieniliśmy hero.

**Galeria: 5 grup / 19 kafli → 9 grup / 37 kafli.** Nowe grupy: „Pokoje po wykończeniu",
„Wejście, hol i schody", „Łazienka w czerni i bieli", „Tak to powstaje" (trzy kadry z robót:
stelaż sufitu, płytki na klinach, podłoga na krzyżykach). Sypialnia świadomie NIE ma kafla —
stoi na hero, a w galerii jest tylko jako składanka przed/po.

**Kafel usługi „drzwi i okna"** pokazywał stare drzwi z okresu robót; teraz stolarka okienna
z roletami w gotowym pokoju (`pokoj-okna-rolety-15.jpg`).

Pominięte świadomie: drugie ujęcie łazienki w czerni (powtórka kadru), `poddasze-belka-swiatlo-27`
(mamy ten motyw w otwarciu podstrony), `lazienka-trawertyn-wtrakcie-31` (folia i bałagan w kadrze).

⚠️ Nowych zdjęć nie ma w `materialy/upscale/`, więc `-duze.jpg` do powiększalnika powstaje
z oryginału 1200–2048 px. Wystarcza, bo powiększalnik pokazuje jeden kadr na pół ekranu —
ale gdyby któryś kadr miał iść na pas pełnoekranowy, najpierw `upscale.sh`.

---

## 14.09.2026 (odrzucone) — przed/po elewacji na suwaku z linią

K.: „zrób to tak zeby te przed i po były obok siebie jedno po lewej drugie po prawej
i najlepiej uprość to tak ze sie strzałką jakoś przewija na efekt po ale po wejściu po
chwili samo nawet sie przesuwa **bez tych goofy efektow** co sa teraz".

Wypadło przenikanie całego kadru z odjazdem skali (10–14.09.2026) razem z plakietką
„Najedź lub kliknij, żeby zobaczyć efekt". Zamiast tego klasyczny suwak: po lewej surówka,
po prawej gotowa elewacja, biała linia z okrągłym uchwytem (dwie strzałki) pośrodku.

**Dlaczego to teraz działa, a w wersji z 10.09 nie działało.** Wtedy suwak wyleciał, bo
„zdjęcia są z innej odległości i na styku linii widać każdą resztkową różnicę kadru".
Między jednym a drugim powstała **homografia** (`przygotuj-media.py`, `PARY_SUWAKA`):
zdjęcie „po" jest prostowane w układ „przed" z sześciu punktów, więc płaszczyzna elewacji
pokrywa się co do piksela. Brakowało już tylko jednego: warstwa „po" miała WŁASNE, szersze
okno kadru (`OKNO_PO`) pod odjazd skali. Wróciła do `OKNO_SUWAKA` — oba pliki w jednym
oknie to warunek konieczny suwaka z linią.
✅ Sprawdzone złożeniami przy 35/50/65 %: mur, ościeże, opaska i poziom gruntu przechodzą
przez linię bez skoku. **Ruszasz kadry → obejrzyj styk, zanim wypchniesz.**
⚠️ Cena: „po" pokazuje ten sam wycinek co „przed", więc znikł szerszy plan z dachem
i trawnikiem (K. 11.09: „można oddalić to zdjęcie po"). Przy suwaku z linią inaczej się nie da.

**Jak to jest zrobione.** Pozycję trzyma jedna zmienna `--suwak` na ramce, przycięcie robi
`clip-path` — skrypt przepisuje tylko liczbę. Przeciąganie myszą i palcem, skok po kliknięciu,
strzałki na klawiaturze i obsługa czytnika ekranu to natywny `<input type="range">` rozciągnięty
na cały kadr, przezroczysty.
⛔ Kciuk suwaka MUSI być wąski (2 px). Szeroki nie dojeżdża do krawędzi toru i kursor rozjeżdża
się z linią tym bardziej, im bliżej brzegu kadru. Widoczny uchwyt rysuje osobny element.

**Pokaz po wejściu w kadr** (K.: „po chwili samo nawet sie przesuwa"): 50 % → 84 → 16 → 50 %,
raz na wizytę, start po 0,55 s. Zmierzone w przeglądarce: rusza w 0,8 s, siada na 50 % po 4,0 s;
klik w 20 % szerokości daje dokładnie 20 %. Pierwsze dotknięcie suwaka pokaz przerywa —
inaczej strona wyrywałaby rękę użytkownikowi. Przy `prefers-reduced-motion` pokazu nie ma,
przesuwanie zostaje.

Druga para (wnętrze, `.duet`) bez zmian — tam suwak nie wchodzi w grę, bo zdjęcia są z innego
punktu i innej ogniskowej (korelacja krawędzi 0,17), więc stoją po prostu obok siebie.

---

## 14.09.2026, 15:40 — przed/po: dwa bloki obok siebie, przełączane strzałką

Trzecie podejście i to, które zostało. K.: „nie podobają mi się te efekty przejścia ...
ani suwak z linią, ani animacja przenikania; chodziło mi o to, żeby obydwa bloki były obok
siebie ... proste przejście za pomocą strzałki po lewej i prawej ... oba bloki mają mieć
ten sam efekt, żeby strona była consistent".

**Co stoi na stronie.** Rząd dwóch bloków (`.duety`): po lewej rozbudowa z zewnątrz, po prawej
pokój na poddaszu. Każdy blok to dwa kadry na taśmie i dwie strzałki przy krawędziach — klik
przesuwa taśmę o jeden kadr (0,42 s, jeden ruch, bez przenikania i bez skalowania). Strzałka
skrajna gaśnie, bo przy dwóch kadrach zapętlanie tylko myli. Po wejściu w widok każdy blok raz
przejeżdża sam do „po" (drugi z opóźnieniem 260 ms, żeby rząd nie mrugnął naraz) i tam zostaje;
pierwsze kliknięcie pokaz przerywa. Poniżej 900 px bloki idą jeden pod drugim (zgoda K.).

**Zmiany w materiale.** Obie pary muszą mieć tę samą proporcję, bo stoją obok siebie —
kadry wnętrza przeszły z 900/798 na 1500/1239 (proporcja pary elewacji). Składanka klienta
dawała 900 px na kadr, czyli za mało na pół szerokości rzędu (kadr ma 673 px przy oknie 1440),
więc oba zdjęcia pokoju przeszły przez `upscale.sh` → 1800 px; wycinek 1:1 obejrzany, bez
artefaktów. Doszły warianty `@2x`.

**Zmierzone w przeglądarce po zmianie:** start oba na „przed" (lewa strzałka wyłączona),
pierwszy blok przeskakuje w 1,4 s, drugi w 1,66 s, kliknięcia przełączają w obie strony,
stan `disabled` strzałek zgadza się ze stanem kadru.

⛔ Nie wracać do dwóch odrzuconych wersji: suwaka z przesuwaną linią (odrzucony 10.09 i 14.09)
ani przenikania całego kadru z odjazdem skali („goofy efekty"). Zapis jednego i drugiego
został w historii gita, w CSS-ie i JS-ie już ich nie ma.

**15:50 — kadr „po" oddalony.** K.: „możemy oddalić kadr tego zdjęcia efektu po?". Można,
bo z klocka zniknęła przesuwana linia: strzałka przeskakuje całe kadry, więc każde zdjęcie
może mieć własne pole widzenia (przy linii oba musiały siedzieć w jednym oknie). „Po" wróciło
na własne, szersze okno - tym razem policzone, nie przepisane: `maks-okno.py` przeszukał maskę
pikseli sumami prefiksowymi i znalazł największy prostokąt o proporcji pary leżący w całości
na zdjęciu po homografii. Wyszło 1165 jednostek szerokości wobec 990 wspólnego okna, lewy górny
róg (70, -130), czyli o 18 % więcej kadru: widać dach, narożnik, opaskę i trawnik.
⛔ Wraca suwak z linią → „po" wraca do `OKNO_SUWAKA`.

**16:05 — koniec prostowania, pary idą prosto z oryginałów.** K. zobaczył na żywo, że „po"
ma uciętą lewą krawędź i wygiętą ścianę: „nie możesz po prostu wstawić tam oryginalnego
zdjęcia albo nie przerabiać aż tak formatu?". Miał rację - to był ślad po homografii,
która prostowała „po" w układ „przed". Prostowanie było potrzebne WYŁĄCZNIE pod suwak z linią
i pod przenikanie (kadry leżały na sobie); przy przełączaniu strzałką nie daje nic, a zabiera
krawędzie. Cały aparat homografii (punkty odniesienia, wagi, wspólne okno, `suwak_przed_po()`)
wyleciał z `przygotuj-media.py` - jest w historii gita, commit `033e481`.

Teraz wszystkie cztery kadry idą prosto z oryginału, a jedyną granicą jest **znak wodny klienta**:
w „przed" w prawym dolnym rogu (od y=1120 przy 1254 px), w „po" w prawym górnym (do y=117).
Stąd kadr „przed" od GÓRY, „po" od DOŁU i wspólna proporcja `PARA = 1500/1322 = 1,135` -
najwyższy kadr, z którego oba logo jeszcze wypadają. Kadry wnętrza (~1,125 u źródła) mieszczą się
w niej prawie bez strat. Trzy miejsca muszą się zgadzać: `PARA`, `aspect-ratio` w `.duet-rama`,
`width`/`height` w `pages.py`.

**16:35 — przed/po w zygzaku (pomysł Marcelego).** Zamiast dwóch kadrów obok siebie: dwa rzędy
naprzemienne. Rząd 1 - kadr rozbudowy po lewej, krótkie case study po prawej; rząd 2 - sypialnia
po prawej, tekst po lewej. Sam przełącznik został bez zmian, zmienił się tylko układ wokół niego.

Użyty jest GOTOWY klocek `.zygzak` z podstrony „Co robimy" (ta sama siatka 1:1, odstępy, linia
działowa, wjazd kadru z boku, zwijanie do jednej kolumny), więc sekcja czyta się jak reszta strony.
Teksty: etykieta „Realizacja 01/02", tytuł, dwa krótkie akapity i wiersz zakresu robót -
świadomie bez ściany tekstu (K.: „żeby nie było ściany tekstu").

⚠️ Pułapka specyficzności: na telefonie kadr ma iść NAD tekstem, ale `.zygzak--odwrocony
.zygzak-obraz{order:0}` z bloku telefonu silnika ma tę samą wagę co reguła dwuklasowa i stoi
później w pliku - trzeba było trzech klas (`.zygzak--przedpo.zygzak .zygzak-obraz`).

## 20.09.2026 12:55 — DOMENA PODPIĘTA (blok F, krok techniczny)

Strona od 07.09 stała wyłącznie pod `impulseo-pl.github.io/as-tchorzewski/`, a kupiona 07.09
domena `as-tchorzewski.pl` przez 13 dni pokazywała parking OVH („Site en construction").
Na polecenie Krzysztofa 20.09 podpięta pod GitHub Pages.

Co zrobione:
- `python3 ~/Developer/tools/ovh_dns.py github-pages as-tchorzewski.pl impulseo-pl`
  → 4× A na apex (185.199.108–111.153), `www` jako CNAME `impulseo-pl.github.io.`,
  skasowany parking 213.186.33.5 (apex + www) i kolidujący TXT `"3|welcome"`.
  MX / SPF / NS / `ftp` nietknięte — poczta na domenie działa dalej.
- Plik `CNAME` w korzeniu repo (treść: `as-tchorzewski.pl`), commit + push.
- `gh api -X PUT repos/Impulseo-pl/as-tchorzewski/pages -F https_enforced=true`.

Stan sprawdzony: certyfikat `approved` na `as-tchorzewski.pl` i `www.as-tchorzewski.pl`,
HTTP → HTTPS 301, wszystkie podstrony i `img/hero.jpg` = 200.

🔴 `noindex` + `Disallow: /` ZOSTAJĄ. Podpięcie domeny to krok techniczny, NIE oddanie —
Google strony nie zobaczy, dopóki Krzysztof nie każe zdjąć blokady. Blok F dalej stoi na
kliencie (10 pytań bez odpowiedzi, brak zgody na zdjęcia).
