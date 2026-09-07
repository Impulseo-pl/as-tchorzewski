# NOTATKI BUDOWY — as-tchorzewski.pl

Klient: **Firma Ogólnobudowlana Artur Tchórzewski (A.S TCHÓRZEWSKI)** · opiekun **Adam**
Zamówienie IMP/2026/09/005, opłacone w całości 04.09.2026. Karta CRM `de55d1aa-3deb-44f1-88b7-ca3a19ad8b7c`.

---

## STAN PO BLOKU C (07.09.2026, 18:40) ⬅️ CZYTAJ TO

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
