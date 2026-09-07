# Kandydat C — „Redakcja"

**Fundament:** [Editorial Contemporâneo](https://designmd.app/library/editorial-contemporaneo) · biblioteka `DESIGN.md`
**Makieta:** `kierunki/kierunek-C-redakcja.html`
**Dla kogo gra:** ktoś, kto czyta, zanim zadzwoni — buduje dom, ma budżet i chce wiedzieć,
z kim ma do czynienia. Strona czyta się jak rozkładówka, a nie jak wizytówka.

## Dlaczego ten fundament dla TEJ firmy

Filozofia szablonu: **„sam układ niesie opinię, a hierarchia typograficzna przejmuje pracę,
którą w druku monopolizowało kierowanie artystyczne".**

To jedyny z trzech kierunków, który potrafi **opowiedzieć historię firmy rodzinnej z dwiema datami**
(2005 Niemcy → 2015 Polska) i przy okazji rozwiązać dwa nasze realne problemy:

1. ⭐ **Indeks realizacji zamiast galerii.** Cztery–sześć robót z nazwą, miejscem i zakresem bije
   trzydzieści anonimowych fotek w siatce — a przy okazji **każda pozycja potrzebuje tylko małego
   zdjęcia (210×132)**, więc materiał z Instagrama w 1200 px jest tu w zupełności wystarczający.
   To najbezpieczniejszy kierunek pod kątem jakości zdjęć.
2. ⭐ **Pasek faktów** (5 dni · gwarancja · 2005→2015 · 8–20) daje miejsce na liczby, o które
   dopytujemy klienta — i widać w nim od razu, której liczby jeszcze nie ma.

## Tokeny oryginału

| co | wartość |
|---|---|
| kolory pierwsze | `#FFFFFF` · `#000000` · `#800000` wino · `#333333` szarość |
| kolory wtórne | `#FFD700` złoto · `#000080` granat · `#2ECC40` szmaragd · `#F5F5DC` beż |
| typografia | Playfair Display: tytuły 700 (2,25–4rem), tekst 400 1rem/1.6 max 72ch, etykiety 0,875rem/500 · JetBrains Mono na kod |
| siatka | CSS Grid, max 1280px, padding 1,5rem · **hero asymetryczny** · sekcje o różnych rozmiarach kart · zero trzech równych kolumn |
| odstępy | jednostka 8px · przerwy sekcji `clamp(4rem,8vw,8rem)` |
| zaokrąglenia | 8px |
| cienie | `0 2px 12px rgba(0,0,0,.06)` + obrys 1px |
| ruch | ease-out 200–300 ms · wejście fade + translateY 16px→0 przez 420 ms, kaskada 80 ms · przejścia stron tylko fade 200 ms |

## Do's oryginału

kontrastująca typografia · kompozycja warstwowa obraz + tekst · nacisk na jakość materiału wizualnego ·
elementy dekoracyjne (linie, ramki) · mikrointerakcje przy artykułach

## Don'ts oryginału

zero emoji · **zero czystej czerni — charcoal zamiast** · nasycenie max 80% ·
**zero trzech równych kolumn — zygzak albo asymetria** · zero `h-screen` · zero klisz AI ·
zero martwych linków do obrazów

## ⚠️ Odstępstwa — co odrzucamy i dlaczego

1. **🔴 Playfair Display jako krój TEKSTU — ODRZUCONE.** Szablon sam sobie tu szkodzi: Playfair to
   szeryf displayowy o wysokim kontraście kresek, w rozmiarze 16 px na telefonie robi się nieczytelny.
   Bierzemy **Fraunces** na nagłówki (szeryf o miękkim, rzemieślniczym rysunku, pełne polskie znaki)
   i **Inter** na cały tekst.
2. **🔴 Sprzeczność w oryginale: paleta podaje `#000000`, a „don'ts" zakazuje czystej czerni.**
   Rozstrzygamy na korzyść „don'ts" — atrament `#23211D` (ciepły węgiel), tło `#F3F0E9` (papier).
3. **🔴 Złoto `#FFD700`, granat `#000080`, szmaragd `#2ECC40`, wino `#800000` — ODRZUCONE w całości.**
   Nasycone złoto i granat na stronie firmy wykończeniowej to kostium. Jeden akcent: **`#A8451A`** —
   przyciemniona wersja pomarańczu z jego logo, tak żeby trzymała kontrast na papierowym tle.
4. **„Przewracanie strony" jako efekt przejścia — ODRZUCONE.** Ozdobnik, który kosztuje czas ładowania
   i na telefonie wygląda jak błąd. Zostają fade + translateY z tokenów.
5. **Ramki i linie dekoracyjne — BIERZEMY, ale cienkie (1px `#D6D0C2`) i tylko jako podział treści.**
   ⛔ Zero grubych czarnych ramek — to nasza własna reguła po demie HG Group.
6. **Logo:** tak jak w kierunku A, znak idzie w wersji przemalowanej na ciemny (`logo-nowe-na-jasne-tlo.png`).

## Ryzyko

⚠️ Szeryf + papier czyta się jako „firma z historią". **Historii nie mamy jeszcze potwierdzonej** —
nie wiemy, kto tworzy „A.S", ile osób liczy ekipa i co dokładnie robili w Niemczech (pytania 11 i 14).
Jeśli klient nie da tych odpowiedzi, ten kierunek będzie ładnym opakowaniem bez zawartości.
