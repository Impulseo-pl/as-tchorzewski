---
name: "A.S TCHÓRZEWSKI"
opis: "Wykończenia wnętrz — Błońsko k. Rakoniewic, wielkopolskie i lubuskie"
fundament: "Apple Premium Cinematic (designmd.app) — kierunek B „Scena”"
wybrany: "2026-09-07 przez Krzysztofa, z poleceniem: BEZ ZAOKRĄGLONYCH RAMEK"
kolory:
  tlo: "#0F0F12"
  tlo_jasne: "#F3F1ED"
  tekst: "#F5F5F7"
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
> pokazuje jedną rzecz naraz.* Wybrane, bo (1) **nowe logo klienta jest białe i żyje na czerni**,
> więc ten szablon je kontynuuje zamiast z nim walczyć, i (2) **wszystkie jego dobre zdjęcia są
> pionowe** — ciemna scena pozwala postawić kadr pionowy bez kadrowania.
> **Makieta źródłowa:** `design/kierunki/kierunek-B-scena.html` · uzasadnienie: `design/kandydat-B-scena.md`

---

## 🔴 Polecenie Krzysztofa, które nadpisuje szablon

> **„Możemy zrobić B, ale bez zaokrąglonych ramek?"** (07.09.2026)

**`border-radius: 0` na WSZYSTKIM.** Przyciski, karty, zdjęcia, etykiety, pola formularza, ramki
sekcji — zero zaokrągleń, bez wyjątków. To unieważnia najbardziej charakterystyczny element
oryginału (pigułki `980px`) i jest świadome: ostra krawędź pasuje do cienkiej, prostej kreski
w jego logo i do branży budowlanej lepiej niż zaokrąglenia Apple'a.

⛔ Jeżeli w trakcie budowy pojawi się gdziekolwiek `border-radius` inny niż `0` — to jest błąd,
nie decyzja. Kontrola: `grep -rn "border-radius" *.css | grep -v ":0"` musi zwrócić pustkę.

---

## Kolory

| Nazwa | Wartość | Zastosowanie |
|---|---|---|
| noc | `#0F0F12` | tło główne · **zmierzone z jego własnego banera**, nie wymyślone |
| noc jaśniejsza | `#17171B` | karty i pola na ciemnym tle, jeśli w ogóle potrzebne |
| dzień | `#F3F1ED` | tło sekcji jasnych (naprzemienność ciemna ↔ jasna) |
| biel | `#F5F5F7` | tekst na ciemnym |
| przygaszony | `#9A9AA2` | tekst drugiego planu na ciemnym |
| atrament | `#1B1B1E` | tekst na sekcjach jasnych |
| przygaszony jasny | `#63636B` | tekst drugiego planu na jasnym |
| **akcent** | `#C85C13` | **jedyny kolor akcentu** — odczytany z pikseli jego logo |
| WhatsApp | `#25A63F` | wyłącznie tło przycisku WhatsApp (znaczeniowe, nie dekoracyjne) |
| linia na ciemnym | `rgba(255,255,255,.16)` | obrysy, ramki, podziały |

⛔ **Jeden akcent i nic więcej.** Zero drugiego koloru „dla ożywienia". Zero gradientów
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
Oba kroje mają pełne polskie znaki. Ładowane z Google Fonts, `display=swap`.

## Układ

- Siatka CSS Grid, `max-width: 1240px`, padding boczny 32px (20px na telefonie).
- Rytm sekcji: `clamp(4rem, 8vw, 8rem)`.
- **Sekcje naprzemiennie: ciemna → jasna → ciemna.** To jest kręgosłup tego szablonu.
- Hero: tekst po lewej, **jeden kadr pionowy po prawej**, w cienkiej ramce odsuniętej o 26px.
- ⛔ **Zero trzech równych kolumn** (zakaz szablonu). Cztery kafle wolno, zygzak wolno.
- ⛔ Zero `h-screen` — `min-h:100dvh`.
- Telefon: **przycisk „Menu"**, nie pasek pozycji + **przyklejony na dole pasek**
  „Zadzwoń 667 434 222" / „WhatsApp".

