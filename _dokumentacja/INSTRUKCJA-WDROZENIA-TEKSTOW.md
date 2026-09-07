# INSTRUKCJA WDROŻENIA TEKSTÓW — A.S TCHÓRZEWSKI

> 07.09.2026, blok D, etap 6. **Wdrożone i przebudowane** - ten dokument jest zapisem tego,
> co zostało zmienione, a nie listą do zrobienia.
> ⛔ Edytuje się **`pages.py`** (źródło), nie generowane `.html`.
> Cofnięcie całości: `git reset --hard przed-tekstami`
> Rozumowanie i autorewizja: `AUDYT-TEKSTOW.md` w tym katalogu.

**Wynik:** 25 zamian w 5 podstronach · treść -190 znaków (-2,2 %) · bramka języka 0 błędów ·
bramki statyczne czyste. **Żaden fakt podyktowany przez klienta nie zniknął** - zniknęły
trzecie i czwarte powtórzenia sześciu argumentów.

---

## `index.html`

### Z-02 — sekcja „Przed i po", nagłówek H2

**STARE**
```
Ta sama bryła. Dwa zdjęcia.
```

**NOWE**
```
Ten sam dom. Dwa zdjęcia.
```

### Z-01 — sekcja „Przed i po", podpis pod nagłówkiem

**STARE**
```
Zdjęcia z budowy trudno wziąć z internetu - dlatego pokazujemy stan surowy obok tego, co po sobie zostawiliśmy.
```

**NOWE**
```
Przed rozbudową i po niej. Na gotowym zdjęciu nie widać już, od czego się zaczynało.
```

### Z-03 — sekcja „Zakres", podpis pod nagłówkiem

**STARE**
```
Kolejność nie jest przypadkowa - tak wygląda robota, którą bierzemy najczęściej.
```

**NOWE**
```
Cztery roboty, na których stoi większość naszych budów. Montaż drzwi i okien robimy do kompletu.
```

### Z-04 — kafel „Montaż drzwi i okien", opis

**STARE**
```
Robimy przy okazji wykończenia, razem z obróbką po montażu.
```

**NOWE**
```
Wstawiamy, gdy ściany są gotowe - z obróbką ościeży.
```

### Z-05a — sekcja z filmem, etykieta

**STARE**
```
Nasza robota, nie zdjęcie z internetu
```

**NOWE**
```
Kadr z roboty
```

### Z-05b — sekcja z filmem, podpis

**STARE**
```
Na filmie malujemy agregatem natryskowym. Bierzemy go tam, gdzie powierzchnia jest duża, a powłoka ma być równa - bez śladów po wałku.
```

**NOWE**
```
Malowanie agregatem - trzydzieści siedem sekund prosto z budowy, bez montażu i bez komentarza.
```

### Z-05c — sekcja z filmem, przycisk i jego adres

**STARE**
```
Drugi film, z roboty przy elewacji, stoi na stronie z realizacjami.
<a class="duch" href="realizacje.html">Zobacz realizacje</a>
```

**NOWE**
```
<a class="duch" href="co-robimy.html#u-02">Zobacz, jak malujemy</a>
```

### Z-06 — sekcja „Uczciwie", drugi akapit

**STARE**
```
Pracujemy w wielkopolskiem i lubuskiem, telefon odbieramy od 8:00 do 20:00.
```

**NOWE**
```

```

→ *akapit usunięty bez zastąpienia.*

### Z-07 — domknięcie strony, nagłówek H2

**STARE**
```
Wycena po oględzinach - do 5 dni roboczych
```

**NOWE**
```
Zacznijmy od telefonu
```

## `co-robimy.html`

### Z-08 — otwarcie podstrony, lead

**STARE**
```
Robimy to, na czym się znamy - a przy robocie, której nie bierzemy, polecamy sprawdzone osoby. Cena zależy od zakresu i stanu wnętrza, dlatego wyceniamy po oględzinach na miejscu.
```

**NOWE**
```
Pięć robót, które bierzemy najczęściej - i to, co przy każdej z nich decyduje o efekcie. Ceny nie podajemy z góry - zależy od zakresu i od tego, co zastaniemy na ścianie.
```

### Z-09 — blok 05 „Montaż drzwi i okien", treść

**STARE**
```
Montujemy drzwi i okna najczęściej przy okazji wykończenia wnętrza - razem z obróbką ościeży i wykończeniem ściany po montażu.
```

**NOWE**
```
Drzwi i okna montujemy zwykle na końcu wykończenia - wtedy, gdy ściany są już gotowe i wiadomo, w co się wstawia.
Po montażu zostaje obróbka ościeży i wykończenie ściany wokół futryny.
```

### Z-10 — blok 04 „Sucha zabudowa", drugi akapit

**STARE**
```
Zabudowę prowadzimy tak, żeby od razu szła pod gładź - to ta sama ekipa, więc nikt nie zrzuca winy za nierówności na poprzednika.
```

**NOWE**
```
Zabudowę prowadzimy tak, żeby od razu szła pod gładź: równe płaszczyzny, wyprowadzone narożniki, taśmowanie na łączeniach.
```

## `realizacje.html`

### Z-11 — otwarcie podstrony, lead

**STARE**
```
Wszystkie zdjęcia na tej stronie są z naszych budów. Część kadrów jest „w trakcie” i tak je podpisujemy - pokazują to, czego na gotowym zdjęciu już nie widać.
```

