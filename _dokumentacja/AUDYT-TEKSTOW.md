# AUDYT TEKSTÓW — A.S TCHÓRZEWSKI (blok D, etap 6)

> 07.09.2026 · skill `redakcja-tekstow`, osiem etapów · źródło tekstów: `pages.py`
> (generowane `.html` to tylko wynik — **edytujemy `pages.py`**).

---

## KROK 0a — stan wejściowy

Kod stoi (blok C), bramki czyste, nic nie opublikowane. `PODGLAD_ROBOCZY = True`.
**Odpowiedzi klienta na 10 pytań NIE PRZYSZŁY** — sprawdzone 07.09.2026 18:55:
karta CRM `de55d1aa` ma tylko komentarz automatu z 21.08, w Gmailu jest wyłącznie
potwierdzenie rejestracji domeny z OVH. Redakcja idzie więc na tym, co stoi;
luki z `DO-POTWIERDZENIA.md` zostają lukami.

## KROK 0c — ⛔ ZDANIA OD KLIENTA (wolno skrytykować, NIE WOLNO zmienić bez zgody)

Źródło: `BRIEF-KLIENTA.md` — checklista spisana przez **Adama po rozmowie z klientem**
07.09.2026 11:11 (nie nasza rekomendacja — to jest zapis rozmowy; ostrzeżenie o PEC STAL
sprawdzone i tu nie zachodzi).

| co | brzmienie z checklisty |
|---|---|
| forma | **liczba mnoga** — firma o sobie „robimy" (do czytelnika zostaje pojedyncza) |
| cena | „w kwestii ceny trzeba się skontaktować" — **zero cen i widełek** |
| wycena | **do 5 dni roboczych** |
| zakres, w tej kolejności | szpachlowanie · malowanie · łazienki · sucha zabudowa; **niżej** montaż drzwi i okien |
| polecanie | „pytają o usługi, których nie robią → **poleca sprawdzone osoby**" |
| historia | firma **rodzinna**, **ponad 20 lat** (nie zaokrąglać), Niemcy **2005**, Polska **2015** |
| kontakt | tel. 667 434 222 · WhatsApp 882 832 244 **z ikoną WA** · godziny **8-20** |
| obszar | województwo **wielkopolskie i lubuskie** |

⛔ Żadnego z tych FAKTÓW nie wolno usunąć ani rozszerzyć. Wolno zmienić **ile razy** i **gdzie**
się je powtarza — i tego dotyczy większość tego audytu.

## KROK 0d — czego NIE WIEMY (luki, nie do załatania copywritingiem)

gwarancja (ile lat, na co) · **kiedy oddzwaniają**, gdy nie odbiorą · ilu ich jest w ekipie ·
pięć najczęstszych miejscowości · czy oględziny są bezpłatne · zgoda na przepisanie opinii z Google.
Wszystkie wiszą w `DO-POTWIERDZENIA.md`. **Żadnej z nich nie zaklejam ogólnikiem.**

---

# ETAP 1 — AUDYT, PODSTRONA PO PODSTRONIE

Perspektywa: człowiek remontuje łazienkę albo kończy poddasze, dostał nazwisko z polecenia,
otwiera stronę na telefonie i chce zdecydować w dwie minuty. Nie oceniam SEO, estetyki ani kodu.

## Liczby na wejście — ile razy to samo (bez stopki i menu)

| fraza | index | co-robimy | realizacje | o-nas | kontakt | razem |
|---|---|---|---|---|---|---|
| „5 dni roboczych" | 2 | 1 | 1 | 1 | 1 | **6** |
| „oględziny" | 2 | 2 | 1 | 1 | 2 | **8** |
| „polecamy sprawdzone osoby" | 1 | 2 | 0 | 1 | 0 | **4** |
| „wielkopolskie/-em i lubuskie/-em" | 2 | 1 | 1 | 3 | 1 | **8** |
| godziny 8-20 | 3 | 1 | 1 | 2 | 4 | **11** |
| „to nasze zdjęcia, nie z internetu" (ta sama myśl) | 2 | 0 | 2 | 0 | 0 | **4** |
| „agregat natryskowy" | 3 | 3 | 2 | 0 | 0 | **8** |
| „firma rodzinna" | 1 | 0 | 0 | 4 | 0 | **5** |

---

## 1. `index.html` — strona główna

### 🔴 Do poprawienia

**1.1 · „Zdjęcia z budowy trudno wziąć z internetu - dlatego pokazujemy stan surowy obok tego,
co po sobie zostawiliśmy." — ważność 8**
Ta sama myśl stoi na stronie **cztery razy**: tutaj, w etykiecie „Nasza robota, nie zdjęcie
z internetu" dwie sekcje niżej, w H1 realizacji („Nasze budowy, nasze zdjęcia") i w ich leadzie.
Przy czwartym powtórzeniu przestaje być dowodem, a zaczyna brzmieć jak tłumaczenie się.
Dodatkowo zdanie jest dwuznaczne — przez sekundę czyta się „trudno nam było zdobyć zdjęcia",
a nie „konkurencja wstawia stock". **Wpływ na decyzję:** argument, który miał budować zaufanie,
zużywa się na własne powtórzenia.

**1.2 · „Na filmie malujemy agregatem natryskowym. Bierzemy go tam, gdzie powierzchnia jest duża,
a powłoka ma być równa - bez śladów po wałku." — ważność 8**
Na `co-robimy.html` stoi to samo zdanie, prawie znak w znak: *„Agregat bierzemy tam, gdzie
powierzchnia jest duża, a powłoka ma być równa - bez śladów po wałku i bez łączeń."*
To nie jest podobieństwo, to duplikat. Kto wejdzie na obie podstrony (a wejdzie — ma je w menu),
zobaczy, że tekst się powiela. **Wpływ:** strona traci wiarygodność „pisanej przez fachowca".