## Ruch

- Wejście: fade + `translateY(16px → 0)`, 540 ms ease-out, kaskada 120 ms.
- Hover: `scale(1.03)` + delikatny cień, 200 ms.
- **Tylko `transform` i `opacity`.** Żadnych właściwości uruchamiających przeliczanie układu.
- `@media (prefers-reduced-motion: reduce)` wyłącza wszystko.
- ⛔ Zero animowanych liczników. Liczby stoją statycznie (REMPERFEKT ma na żywej stronie
  liczniki pokazujące „0 +" — to jest bramka, nie anegdota).

## Komponenty

- **Przycisk główny:** prostokąt, tło `#C85C13`, tekst biały, waga 500, hover ciemniej o 8%,
  active `translateY(-1px)`. Zero poświat.
- **Przycisk drugi („duch"):** obrys 1,5px `rgba(255,255,255,.22)`, tło przezroczyste.
- **Kafel/karta:** obrys 1px, tło `#17171B`, **krawędź ostra**, cień nie cięższy niż
  `0 2px 8px rgba(0,0,0,.08)`.
- **Pole formularza:** etykieta NAD polem, obrys 1px, focus ring 2px w kolorze akcentu z offsetem 2px,
  błąd pod polem. Zero floating labels.
- **Nawigacja:** tło `rgba(15,15,18,.8)` + `backdrop-filter: saturate(180%) blur(20px)`.

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

## Logo klienta

**Idzie NOWE logo** (monogram A+S, cienka biała kreska + pomarańczowa esica, wordmark
`A.S_TCHORZEWSKI` / `USŁUGI OGÓLNOBUDOWLANE`) — nie stare, rysunkowe z domkami i narzędziami.
To nim firma znakuje własne zdjęcia.

**Czego wolno:** stawiać je na ciemnym tle w oryginalnych kolorach; skalować proporcjonalnie.
**Czego NIE wolno:** przemalowywać, dodawać poświat i cieni, rozciągać, poprawiać `A.S_TCHORZEWSKI`
na `A.S TCHÓRZEWSKI` w samym ZNAKU (w tekstach idzie wersja z „ó" — w znaku nie).

⚠️ **Plik, którego używamy, jest ODZYSKANY z JPG, nie oryginałem od grafika.** W nagłówku będzie
minimalnie miękki. Oryginał (SVG/AI/PDF) zamówiony u klienta — pytanie 2 w `PYTANIA-DO-KLIENTA.md`.
Po jego otrzymaniu **podmienić i skasować odzyskany plik**.

**Przepis do odtworzenia** (gdyby plik zginął):
```
źródło: materialy/logo/baner-fb-z-nowym-logo-1942.jpg  (okładka FB, 1942×809)
wycinek: [89:243, 89:793]
alfa   = clip((max(R,G,B) − 42) / (200 − 42), 0, 1);  alfa < 0.06 → 0
kolor  = piksel / max(alfa, 0.10)      # zdjęcie krycia z przyciemnionej krawędzi
wynik  → materialy/logo/logo-nowe-przezroczyste.png    (704×154, na ciemne tło)
```
Wersja na jasne tło (`logo-nowe-na-jasne-tlo.png`) powstaje z tego samego wycinka przez
przemalowanie pikseli neutralnych na `#111114`. **W tym kierunku nie jest potrzebna** — cały
nagłówek i stopka są ciemne. Trzymamy ją wyłącznie na wypadek jasnych materiałów drukowanych.

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

## Kontrola przed każdym pokazaniem i każdym wypchnięciem

```bash
python3 ~/.claude/skills/bramki/sprawdz.py ~/Developer/impulseo-klienci/as-tchorzewski
grep -rn "border-radius" ~/Developer/impulseo-klienci/as-tchorzewski/*.css | grep -v ":0"   # musi być pusto
```
