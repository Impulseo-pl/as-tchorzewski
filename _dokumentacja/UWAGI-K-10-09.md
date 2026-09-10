# Uwagi Krzysztofa z 10.09.2026 — co było, na co poprawione, dlaczego

Runda po obejrzeniu podglądu na `localhost:8765`. Wszystko wdrożone i zbudowane,
commit `03e2666`. Rdzeń stron docelowych podbity do wersji 12 (commit `bd22dfd`
w repo skilli) — suwak i karuzela są od teraz dostępne u każdego następnego klienta.

## Teksty

| # | Uwaga K. | Było | Jest | Dlaczego |
|---|---|---|---|---|
| 1 | „brzmi jakby to zostało nie zrobione" | *Po montażu **zostaje** obróbka ościeży i wykończenie ściany wokół futryny.* | *Po montażu **sami obrabiamy** ościeża i wykańczamy ścianę wokół futryny.* | „Zostaje" czyta się jako robota dla kogoś innego. Linia `spec` pod spodem już wcześniej mówiła „obróbka i wykończenie po montażu", więc zdanie tylko doganiało fakt. ⛔ Świadomie **nie** dopisałem, że to „w cenie" — o zakresie wolno pisać, o cenie nie. |
| 2 | „powtarzasz bez sensu… wogóle ja bym tego nie dawał" | *Czego nie bierzemy - mówimy od razu i polecamy sprawdzone osoby…* (co-robimy) + bliźniacze zdanie na `o-nas` + trzecie na głównej | wycięte we wszystkich trzech miejscach | To samo zdanie stało trzy razy. ⚠️ **Uwaga: to jest zdanie klienta** — brief, „Pytają o usługi, których nie robią → poleca sprawdzone osoby". Wyciąłem na Twoje polecenie, ale klient może o nie zapytać. |
| 3 | „to jest oczywista oczywistość i brzmi wręcz podejrzanie" | H1 *Nasze budowy, nasze zdjęcia* + *Wszystkie z naszych budów - **żadnego kupionego w banku zdjęć***. | H1 *Skończone wnętrza i kadry z budowy*; lead zaczyna się od tego, czego na gotowym zdjęciu nie widać | Zaprzeczanie zarzutowi, którego nikt nie postawił, sam zarzut podsuwa. Nowy nagłówek mówi, **co** jest w galerii, zamiast tłumaczyć, czego nie ma. |
| 4 | „i wszystkie podobne miejsca gdzie sie tłumaczysz" | *Dwa kadry prosto z roboty, **bez montażu i bez pozowania***; podpis filmu *nasza ekipa, **nie zdjęcie z katalogu***; *…i że **nie znikamy po odbiorze*** | *Dwa kadry prosto z roboty.*; *Dzień na rusztowaniu przy elewacji - tynk, obróbki i podbitka.*; zdanie wycięte | Trzy kolejne warianty tej samej wady. Przeszedłem grepem po wszystkich negacjach w tekstach; **zostawiłem** świadomie jedną: *„zabudowa, gładzie i malowanie idą u nas jedną ręką - nie ma komu zrzucić winy za nierówną ścianę"* — to realny argument sprzedażowy, nie tłumaczenie się. |
| 5 | „to wogóle brzmi tragicznie" | **Co znaczy „rodzinna"** — *Tyle, że nazwisko na fakturze i ludzie na budowie to ta sama historia - i że nie znikamy po odbiorze.* | *Że na budowie pracują ci sami ludzie, którzy podpisują fakturę. Firma stoi w Polsce od 2015 roku, a wcześniej przez dziesięć lat robiliśmy to samo na budowach w Niemczech.* + nowy akapit **Co robimy najczęściej** | Nagłówek pytał, akapit nie odpowiadał („to ta sama historia" nic nie znaczy). Nowa wersja odpowiada jednym zdaniem. Dwa akapity faktów doszły też dlatego, że po wycięciach `o-nas` spadła **poniżej progu treści** w bramce (1541 znaków przy progu 1800) — dosypane faktami z briefu, nie watą. |
| 6 | „tu po prostu zadzwoń, telefonem brzmi dziwnie" | **Najszybciej - telefonem** / *Nie odbieramy tylko wtedy, gdy jesteśmy na rusztowaniu - wtedy oddzwaniamy.* | **Zadzwoń** / *Jesteśmy pod telefonem od 8 do 20. Gdy nie odbierzemy, oddzwaniamy.* | Nagłówek domknięcia ma być poleceniem, nie porównaniem sposobów kontaktu. Zdanie pod spodem to był ten sam błąd co wyżej — zaczynało się od tego, czego nie robią. |
| 7 | „co znaczy że wiem kto przyjedzie - nie było żadnego zdjęcia właściciela" | **Teraz wiesz, kto przyjedzie** (domknięcie `o-nas`) | **Reszty dowiesz się przez telefon** | Masz rację — na podstronie nie ma ani jednej twarzy, więc nagłówek obiecywał coś, czego strona nie dowozi. ⏳ Zdjęcie ekipy albo właściciela jest w pytaniach do klienta; jak przyśle, nagłówek może wrócić. |

## Zdjęcia i wygląd

| # | Uwaga K. | Było | Jest | Dlaczego |
|---|---|---|---|---|
| 8 | „te 2 zdjęcia są praktycznie takie same a mają inne opisy" | `beton-02` i `beton-03` — **ta sama ściana** z dwóch ujęć, podpisy *„jasny beton architektoniczny"* i *„ściana dekoracyjna przy skosie"* | drugi kafel zastąpiony ciemną ścianą z czarnymi listwami (`beton-arch-ciemny-01`), podpis *Ciemny beton architektoniczny z czarnymi listwami* | Sprawdziłem materiały: `jasny-02`, `-03` i `-04` to **jedno pomieszczenie z trzech stron**. Dwa różne podpisy na jednej ścianie to wprowadzanie w błąd. Zdjęłem też „W trakcie" z nowego kafla — ta ściana wygląda na skończoną. |
| 9 | „to zdjęcie bym zwiększył wzdłuż, żeby było widać trochę tej wanny" | pas łazienki: 420 px wysokości (klasa `.pas`) | 620 px (`.pas .pas--duzy`) | Przy 420 px w kadr wchodził głównie skos i ściana. Sprawdzone zrzutem przy DPR 2 na trzech pozycjach przewinięcia — wanna jest teraz widoczna w całości. |
| 10 | „na 4 blokach po najechaniu powinien zmienić się kolor bloczka pod spodem, ale żeby całość była dalej bardzo dobrze czytelna" | hover ruszał tylko zdjęcie (powiększenie 1,03) | dolny blok przewraca się na noc `#0F0F12`: nagłówek biel, opis 74 % bieli, „Zobacz →" pomarańcz | Kontrasty policzone, nie na oko: **18,3 · 10,4 · 5,9** przy progu 4,5. Przejście 0,28 s, powiększenie zdjęcia zostało bez zmian. Działa też na `:focus-visible`, czyli z klawiatury. |
| 11 | „mapa dopiero po kliknięciu - rób od razu jak na innych stronach" | zasłona z przyciskiem „Pokaż mapę" (`data-po-kliknieciu`) | zwykły `<iframe>` z mapą, `loading="lazy"`, 440 px wysokości, przybliżenie 15 z pinezką na Błońsku 46 | Tak samo robi to silnik dem (`multipage.py`). ⚠️ Bramka wypisuje przy tym ostrzeżenie „mapa ładuje się od razu" — to Twoja świadoma decyzja, zostawiam. Poprawiłem też **politykę prywatności**, która twierdziła, że przeglądarka nie łączy się z Google — teraz łączy. |
| 12 | „zamiast 2 zdjęć jedno, po najechaniu zajebista animacja, na telefonie po przesunięciu, a pierwsze przesunięcie samo" | dwa kwadraty 1100×1100 obok siebie, podpisy „Przed" i „Po" | **jeden suwak 3:2** na pełnej szerokości sekcji, pliki 1600 px + 2500 px dla Retiny | Trzy wejścia, wszystkie sprawdzone w przeglądarce: **mysz** — styk sam idzie pod kursorem i wraca na środek po zjechaniu; **palec** — ciągnięcie w bok, pionowe przewijanie strony nietknięte; **pierwsze wejście w kadr** — suwak sam raz przejeżdża do „po" i wraca, dokładnie o to prosiłeś. Do tego klawiatura (strzałki) i wyłączenie ruchu przy `prefers-reduced-motion`. |
| 13 | „sekcja z opiniami, znaczek Google i karuzela, bez łącznej liczby opinii" | brak sekcji opinii | sekcja **Co mówią ci, u których byliśmy** przed domknięciem głównej: plakietka Google **5,0** + gwiazdki + „w Google", pod spodem karuzela jadąca sama w kółko, pauza pod kursorem | Opinie przepisane z wizytówki dzisiaj — **zweryfikowałem telefonem 667 434 222**, bo pod tym samym adresem jest druga firma budowlana o tym samym nazwisku (Tadeusz Tchórzewski). Sześć opinii, wszystkie 5★, **treść ma tylko trzy** — te trzy są na stronie. Brak liczby opinii to nie tylko Twoja prośba: tak samo każe standard plakietki ze skilla przy progu poniżej dziesięciu. |

## Odpowiedź na pytanie, nie uwagę

**„Wycena do 5 dni roboczych" — czy klient tak powiedział?**
Tak, to jego słowa. `BRIEF-KLIENTA.md`, sekcja „Twarde dane — GŁOS KLIENTA":

> **Cena:** „trzeba się skontaktować" — wycena **do 5 dni roboczych**, bardzo indywidualna

Źródło: checklista spisana przez **Adama po rozmowie telefonicznej z klientem, 07.09.2026, 11:11**.
Zostaje.

## Czeka na decyzję

1. **Zgoda klienta na opinie z nazwiskami** — pytanie 7 w `PYTANIA-DO-KLIENTA.md`, bez odpowiedzi. Sekcja stoi na publicznych opiniach z jego wizytówki, ale warto to potwierdzić przed oddaniem.
2. **Czerwona zaślepka podejścia wodnego** w kadrze pasa łazienki — zostawić czy przesunąć kadr.
3. **Oryginały zdjęć z telefonu klienta** — te na stronie przyszły przez sociale (1200–1440 px) i są powiększane Upscaylem; elewacja przyszła inną drogą i ma 3072 px.