**1.3 · „Co robimy najczęściej" + „Kolejność nie jest przypadkowa - tak wygląda robota,
którą bierzemy najczęściej." — ważność 7**
Dwa problemy w dwóch linijkach. Po pierwsze „najczęściej" pada dwa razy w nagłówku i podpisie
pod nim. Po drugie zdanie **opisuje stronę, nie firmę** — tłumaczy klientowi, dlaczego kafle
są ułożone tak, a nie inaczej. Klienta nie obchodzi kolejność kafli; obchodzi go, czy robią
jego łazienkę.

**1.4 · „Robimy przy okazji wykończenia, razem z obróbką po montażu." (montaż drzwi i okien)
— ważność 6**
„Przy okazji" czyta się jako „to dla nas margines, nie zależy nam". Klient miał rację,
że ta usługa idzie **niżej** — ale niżej znaczy „dalej w kolejności", nie „zniechęcamy".
Ktoś, kto szuka montażu drzwi po wykończeniu, odbije się od tego zdania. To samo zdanie wraca
na `co-robimy.html` („najczęściej przy okazji wykończenia wnętrza").

**1.5 · „Pracujemy w wielkopolskiem i lubuskiem, telefon odbieramy od 8:00 do 20:00."
— ważność 5**
Akapit doklejony na końcu sekcji **o poleceniach innych fachowców**, z którą nie ma nic wspólnego.
Obie informacje już są na tej samej stronie: obszar w etykiecie nad H1, godziny w pasku pod
przyciskami i w stopce. Trzecie wystąpienie w treści, w przypadkowym miejscu.

**1.6 · „Wycena po oględzinach - do 5 dni roboczych" (nagłówek domknięcia) — ważność 6**
Dokładnie ta sama obietnica stoi 1,5 ekranu wyżej, w ramce pod H1. Powtórzenie **na tej samej
podstronie** nie wzmacnia obietnicy, tylko zdradza, że skończyły się argumenty. Fakt zostaje
(polecenie klienta), zmienia się nagłówek.

**1.7 · „Ta sama bryła. Dwa zdjęcia." — ważność 4**
„Bryła" to słowo architekta. Człowiek, który patrzy na dwa zdjęcia domu, myśli „ten sam dom".
Drobiazg, ale to pierwszy nagłówek po hero.

**1.8 · „Drugi film, z roboty przy elewacji, stoi na stronie z realizacjami." — ważność 5**
Znowu zdanie o stronie, nie o firmie — i w dodatku niepotrzebne, bo pod spodem stoi przycisk
„Zobacz realizacje", który mówi to samo działaniem.

**1.9 · Lead: „w Polsce pracujemy od 2015 roku" — ważność 4**
Bez zdania o Niemczech (jest dopiero na `o-nas`) czytelnik zostaje z pytaniem „a wcześniej gdzie?".
Zawieszony fakt w najważniejszym akapicie strony.

### ✅ Co jest dobre i czego NIE ruszam

- **H1 „Zostawiamy wnętrze gotowe do wprowadzenia."** — mówi o rezultacie, nie o usłudze.
  Żadna z sześciu firm z regionu sprawdzonych w researchu nie ma nagłówka o rezultacie.
- **„Nie bierzemy każdej roboty. Za to wiemy, kto ją zrobi."** — najlepszy nagłówek w całym
  serwisie. Zamienia „nie robimy tego" (ubytek) w powód do zaufania.
- **Ramka „Wycena do 5 dni roboczych / od oględzin na miejscu"** pod H1 — jedyny twardy termin
  w całej branży w tym regionie. Zostaje dokładnie tam, gdzie jest.
- **Podpisy „Przed" / „Po"** — konkretne, mówią, co widać w kadrze.

### ⚠️ Czego na tej stronie NIE MA, a klient tego szuka
Ani jednego zdania od kogoś z zewnątrz (opinia) i ani jednej liczby poza „20 lat" i „5 dni".
To nie jest wina tekstu — to brak zgód i danych od klienta (`DO-POTWIERDZENIA.md` #7, #11).

---

## 2. `co-robimy.html` — katalog usług

### 🔴 Do poprawienia

**2.1 · „polecamy sprawdzone osoby" DWA RAZY na jednej podstronie — ważność 8**
W leadzie pod H1: *„a przy robocie, której nie bierzemy, polecamy sprawdzone osoby"*.
Dwa ekrany niżej, w sekcji „Poza wnętrzami": *„Czego nie bierzemy - mówimy od razu i polecamy
sprawdzone osoby, z którymi pracujemy na budowach."* To samo zdanie, ta sama podstrona.
W całym serwisie ta myśl pada **cztery razy** (jeszcze `index` i `o-nas`). To jest drugi
wyróżnik firmy — a przez powtarzanie zamienia się w wypełniacz.

**2.2 · „Robimy to, na czym się znamy" — ważność 6**
Pasuje do każdej firmy budowlanej w Polsce, nie mówi nic. Zajmuje pierwsze słowa leadu
podstrony, którą otwiera człowiek szukający **swojej konkretnej roboty** („czy robią łazienki?").

**2.3 · Malowanie 02: „Agregat bierzemy tam, gdzie powierzchnia jest duża, a powłoka ma być
równa - bez śladów po wałku i bez łączeń." — ważność 8** (druga strona duplikatu 1.2)
Jedno z tych dwóch miejsc musi zniknąć. **Zostaje to** — tu jest opis usługi, tam była podpórka
pod film. Wersja stąd jest lepsza („i bez łączeń").

**2.4 · Sucha zabudowa 04: „to ta sama ekipa, więc nikt nie zrzuca winy za nierówności
na poprzednika." — ważność 7**
Na `o-nas` stoi ta sama figura: *„zabudowa, gładzie i malowanie idą jedną ręką - nie ma komu
zrzucić winy za nierówną ścianę"*. Ten sam argument, ta sama metafora, dwie podstrony.
Argument jest mocny (celuje w realny strach: 76% Polaków miało problem z fachowcem) — właśnie
dlatego ma paść **raz, mocno**, a nie dwa razy słabiej.

**2.5 · Montaż 05: jedyny blok z jednym akapitem + „najczęściej przy okazji wykończenia" — ważność 6**
Widać, że to dopisek: cztery bloki mają po dwa akapity, ten jeden. Do tego „przy okazji"
(patrz 1.4). Klient kazał postawić tę usługę niżej — nie kazał jej sprzedawać gorzej.

**2.6 · „Cena zależy od zakresu i stanu wnętrza, dlatego wyceniamy po oględzinach na miejscu."
— ważność 5**
Na `kontakt.html`, krok 2: *„cenę robi zakres i stan wnętrza, a tego nie da się ocenić przez
telefon"*. Ta sama treść dwa razy. Wersja z `kontakt` jest lepsza — mówi, **dlaczego** nie przez
telefon, więc uprzedza rozczarowanie („czemu nie podadzą ceny?").

**2.7 · „nie ma dróg na skróty" (01) vs „widać każdą drogę na skróty" (`o-nas`) — ważność 5**
Ta sama metafora w dwóch miejscach. Zdanie z 01 jest lepsze i zostaje.

### ✅ Co jest dobre i czego NIE ruszam

- **„Gładź decyduje o tym, jak ściana wygląda po pomalowaniu. Każde zafalowanie widać dopiero
  wtedy, gdy padnie na nie światło z okna."** — najlepszy akapit w serwisie. Tak mówi fachowiec,
  nie copywriter, i to jest dokładnie to, po czym klient poznaje, że ktoś umie robotę.
- **„Podłogi, stolarkę i grzejniki zaklejamy przed robotą, a nie po niej."** — konkret o szacunku
  dla cudzego mieszkania. Odpowiada na lęk, o którym klient nawet nie zapyta.
- **„Łazienka to najwięcej rzemiosła na najmniejszym metrażu"** i **„Płytka wielkoformatowa
  nie wybacza krzywej ściany"** — dwa zdania, które sprzedają najdroższą usługę bez ani jednej liczby.
- **H1 „Wykończenia wnętrz od gładzi po drzwi"** — obejmuje cały zakres w pięciu słowach.
- **„na koncie mamy też elewacje z podbitką"** — ostrożne sformułowanie, bo nie wiemy jeszcze,
  czy elewacje mają być pełną usługą (`DO-POTWIERDZENIA` #6). Zostaje do decyzji klienta.

---

## 3. `realizacje.html` — indeks galerii

### 🔴 Do poprawienia

**3.1 · H1 „Nasze budowy, nasze zdjęcia" + lead „Wszystkie zdjęcia na tej stronie są z naszych
budów." — ważność 8**
Nagłówek i pierwsze zdanie leadu mówią **dokładnie to samo**, jedno pod drugim. A razem
z `index` to trzecie i czwarte wystąpienie tej myśli w serwisie (patrz 1.1). Miejsce, w którym
argument „to są prawdziwe zdjęcia" działa najmocniej, jest właśnie tutaj — pod warunkiem,
że nie zużyliśmy go wcześniej na stronie głównej.

**3.2 · „Część kadrów jest »w trakcie« i tak je podpisujemy - pokazują to, czego na gotowym
zdjęciu już nie widać." — ważność 6**
Pierwsza połowa to **instrukcja obsługi galerii** (jak podpisujemy kadry). Druga połowa jest
świetna i jest prawdziwym argumentem: na gotowej łazience nie widać, czy podejścia zrobiono
porządnie. Zdanie trzeba odwrócić — najpierw argument, potem konwencja albo wcale.

**3.3 · „Oba filmy są bez dźwięku i ruszają dopiero po kliknięciu - nie zjadają transferu
na telefonie." — ważność 6**
Znowu instrukcja obsługi strony, w dodatku językiem technicznym („transfer"). Człowiek szukający
fachowca do łazienki nie przyszedł czytać o transferze. Sam fakt (film nie startuje sam, jest
cicho) jest wart jednego półzdania, nie całego akapitu pod nagłówkiem.

**3.4 · „Dwie minuty roboty" — ważność 3**
Ładny nagłówek, ale filmy trwają 37 s i 39 s, czyli **1 minutę 16 sekund**. „Dwie minuty" to
zaokrąglenie w górę — dokładnie ten rodzaj drobnego naciągnięcia, którego klient zakazał przy
„ponad 20 lat". Konsekwencja kosztuje tu jedno słowo.

### ✅ Co jest dobre i czego NIE ruszam

- **„Chcesz mieć podobnie u siebie?"** — najlepsze wezwanie w serwisie. Jedyne, które wyrasta
  z tego, na co człowiek właśnie patrzy, zamiast powtarzać „zadzwoń".
- **Podpisy kadrów** — mówią, co widać („W trakcie: podejścia wodne wyprowadzone w płytkach"),
  nie dopowiadają faktów o firmie. Reguła 8 z `pages.py` dotrzymana w komplecie.
- **Kadry „w trakcie" pokazane wprost** — konkurencja pokazuje wyłącznie gotowe wnętrza.
  To jest realna przewaga tej galerii i nie wolno jej stąd usunąć.

---

## 4. `o-nas.html` — oś lat i narracja

### 🔴 Do poprawienia

**4.1 · Lead i oś lat mówią to samo, jeden pod drugim — ważność 8. Największy problem tej podstrony.**
Lead: *„Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku pod własnym
szyldem w Polsce. Pracujemy w wielkopolskiem i lubuskiem."*
Oś zaraz pod nim: *2005 - zaczynamy pracę na budowach w Niemczech · 2015 - rejestrujemy własną
firmę w Polsce · Dziś - wykończenia wnętrz w wielkopolskiem i lubuskiem.*
**Trzy punkty osi to przepisany lead.** Czytelnik czyta tę samą historię dwa razy w odstępie
dwóch sekund i nie dowiaduje się nic nowego. Oś ma nieść to, czego nie zmieści lead — daty,
konkret, zmianę.

**4.2 · Punkt „Dziś" na osi = powtórzenie stopki — ważność 6**
*„Wykończenia wnętrz w wielkopolskiem i lubuskiem. Telefon odbieramy od 8:00 do 20:00."*
To czwarte wystąpienie godzin na tej samej podstronie (pasek pod przyciskami, ten punkt,
domknięcie, stopka) i trzecie wystąpienie obszaru. Oś historii kończy się danymi teleadresowymi
zamiast puentą — traci sens gatunku.

**4.3 · „Firma rodzinna" trzy razy na jednym ekranie — ważność 7**
H1 „Firma rodzinna z Błońska" → H3 „Firma rodzinna" → pierwsze słowa akapitu „Jesteśmy firmą
rodzinną." Nagłówek H3 i otwarcie akapitu pod nim to ta sama fraza — czytelnik dostaje ją
dwa razy z rzędu, zanim padnie jakakolwiek treść.

**4.4 · „zabudowa, gładzie i malowanie idą jedną ręką - nie ma komu zrzucić winy za nierówną
ścianę" — ważność 7** (druga strona duplikatu 2.4)
Argument zostaje **tutaj** — na `o-nas` jest o firmie, na `co-robimy` był doklejony do opisu
jednej usługi. Wersja stąd jest też mocniejsza („nie ma komu" > „nikt nie zrzuca").

**4.5 · H3 „Robota, która sama się sprawdza" — ważność 4**
Nagłówek brzmi ładnie i nie znaczy nic konkretnego. Akapit pod nim mówi rzecz zupełnie inną
i lepszą: że po wyschnięciu widać każdy skrót. Nagłówek powinien to zapowiadać.

**4.6 · Domknięcie „Poznajmy się przy wycenie" — ważność 5**
Najmiękkie wezwanie w serwisie, a stoi na podstronie, po której człowiek jest **najbliżej
telefonu** — właśnie przeczytał, kim oni są. „Poznajmy się" odsuwa decyzję zamiast ją domykać.

### ✅ Co jest dobre i czego NIE ruszam

- **„nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze"**
  ⭐ Trafia w jedyny prawdziwy lęk tego klienta: że ekipa zniknie po odebraniu pieniędzy.
  Najlepsze zdanie na tej podstronie. Nie tykam ani słowa.
- **„Bez pozowania i bez lektora - po prostu tak wygląda dzień na rusztowaniu."** — uczciwe
  ustawienie oczekiwań przed filmem nagranym telefonem. Zamienia słabość materiału w atut.
- **Lead z rozdzieleniem Niemcy 2005 / Polska 2015** — rozwiązuje zagadkę, którą zostawia
  strona główna (1.9).

### ⚠️ Luka, której copywriting nie załata
To jedyna podstrona mówiąca o LUDZIACH — i nie pada na niej **ani jedna liczba osób**.
Film pokazuje trzy-cztery osoby na rusztowaniu, ale strona tego nie nazywa.
`DO-POTWIERDZENIA` #11 — jedna prawdziwa liczba od klienta wystarczy.

---

## 5. `kontakt.html` — dokument

### 🔴 Do poprawienia

**5.1 · „Mapa łączy się z Google dopiero wtedy, gdy ją włączysz - do tego czasu ta strona
nie wysyła o tobie nigdzie ani jednej informacji." — ważność 7**
To jest akapit o RODO postawiony pod nagłówkiem sekcji „gdzie nas znaleźć", czyli w miejscu,
w którym człowiek sprawdza, **jak daleko oni mają do niego**. Zabiera całą uwagę sekcji
na temat, którego nikt tu nie ma w głowie. Dodatkowo „nie wysyła o tobie nigdzie ani jednej
informacji" to twarda deklaracja prawna, którą trzeba by w razie czego utrzymać — a przy
mapie po kliknięciu wystarczy pół zdania, żeby powiedzieć to samo bez zobowiązania.

**5.2 · Sekcja „Błońsko, powiat grodziski" nie mówi, gdzie to jest — ważność 6**
Nagłówek obiecuje odpowiedź na pytanie „gdzie wy jesteście", a pod nim nie ma **ani jednej
miejscowości, ani jednej odległości** — tylko akapit o cookies i przycisk mapy.
Człowiek z Wolsztyna, Grodziska czy Zielonej Góry nie dowie się, czy do niego dojadą.
To jest miejsce, w które wchodzi pięć miejscowości z `DO-POTWIERDZENIA` #5 — dopóki ich nie ma,
nagłówek obiecuje więcej, niż sekcja daje.

**5.3 · „Wracamy z wyceną do 5 dni roboczych od oględzin." (krok 3) — ważność 4**
Szóste wystąpienie tej obietnicy w serwisie i **drugie na tej samej podstronie** (jest jeszcze
w domknięciu... a właściwie nie ma — domknięcie mówi o telefonie). Tutaj akurat jest u siebie:
to jedyne miejsce, gdzie opisujemy drogę do ceny krok po kroku. **Zostaje bez zmian.**
Redukować trzeba wystąpienia z `index` i `o-nas`, nie to.

**5.4 · Krok 2 vs lead `co-robimy` — ważność 5** (druga strona duplikatu 2.6)
Zostaje wersja stąd.

### ✅ Co jest dobre i czego NIE ruszam

- ⭐ **„Na WhatsAppie możesz od razu wrzucić zdjęcia wnętrza - to najszybszy sposób, żebyśmy
  wiedzieli, o czym mowa."** — **najbardziej użyteczne zdanie w całym serwisie.** Daje człowiekowi
  gotowy sposób na zaczepkę, która nic nie kosztuje i nie wymaga rozmowy. Powinno stać także
  na stronie głównej, a nie tylko tutaj (patrz etap 2).
- ⭐ **„Nie odbieramy tylko wtedy, gdy jesteśmy na rusztowaniu - oddzwaniamy."** — jednym zdaniem
  rozbraja najczęstszy zarzut wobec ekip budowlanych i robi to językiem człowieka z budowy.
- **Karta danych** — komplet, czytelna, bez ozdób. Dokładnie to, po co ktoś wchodzi na „Kontakt".
- **„Trzy kroki do ceny"** — uprzedza rozczarowanie „czemu nie ma cennika" i tłumaczy je
  rzeczowo, nie wykrętem.

### ⚠️ Luka, której copywriting nie załata
**„oddzwaniamy" nie mówi KIEDY.** To jest dokładnie ten brak, który w metodzie wraca na każdej
stronie („czas reakcji"). „Oddzwaniamy tego samego dnia" byłoby drugą twardą obietnicą obok
pięciu dni — i drugą, której nie ma żadna firma z regionu. Jedno pytanie do klienta.
W karcie danych brakuje też **wiersza o gwarancji** (`DO-POTWIERDZENIA` #1) — miejsce jest
przygotowane, czeka na liczbę.

---

## Podsumowanie etapu 1

**Teksty są na wysokim poziomie** — nie ma w nich ani jednego frazesu z listy zakazanej,
ani jednego zdania zastępczego, ani jednej wymyślonej liczby. Język jest językiem budowy,
nie agencji. To rzadkość i nie zamierzam tego psuć skracaniem.

**Jest jeden problem i jest systemowy: powtórzenia między podstronami.**
Sześć argumentów firmy pada po trzy-cztery razy każdy, w prawie identycznym brzmieniu.
Powstało to naturalnie — każda podstrona była pisana tak, żeby broniła się sama — ale człowiek
czyta je jedna po drugiej i widzi obieg zamknięty. **Cała redakcja sprowadza się do decyzji,
GDZIE każdy z sześciu argumentów pada raz i mocno**, a nie do przepisywania zdań.

Drugi wątek, drobniejszy: **pięć miejsc, w których strona mówi o sobie zamiast o firmie**
(kolejność kafli, konwencja podpisów, transfer na telefonie, gdzie stoi drugi film, RODO przy mapie).

⛔ **Czego ten audyt nie naprawi:** braku opinii, gwarancji, liczby ludzi, listy miejscowości
i czasu oddzwaniania. To są pytania do klienta, nie zadania dla redaktora.

---

# ETAP 2 — POPRAWKI STARE / NOWE

## Zasada porządkująca całą redakcję

Sześć argumentów firmy pada dziś po trzy-cztery razy. **Każdy dostaje jedno miejsce, w którym
pada raz i mocno**, a z pozostałych znika:

| argument | zostaje na | znika z |
|---|---|---|
| to nasze zdjęcia, nie stock | **realizacje** (H1 + lead) | index ×2 |
| polecamy sprawdzone osoby | **index** („Nie bierzemy każdej roboty") + co-robimy („Poza wnętrzami") | lead co-robimy, o-nas |
| agregat: duża powierzchnia, równa powłoka | **co-robimy 02** | index |
| jedna ekipa, nie ma komu zrzucić winy | **o-nas** | co-robimy 04 |
| „drogi na skróty" | **co-robimy 01** | o-nas |
| wycena do 5 dni roboczych | hero index · domknięcie realizacji · **kontakt, krok 3** | domknięcie index, domknięcie o-nas |

⛔ Żaden FAKT nie znika ze strony - znika tylko jego trzecie i czwarte powtórzenie.

---

## `index.html`

**Z-01 · lead sekcji „Przed i po"**
STARE: `Zdjęcia z budowy trudno wziąć z internetu - dlatego pokazujemy stan surowy obok tego, co po sobie zostawiliśmy.`
NOWE: `Przed rozbudową i po niej. Na gotowym zdjęciu nie widać już, od czego się zaczynało.`
→ Argument „nasze zdjęcia" przenosi się w całości na realizacje; tu zdanie zaczyna pracować na to, na co człowiek patrzy.

**Z-02 · H2 tej samej sekcji**
STARE: `Ta sama bryła. Dwa zdjęcia.`
NOWE: `Ten sam dom. Dwa zdjęcia.`
→ „Bryła" to słowo architekta; człowiek patrzy na dom.

**Z-03 · podpis pod „Co robimy najczęściej"**
STARE: `Kolejność nie jest przypadkowa - tak wygląda robota, którą bierzemy najczęściej.`
NOWE: `Cztery roboty, na których stoi większość naszych budów - i montaż drzwi i okien do kompletu.`
→ Zdanie przestaje tłumaczyć układ STRONY, zaczyna mówić o firmie; „najczęściej" pada raz zamiast dwóch.

**Z-04 · kafel „Montaż drzwi i okien"**
STARE: `Robimy przy okazji wykończenia, razem z obróbką po montażu.`
NOWE: `Drzwi wewnętrzne i zewnętrzne, okna - z obróbką ościeży po montażu.`
→ „Przy okazji" zniechęca człowieka, który szuka właśnie tego. Klient kazał tę usługę postawić **niżej**, nie sprzedawać jej gorzej.

**Z-05 · sekcja z filmem (etykieta + podpis)**
STARE etykieta: `Nasza robota, nie zdjęcie z internetu`
NOWE etykieta: `Z naszej budowy`
STARE: `Na filmie malujemy agregatem natryskowym. Bierzemy go tam, gdzie powierzchnia jest duża, a powłoka ma być równa - bez śladów po wałku. Drugi film, z roboty przy elewacji, stoi na stronie z realizacjami.`
NOWE: `Malowanie agregatem - trzydzieści siedem sekund prosto z budowy, bez montażu i bez komentarza.`
→ Usuwa duplikat z `co-robimy` (opis agregatu zostaje tam, gdzie opisujemy usługę) i zdanie o tym, gdzie stoi drugi film - przycisk pod spodem mówi to samo działaniem.

**Z-06 · akapit doklejony do sekcji o poleceniach**
STARE: `Pracujemy w wielkopolskiem i lubuskiem, telefon odbieramy od 8:00 do 20:00.`
NOWE: *(usunąć bez zastąpienia)*
→ Obie informacje są na tej stronie wyżej (etykieta nad H1, pasek godzin) i w stopce. Sekcja kończy się teraz puentą „Nikt nie odchodzi od nas z niczym" zamiast danymi teleadresowymi.

**Z-07 · nagłówek domknięcia**
STARE: `Wycena po oględzinach - do 5 dni roboczych`
NOWE: `Zacznijmy od obejrzenia`
→ Ta sama obietnica stała 1,5 ekranu wyżej, w ramce pod H1. Zdanie pod nagłówkiem **zostaje bez zmian** - argument nietknięty.

---

## `co-robimy.html`

**Z-08 · lead**
STARE: `Robimy to, na czym się znamy - a przy robocie, której nie bierzemy, polecamy sprawdzone osoby. Cena zależy od zakresu i stanu wnętrza, dlatego wyceniamy po oględzinach na miejscu.`
NOWE: `Pięć robót, które bierzemy najczęściej - i to, co przy każdej z nich decyduje o efekcie. Ceny nie podajemy z góry: zależy od zakresu, a zakres widać dopiero na miejscu.`
→ Trzy naprawy naraz: „robimy to, na czym się znamy" pasowało do każdej firmy w Polsce; „polecamy sprawdzone osoby" stało dwa razy na jednej podstronie; opis wyceny był bliźniaczy z krokiem 2 na `kontakt`.

**Z-09 · blok 05, montaż drzwi i okien**
STARE: `Montujemy drzwi i okna najczęściej przy okazji wykończenia wnętrza - razem z obróbką ościeży i wykończeniem ściany po montażu.`
NOWE (dwa akapity):
`Drzwi i okna montujemy najczęściej na końcu wykończenia - wtedy, gdy ściany są już gotowe i wiadomo, w co się wstawia.`
`Po montażu zostaje obróbka ościeży i wykończenie ściany - to część tej samej roboty, nie osobne zlecenie.`
→ Znika „przy okazji". Blok przestaje być jedynym jednoakapitowym w całym katalogu, czyli przestaje wyglądać na dopisek.

**Z-10 · blok 04, sucha zabudowa**
STARE: `Zabudowę prowadzimy tak, żeby od razu szła pod gładź - to ta sama ekipa, więc nikt nie zrzuca winy za nierówności na poprzednika.`
NOWE: `Zabudowę prowadzimy tak, żeby od razu szła pod gładź: równe płaszczyzny, wyprowadzone narożniki, taśmowanie na łączeniach.`
→ Argument „jedna ekipa, nie ma komu zrzucić winy" zostaje na `o-nas`, gdzie jest o firmie. Tutaj wchodzi w to miejsce konkret rzemieślniczy - czyli to, po co ktoś czyta opis usługi.

---

## `realizacje.html`

**Z-11 · lead**
STARE: `Wszystkie zdjęcia na tej stronie są z naszych budów. Część kadrów jest „w trakcie” i tak je podpisujemy - pokazują to, czego na gotowym zdjęciu już nie widać.`
NOWE: `Na gotowej łazience nie widać już, jak wyprowadzono podejścia wodne ani co siedzi pod płytką. Dlatego obok skończonych wnętrz pokazujemy kadry z samej roboty - podpisane „w trakcie”.`
→ Pierwsze zdanie było powtórzeniem H1 stojącego nad nim. Teraz argument idzie pierwszy, konwencja podpisów na końcu.

**Z-12 · sekcja filmów**
STARE H2: `Dwie minuty roboty`
NOWE H2: `Minuta i szesnaście sekund roboty`
→ Filmy trwają 37 i 39 sekund. „Dwie minuty" to zaokrąglenie w górę - dokładnie to, czego klient zakazał przy „ponad 20 lat". Sama precyzja jest tu komunikatem.
STARE: `Oba filmy są bez dźwięku i ruszają dopiero po kliknięciu - nie zjadają transferu na telefonie.`
NOWE: `Oba z budowy, oba bez dźwięku - ruszają dopiero, gdy je włączysz.`
→ „Transfer" to nie jest język człowieka szukającego fachowca do łazienki. Fakt zostaje, akapit o obsłudze strony znika.

---

## `o-nas.html`

**Z-13 · lead**
STARE: `Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku pod własnym szyldem w Polsce. Pracujemy w wielkopolskiem i lubuskiem.`
NOWE: `Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku pod własnym szyldem w Polsce.`
→ Obszar pada na tej podstronie trzy razy. Fakty klienta („ponad 20 lat", 2005, 2015) nietknięte.

**Z-14 · punkt „Dziś" na osi lat**
STARE: `Wykończenia wnętrz w wielkopolskiem i lubuskiem. Telefon odbieramy od 8:00 do 20:00.`
NOWE: `Wykończenia wnętrz pod klucz - od gładzi i malowania po łazienki, poddasza i montaż drzwi.`
→ Oś historii kończyła się danymi teleadresowymi (czwarte wystąpienie godzin na tej podstronie). Teraz kończy się puentą: pokazuje, jak urósł zakres.

**Z-15 · H3 + otwarcie akapitu**
STARE H3: `Firma rodzinna`
NOWE H3: `Co znaczy „rodzinna”`
STARE: `Jesteśmy firmą rodzinną. To znaczy tyle, że nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze.`
NOWE: `Tyle, że nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze.`
→ Nagłówek i pierwsze słowa akapitu były tą samą frazą, a H1 nad nimi trzecią. ⭐ Zdanie, które niesie całą sekcję, zostaje znak w znak.

**Z-16 · H3 + akapit o skrótach**
STARE H3: `Robota, która sama się sprawdza`
NOWE H3: `Po wyschnięciu widać wszystko`
STARE: `Gładź, płytka wielkoformatowa i skos poddasza mają tę wspólną cechę, że po wyschnięciu widać każdą drogę na skróty. Dlatego u nas zabudowa, gładzie i malowanie idą jedną ręką - nie ma komu zrzucić winy za nierówną ścianę.`
NOWE: `Gładź, płytka wielkoformatowa i skos poddasza mają jedną wspólną cechę: efekt widać dopiero wtedy, gdy jest za późno na poprawki. Dlatego zabudowa, gładzie i malowanie idą u nas jedną ręką - nie ma komu zrzucić winy za nierówną ścianę.`
→ Nagłówek zaczyna zapowiadać to, co akapit naprawdę mówi. „Droga na skróty" zostaje wyłącznie na `co-robimy 01`. Argument o jednej ekipie - nietknięty, to jego miejsce.

**Z-17 · podpis pod filmem**
STARE: `Film z budowy przy elewacji. Bez pozowania i bez lektora - po prostu tak wygląda dzień na rusztowaniu.`
NOWE: `Film z budowy przy elewacji. Nikt tu nie pozuje - tak po prostu wygląda dzień na rusztowaniu.`
→ Wzorzec „bez X i bez Y" wchodzi w Z-05 na stronie głównej; zostawiony w obu miejscach byłby nowym powtórzeniem stworzonym przez tę redakcję.

**Z-18 · domknięcie**
STARE H2: `Poznajmy się przy wycenie`
NOWE H2: `Teraz wiesz, kto przyjedzie`
STARE: `Zadzwoń - umawiamy oględziny na miejscu i wracamy z wyceną do 5 dni roboczych.`
NOWE: `Zadzwoń albo napisz - umawiamy oględziny na miejscu.`
→ Najmiękkie wezwanie w serwisie stało tam, gdzie człowiek jest najbliżej telefonu. Nowy nagłówek domyka narrację podstrony i szóste „5 dni" znika.

---

## `kontakt.html`

**Z-19 · podpis sekcji mapy**
STARE: `Mapa łączy się z Google dopiero wtedy, gdy ją włączysz - do tego czasu ta strona nie wysyła o tobie nigdzie ani jednej informacji.`
NOWE: `Błońsko leży pod Rakoniewicami, w powiecie grodziskim - stąd wyjeżdżamy na budowy w wielkopolskiem i lubuskiem. Mapa włącza się dopiero po kliknięciu.`
→ Sekcja nazywa się „Błońsko, powiat grodziski" i nie mówiła, gdzie to jest. Akapit o RODO schodzi do pół zdania - fakt zostaje, deklaracja prawna („nie wysyła o tobie nigdzie ani jednej informacji") znika.
🔴 **Tu wchodzi pięć miejscowości**, gdy klient je poda (`DO-POTWIERDZENIA` #5).

**Bez zmian zostają:** karta danych, „Trzy kroki do ceny", domknięcie „Najszybciej - telefonem",
lead z WhatsAppem i zdjęciami wnętrza (⭐ najlepsze zdanie w serwisie - i **celowo nie przenoszę
go na stronę główną**, bo powstałoby powtórzenie, którego ta redakcja właśnie się pozbywa).

---

# ETAP 4 — AUTOREWIZJA ⭐

Siedem pytań do każdej z 19 własnych propozycji. **Wynik: 9 poprawek do poprawienia,
1 fragment do wycofania, 9 bez zastrzeżeń.**

## ⛔ WYCOFANE

**Z-09, drugi akapit — „to część tej samej roboty, nie osobne zlecenie"**
To jest **obietnica cenowa złożona za klienta.** Czyta się jako „obróbki ościeży nie doliczamy".
Nie wiem, czy jej nie doliczają, a dotrzymać jej musiałby on. To dokładnie błąd z PEC STAL
(dopisany „bezpłatny pomiar" przy miastach 30-40 km stąd).
→ zastąpione czystym opisem zakresu: `Po montażu zostaje obróbka ościeży i wykończenie ściany wokół futryny.`

## 🔧 POPRAWIONE

**Z-03** — „Cztery roboty (...) - i montaż drzwi i okien do kompletu" ma dwa „i" w jednym członie.
→ `Cztery roboty, na których stoi większość naszych budów. Montaż drzwi i okien robimy do kompletu.`

**Z-04** — moja propozycja („Drzwi wewnętrzne i zewnętrzne, okna - z obróbką ościeży po montażu")
była **znak w znak listą `spec` z `co-robimy` 05.** Redakcja, która wycina powtórzenia, właśnie
tworzyła nowe.
→ `Wstawiamy, gdy ściany są gotowe - z obróbką ościeży.`

**Z-05** — dwa błędy. (1) Etykieta „Z naszej budowy" i podpis „prosto z budowy" - słowo „budowa"
dwa razy w jednym bloku. (2) 🔴 Poważniejszy: usuwając duplikat opisu agregatu, zdejmowałem
ze **strony głównej** jedyne wyjaśnienie, po co ten agregat - a strona główna jest oglądana
najczęściej. Wyjaśnienie zostaje na `co-robimy 02`, ale przycisk pod filmem prowadził
do **realizacji**, nie do niego.
→ etykieta: `Kadr z roboty` · podpis bez zmian · **przycisk `Zobacz realizacje` → `Zobacz, jak malujemy`, href na `co-robimy.html#u-02`**.
(To jedyna zmiana nawigacji w całej redakcji i jest tu po to, żeby argument nie zniknął, tylko się przeniósł.)

**Z-07** — „Zacznijmy od obejrzenia" powtarzało zdanie stojące pod nim („Umawiamy się na miejscu,
oglądamy zakres").
→ `Zacznijmy od telefonu`

**Z-08** — „zależy od zakresu, a zakres widać dopiero na miejscu" - „zakres" dwa razy w jednym zdaniu.
→ `Ceny nie podajemy z góry - zależy od zakresu i od tego, co zastaniemy na ścianie.`

**Z-11** — 🔴 **najpoważniejszy błąd tej redakcji, wyłapany dopiero tutaj.** Wycinałem
z `index` zdanie o zdjęciach z internetu (Z-01) **i jednocześnie** z leadu realizacji zdanie
„Wszystkie zdjęcia na tej stronie są z naszych budów" - z argumentem rzekomo „przeniesionym
na realizacje". Po obu zmianach argument nie stałby **nigdzie**: zostawał sam H1 „Nasze budowy,
nasze zdjęcia", który dla człowieka nieświadomego, że konkurencja wstawia stock, brzmi
jak oczywistość.
→ lead realizacji **nazywa rzecz mocniej niż oryginał**:
`Wszystkie z naszych budów - żadnego kupionego w banku zdjęć. Na gotowej łazience nie widać już, jak wyprowadzono podejścia wodne ani co siedzi pod płytką, więc obok skończonych wnętrz pokazujemy kadry z samej roboty, podpisane „w trakcie”.`

**Z-13 + Z-14** — po obu zmianach **obszar działania znikał z całej treści `o-nas`** (zostawał
tylko w stopce). To podstrona, na której człowiek sprawdza „czy to firma dla mnie", a zasięg
jest pierwszym kryterium.
→ punkt „Dziś" zatrzymuje obszar: `Wykończenia wnętrz pod klucz, od gładzi po montaż drzwi - w wielkopolskiem i lubuskiem.`

**Z-19** — „stąd wyjeżdżamy na budowy w wielkopolskiem i lubuskiem" byłoby **trzecim** wystąpieniem
obszaru na `kontakt.html` (karta danych, ten akapit, domknięcie).
→ `Błońsko leży pod Rakoniewicami, w powiecie grodziskim - stąd wyjeżdżamy na budowy. Mapa włącza się dopiero po kliknięciu.`

## ✅ BEZ ZASTRZEŻEŃ

**Z-01** (po naprawie Z-11 argument wraca wzmocniony) · **Z-02** · **Z-06** (usuwane dane stoją
na tej stronie trzy razy wyżej; sekcja kończy się teraz puentą, nie adresem) · **Z-10** ·
**Z-12a/b** · **Z-15** · **Z-16** · **Z-17** · **Z-18**.

**Z-18 — sprawdzone osobno, bo usuwa obietnicę klienta.** „do 5 dni roboczych" znika z domknięcia
`o-nas`, ale zostaje w trzech miejscach: ramka pod H1 na stronie głównej, domknięcie realizacji
i krok 3 na `kontakt`. Główny wyróżnik firmy nadal pada **na trzech z pięciu podstron**,
w tym na pierwszym ekranie. To nie jest usunięcie argumentu, tylko zdjęcie jego szóstej kopii.

## Kontrola z listy błędów Stryszyka

| błąd | czy wystąpił tu |
|---|---|
| wycięcie tekstu klienta | **nie** - żaden fakt z checklisty Adama nie znika; sprawdzone po kolei w etapie 5 |
| argument sprzedażowy → techniczny | **omal** (Z-05) - złapane, naprawione przyciskiem do opisu usługi |
| skrócenie kosztem argumentów | **tak** (Z-11) - złapane, lead wychodzi mocniejszy niż był |
| pominięty trade-off biznesowy | **nie** |
| marka/fraza wyrzucona z nagłówka | **nie** - H1 nietknięte na wszystkich pięciu podstronach |
| własny błąd, wcześniej wytykany | **tak** (Z-04) - tworzyłem nowe powtórzenie, wycinając stare |
| **obietnica za klienta** | **tak** (Z-09) - ⛔ wycofane w całości |
