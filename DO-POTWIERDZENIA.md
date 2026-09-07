# DO POTWIERDZENIA U KLIENTA — co stoi na stronie, a nie jest jeszcze potwierdzone

> Lista powstała przy budowie (blok C, 07.09.2026). Numery odsyłają do `PYTANIA-DO-KLIENTA.md`.
> ⛔ Dopóki tu coś wisi, `PODGLAD_ROBOCZY = True` w `build.py` (noindex + `robots.txt` zamknięty).
> Każdy punkt ma napisane, **co zrobić z tekstem**, gdy odpowiedź przyjdzie — żeby poprawka
> zajęła minutę, a nie kolejny wieczór.

## 🔴 Blokuje publikację

| # | co stoi na stronie | czego brakuje | co zrobić po odpowiedzi |
|---|---|---|---|
| 3 | **38 zdjęć i 2 filmy z ich IG/FB** — cała strona | pisemnej zgody klienta (czy to ich realizacje, czy właściciele wnętrz się zgadzają) | brak zgody na część kadrów → wyrzucić klucze z `KADRY` w `pages.py` i wpisy z `PLAN` w `przygotuj-media.py` |
| 4 | **„Wycena do 5 dni roboczych od oględzin"** — nagłówek strony głównej, zamknięcie każdej podstrony, `kontakt.html` | czy to ma być publiczna obietnica i od czego liczymy 5 dni | „nie" → wyciąć blok `.obietnica` i zmienić teksty domknięć na „wracamy z wyceną po oględzinach" |
| 4 | ⛔ **nigdzie nie piszemy „bezpłatna wycena"** (demo pisało w 5 miejscach) | czy oględziny są bezpłatne i do ilu km | „bezpłatne" → dopisać jedno zdanie w `kontakt.html`, sekcja „Trzy kroki do ceny" |
| 2 | **logo odzyskane z JPG** (`img/logo.png`, 704×154) | pliku od grafika (SVG/AI/PDF) | podmienić plik, przeliczyć `width`/`height` w `build.py` (nagłówek i stopka) |

## 🟡 Trzeba poprawić, ale nie blokuje

| # | co stoi na stronie | czego brakuje | co zrobić po odpowiedzi |
|---|---|---|---|
| 9 | adres **Błońsko 46, 64-308 Błońsko** | ✅ potwierdzony 07.09.2026 na białej liście VAT (NIP 9950044465, REGON 363138510, `registrationLegalDate` 2015-12-02, adres `BŁOŃSKO 46, 64-308 BŁOŃSKO`). Zostaje pytanie, czy listy dochodzą pod tym kodem, czy pod „Jabłonna” | poczta wymaga Jabłonny: popraw `MIASTO` w `build.py` |
| 9 | e-mail **a.s-tchorzewski@wp.pl** | który z trzech zapisów jest prawdziwy | podmienić w `build.py` (`MAIL`), `pages.py` (kontakt, polityka) |
| 8 | godziny **8:00–20:00** | których dni dotyczą (wizytówka Google mówi 18:00) | dopisać dni; dopiero wtedy wolno wpisać godziny do danych strukturalnych w `build.py` |
| 5 | obszar opisany jako **„wielkopolskie i lubuskie"** | pięciu najczęstszych miejscowości | dopisać miasta do tekstów i do `areaServed` — bez tego strona nie pokaże się w wyszukiwaniach lokalnych |
| 6 | zakres: szpachlowanie, malowanie, łazienki, sucha zabudowa + drzwi i okna; **elewacje, podbitka, beton architektoniczny i schody** opisane jako „mamy na koncie", nie jako oferta | czy elewacje mają być pełnoprawną usługą | „tak" → osobny blok `U-06` w `co-robimy.html` |
| 1 | ⛔ **o gwarancji nie ma na stronie ani słowa** | ile lat i na co | dopisać jeden wiersz w karcie danych na `kontakt.html` + zdanie w `o-nas.html` |
| 7 | ⛔ **nie ma sekcji opinii** (mamy 0 zgód na przepisanie) | zgody na przepisanie 3 opinii z Google | dopiero wtedy sekcja opinii + ewentualnie plakietka Google (jest w rdzeniu) |
| 10 | ⛔ **nie ma plakietki „opinie w Google"** | potwierdzenia, że wizytówka z 6 opiniami to ICH wizytówka (pod tym samym adresem jest druga firma o tym nazwisku) | potwierdzone → wkleić plakietkę wg wzoru ze `SKILL.md` (przy 6 opiniach: ocena i gwiazdki, bez liczby osób) |
| 11 | nigdzie nie podajemy **liczby osób w ekipie** | ilu ich jest | jedna prawdziwa liczba wchodzi do `o-nas.html` |

## ✅ Świadome decyzje budowy (nie pytania - do wiadomości)

- 🔴 **Firma mówi o sobie w liczbie MNOGIEJ („robimy”), do czytelnika mówimy
  w liczbie POJEDYNCZEJ („zadzwoń”).** Polecenie klienta dotyczyło tego, jak firma mówi
  o sobie. „Zadzwońcie” brzmi, jakby strona zwracała się do kilku osób naraz, a bramka
  języka takie zwroty blokuje. Gdyby klient chciał inaczej - zmiana siedzi w `pages.py`,
  w kilku zdaniach.
- ✅ **Rok 2015 potwierdzony w rejestrze**, wpisany do `.deklaracje-potwierdzone`.

- **Bez formularza kontaktowego.** Klient sprzedaje przez telefon i WhatsAppa; formularz
  wymagałby zaplecza i zgód RODO, a nie przyniósłby ani jednego telefonu więcej.
- **Bez kurtyny powitalnej** (jest u Meble FRONT i PEC STAL). Tutaj bohaterem jest pierwszy
  kadr, a nie logo odzyskane z JPG-a — kurtyna pokazałaby na pełnym ekranie właśnie ten
  miękki plik. Wrócić do tematu, gdy przyjdzie wektor.
- **Filmy bez dźwięku** i ładowane dopiero po kliknięciu.
- **Mapa Google dopiero po kliknięciu** → strona nie potrzebuje banera cookies.