**NOWE**
```
Wszystkie z naszych budów - żadnego kupionego w banku zdjęć. Na gotowej łazience nie widać już, jak wyprowadzono podejścia wodne ani co siedzi pod płytką, więc obok skończonych wnętrz pokazujemy kadry z samej roboty, podpisane „w trakcie”.
```

### Z-12a — sekcja „Filmy z budowy", nagłówek H2

**STARE**
```
Dwie minuty roboty
```

**NOWE**
```
Minuta i szesnaście sekund roboty
```

### Z-12b — sekcja „Filmy z budowy", podpis

**STARE**
```
Oba filmy są bez dźwięku i ruszają dopiero po kliknięciu - nie zjadają transferu na telefonie.
```

**NOWE**
```
Oba z budowy, oba bez dźwięku - ruszają dopiero, gdy je włączysz.
```

## `o-nas.html`

### Z-13 — otwarcie podstrony, lead

**STARE**
```
Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku pod własnym szyldem w Polsce. Pracujemy w wielkopolskiem i lubuskiem.
```

**NOWE**
```
Na budowach jesteśmy od ponad 20 lat - najpierw w Niemczech, od 2015 roku pod własnym szyldem w Polsce. Pracujemy w wielkopolskiem i lubuskiem.
```

### Z-14 — oś lat, punkt „Dziś"

**STARE**
```
Wykończenia wnętrz w wielkopolskiem i lubuskiem. Telefon odbieramy od 8:00 do 20:00.
```

**NOWE**
```
Wykończenia wnętrz pod klucz - od gładzi i malowania po łazienki, poddasza i montaż drzwi.
```

### Z-15a — nagłówek H3

**STARE**
```
<h3>Firma rodzinna</h3>
```

**NOWE**
```
<h3>Co znaczy „rodzinna”</h3>
```

### Z-15b — akapit pod H3

**STARE**
```
Jesteśmy firmą rodzinną. To znaczy tyle, że nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze.
```

**NOWE**
```
Tyle, że nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze.
```

### Z-16a — nagłówek H3

**STARE**
```
Robota, która sama się sprawdza
```

**NOWE**
```
Po wyschnięciu widać wszystko
```

### Z-16b — akapit pod H3

**STARE**
```
Gładź, płytka wielkoformatowa i skos poddasza mają tę wspólną cechę, że po wyschnięciu widać każdą drogę na skróty. Dlatego u nas zabudowa, gładzie i malowanie idą jedną ręką - nie ma komu zrzucić winy za nierówną ścianę.
```

**NOWE**
```
Gładź, płytka wielkoformatowa i skos poddasza mają jedną wspólną cechę: efekt widać dopiero wtedy, gdy jest za późno na poprawki. Dlatego zabudowa, gładzie i malowanie idą u nas jedną ręką - nie ma komu zrzucić winy za nierówną ścianę.
```

### Z-17 — sekcja z filmem, podpis

**STARE**
```
Film z budowy przy elewacji. Bez pozowania i bez lektora - po prostu tak wygląda dzień na rusztowaniu.
```

**NOWE**
```
Film z budowy przy elewacji. Nikt tu nie pozuje - tak po prostu wygląda dzień na rusztowaniu.
```

### Z-18a — domknięcie, nagłówek H2

**STARE**
```
Poznajmy się przy wycenie
```

**NOWE**
```
Teraz wiesz, kto przyjedzie
```

### Z-18b — domknięcie, zdanie

**STARE**
```
Zadzwoń - umawiamy oględziny na miejscu i wracamy z wyceną do 5 dni roboczych.
```

**NOWE**
```
Zadzwoń albo napisz - umawiamy oględziny na miejscu.
```

## `kontakt.html`

### Z-19 — sekcja mapy, podpis pod nagłówkiem

**STARE**
```
Mapa łączy się z Google dopiero wtedy, gdy ją włączysz - do tego czasu ta strona nie wysyła o tobie nigdzie ani jednej informacji.
```

**NOWE**
```
Błońsko leży pod Rakoniewicami, w powiecie grodziskim - stąd wyjeżdżamy na budowy. Mapa włącza się dopiero po kliknięciu.
```

---

## Czego świadomie NIE zmieniono

- **Wszystkie H1** na pięciu podstronach - nietknięte.
- **Karta danych, „Trzy kroki do ceny", domknięcie „Najszybciej - telefonem"** na `kontakt.html`.
- ⭐ **„Na WhatsAppie możesz od razu wrzucić zdjęcia wnętrza"** - najlepsze zdanie w serwisie;
  celowo NIE przeniesione na stronę główną, bo powstałoby powtórzenie.
- ⭐ **„Nie bierzemy każdej roboty. Za to wiemy, kto ją zrobi."**, **„Gładź decyduje o tym,
  jak ściana wygląda po pomalowaniu"**, **„Podłogi, stolarkę i grzejniki zaklejamy przed robotą"**,
  **„nazwisko na fakturze i ludzie na budowie to ta sama historia"**, **„Chcesz mieć podobnie
  u siebie?"** - bronione w audycie, zostają znak w znak.
- **Wszystkie podpisy kadrów w galerii** - mówią, co widać, i tak ma zostać.

## ⚠️ Do sprawdzenia przy następnej zmianie

- **Z-12a: „Minuta i szesnaście sekund roboty"** liczy 37 s + 39 s. Zmiana filmów = zmiana nagłówka.
- **Z-19** zostawia miejsce na **pięć miejscowości** z `DO-POTWIERDZENIA.md` #5.
- Karta danych na `kontakt.html` czeka na **wiersz o gwarancji** (`DO-POTWIERDZENIA.md` #1).
