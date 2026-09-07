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

## 🆕 CO PRZYSZŁO OD ADAMA 07.09.2026 20:16 (WhatsApp) - i co z tego wynika

| co | stan |
|---|---|
| **logo** | ✅ **ROZSTRZYGNIĘTE 07.09 21:05 - klient potwierdził Adamowi, że aktualne jest STARE logo** (domki, młotek, kielnia), a nie monogram A+S z banera FB. ⛔ To NIE jest podmiana pliku: stare logo ma CZARNY napis i czarne wieżowce, więc na tle `#0F0F12` znika. Cały ciemny kierunek „Scena" wybraliśmy dlatego, że biały monogram żył na czerni. **Rozwidlenie do decyzji K. - opisane w `DESIGN.md`.** Plik mamy u siebie, czysty i przezroczysty: `materialy/logo/logo-stare-przezroczyste.png` (1018×753) - lepszy niż ten z WhatsAppa, Adam nic nie musi dosyłać |
| **„Darmowa wycena"** | ✅ stoi w opisie **ich własnego Facebooka**. Zdejmuje mój blok na to zdanie (bałem się go, bo klient go nie wypowiedział). ⏳ Zostaje tylko zakres: do ilu km oględziny są darmowe |
| **adres** | ✅ **ROZSTRZYGNIĘTE BEZ KLIENTA.** `64-308` to poczta **Jabłonna**, obejmująca m.in. Błońsko. Poprawnie: **`Błońsko 46, 64-308 Jabłonna`** - wpisane w `build.py`, kartę danych, politykę i dane strukturalne. ⛔ Nasze poprzednie „64-308 Błońsko" było błędne |
| **„20 lat doświadczenia"** | ✅ zgodne z tym, co mówił klient („ponad 20 lat"). Na FB jest też 🇩🇪🇵🇱 - potwierdza wątek niemiecki |
| ich hasła z FB | „Budujemy jakość na lata" · „Zawsze na czas" · „Nowoczesny sprzęt" - **ich własne słowa**, więc wolno ich użyć. ⚠️ Ale to są dokładnie te ogólniki, których unikamy; „Zawsze na czas" warto zamienić na nasze twarde „wycena do 5 dni roboczych" |
| **Instagram** | 🔴 profil ma teraz **9 postów**, a my ściągnęliśmy materiał z **8**. Sprawdzić, czy doszedł nowy - zdjęcia są dziś wąskim gardłem |
| zasięgi | FB 86 polubień, IG 54 obserwujących - ⛔ za mało, żeby to gdziekolwiek pokazywać |

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
