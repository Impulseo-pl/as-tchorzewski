# Kandydat A — „Obietnica"

**Fundament:** [Trust & Authority](https://designmd.app/library/trust-authority) · biblioteka `DESIGN.md` (designmd.app)
**Makieta:** `kierunki/kierunek-A-obietnica.html`
**Dla kogo gra:** ktoś dostał nazwisko z polecenia i sprawdza w Google, czy firma jest prawdziwa.
Ma znaleźć w pierwszych trzech sekundach cztery konkrety, z których da się firmę rozliczyć.

## Dlaczego ten fundament dla TEJ firmy

Filozofia szablonu: **„sygnały zaufania są treścią, nie ozdobą" — obietnice stoją w miejscu decyzji,
nie w stopce.** Nasz jedyny wyróżnik jest właśnie obietnicą z liczbą („wycena do 5 dni roboczych"),
a nasz odbiorca przychodzi ze strachem: 76,1% Polaków miało problemy z fachowcami, najczęściej
z jakością wymagającą poprawek i z opóźnieniami. Ten szablon jest zbudowany dokładnie pod taką sytuację.

⭐ **Największa zaleta praktyczna:** to jedyny z trzech kierunków, który **nie zależy od tego,
ile zdjęć przyśle klient.** Stoi na typografii i obietnicach; jedno dobre zdjęcie wystarcza.

## Tokeny oryginału

| co | wartość |
|---|---|
| kolory | `#1A1A1A` tekst · `#4A4A4A` drugi plan · `#0066FF` akcent · `#1E40AF` odznaki · `#059669` weryfikacja · `#F59E0B` liczby · `#FFFFFF` powierzchnia |
| ograniczenie palety | zero czystej czerni; nasycenie max 80% |
| typografia | Hero `clamp(2.5rem,5vw,4rem)/700` · H1 2,25rem · H2 1,5rem · tekst 1rem/1.6, max 72ch · etykiety 0,875rem/500 |
| siatka | CSS Grid, max 1280px, padding 1,5rem · hero split (tekst lewo, wizual prawo) · sekcje zygzakiem |
| odstępy | jednostka 8px · przerwy sekcji `clamp(4rem,8vw,8rem)` |
| zaokrąglenia | 8px |
| cienie | karta `0 2px 12px rgba(0,0,0,.06)` |
| ruch | wejście fade + translateY 16px→0 przez 480 ms, kaskada 100 ms · hover scale(1.03) + cień 200 ms · tylko `transform` i `opacity` |
| komponenty | przycisk główny: wypełnienie akcentem, waga 600, hover ciemniej o 8%, active −1px · przycisk drugi: obrys 1,5px · input: etykieta nad polem, focus ring 2px offset 2px |

## Do's oryginału (lista kontrolna przed pokazaniem)

odznaki zaufania widoczne · certyfikaty z linkiem weryfikującym · liczby ze źródłem · profesjonalne zdjęcia ·
**gwarancja napisana wprost** · kontakt dostępny wszędzie · ikony wyłącznie SVG (Lucide/Heroicons) ·
sygnały weryfikowalne zamiast dekoracyjnych

## Don'ts oryginału

zero emoji w interfejsie · zero czystej czerni `#000000` · zero przesyconych kolorów ·
**zero trzech równych kolumn** · zero `h-screen` (używać `min-h-[100dvh]`) ·
zero klisz „Elevate / Seamless / Unleash / Next-Gen" · zero martwych linków do obrazów · zero lorem ipsum

## ⚠️ Odstępstwa — co odrzucamy i dlaczego

1. **🔴 „System UI" jako krój — ODRZUCONE.** To jest dokładnie ten błąd, za który dostaliśmy zwrot.
   Zamiast tego: **Archivo** (nagłówki, 600) + **Inter** (tekst). Oba mają pełne polskie znaki.
   Archivo ma szeroki, geometryczny rysunek — ten sam charakter, co wordmark w nowym logo klienta.
2. **Cała paleta zaufania (niebieski `#0066FF`, granat `#1E40AF`, zieleń `#059669`, bursztyn `#F59E0B`) —
   ODRZUCONA.** To paleta bankowo-medyczna. Bierzemy **jeden akcent z jego własnego logo:
   `#C25A14`** (przygaszona wersja pomarańczu ze znaku). Zieleń zostaje wyłącznie jako kropka
   „odbieramy teraz" przy numerze i jako tło przycisku WhatsApp — tam jest znaczeniowa, nie dekoracyjna.
3. **Tło:** oryginał daje `#FFFFFF`. Dajemy ciepłą złamaną biel `#F6F5F2` + `#EDEBE6` na pas obietnic.
   Czysta biel przy zdjęciach z budowy wygląda szpitalnie.
4. **„Odznaki zaufania" i „certyfikaty" — POMIJAMY.** Klient nie ma żadnych papierów ani autoryzacji
   producenckich (sprawdzone). ⛔ Nie budujemy pustej sekcji „certyfikaty" — to błąd, który
   widzieliśmy u konkurencji (PK FLIZ: sekcja opinii bez opinii).
5. **Cztery kafle obietnic zamiast trzech** — szablon zakazuje trzech równych kolumn, więc układ
   4-kolumnowy jest zgodny; przy tym czwarta obietnica („odbieramy 8–20") jest realna i darmowa.
6. **Logo:** nowy znak jest biały, więc na jasnym tle idzie w wersji przemalowanej na `#111114`
   (plik `materialy/logo/logo-nowe-na-jasne-tlo.png`). ⚠️ Przemalowanie znaku wymaga zgody klienta —
   pytanie nr 2 na liście do Adama.

## Ryzyko

Bez potwierdzenia „wyceny do 5 dni" jako publicznej obietnicy (pytanie 4 do klienta) **ten kierunek
traci swoje serce** i staje się zwykłą stroną z kaflami. To jedyny kierunek, który tak mocno stoi
na jednej odpowiedzi klienta.
