[
 {
  "tor": "fakty",
  "dane": {
   "tor": "TOR 1 — FAKTY PEWNE O FIRMIE (Firma Ogólnobudowlana Artur Tchórzewski / „A.S Tchórzewski\", NIP 9950044465)",
   "fakty": [
    {
     "stwierdzenie": "Przedsiębiorca w rejestrze: ARTUR TCHÓRZEWSKI, NIP 9950044465, REGON 363138510.",
     "zrodlo": "API białej listy VAT Ministerstwa Finansów: https://wl-api.mf.gov.pl/api/search/nip/9950044465?date=2026-09-07 (odpowiedź z 07.09.2026, requestId jALWV-98fc6l3)",
     "pewnosc": "potwierdzony",
     "uzycie": "stopka strony, podstrona kontakt, dane do regulaminu/polityki prywatności"
    },
    {
     "stwierdzenie": "Forma prawna: jednoosobowa działalność gospodarcza osoby fizycznej — w białej liście brak numeru KRS, brak wspólników i brak reprezentantów, REGON 9-cyfrowy.",
     "zrodlo": "Biała lista VAT MF, pola krs=null, partners=[], representatives=[] (zapytanie 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "stopka, dokumenty prawne — NIE pisać „firma\" w znaczeniu spółki"
    },
    {
     "stwierdzenie": "Status VAT: podatnik VAT czynny; data rejestracji do VAT 2015-12-02, brak daty wykreślenia ani odmowy rejestracji.",
     "zrodlo": "Biała lista VAT MF (statusVat: „Czynny\", registrationLegalDate: 2015-12-02)",
     "pewnosc": "potwierdzony",
     "uzycie": "nie na stronę — potwierdza „w Polsce od 2015\" z briefu i porządkuje fakturowanie"
    },
    {
     "stwierdzenie": "Adres rejestrowy: Błońsko 46, 64-308 Błońsko. W rejestrze NIE ma zgłoszonego osobnego adresu wykonywania działalności (workingAddress = null).",
     "zrodlo": "Biała lista VAT MF (residenceAddress: „BŁOŃSKO 46, 64-308 BŁOŃSKO\", workingAddress: null)",
     "pewnosc": "potwierdzony",
     "uzycie": "stopka, kontakt, dane strukturalne LocalBusiness/schema.org"
    },
    {
     "stwierdzenie": "„Błońsko 46, 64-308 Błońsko\" (rejestr) i „Błońsko 46, 64-308 Jabłonna\" (faktura, Facebook, Instagram, nasze demo) to TEN SAM adres — Błońsko to wieś w gminie Rakoniewice, powiat grodziski, woj. wielkopolskie, obsługiwana przez pocztę w Jabłonnie (kod 64-308). To nie jest rozbieżność do wyjaśniania.",
     "zrodlo": "Geokodowanie OSM/Nominatim: https://nominatim.openstreetmap.org/search?street=46&city=Błońsko&country=Polska → „46, Błońsko, gmina Rakoniewice, powiat grodziski, województwo wielkopolskie, 64-308\" (52.1885, 16.1348); dodatkowo http://www.rakoniewice.pl/asp/pl_start.asp?typ=14&menu=277&sub=1&subsub=10",
     "pewnosc": "potwierdzony",
     "uzycie": "decyzja, którą wersję adresu wpisać na stronę — rekomendacja: „Błońsko 46, 64-308 Jabłonna\", bo tak jest w wizytówce Google i na socialach (spójność NAP dla SEO lokalnego)"
    },
    {
     "stwierdzenie": "Telefon główny: 667 434 222.",
     "zrodlo": "Wizytówka Google „A.S TCHÓRZEWSKI\" (odczyt karty 07.09.2026, CID 6254345826693595080) + opis strony FB „A.S Tchórzewski\" + brief Adama z 07.09",
     "pewnosc": "potwierdzony",
     "uzycie": "nagłówek, przycisk „Zadzwoń\", stopka, kontakt"
    },
    {
     "stwierdzenie": "WhatsApp: 882 832 244 (inny numer niż główny).",
     "zrodlo": "Opis strony FB „A.S Tchórzewski\": „667 434 222 Whatapp : 882 832 244\" (odczyt 07.09.2026) + brief Adama z 07.09",
     "pewnosc": "potwierdzony",
     "uzycie": "przycisk WhatsApp — musi być opisany osobno, żeby klienci nie dzwonili na WA na numer główny"
    },
    {
     "stwierdzenie": "E-mail: a.s-tchorzewski@wp.pl.",
     "zrodlo": "Facebook, zakładka Informacje: https://www.facebook.com/profile.php?id=61589974670830&sk=about (odczyt 07.09.2026) + brief Adama z 07.09",
     "pewnosc": "potwierdzony",
     "uzycie": "kontakt, adres docelowy formularza"
    },
    {
     "stwierdzenie": "Firma ma wizytówkę Google „A.S TCHÓRZEWSKI\", kategoria „Usługi remontowo-budowlane\", ocena 5,0 z 6 opinii — wszystkie opinie wystawione około miesiąca temu (sierpień 2026).",
     "zrodlo": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/... (FID 0x4b6e291d6c883407:0x56cbe6647684bfc8), odczyt karty 07.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "sekcja opinii — można pokazać „5,0 w Google\" i 2-3 cytaty; ⛔ nie pisać „setki klientów\" ani „lata opinii\""
    },
    {
     "stwierdzenie": "Wizytówka Google należy do nich — jest podlinkowana w bio Instagrama (maps.app.goo.gl/WYxcgp5aDWKc59af9).",
     "zrodlo": "https://www.instagram.com/a.s_tchorzewski/ — bio (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "po oddaniu strony: wpiąć adres as-tchorzewski.pl w pole „Witryna\" wizytówki (dziś puste)"
    },
    {
     "stwierdzenie": "Facebook: strona firmowa „A.S Tchórzewski\", https://www.facebook.com/profile.php?id=61589974670830 — kategoria „Firma budowlana\", 86 obserwujących, 0 opinii, adres Błońsko 46, Jabłonna 64-308.",
     "zrodlo": "https://www.facebook.com/profile.php?id=61589974670830&sk=about (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "ikona FB w stopce; numeryczny ID (61589…) oznacza stronę założoną niedawno — nie chwalić się „społecznością\""
    },
    {
     "stwierdzenie": "Instagram: @a.s_tchorzewski, nazwa „AS Tchorzewski\", kategoria Construction Company, 9 postów, 54 obserwujących; w bio adres Błońsko 46, Jabłonna 64-308.",
     "zrodlo": "https://www.instagram.com/a.s_tchorzewski/ (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "ikona IG w stopce; 9 postów = to cały ich publiczny zapas zdjęć"
    },
    {
     "stwierdzenie": "Konto TikTok pod nickiem @a.s_tchorzewski NIE istnieje („Couldn't find this account\").",
     "zrodlo": "https://www.tiktok.com/@a.s_tchorzewski (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "⛔ nie wstawiać ikony TikToka do stopki"
    },
    {
     "stwierdzenie": "Domena as-tchorzewski.pl zarejestrowana 07.09.2026 o 11:45:08, wygasa 07.09.2027, serwery nazw OVH (dns111.ovh.net / ns111.ovh.net), A rekord na 213.186.33.5 (parking OVH) — pod adresem nic jeszcze nie stoi.",
     "zrodlo": "whois as-tchorzewski.pl + dig (sprawdzone 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "planowanie wdrożenia i przypomnienie o odnowieniu 07.09.2027"
    },
    {
     "stwierdzenie": "Rachunek zgłoszony do białej listy VAT: 97 1090 1388 0000 0001 4437 4728 (jeden, brak rachunków wirtualnych).",
     "zrodlo": "Biała lista VAT MF (accountNumbers), zapytanie 07.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "⛔ NIE na stronę — tylko do naszych rozliczeń/faktur"
    },
    {
     "stwierdzenie": "Firma sama deklaruje na obu profilach identyczny zestaw haseł: „🇩🇪 🇵🇱 20 lat doświadczenia\", „Budujemy jakość na lata\", „Zawsze na czas\", „Nowoczesny sprzęt\", „Darmowa wycena\".",
     "zrodlo": "Bio Instagrama @a.s_tchorzewski + opis strony FB (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "to ICH deklaracje, nie fakty — można ich użyć jako obietnic firmy (z zachowaniem liczby mnogiej), ale nie jako weryfikowalnych danych"
    },
    {
     "stwierdzenie": "Pod tym samym adresem (Błońsko 46) katalogi z danymi CEIDG pokazują drugą działalność: „Firma Ogólnobudowlana Tadeusz Tchórzewski\", NIP 7881441770, data rozpoczęcia 16.08.2016. Ten NIP NIE figuruje w białej liście VAT (odpowiedź: subject = null), więc wpis może być nieaktualny.",
     "zrodlo": "https://aleo.com/pl/firma/firma-ogolnobudowlana-tadeusz-tchorzewski-wolsztyn oraz https://www.gowork.pl/firma-ogolnobudowlana-tadeusz-tchorzewski,26441157/dane-kontaktowe-firmy (obie strony dziś zwracają 404/403 — dane z wyników wyszukiwania 07.09.2026); weryfikacja NIP: biała lista VAT MF, 07.09.2026",
     "pewnosc": "prawdopodobny",
     "uzycie": "nie na stronę — najpewniej wyjaśnia „biznes rodzinny\" i „ponad 20 lat\" z briefu; do potwierdzenia u klienta"
    },
    {
     "stwierdzenie": "Nie znaleziono ŻADNYCH uprawnień, certyfikatów ani autoryzacji producenckich (np. Knauf, Rigips, Caparol, autoryzacja montażu stolarki) przypisanych do firmy.",
     "zrodlo": "Brak trafień w wyszukiwaniach 07.09.2026; w CEIDG/białej liście takich danych się nie publikuje",
     "pewnosc": "niepotwierdzony",
     "uzycie": "⛔ nie budować sekcji „certyfikaty\" — chyba że klient przyśle skany"
    }
   ],
   "luki": [
    "GODZINY PRACY — brief mówi 8–20, a wizytówka Google 07.09.2026 pokazywała „Otwarte · Zamknięcie: 18:00\". Które są prawdziwe i czy sobota/niedziela różnią się od dni roboczych? (Trzeba to ujednolicić na stronie i w wizytówce, inaczej Google karze niespójność.)",
    "ZASIĘG — brief mówi „wielkopolskie i lubuskie\", nasze demo wypisuje konkretne miasta („Wolsztyn, Jabłonna, Zbąszyń, Nowy Tomyśl, Grodzisk Wielkopolski\"), a wizytówka Google ma obszar ustawiony tak szeroko, że pinezka wypada pod Nekłą (pow. wrzesiński). Do jakiego promienia realnie jeżdżą i czy chcą listę konkretnych miast na stronie (to lepiej działa w Google) czy tylko dwa województwa?",
    "WYCENA — na FB i IG piszą „Darmowa wycena\", a w briefie jest „wycena do 5 dni roboczych, bardzo indywidualna, trzeba się skontaktować\". Czy oględziny i wycena są bezpłatne i niezobowiązujące? Można to napisać wprost na stronie?",
    "GWARANCJA — klient obiecał podać długość (07.09 wieczorem). Na ile lat i na co: na robociznę, na materiał, czy na całość? Bez liczby nie stawiamy sekcji o gwarancji.",
    "„PONAD 20 LAT DOŚWIADCZENIA\" i „firma rodzinna\" — polski wpis to grudzień 2015, a pod tym samym adresem widnieje druga działalność (Tadeusz Tchórzewski, od 2016). Kto tworzy „A.S\" w nazwie (Artur i kto?), kto jeszcze pracuje w firmie i od kiedy dokładnie liczymy staż w Niemczech (2005)? To trzeba napisać precyzyjnie, bo inaczej „20 lat\" wygląda na przechwałkę przy firmie zarejestrowanej w 2015.",
    "WIELKOŚĆ EKIPY — ile osób pracuje na budowie? Potrzebne do sformułowań w liczbie mnogiej („nasza ekipa\", „przyjeżdżamy w X osób\") i do sekcji o terminach.",
    "NAZWA NA STRONIE — użyć „A.S Tchórzewski\" (tak jest w Google, na FB i IG) czy pełnego „Firma Ogólnobudowlana Artur Tchórzewski\" (tak brzmi wpis)? W stopce i tak podamy pełne dane rejestrowe.",
    "MONTAŻ DRZWI I OKIEN — brief mówi, że to najmniejszy zarobek. Ma to być osobna podstrona, jeden kafel na stronie usług, czy w ogóle zejść z tym na drugi plan?",
    "POLECANIE SPRAWDZONYCH FACHOWCÓW przy usługach, których nie robią (z briefu) — czy chcą to mieć napisane na stronie jako atut? Jeśli tak, których branż to dotyczy (elektryk, hydraulik, glazurnik)?",
    "ZDJĘCIA — na FB jest ok. 9 zdjęć, na IG 9 postów i to prawdopodobnie ten sam materiał. Czy zdjęcia z ich profili to NA PEWNO ich własne realizacje (a nie fotki z internetu)? Bez pisemnego „tak\" nie wolno ich przenieść na płatną stronę.",
    "WIZYTÓWKA GOOGLE — dostaniemy dostęp (zaproszenie na maila), żeby wpiąć stronę, poprawić godziny i zawęzić obszar działania? Dziś pole „Witryna\" jest puste, a to najtańszy sposób na telefony."
   ],
   "materialy": [
    {
     "co": "Logo firmy — dziś mamy tylko bitmapę ze zdjęcia profilowego",
     "skad": "Zdjęcie profilowe strony FB https://www.facebook.com/profile.php?id=61589974670830 oraz awatar IG @a.s_tchorzewski; już użyte w demie",
     "czy_na_pewno_ich": "TAK — to awatar ich własnej, firmowej strony na Facebooku i Instagramie (obie potwierdzone tym samym numerem 667 434 222 i adresem Błońsko 46). ⚠️ To awatar, nie plik źródłowy — mała rozdzielczość, bez wersji na ciemne tło; klient obiecał plik 07.09 wieczorem"
    },
    {
     "co": "Zdjęcia realizacji — ok. 9 sztuk",
     "skad": "Zakładka Zdjęcia strony FB (9 kafli w siatce) oraz 9 postów na https://www.instagram.com/a.s_tchorzewski/ — prawdopodobnie ten sam materiał publikowany na obu kanałach",
     "czy_na_pewno_ich": "NIE POTWIERDZONE, że to ich własne realizacje. Pewne jest tylko tyle, że opublikowali je na swoich profilach. Przy koncie założonym niedawno (ID strony 61589…, 54–86 obserwujących, 9 postów) ryzyko, że część to zdjęcia z internetu, jest realne — wymaga jednoznacznego potwierdzenia od klienta, zanim trafią na płatną stronę"
    },
    {
     "co": "Galeria z obecnego demo",
     "skad": "https://impulseo-pl.github.io/a-s-tchorzewski/",
     "czy_na_pewno_ich": "NIE — to stock z Pexels, wstawiony przez silnik dem (potwierdza brief Adama, sekcja „Punkt wyjścia\"). ⛔ Nie wolno tego przenieść na stronę docelową"
    },
    {
     "co": "Opinie klientów — 6 sztuk, ocena 5,0",
     "skad": "Wizytówka Google „A.S TCHÓRZEWSKI\" (CID 6254345826693595080); odczytane w całości 3 pierwsze (Kinga Zielonacka, Sylwia Nowicka, Daria Jozwikowska)",
     "czy_na_pewno_ich": "TAK — wizytówka jest ich, bo sami linkują do niej z bio Instagrama (maps.app.goo.gl/WYxcgp5aDWKc59af9). ⚠️ Wszystkie 6 opinii pochodzi z ostatniego miesiąca; na Facebooku opinii jest 0"
    },
    {
     "co": "Dane rejestrowe do stopki i dokumentów prawnych",
     "skad": "API białej listy VAT MF (wl-api.mf.gov.pl), zapytanie 07.09.2026",
     "czy_na_pewno_ich": "TAK — zapytanie po NIP 9950044465 z briefu, odpowiedź: ARTUR TCHÓRZEWSKI, REGON 363138510, Błońsko 46, 64-308 Błońsko, VAT czynny"
    },
    {
     "co": "Domena as-tchorzewski.pl",
     "skad": "whois + dig, 07.09.2026",
     "czy_na_pewno_ich": "Zarejestrowana 07.09.2026 11:45 na koncie Impulseo w OVH (zgodnie z briefem) — abonentem jesteśmy MY, nie klient. Do ustalenia przy oddaniu, kto zostaje abonentem"
    }
   ],
   "uwagi": "DWIE RZECZY DO ŚWIADOMOŚCI, ZANIM KTOŚ POJEDZIE DALEJ:\n\n1) Czego NIE udało się dociągnąć u źródła. Wpis CEIDG (pełna nazwa handlowa, data rozpoczęcia działalności, lista kodów PKD, ewentualne zawieszenia) — CEIDG i biznes.gov.pl blokują dostęp automatyczny (Akamai, 403), a formularz wymaga ręcznego klikania. Dlatego pełna nazwa „Firma Ogólnobudowlana Artur Tchórzewski\" jest u mnie oparta na briefie i na streszczeniach z katalogów, a nie na dokumencie — w białej liście widnieje samo „ARTUR TCHÓRZEWSKI\" (tak MF zapisuje jednoosobowe działalności, to normalne, ale nie potwierdza brzmienia nazwy). Jeśli nazwa ma pójść do stopki i regulaminu, ktoś powinien raz wejść ręcznie na aplikacja.ceidg.gov.pl i wyszukać po NIP 9950044465 — to 2 minuty.\n\n2) Konflikt na przeglądarce. Podczas sprawdzania wizytówki Google przejąłem kartę, na której ktoś w tym samym czasie przeglądał Instagram i TikTok tej samej firmy (karty przeskakiwały mi pod ręką między instagram.com/p/... a tiktok.com/@a.s_tchorzewski). Wygląda na to, że równolegle chodzi druga sesja albo Krzysztof pracuje ręcznie nad tym samym klientem. Dalsze wejścia w Chrome robiłem na własnej, nowej karcie i zamknąłem ją po sobie — ale warto to zderzyć, żeby nie robić tej samej roboty dwa razy.\n\nTRZY RZECZY, KTÓRE ZMIENIAJĄ ROBOTĘ PRZY STRONIE:\n- Materiału graficznego jest MAŁO (ok. 9 zdjęć, i to niepewnego pochodzenia). Bez dosłania zdjęć przez klienta strona będzie musiała stać na typografii i układzie, nie na galerii — warto to Adamowi powiedzieć teraz, a nie na etapie odbioru.\n- Wizytówka Google jest źle ustawiona (brak witryny, obszar tak szeroki, że pinezka wypada 130 km od Błońska). Poprawienie tego jest darmowe, zajmuje kwadrans i realnie da klientowi telefony — dobry pretekst do kolejnego kontaktu i do upsellu.\n- Firma nie ma żadnego śladu w sieci poza Google/FB/IG. Zgłoszenie strony do Google Search Console po wdrożeniu jest tu obowiązkowe, bo startujemy dosłownie od zera."
  }
 },
 {
  "tor": "materialy",
  "dane": {
   "tor": "TOR 2 — MATERIAŁY (zdjęcia, logo, opinie) — Firma Ogólnobudowlana Artur Tchórzewski / A.S TCHÓRZEWSKI, NIP 9950044465, Błońsko 46",
   "fakty": [
    {
     "stwierdzenie": "Instagram @a.s_tchorzewski ma 9 postów, 54 obserwujących — i to JEST magazyn realnych zdjęć firmy; Facebook i wizytówka Google mają tylko ułamek tego.",
     "zrodlo": "https://www.instagram.com/a.s_tchorzewski/ (oglądane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Źródło całej galerii realizacji — stock z dema wymieniamy na te zdjęcia"
    },
    {
     "stwierdzenie": "Wizytówka Google „A.S TCHÓRZEWSKI\" nie ma ANI JEDNEGO zdjęcia — Google wyświetla domyślną niebieską grafikę i przycisk „Dodaj zdjęcie\".",
     "zrodlo": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/ (place: 0x4b6e291d6c883407:0x56cbe6647684bfc8, oglądane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Zero materiału z Google. Zarazem darmowa dźwignia po oddaniu strony: wgrać zdjęcia + link do domeny"
    },
    {
     "stwierdzenie": "Wizytówka Google ma 6 opinii i średnią 5,0; kategoria „Usługi remontowo-budowlane\", telefon 667 434 222.",
     "zrodlo": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/ (zakładka Opinie, 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja opinii na stronie głównej + odznaka „5,0 w Google\""
    },
    {
     "stwierdzenie": "Wszystkie 6 opinii Google zostało wystawionych w tym samym okresie („miesiąc temu\"), żadna nie ma dołączonego zdjęcia.",
     "zrodlo": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/ (zakładka Opinie, 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Nie chwalić się „latami opinii\"; cytować treść, nie datę"
    },
    {
     "stwierdzenie": "Dwie osoby z opinii Google potwierdzają się niezależnie w komentarzach na Instagramie: Kinga Zielonacka = kingazielonacka_instruktor, Piotr Lemanski = lemanek07.",
     "zrodlo": "Google Maps (opinie) + https://www.instagram.com/p/Da_BmaQArMI/ i https://www.instagram.com/p/DVvnPlwgng3/",
     "pewnosc": "potwierdzony",
     "uzycie": "To realni klienci, nie boty — można ich cytować na stronie po zgodzie"
    },
    {
     "stwierdzenie": "Firma używa DWÓCH różnych logo naraz: stare (rysunkowe domki + narzędzia, napis „A.S TCHÓRZEWSKI\") jako awatar FB i IG, oraz nowe (elegancki monogram AS + „A.S_TCHORZEWSKI / USŁUGI OGÓLNOBUDOWLANE\") na okładce FB, w banerach i jako znak wodny na zdjęciach realizacji.",
     "zrodlo": "https://www.facebook.com/profile.php?id=61589974670830 (awatar vs okładka) + https://www.instagram.com/p/Da_BmaQArMI/",
     "pewnosc": "potwierdzony",
     "uzycie": "Nagłówek i stopka strony — trzeba rozstrzygnąć z klientem, które jest aktualne"
    },
    {
     "stwierdzenie": "Nowe logo (monogram AS) jest tym, którym firma znakuje własne zdjęcia realizacji — stare rysunkowe pojawia się tylko na starszym banerze z 14.05 i jako awatar.",
     "zrodlo": "Znak wodny na https://www.instagram.com/p/Da_BmaQArMI/ vs baner FB z 14 maja (fbid 122093201547332489)",
     "pewnosc": "prawdopodobny",
     "uzycie": "Argument, żeby na stronie iść w nowe logo"
    },
    {
     "stwierdzenie": "Demo, na podstawie którego klient kupił, używa STAREGO logo (img/logo.jpg, JPG 720×720 na białym tle, bez przezroczystości) — czyli awatara z FB.",
     "zrodlo": "/Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/img/logo.jpg",
     "pewnosc": "potwierdzony",
     "uzycie": "Na stronę docelową ten plik jest za słaby (JPG, białe tło) — potrzebny plik od klienta"
    },
    {
     "stwierdzenie": "Ich własna okładka FB podaje 18 usług — znacznie szerzej niż brief: dochodzą tapetowanie, beton architektoniczny, zabudowa i ścianki działowe GK, układanie płytek, biały montaż, wylewki samopoziomujące, prace naprawcze i odświeżające, prace rozbiórkowe, układanie paneli podłogowych.",
     "zrodlo": "Okładka FB / baner IG (fbid 122107934697332489), pełna lista odczytana 07.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "Podstrona Oferta — ale zakres do potwierdzenia u klienta, bo brief mówił węziej"
    },
    {
     "stwierdzenie": "Robią też elewacje: mycie i oczyszczenie elewacji, malowanie farbami zewnętrznymi oraz renowacja i malowanie drewnianej podbitki dachowej — usługa nieobecna w briefie.",
     "zrodlo": "https://www.instagram.com/p/DZijR8Egq-d/ (post z 13.06, opis realizacji)",
     "pewnosc": "potwierdzony",
     "uzycie": "Ewentualna dodatkowa pozycja w ofercie — po potwierdzeniu"
    },
    {
     "stwierdzenie": "Deklarują też „drobne naprawy elektryczne i hydrauliczne\" w ramach kompleksowej realizacji.",
     "zrodlo": "https://www.instagram.com/p/Da_BmaQArMI/ (opis realizacji z 19.07)",
     "pewnosc": "potwierdzony",
     "uzycie": "Wzmacnia przekaz „od A do Z\" na stronie głównej"
    },
    {
     "stwierdzenie": "Bio na FB i IG brzmi identycznie: „20 lat doświadczenia / Budujemy jakość na lata / Zawsze na czas / Nowoczesny sprzęt / Darmowa wycena\" (z flagami 🇩🇪🇵🇱).",
     "zrodlo": "https://www.instagram.com/a.s_tchorzewski/ + https://www.facebook.com/profile.php?id=61589974670830",
     "pewnosc": "potwierdzony",
     "uzycie": "Gotowy zestaw obietnic pod sekcję „Dlaczego my\" — ich własne słowa, nie nasze wymyślone"
    },
    {
     "stwierdzenie": "Bio deklaruje „Darmowa wycena\", a brief mówi „trzeba się skontaktować, wycena do 5 dni roboczych\" — to dwa różne komunikaty o tym samym.",
     "zrodlo": "Bio IG/FB vs /Users/krzysztof/Developer/impulseo-klienci/as-tchorzewski/BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja kontakt/CTA — trzeba wybrać jeden komunikat"
    },
    {
     "stwierdzenie": "Ich własne hashtagi wskazują teren: #wielkopolska, #poznań, #wolsztyn.",
     "zrodlo": "https://www.instagram.com/p/Da_BmaQArMI/ + baner FB (fbid 122107932879332489)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja „Obszar działania\" i SEO lokalne"
    },
    {
     "stwierdzenie": "Jedna z realizacji (łazienka na poddaszu) jest oznaczona lokalizacją Wolfenbüttel w Niemczech — to fizyczny dowód na niemiecką nogę firmy od 2005.",
     "zrodlo": "https://www.instagram.com/p/DX6FvMCDIkQ/ (post z 04.05, znacznik lokalizacji)",
     "pewnosc": "potwierdzony",
     "uzycie": "Podstrona O nas — uwiarygadnia „w Niemczech od 2005\""
    },
    {
     "stwierdzenie": "Adres w materiałach firmy konsekwentnie brzmi „Błońsko 46, 64-308 Jabłonna\" — nie „64-308 Błońsko\" jak w rejestrze.",
     "zrodlo": "Okładka FB, bio IG, banery — vs biała lista VAT / BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Stopka i dane kontaktowe — trzeba rozstrzygnąć, co idzie na stronę"
    },
    {
     "stwierdzenie": "W ich materiałach krążą TRZY zapisy adresu e-mail: a.s-tchorzewski@wp.pl (brief), a.s_tchorzewski@wp.pl (baner z 19.07) i „a.s - tchorzewski@wp.pl\" (baner z 14.05).",
     "zrodlo": "BRIEF-KLIENTA.md + banery FB fbid 122107934697332489 i 122093201547332489",
     "pewnosc": "potwierdzony",
     "uzycie": "Formularz kontaktowy i stopka — zły adres = utracone zapytania"
    },
    {
     "stwierdzenie": "Wizytówka Google podaje godziny zamknięcia o 18:00, a brief mówi 8–20.",
     "zrodlo": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/ (07.09.2026) vs BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja godzin na podstronie Kontakt"
    },
    {
     "stwierdzenie": "Firma nie ma konta na TikToku — pod @a.s_tchorzewski konto nie istnieje, a wyszukiwarka TikToka zwraca wyłącznie niepowiązane osoby prywatne o tym nazwisku.",
     "zrodlo": "https://www.tiktok.com/@a.s_tchorzewski („Couldn't find this account\") + wyszukiwarka TikTok, 07.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "Nie linkować TikToka w stopce; nie ma stamtąd materiału"
    },
    {
     "stwierdzenie": "Facebook nie ma ani jednej opinii/rekomendacji — zakładka Opinie pokazuje tylko pytanie „Czy polecasz firmę\".",
     "zrodlo": "https://www.facebook.com/profile.php?id=61589974670830&sk=reviews (07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Cała sekcja opinii musi stanąć na Google + komentarzach IG"
    },
    {
     "stwierdzenie": "Facebook ma tylko 7 pozycji w zdjęciach (2 realne zdjęcia + 4 grafiki marketingowe + awatar) i 86 obserwujących — jest wyraźnie uboższy niż Instagram.",
     "zrodlo": "https://www.facebook.com/profile.php?id=61589974670830&sk=photos (07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Nie tracić czasu na FB przy zbieraniu zdjęć — iść na IG"
    },
    {
     "stwierdzenie": "Na tym samym adresie (Błońsko 46) figuruje w CEIDG DRUGA firma: „Firma Ogólnobudowlana Tadeusz Tchórzewski\" — to nie jest nasz klient.",
     "zrodlo": "https://aleo.com/pl/firma/firma-ogolnobudowlana-tadeusz-tchorzewski-wolsztyn",
     "pewnosc": "prawdopodobny",
     "uzycie": "Pułapka przy weryfikacji danych rejestrowych — nasz klient to Artur, NIP 9950044465"
    }
   ],
   "materialy": [
    {
     "co": "REALIZACJA „Od surowej bryły do nowoczesnego wykończenia\" — 2 zdjęcia: stan surowy (pustaki, stemple pod stropem) i stan gotowy (biała bryła z przeszkleniem, trawnik, kostka). Najsilniejszy materiał, jaki mają.",
     "skad": "https://www.instagram.com/p/Da_BmaQArMI/ (19.07, 22 polubienia — ich najpopularniejszy post). Te same 2 kadry osobno na FB: fbid 122107943421332489 i 122107943415332489",
     "czy_na_pewno_ich": "POTWIERDZONE, najmocniejszy dowód w całym researchu: mają zdjęcie TEGO SAMEGO budynku w trakcie budowy i po skończeniu — ten sam trawnik, ta sama opaska z kostki, ta sama linia dachu w tle. Zdjęcia stockowego nie da się mieć w wersji „w trakcie\". Do tego własny znak wodny i opis „W tej realizacji wykonaliśmy: malowanie agregatem, szpachlowanie i gładzie maszynowe, beton architektoniczny, zabudowy i sufity GK\"."
    },
    {
     "co": "REALIZACJA „Kompleksowe wykończenie poddasza\" — 11 zdjęć (odliczone kropki karuzeli): otwarta przestrzeń pod skosami, odsłonięte drewniane belki, wielkoformatowe płytki na podłodze, pas okien.",
     "skad": "https://www.instagram.com/p/DVs1y9VAjaE/ (10.03, 14 polubień)",
     "czy_na_pewno_ich": "POTWIERDZONE opisem w pierwszej osobie: „W ramach realizacji wykonaliśmy szpachlowanie i malowanie ścian, odświeżenie drewnianych belek\". Zdjęcia telefonem (nierówny balans bieli, odbicia w płytkach), nie sesja stockowa. Najwięcej kadrów z jednego obiektu w całym profilu."
    },
    {
     "co": "REALIZACJA „Renowacja elewacji i podbitki\" — 10 pozycji w karuzeli, w tym film: ekipa na drabinie przy elewacji, przygotowanie powierzchni, rolki papy/folii na kostce.",
     "skad": "https://www.instagram.com/p/DZijR8Egq-d/ (13.06, 15 polubień)",
     "czy_na_pewno_ich": "POTWIERDZONE: opis w pierwszej osobie opisuje własny zakres prac krok po kroku (mycie elewacji → malowanie farbami zewnętrznymi → renowacja podbitki), a na kadrach widać ich ludzi przy pracy. Materiał „ludzie w akcji\" — najrzadszy i najbardziej wiarygodny typ zdjęcia."
    },
    {
     "co": "REALIZACJA „Kompleksowe wykończenie łazienki\" — 6 zdjęć: wolnostojąca wanna, wielkoformatowe płytki, podłoga w drewnopodobnej ceramice.",
     "skad": "https://www.instagram.com/p/DVSzMI3gt_C/ (28.02, 10 polubień)",
     "czy_na_pewno_ich": "POTWIERDZONE opisem „Kompleksowe wykończenie łazienki wykonane od podstaw z dbałością o każdy detal\". Na kadrze widać nieukończone detale (wystające podejścia wodne, niezamontowana bateria) — stock takich rzeczy nie pokazuje."
    },
    {
     "co": "REALIZACJA „Łazienka na poddaszu\" — 5 zdjęć: wanna w zabudowie pod skosem, dwa okna dachowe, ściana prysznicowa w strukturalnym wykończeniu.",
     "skad": "https://www.instagram.com/p/DX6FvMCDIkQ/ (04.05, 11 polubień)",
     "czy_na_pewno_ich": "POTWIERDZONE opisem własnym („Projekt oparty na maksymalnym wykorzystaniu przestrzeni pod skosami…\"). ⚠️ ALE: post ma znacznik lokalizacji Wolfenbüttel, Niemcy — to realizacja z niemieckiej nogi firmy. Ich praca, tylko nie w Polsce."
    },
    {
     "co": "REALIZACJA „Beton architektoniczny\" — łącznie 4 zdjęcia w dwóch postach: ściana w szarym betonie dekoracyjnym oraz antracytowa ściana z czarnymi listwami w geometrycznym układzie.",
     "skad": "https://www.instagram.com/p/DVSzaicgmMm/ (3 zdjęcia) + https://www.instagram.com/p/DVSzRPgggc8/ (1 zdjęcie), oba 28.02",
     "czy_na_pewno_ich": "POTWIERDZONE opisami „Kolejna realizacja ✔️ Ścianka z betonu architektonicznego\" i „Nowoczesna ścianka z betonu architektonicznego\". ⚠️ Na obu kadrach widać bałagan budowlany (wiadra, folia, drabina, stelaż) — do użycia trzeba je skadrować."
    },
    {
     "co": "FILM „Malowanie natryskowe agregatem\" — dwóch pracowników, jeden w białym kombinezonie z pistoletem natryskowym, pomieszczenie zafoliowane. Najlepszy materiał „człowiek przy pracy\", jaki mają.",
     "skad": "https://www.instagram.com/p/DVvnPlwgng3/ (11.03, 13 polubień)",
     "czy_na_pewno_ich": "POTWIERDZONE: własny opis techniczny usługi + realni ludzie w realnym wnętrzu + pod postem komentarz klienta („Robił mi 2 pokoje i jestem zadowolony\"). Nie da się tego podrobić stockiem."
    },
    {
     "co": "LOGO NOWE — monogram AS + napis „A.S_TCHORZEWSKI / USŁUGI OGÓLNOBUDOWLANE\", pomarańcz + granat/czerń.",
     "skad": "Okładka FB (fbid 122107934697332489) i wersja pionowa (fbid 122107932879332489); ten sam znak jako znak wodny na zdjęciach realizacji",
     "czy_na_pewno_ich": "POTWIERDZONE — to ich własna okładka i ich własny znak wodny. ⚠️ ALE mamy go WYŁĄCZNIE wtopionego w baner, na ciemnym tle, razem z tekstem. Nie mamy czystego pliku logo. Bez pliku od klienta zostaje wycinanie z JPG — słaba jakość na nagłówek strony."
    },
    {
     "co": "LOGO STARE — rysunkowe (bloki, domki, młotek, kielnia, wałek) z napisem „A.S TCHÓRZEWSKI\".",
     "skad": "Awatar FB i IG; już pobrane: /Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/img/logo.jpg (720×720 JPG)",
     "czy_na_pewno_ich": "POTWIERDZONE — to zdjęcie profilowe obu ich oficjalnych profili. ⚠️ Plik jest JPG na białym tle, bez przezroczystości i w niskiej rozdzielczości — na demo wystarczył, na płatną stronę jest za słaby."
    },
    {
     "co": "OPINIE GOOGLE — 6 sztuk, wszystkie 5★, treści gotowe do cytowania (m.in. Kinga Zielonacka: „Fachowcy pierwsza klasa… znalazłam swoją sprawdzoną ekipę\"; Piotr Lemanski: „Miły pan, terminowo, bez poprawek\"; dradex: „Szczerze nie znam lepszego fachowca w tak dobrej i przystępnej cenie\").",
     "skad": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/ → zakładka Opinie",
     "czy_na_pewno_ich": "POTWIERDZONE — opinie wystawione bezpośrednio pod ich wizytówką, a dwoje autorów (Zielonacka, Lemanski) niezależnie komentuje też ich posty na Instagramie. ⚠️ Trzy z sześciu opinii są na Google przycięte („Więcej\" nie rozwinęło się w automacie) — pełne treści trzeba doczytać ręcznie w przeglądarce."
    },
    {
     "co": "OPINIE Z INSTAGRAMA — 3 komentarze klientów: „Robił mi 2 pokoje i jestem zadowolony, bez opóźnień\" (lemanek07), „Bardzo dokładna robota 👏\" (kingazielonacka_instruktor), „Bardzo ładne, chce to mieć ❤️\" (lemanek07).",
     "skad": "https://www.instagram.com/p/DVvnPlwgng3/ i https://www.instagram.com/p/Da_BmaQArMI/",
     "czy_na_pewno_ich": "POTWIERDZONE — komentarze pod ich własnymi postami, od kont, które pokrywają się z autorami opinii Google. To ta sama, realna grupa klientów widziana z dwóch niezależnych stron."
    },
    {
     "co": "RELACJA WYRÓŻNIONA na IG — „Szlifowanie belek\" (pracownik szlifujący drewnianą belkę).",
     "skad": "https://www.instagram.com/a.s_tchorzewski/ → kółko relacji wyróżnionych",
     "czy_na_pewno_ich": "PRAWDOPODOBNIE ich (ich własna relacja, opis techniczny procesu). ⚠️ Kadr ma wypalony napis na obrazie — bez czystej wersji od klienta nie nadaje się na stronę."
    },
    {
     "co": "⛔ GALERIA Z DEMA — hero.jpg, about.jpg, g1–g14.jpg (16 plików).",
     "skad": "/Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/img/",
     "czy_na_pewno_ich": "BRAK DOWODU — to STOCK z Pexels, wstawiony przez nas przy budowie dema (potwierdza to BRIEF-KLIENTA.md, pkt „Punkt wyjścia\"). Na stronie docelowej musi zniknąć w całości."
    },
    {
     "co": "⛔ TŁA BANERÓW — ciemne eleganckie wnętrze z czarną pufą i grafiką na ścianie (okładka FB) oraz nowoczesny dom z kamienną elewacją i trzema garażami (baner z 14.05).",
     "skad": "Okładka FB (fbid 122107934697332489) i baner FB (fbid 122093201547332489)",
     "czy_na_pewno_ich": "BRAK DOWODU — to tła grafik reklamowych, nie realizacje. Dom z banera z 14.05 ma wszystkie cechy renderu generowanego (nienaturalne światło, „idealna\" geometria). Nigdzie w profilu nie ma tych obiektów jako realizacji. NIE używać jako zdjęć prac."
    },
    {
     "co": "⛔ ZDJĘCIA Z WIZYTÓWKI GOOGLE",
     "skad": "https://www.google.com/maps/place/A.S+TCHÓRZEWSKI/",
     "czy_na_pewno_ich": "NIE ISTNIEJĄ — wizytówka nie ma ani jednego zdjęcia (Google pokazuje domyślną grafikę i prosi o dodanie). Zero materiału, ale też zero ryzyka zaśmiecenia cudzymi zdjęciami."
    }
   ],
   "luki": [
    "KTÓRE LOGO JEST AKTUALNE? Firma używa naraz dwóch: rysunkowego (awatar FB/IG, to samo, które jest w demie) i eleganckiego monogramu AS (okładka FB, znak wodny na zdjęciach). Które ma iść na stronę?",
    "POTRZEBUJEMY PLIKU LOGO. Nowe logo mamy tylko wtopione w baner JPG na ciemnym tle, stare tylko jako JPG 720×720 na białym. Na płatną stronę potrzebny plik wektorowy (SVG/AI/PDF) albo PNG z przezroczystym tłem. Klient obiecał logo 07.09 wieczorem — to jest ta rzecz.",
    "CZY MAJĄ ORYGINAŁY ZDJĘĆ Z TELEFONU? Wszystko, co ściągniemy z Instagrama i Facebooka, jest skompresowane do ok. 1080 px — za mało na duże zdjęcie w nagłówku strony. Oryginały z telefonu (2000–4000 px) zmieniają jakość strony o klasę.",
    "KTÓRY ADRES E-MAIL JEST PRAWIDŁOWY: a.s-tchorzewski@wp.pl (z myślnikiem, brief), a.s_tchorzewski@wp.pl (z podkreślnikiem, ich baner z 19.07), czy „a.s - tchorzewski@wp.pl\" (baner z 14.05)? Zły adres w formularzu = zapytania klientów lecą w próżnię.",
    "JAKI ADRES NA STRONĘ: „Błońsko 46, 64-308 Błońsko\" (rejestr, biała lista VAT) czy „Błońsko 46, 64-308 Jabłonna\" (tak piszą wszędzie u siebie — okładka FB, bio IG, faktura)?",
    "GODZINY: brief mówi 8–20, wizytówka Google mówi zamknięcie o 18:00. Które podać na stronie i czy poprawić Google?",
    "WYCENA DARMOWA CZY NIE? Ich bio na FB i IG obiecuje „Darmowa wycena\", brief mówi „trzeba się skontaktować, wycena bardzo indywidualna, do 5 dni roboczych\". Trzeba wybrać jeden komunikat pod przycisk kontaktu.",
    "PEŁNY ZAKRES USŁUG NA STRONĘ? Ich własna okładka wymienia 18 usług (m.in. tapetowanie, beton architektoniczny, ścianki i sufity GK, układanie płytek, biały montaż, wylewki samopoziomujące, prace rozbiórkowe), a na IG dochodzą jeszcze elewacje i „drobne naprawy elektryczne i hydrauliczne\". Brief wymieniał tylko 5 pozycji. Co pokazujemy, a co pomijamy?",
    "CZY MOŻEMY POKAZAĆ REALIZACJĘ Z NIEMIEC? Łazienka na poddaszu jest oznaczona lokalizacją Wolfenbüttel — to ich praca, ale niemiecka. Na stronie kierowanej do wielkopolskiego i lubuskiego to podpiera historię „w Niemczech od 2005\", ale warto mieć zgodę.",
    "CZY MAJĄ WIĘCEJ PAR „PRZED I PO\"? Mają dokładnie jedną (surowa bryła → gotowy budynek) i to najmocniejszy materiał w całym profilu. Każda kolejna para jest warta więcej niż dziesięć ładnych kadrów.",
    "CZY MOŻEMY PRZEPISAĆ OPINIE Z GOOGLE NA STRONĘ z imieniem i nazwiskiem autora? Sześć opinii 5★ to jedyny dowód społeczny, jaki mają — Facebook nie ma ani jednej.",
    "KTO MA DOSTĘP DO WIZYTÓWKI GOOGLE? Nie ma tam ani jednego zdjęcia ani linku do strony. Po oddaniu strony to jest darmowy strzał: wgrać 10 zdjęć realizacji + podpiąć as-tchorzewski.pl.",
    "CZY JEST CZYSTA WERSJA FILMU „SZLIFOWANIE BELEK\" (bez wypalonego napisu na obrazie)? To dobry materiał na sekcję „jak pracujemy\", ale w obecnej formie nie do użycia.",
    "CZY NA ZDJĘCIACH SĄ WNĘTRZA KLIENTÓW, KTÓRZY NIE ZGODZILI SIĘ NA PUBLIKACJĘ? Na Instagramie to przechodzi, na firmowej stronie z domeną warto mieć to przegadane — zwłaszcza przy realizacji z Niemiec."
   ],
   "uwagi": "SKĄD BRAĆ ZDJĘCIA: cały materiał siedzi na Instagramie, nie na Facebooku i nie w Google. Licząc slajdy w karuzelach jest tam ok. 37 realnych zdjęć + 2 filmy z 7 realizacji. Facebook ma z tego tylko 2 zdjęcia, wizytówka Google — zero. Do ściągnięcia jest skill `social-foto` (droga przez Chrome, za darmo).\n\nCO PROPONUJĘ NA GALERIĘ (od najmocniejszego): (1) para „przed i po\\\" białej bryły — na nagłówek strony głównej albo osobną sekcję, bo to jedyny materiał, którego konkurencja nie ma; (2) poddasze, 11 kadrów — najbogatszy jednolity zestaw, gotowa podstrona realizacji; (3) łazienka, 6 kadrów — pod usługę, na której zarabiają; (4) film z agregatem — pod „malowanie agregatem\\\", pokazuje ludzi, a nie puste ściany; (5) elewacja, 10 pozycji — jeśli klient potwierdzi, że chce tę usługę na stronie.\n\nCZEGO NIE RUSZAĆ: 16 plików w img/ dema to stock z Pexels — na płatnej stronie muszą zniknąć co do jednego. Tła banerów (ciemne wnętrze z pufą, dom z kamienną elewacją) to grafiki reklamowe, prawie na pewno render/stock — nie wolno ich podawać jako realizacji.\n\n⚠️ RYZYKO, KTÓRE WARTO ZNAĆ: wszystkie 6 opinii Google powstało w tym samym okresie („miesiąc temu\\\"). Nie mam podstaw twierdzić, że są nieprawdziwe — przeciwnie, dwoje autorów niezależnie komentuje ich posty na Instagramie, co jest dobrym sygnałem. Ale nie budowałbym na stronie narracji „lata zadowolonych klientów\\\" opartej o tę wizytówkę; lepiej cytować treść niż liczby i daty.\n\n⚠️ PUŁAPKA PRZY WERYFIKACJI: pod tym samym adresem Błońsko 46 figuruje w CEIDG druga firma — „Firma Ogólnobudowlana Tadeusz Tchórzewski\\\". To nie nasz klient. Nasz to Artur Tchórzewski, NIP 9950044465. Osobno: w wynikach Facebooka wychodzi zweryfikowane konto „Łukasz Tchórzewski\\\" (twórca z TikToka) — kompletnie niepowiązane.\n\nCZEGO NIE UDAŁO MI SIĘ DOKOŃCZYĆ: trzy z sześciu opinii Google są przycięte, a przycisk „Więcej\\\" nie dał się kliknąć automatem — pełne treści trzeba doczytać ręcznie, jeśli mają iść na stronę w całości. Instagram blokuje odczyt adresów plików skryptem, więc same pliki trzeba ściągnąć przez skill `social-foto`, nie przez javascript.\n\nDROBIAZG: nowe logo zapisuje nazwisko bez polskiego znaku — „A.S_TCHORZEWSKI\\\", a nazwa firmy i wizytówka Google używają „TCHÓRZEWSKI\\\". Na stronie w tekstach idzie oczywiście wersja z „ó\\\", ale przy samym znaku graficznym nie poprawiać go na siłę."
  }
 },
 {
  "tor": "glos",
  "dane": {
   "tor": "TOR 3 — GŁOS KLIENTA (teksty nietykalne) · Firma Ogólnobudowlana Artur Tchórzewski (A.S TCHÓRZEWSKI), NIP 9950044465",
   "fakty": [
    {
     "stwierdzenie": "JEDYNE źródło głosu klienta to checklista Adama w Notatkach z 07.09.2026, 11:11 — odczytałem oba zrzuty w całości, od tytułu „Checklista as-tchórzewski\" do ostatniej linijki; nic więcej od klienta nie istnieje w mailu, WhatsAppie ani iMessage Krzysztofa.",
     "zrodlo": "zrzuty ekranu notatki: ~/Library/Metadata/CoreSpotlight/PasteboardHistory/2026-09-07_11-30-58.heic i 2026-09-07_11-31-05.heic (przekonwertowane do PNG); brak trafień w Gmailu (fraza „tchorzewski\" → tylko mail rejestracji domeny z dns.pl), pusta ZWAMESSAGE dla numerów 667434222 / 724795855 / 882832244",
     "pewnosc": "potwierdzony",
     "uzycie": "Podstawa całej redakcji tekstów — 15 linijek niżej to komplet, nie wyimek."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, ostatnia linijka notatki, z wykrzyknikiem: „Wszystko w liczbie mnogiej!\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-31-05), potwierdzone w BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Firma mówi o sobie „my/robimy/polecamy/wyceniamy\" na KAŻDEJ podstronie. Łamie domyślną regułę silnika („liczba pojedyncza wszędzie\") — tu wygrywa klient."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, zakres usług słowami klienta: „Szpachlowanie, malowanie i łazienki, sucha zabudowa - kluczowe działania, reszta to są mniejsze zarobki- montaż dziwi okien\" (w notatce literówka: „dziwi\" = drzwi).",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58)",
     "pewnosc": "potwierdzony",
     "uzycie": "Kolejność i hierarchia kafli oferty: szpachlowanie, malowanie, łazienki, sucha zabudowa NA GÓRZE; montaż drzwi i okien jako pozycja mniejsza, niżej. Cztery pierwsze to ich pieniądze."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, ich sposób obsługi zapytań spoza zakresu: „Nawet jeśli ktoś pyta o usługi których nie wykonują- oni zajmują się typowo wykończeniem wnętrz- to on poleca osoby które się tym zajmują\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58)",
     "pewnosc": "potwierdzony",
     "uzycie": "Osobny akapit/sekcja na stronie — to jest ich realny wyróżnik, sam się o niego upomniał. W liczbie mnogiej: „Zajmujemy się typowo wykończeniem wnętrz. Pytasz o coś, czego nie robimy — polecimy sprawdzone osoby.\" Fraza „typowo wykończeniem wnętrz\" to ICH samookreślenie — zostaw."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, polityka cenowa: „W kwestii ceny trzeba się skontaktować\" oraz „Do 5 dni roboczych wycena- ale jest bardzo indywidualne\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58)",
     "pewnosc": "potwierdzony",
     "uzycie": "Zero cennika i zero widełek na stronie. CTA = kontakt. „do 5 dni roboczych\" można podać jako termin odpowiedzi — ale patrz luki, bo to obietnica, którą klient będzie musiał dowozić."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, historia firmy: „Polskę firmę od 2015 roku, ale w Niemczech miał od 2005 roku jest to rodzinny biznes, 20 lat doświadczenia ponad w branży\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja „O nas\". Trzy fakty do zachowania: polska firma od 2015, Niemcy od 2005, rodzinny biznes, ponad 20 lat doświadczenia. ⚠️ „ponad 20 lat\" — nie zaokrąglać w górę do 25 ani nie pisać „od 20 lat\" jak w demie."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, dane kontaktowe i ich układ: „667 434 222- główny numer\", „882832244- logo WhatsApp przy numerze\", „Mail ten co wysyłałem\" (a.s-tchorzewski@wp.pl), „8-20 godziny działania\", „Facebook i Instagram\", „www.as-tchorzewski.pl- domena\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58); mail potwierdzony w zamówieniu IMP/2026/09/005 i na karcie CRM de55d1aa-3deb-44f1-88b7-ca3a19ad8b7c",
     "pewnosc": "potwierdzony",
     "uzycie": "667 434 222 = numer główny (duży, w nagłówku). 882 832 244 = drugi numer Z IKONĄ WHATSAPPA obok — to wprost zamówiony element wizualny, nie propozycja. Godziny 8–20 i oba social w stopce/kontakcie."
    },
    {
     "stwierdzenie": "🔴 NIETYKALNE, obszar działania: „Województwo wielkopolskie i lubuskie- obszar działania\" — dwa województwa, bez zawężania do miasta.",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-30-58)",
     "pewnosc": "potwierdzony",
     "uzycie": "⛔ Kasuje z dema całą sekcję „Dojeżdżamy do Ciebie\" z Wolsztynem i listą miast (patrz niżej) — klient określił zasięg dwoma województwami."
    },
    {
     "stwierdzenie": "Klient NIE podyktował ani jednego zdania marketingowego — w całej checkliście nie ma słowa „najlepsi\", „profesjonalizm\", „pasja\", „jakość\", „zadowolenie klienta\" ani żadnego hasła reklamowego. Mówi wyłącznie operacyjnie: co robimy, gdzie, w jakich godzinach, jak wyceniamy.",
     "zrodlo": "analiza pełnej treści notatki Adama 07.09.2026 11:11 (15 linijek, wszystkie odczytane)",
     "pewnosc": "potwierdzony",
     "uzycie": "Ton całej strony: rzeczowy, bez przymiotników. Każde zdanie typu „Twoje marzenia stają się rzeczywistością\" będzie ciałem obcym wobec jego głosu."
    },
    {
     "stwierdzenie": "Klient sam zgłosił dwie rzeczy jako niedokończone: „Logo jest- wyślę mi, zdjęcia dośle wieczorem\" oraz „Gwarancja- jest w umowie, ale podeślę wieczorem na ile!\"",
     "zrodlo": "notatka Adama 07.09.2026 11:11 (zrzut 11-31-05)",
     "pewnosc": "potwierdzony",
     "uzycie": "Gwarancja MA być na stronie (sam ją wywołał), ale bez liczby lat nie wolno jej opisać. Do czasu odpowiedzi: puste miejsce, nie zmyślona wartość i nie ogólnik „gwarancja na robociznę\" z dema."
    },
    {
     "stwierdzenie": "⚠️ Demo obiecuje BEZPŁATNĄ wycenę („Potrzebujesz fachowca? Wycenimy za darmo.\", „Za obejrzenie placu i policzenie nie bierzemy pieniędzy. Płacisz za robotę, nie za kosztorys.\") — klient nigdy tego nie powiedział; powiedział tylko, że w kwestii ceny trzeba się skontaktować i że wycena idzie do 5 dni roboczych.",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (index.html, sekcja CTA i FAQ) vs notatka Adama 07.09.2026 11:11",
     "pewnosc": "potwierdzony",
     "uzycie": "Nasz wymysł podany klientowi jako obietnica handlowa. Nie przenosić na płatną stronę bez jego zgody — patrz luki."
    },
    {
     "stwierdzenie": "⚠️ Demo zawęża firmę do Wolsztyna („Wykończenia i remonty pod klucz. Wolsztyn i okolice.\", „Dojazd: Wolsztyn i okolice\", „Najczęściej pracujemy w Wolsztynie: Jabłonna, Zbąszyń, Nowy Tomyśl, Grodzisk Wielkopolski\") — sprzeczne z podyktowanym obszarem „wielkopolskie i lubuskie\".",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (index.html) vs notatka Adama 07.09.2026 11:11",
     "pewnosc": "potwierdzony",
     "uzycie": "Do wycięcia/przepisania na dwa województwa. To nie jest kosmetyka — zawęża mu lejek o całe lubuskie."
    },
    {
     "stwierdzenie": "⚠️ Demo eksponuje „Gładzie i malowanie agregatem\" jako osobną usługę i wpisuje „malowanie agregatem\" do stopki na KAŻDEJ podstronie — klient nie wymienił agregatu ani razu.",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (index.html, oferta.html, stopka wszystkich podstron) vs notatka Adama 07.09.2026 11:11",
     "pewnosc": "potwierdzony",
     "uzycie": "Albo potwierdzić u klienta, albo zejść do neutralnego „szpachlowanie i malowanie\" — jego własnych słów."
    },
    {
     "stwierdzenie": "⚠️ W demie BRAKUJE czterech rzeczy, które klient podyktował: montażu drzwi i okien, polecania sprawdzonych osób, godzin 8–20 i numeru WhatsApp 882 832 244.",
     "zrodlo": "porównanie treści https://impulseo-pl.github.io/a-s-tchorzewski/ (5 podstron) z notatką Adama 07.09.2026 11:11",
     "pewnosc": "potwierdzony",
     "uzycie": "Cztery pozycje do dołożenia na stronie docelowej — to jest różnica między demem a tym, co kupił."
    },
    {
     "stwierdzenie": "⚠️ Demo opisuje proces, którego klient nigdy nie opisał: „Bez podpisanej umowy nie ruszamy\", „Robota idzie etapami z odbiorami\", „Płacisz za to, co już stoi\", „Usterki z przeglądu poprawiamy przed rozliczeniem końcowym\", „Na budowach pracujemy od 20 lat - zaczynaliśmy od murarki\".",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (index.html sekcja 01–04, o-nas.html) vs notatka Adama 07.09.2026 11:11",
     "pewnosc": "potwierdzony",
     "uzycie": "To są nasze zdania, nie jego — wolno je zmieniać dowolnie, ale każde jest deklaracją, z której klient będzie rozliczany. Przed przeniesieniem na płatną stronę: potwierdzić albo wyciąć."
    },
    {
     "stwierdzenie": "Checklistę 07.09 najprawdopodobniej dyktował SYN właściciela, nie Artur Tchórzewski — Adam pisze o firmie w trzeciej osobie („oni zajmują się\", „on poleca\", „w Niemczech miał od 2005\"), a notatka na karcie mówi, że finalizacja czekała na powrót syna z urlopu.",
     "zrodlo": "clients.notes karty CRM de55d1aa-3deb-44f1-88b7-ca3a19ad8b7c („Czekam na kontakt 24.08.2026 od syna właściciela\", „Kontakt 04.09.2026, bo wtedy syn wraca z urlopu- dopięcie i finalizacja\", „KONTAKT DO SYNA: +48 724 795 855\") + trzecioosobowa forma w notatce z 07.09",
     "pewnosc": "prawdopodobny",
     "uzycie": "Przy pytaniach o gwarancję, zdjęcia i akceptację tekstów dzwonić na 724 795 855 (syn) — to on prowadzi temat i on te zdania podyktował."
    },
    {
     "stwierdzenie": "Zakres kupiony i zapisany w zamówieniu (zastępuje §1 umowy): „strona główna, do 5 podstron, zdjęcia i teksty na podstawie udostępnionych materiałów, wersja mobilna, jedna runda poprawek\" — 1 722,00 zł brutto, plus pakiet obsługi 49 zł × 12 mies.",
     "zrodlo": "CRM Supabase, order_items zamówienia IMP/2026/09/005 (order_id 48), paynow_status CONFIRMED, opłacone 06.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "⚠️ „na podstawie udostępnionych materiałów\" — bez jego zdjęć nie mamy z czego zrobić galerii; JEDNA runda poprawek oznacza, że pytania o teksty trzeba zadać PRZED oddaniem, nie po."
    }
   ],
   "luki": [
    "Na ile lat jest gwarancja? Klient sam ją wywołał („Gwarancja- jest w umowie, ale podeślę wieczorem na ile!\", 07.09) i obiecał podać wieczorem — bez liczby nie da się napisać tej sekcji. To najpilniejsze pytanie.",
    "Czy „Wszystko w liczbie mnogiej!\" dotyczy tylko tego, jak firma mówi o SOBIE („robimy, polecamy\"), czy również zwrotu do odwiedzającego — czyli „Państwo\" zamiast „Ty\"? Demo mówi do gościa na „Ty\" („Płacisz\", „Odbierasz mieszkanie\") i klient tego nie zakwestionował, ale instrukcja jest kategoryczna i dwuznaczna. Rekomendacja: firma = „my\", gość = „Ty\", ale trzeba to potwierdzić jednym zdaniem.",
    "Czy zostawiamy obietnicę BEZPŁATNEJ wyceny z dema? Klient powiedział tylko „w kwestii ceny trzeba się skontaktować\" i „do 5 dni roboczych wycena\". Darmowy dojazd i darmowy kosztorys to nasz wymysł — może kosztować go pieniądze.",
    "Czy „do 5 dni roboczych\" ma iść na stronę jako publiczna obietnica terminu, czy to była tylko informacja dla nas? Klient dodał zastrzeżenie „ale jest bardzo indywidualne\".",
    "Czy „malowanie agregatem\" (z dema, w stopce każdej podstrony) to prawda? Klient wymienił tylko szpachlowanie i malowanie.",
    "Obszar: potwierdzić, że zdejmujemy z dema „Wolsztyn i okolice\" oraz listę Jabłonna/Zbąszyń/Nowy Tomyśl/Grodzisk i wpisujemy „wielkopolskie i lubuskie\". Czy jest miejscowość, którą chce wyeksponować jako bazę?",
    "Jaki adres ma być na stronie: Błońsko 46, 64-308 Błońsko (rejestr, biała lista VAT) czy Błońsko 46, 64-308 Jabłonna (jak na fakturze i w demie)? Kod pocztowy się nie zgadza między dokumentami.",
    "Jak ma się nazywać firma na stronie: „A.S Tchórzewski\" (logo, social) czy „Firma Ogólnobudowlana Artur Tchórzewski\" (rejestr, zamówienie)?",
    "Polecanie sprawdzonych osób — czy piszemy to wprost na stronie i czy wymieniamy branże (elektryk, hydraulik, glazurnik), czy zostawiamy ogólnie „polecimy sprawdzone osoby\"?",
    "Numer 882 832 244 — tylko WhatsApp, czy można też na niego dzwonić? Klient powiedział wyłącznie „logo WhatsApp przy numerze\".",
    "Czy mail a.s-tchorzewski@wp.pl publikujemy na stronie, czy kontakt ma iść wyłącznie telefonem i formularzem?",
    "Czy piszemy na stronie o Niemczech (od 2005)? To mocny atut, ale klient podał to jako fakt o historii, nie jako coś do eksponowania — a część klientów w Polsce czyta „niemiecka firma\" inaczej niż my.",
    "„Rodzinny biznes\" — czy pokazujemy to imiennie (kto tworzy ekipę, zdjęcie ojca i syna), czy zostaje ogólne zdanie?",
    "Czy przyszły obiecane wieczorem 07.09 materiały: plik logo i zdjęcia realizacji? Bez nich galeria zostaje pusta albo stockowa — a zamówienie mówi „na podstawie udostępnionych materiałów\"."
   ],
   "materialy": [
    {
     "co": "Logo A.S TCHÓRZEWSKI (grafika: sylwetka domów i wieżowców, młotek, klucz, kielnia, wałek; wordmark „A.S TCHÓRZEWSKI\", pomarańcz + grafit)",
     "skad": "/Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/img/logo.jpg oraz /Users/krzysztof/.claude/skills/strona-klienta/imglib/klienci/a-s-tchorzewski/logo.jpg — pobrane z awatara profilu FB",
     "czy_na_pewno_ich": "TAK. Obejrzałem plik: zawiera wprost napis „A.S TCHÓRZEWSKI\". Profil FB, z którego pochodzi, potwierdzony numerem 667 434 222 widocznym na ich grafice (komentarz Automatu na karcie CRM, 21.08.2026 12:17). ⚠️ To awatar (JPG 719×719, białe tło wtopione), nie plik źródłowy — klient obiecał wysłać logo wieczorem 07.09; do czasu dostarczenia nie nadaje się na duże użycie ani na przezroczyste tło."
    },
    {
     "co": "Galeria dema: hero.jpg, about.jpg, g1–g14.jpg (16 zdjęć wnętrz, łazienek, gładzi)",
     "skad": "/Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/img/ — pobrane z Pexels przez silnik dem",
     "czy_na_pewno_ich": "NIE — to na pewno NIE ICH zdjęcia. Stock Pexels, wpisany wprost w komentarz Automatu na karcie CRM: „galeria to stock Pexels dobrany pod wykończenia wnętrz\". ⛔ Na płatnej stronie nie wolno ich użyć — demo mówi o nich „Każdy z tych kadrów to czyjś dom albo mieszkanie\", co przy stocku jest po prostu nieprawdą."
    },
    {
     "co": "Zdjęcia realizacji od klienta",
     "skad": "Klient — obiecał wysłać wieczorem 07.09.2026 („zdjęcia dośle wieczorem\")",
     "czy_na_pewno_ich": "BRAK — nic jeszcze nie przyszło. Sprawdzone: skrzynka Krzysztofa (zero maili od klienta poza rejestracją domeny), WhatsApp Desktop i iMessage (zero wiadomości z numerów 667 434 222 / 724 795 855 / 882 832 244). Materiały idą do Adama, nie do Krzysztofa — trzeba je od niego odebrać."
    },
    {
     "co": "Zdjęcia z Facebooka i Instagrama firmy",
     "skad": "FB https://www.facebook.com/people/AS-Tch%C3%B3rzewski/61589974670830/ i IG https://www.instagram.com/a.s_tchorzewski/ — zgłoszone do kolejki sociali 21.08.2026",
     "czy_na_pewno_ich": "Profile TAK (numer 667 434 222 na ich własnej grafice — komentarz Automatu na karcie CRM). Zdjęcia — jeszcze nie mamy: automat headless oddał tylko klatki reelsów w 640 px i kolaż, „za małe i za słabe na hero/galerię\". Trzeba dociągnąć przeglądarką z Maca (skill kolejka-sociali / social-foto)."
    },
    {
     "co": "RECON.md i brief.json z biblioteki dema",
     "skad": "/Users/krzysztof/.claude/skills/strona-klienta/imglib/klienci/a-s-tchorzewski/RECON.md",
     "czy_na_pewno_ich": "⛔ NIE — plik zawiera CUDZE profile: IG „alkoholik_z_tiktoka\", TikTok „goskaserafin\", FB „nekla.eu\", a nagłówek mówi „(Nekla)\", choć firma siedzi w Błońsku pod Rakoniewicami. Recon pomylił firmę. Nie brać stąd żadnego linku ani zdjęcia — prawidłowe profile są w komentarzu Automatu na karcie CRM i w gotowym demie."
    },
    {
     "co": "Teksty 5 podstron dema (index, oferta, realizacje, o-nas, kontakt)",
     "skad": "https://impulseo-pl.github.io/a-s-tchorzewski/ · repo lokalne /Users/krzysztof/Desktop/Impulseo/dema/a-s-tchorzewski/",
     "czy_na_pewno_ich": "NIE — to teksty napisane przez nasz silnik 21.08.2026, zanim ktokolwiek rozmawiał z klientem o treści (checklista powstała dopiero 07.09). Wolno je zmieniać w całości. ⚠️ Ale klient KUPIŁ na podstawie tego dema i mógł je przeczytać — zanim wytniemy „darmową wycenę\" czy Wolsztyn, warto go zapytać, a nie po cichu podmienić."
    },
    {
     "co": "Zakres zamówienia (zastępuje §1 umowy) i dane rejestrowe",
     "skad": "CRM Supabase: orders/order_items zamówienia IMP/2026/09/005 (order_id 48), zrzut ekranu panelu z 07.09.2026 11:25",
     "czy_na_pewno_ich": "TAK — zamówienie na NIP 9950044465, mail a.s-tchorzewski@wp.pl, status Paynow CONFIRMED, opłacone 06.09.2026 07:28, dokumenty zaakceptowane 06.09 09:24 z zapisem akceptacji."
    }
   ],
   "uwagi": "🔴 NAJWAŻNIEJSZE ZASTRZEŻENIE, żeby nie powtórzyć wpadki „wyciąłem zdania klienta biorąc je za frazesy\\\": wszystkie 15 linijek z notatki Adama to głos klienta, także te, które brzmią jak nudna administracja („8-20 godziny działania\\\", „Mail ten co wysyłałem\\\"). W tej checkliście NIE MA ani jednego frazesu marketingowego do wycięcia — klient nie powiedział ani słowa o jakości, pasji czy zadowoleniu. Jeśli w trakcie redakcji coś będzie wyglądało na frazes, to prawie na pewno pochodzi z DEMA (nasze), nie od niego.\n\n⚠️ Precyzja źródła: to nie są nagrane, dosłowne słowa klienta — to notatka Adama spisana w trakcie/po rozmowie telefonicznej 07.09.2026 o 11:11. Cytuję ją znak w znak (z literówkami „montaż dziwi okien\\\", „Polskę firmę\\\", „wyślę mi\\\"), ale sformułowania są ręką Adama. Treść i polecenia = klienta; dokładna składnia = handlowca. Dlatego nie wolno tych zdań przeklejać na stronę jako cytatów z klienta, natomiast nie wolno też zmieniać ich SENSU bez jego zgody.\n\n📞 Rozmówcą był najpewniej syn (724 795 855), nie Artur — Adam pisze o firmie w trzeciej osobie, a karta CRM mówi wprost, że finalizacja czekała na powrót syna z urlopu. Pytania z sekcji „luki\\\" kierować na numer syna.\n\n🔻 Największa dziura merytoryczna: demo, na podstawie którego klient kupił, w pięciu miejscach mówi coś innego niż on sam (Wolsztyn zamiast dwóch województw, darmowa wycena, malowanie agregatem, proces 01–04 z umową i odbiorami, „od 20 lat\\\" zamiast „ponad 20 lat\\\"), a jednocześnie nie zawiera czterech rzeczy, o które prosił (drzwi i okna, polecanie sprawdzonych osób, godziny 8–20, WhatsApp). Zamówienie daje JEDNĄ rundę poprawek — te rozbieżności trzeba domknąć pytaniami PRZED oddaniem strony, inaczej zjedzą całą rundę.\n\n🖼️ Blokada wykonawcza: zamówienie mówi „zdjęcia i teksty na podstawie udostępnionych materiałów\\\", a udostępnionych materiałów na dziś NIE MA — jest tylko awatar FB jako logo i 16 zdjęć stockowych, których na płatnej stronie użyć nie wolno. Zdjęcia realizacji + plik logo + długość gwarancji były obiecane na wieczór 07.09 i idą do Adama; bez nich strona stoi."
  }
 },
 {
  "tor": "konkurencja",
  "dane": {
   "tor": "TOR 4 — KONKURENCJA LOKALNA",
   "fakty": [
    {
     "stwierdzenie": "W bezpośredniej okolicy klienta (gmina Rakoniewice, powiat grodziski) firmy wykończeniowe praktycznie NIE MAJĄ własnych stron — istnieją wyłącznie jako wizytówki na Facebooku i wpisy w katalogach (Oferteo, pkt.pl, OLX, baza firm gminy Rakoniewice, nieruchomosci-online).",
     "zrodlo": "Wyszukiwanie z wykluczeniem portali: http://rakoniewice.pl/asp/en_start.asp?typ=3 · https://www.pkt.pl/szukaj/wyko%C5%84czenie-wn%C4%99trz/wielkopolskie-grodziski-tarnowa · https://www.facebook.com/people/Firma-wyko%C5%84czenia-wn%C4%99trz/100063704754298/ · https://aleo.com/pl/firma/matii-projekt-mateusz-krys-rakoniewice",
     "pewnosc": "prawdopodobny",
     "uzycie": "Argument sprzedażowy do klienta i uzasadnienie mocnego SEO lokalnego — strona da mu przewagę, której lokalni konkurenci nie mają. NIE pisać tego na stronie."
    },
    {
     "stwierdzenie": "ROLICZ (Poznań, rolicz.pl) — na wejściu hasło „Licencja na wykańczanie\". Dowody: 30 lat w zawodzie, 2 dyplomy mistrzowskie, 4 autoryzacje producentów (Flügger, Rigips, Isover, Schlüter) ze skanami certyfikatów, 213 filmów na YouTube, 15,9 tys. subskrybentów, gwarancja wieczna Rigips i 50-letnia Isover.",
     "zrodlo": "https://rolicz.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Poprzeczka dowodowa w regionie. Pokazuje, że samo „ponad 20 lat doświadczenia\" u naszego klienta NIE jest wyróżnikiem — ktoś obok ma 30 lat i papiery."
    },
    {
     "stwierdzenie": "ROLICZ NIE MA: formularza kontaktowego, cennika usług (tylko „Zadzwoń i zapytaj\"), żadnego terminu wyceny ani terminu realizacji, i tylko JEDNĄ opinię tekstową. Strona nie wygląda na szablon (kod pisany na miarę), obszar: „Poznań i okolice\".",
     "zrodlo": "https://rolicz.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Luka do zajęcia: konkretny termin wyceny + formularz."
    },
    {
     "stwierdzenie": "REMPERFEKT (Poznań, remperfekt.pl) — hasło „Jakość mamy nie tylko w nazwie. Przekonaj się!\". Dowody: 12 opinii Google 5/5 wciągniętych na stronę wtyczką TrustIndex, galeria „przed/po\", grafiki dyplomu i nagrody bez opisu. 11 pozycji usług w menu, godziny pon.-sob. 07:00-21:00.",
     "zrodlo": "https://remperfekt.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Wzorzec, ile treści sensownie zmieścić w menu; sekcja „przed/po\" warta skopiowania, gdy klient przyśle zdjęcia."
    },
    {
     "stwierdzenie": "REMPERFEKT ma widoczny błąd: liczniki statystyk (lata doświadczenia, liczba realizacji, zużyta farba) wyświetlają się jako „0 +\" zamiast liczb — animacja licznika nie odpala. Strona to WordPress + Elementor, szablon widoczny gołym okiem.",
     "zrodlo": "https://remperfekt.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Ostrzeżenie dla nas: nie robić animowanych liczników. Jeśli dajemy liczby, mają być statyczne."
    },
    {
     "stwierdzenie": "PK FLIZ (Poznań, pk-fliz.pl) — na wejściu cytat Kurta Vonneguta zamiast oferty. ZERO liczb: brak lat działalności, brak liczby realizacji, brak liczby ludzi. Deklaruje się jako firma rodzinna przekazująca fach „z pokolenia na pokolenie\".",
     "zrodlo": "https://pk-fliz.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Dowód, że „firma rodzinna\" bez liczb to pusty frazes — u nas rodzinność MUSI iść w parze z datami 2005/2015."
    },
    {
     "stwierdzenie": "PK FLIZ NIE MA: cennika, terminu wyceny, gwarancji ani treści opinii (jest sekcja „Opinie klientów napawają nas dumą!\", ale to sam link do Google Maps — żadna opinia nie jest przepisana na stronę). Szablon WordPress, układ „5 kroków współpracy\" typowy dla gotowców remontowych.",
     "zrodlo": "https://pk-fliz.pl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Luka: przepisać 2-3 realne opinie na stronę, nie odsyłać do Map."
    },
    {
     "stwierdzenie": "LUX-DOM (Oleśnica k. Zagórowa, lux-dom.com) — hasło „Kompleksowe remonty i wykończenia wnętrz na terenie Wielkopolski\", 20 lat doświadczenia zdobytego w Polsce i Norwegii. To najbliższy odpowiednik naszego klienta: ta sama liczba lat i ta sama historia „doświadczenie z zagranicy\".",
     "zrodlo": "https://lux-dom.com/",
     "pewnosc": "potwierdzony",
     "uzycie": "🔴 Kluczowe: sam wątek „pracowaliśmy za granicą\" NIE jest wyróżnikiem w Wielkopolsce. Trzeba go uzbroić w konkret (dwie daty, dwa rynki), inaczej brzmi jak u każdego."
    },
    {
     "stwierdzenie": "LUX-DOM ma na stronie dwie opinie podpisane „Jane Anderson\" i „James Head\", obie z identyczną angielską treścią o firmie „Earthly Elegance\" — to niewyczyszczone teksty zastępcze z kupionego szablonu WordPress.",
     "zrodlo": "https://lux-dom.com/ (sekcja opinii, sprawdzone 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Najostrzejszy dowód, jak nisko leży poprzeczka. Dla nas: bramka „zero tekstów zastępczych\" przed oddaniem strony."
    },
    {
     "stwierdzenie": "LUX-DOM NIE MA: gwarancji, cennika, terminu wyceny ani terminu realizacji. Menu jest czterozakładkowe (Usługi, Realizacje, O nas, Kontakt), zdjęć realizacji tylko 3.",
     "zrodlo": "https://lux-dom.com/",
     "pewnosc": "potwierdzony",
     "uzycie": "Nasze 5 podstron + porządna galeria od razu wygrywa objętością treści."
    },
    {
     "stwierdzenie": "ART-BART DEVELOPMENT (Bartłomiej Synoradzki, Dopiewo, abde.pl) — jedyna znaleziona firma z własną stroną, która wprost obsługuje TEREN NASZEGO KLIENTA: deklaruje Nowy Tomyśl, Grodzisk Wielkopolski, Kościan, Leszno i ponad 23 miasta w wielkopolskim, lubuskim, pomorskim i śląskim.",
     "zrodlo": "https://abde.pl/uslugi-budowlane/wykonczenia-wnetrz/",
     "pewnosc": "potwierdzony",
     "uzycie": "To realny konkurent w wyszukiwarce na frazy „wykończenia wnętrz Grodzisk Wielkopolski\"."
    },
    {
     "stwierdzenie": "ART-BART obiecuje na wejściu „Nowoczesne Domy i Osiedla Wielkopolska\" i celuje w deweloperów oraz stany surowe — wykończenia wnętrz to u niego 9. pozycja z 11 usług, obok wierceń studni i geotermii. NIE MA: cen, terminów, gwarancji, opinii, certyfikatów. WordPress, polityka prywatności z 2020 r.",
     "zrodlo": "https://abde.pl/uslugi-budowlane/wykonczenia-wnetrz/",
     "pewnosc": "potwierdzony",
     "uzycie": "Wyróżnik naszego klienta: on robi WYŁĄCZNIE wykończenia wnętrz dla osoby prywatnej, nie jest generalnym wykonawcą osiedli. To dwa różne telefony."
    },
    {
     "stwierdzenie": "ŻADNA z sześciu sprawdzonych firm nie podaje na stronie TERMINU, w jakim odda wycenę. Wszystkie kończą na „darmowa wycena\", „niezobowiązująca wycena\", „szybka wycena\" albo „zadzwoń i zapytaj\". Termin 24 h daje tylko portal pośredniczący Fixly, nie firma.",
     "zrodlo": "rolicz.pl · remperfekt.pl · pk-fliz.pl · lux-dom.com · abde.pl · sites.google.com/view/remonty-kundzik (wszystkie sprawdzone 07.09.2026) · https://fixly.pl/kategoria/wykonczenie-pod-klucz/poznan",
     "pewnosc": "potwierdzony",
     "uzycie": "🔴 TO JEST WYRÓŻNIK NA STRONĘ GŁÓWNĄ. „Wycena do 5 dni roboczych\" z briefu klienta to jedyna twarda obietnica terminowa na tym rynku."
    },
    {
     "stwierdzenie": "Żadna ze sprawdzonych firm nie deklaruje na stronie, co robi z zapytaniem o usługę, której nie wykonuje. Nikt nie obiecuje polecenia sprawdzonego fachowca z innej branży.",
     "zrodlo": "rolicz.pl · remperfekt.pl · pk-fliz.pl · lux-dom.com · abde.pl · sites.google.com/view/remonty-kundzik",
     "pewnosc": "potwierdzony",
     "uzycie": "Wyróżnik z briefu („pytają o usługi, których nie robimy → polecamy sprawdzone osoby\") — jedyny w zestawie. Sekcja na stronie głównej albo w „O nas\"."
    }
   ],
   "luki": [
    "🔴 GWARANCJA — ile lat? Brief mówi, że jest w umowie i klient miał podać wieczorem 07.09. To najmocniejszy dowód po stronie konkurencji (ROLICZ chwali się gwarancją wieczną Rigips i 50-letnią Isover) i jedna z niewielu rzeczy, którymi da się bić po liczbie. Bez tego zostaje pusty przymiotnik.",
    "Czy mają papiery zawodowe albo autoryzacje producentów (Knauf, Rigips, Śnieżka, Caparol, Flügger, Schlüter)? Dwóch z sześciu konkurentów wjeżdża tym na wejściu. Jeśli klient coś ma — skan na stronę.",
    "Ile realizacji rocznie / ile mieszkań albo łazienek dotąd zrobili? Konkurenci albo nie podają żadnych liczb (PK FLIZ, ART-BART), albo mają zepsute liczniki (REMPERFEKT). Jedna prawdziwa liczba wygrywa całą tę sekcję rynku.",
    "Ile osób liczy ekipa i kto do kogo należy rodzinnie (ojciec i syn? bracia?)? „Firma rodzinna\" bez tego brzmi tak samo jak u PK FLIZ, czyli jak nic.",
    "Konkretne miejscowości po stronie lubuskiej, w których pracowali (Świebodzin, Sulechów, Babimost, Zbąszynek, Międzyrzecz?). Bez nazw obietnica „wielkopolskie i lubuskie\" nie zadziała w wyszukiwarce ani w głowie klienta z pogranicza.",
    "Czy w Niemczech pracowali na własnej działalności, czy jako podwykonawcy, i w jakim regionie? LUX-DOM gra tą samą kartą (Norwegia, 20 lat) — nasz konkret musi być mocniejszy niż jego jedno zdanie.",
    "Czy „wycena do 5 dni roboczych\" liczy się od telefonu, od maila, czy od oględzin na miejscu? Skoro robimy z tego wyróżnik na stronę główną, sformułowanie musi być takie, żeby klient nie mógł się poczuć oszukany.",
    "Do jakiej wielkości zlecenia dojeżdżają bez opłaty za dojazd? Przy dwóch województwach to pierwsze pytanie klienta z Sulechowa."
   ],
   "materialy": [
    {
     "co": "Zrzuty ekranu 6 stron konkurencji (rolicz.pl, remperfekt.pl, pk-fliz.pl, lux-dom.com, abde.pl, sites.google.com/view/remonty-kundzik) — materiał porównawczy do rozmowy z klientem i do designu",
     "skad": "Do zrobienia u nas — same URL-e są w faktach powyżej",
     "czy_na_pewno_ich": "NIE nasze i NIE klienta — to cudze strony. Wolno użyć wyłącznie wewnętrznie, jako punkt odniesienia. ⛔ Zero zrzutów, treści i zdjęć konkurencji na stronie klienta."
    },
    {
     "co": "Skany certyfikatów / dyplomów / autoryzacji producenckich A.S Tchórzewski",
     "skad": "Od klienta — trzeba dopytać, nie mamy",
     "czy_na_pewno_ich": "Nie wiadomo, czy w ogóle istnieją. Pytanie jest w lukach. Nic nie wstawiamy, dopóki nie przyśle pliku."
    },
    {
     "co": "Zdjęcia realizacji (własne, nie stock)",
     "skad": "Od klienta — obiecane 07.09 wieczorem; zapasowo profil FB „A.S Tchórzewski\" i Instagram @a.s_tchorzewski",
     "czy_na_pewno_ich": "Zdjęcia z ich własnych profili FB/IG = ich. ⛔ Galeria w demie to STOCK z Pexels i musi zniknąć ze strony docelowej — tak stoi w briefie."
    }
   ],
   "uwagi": "CZYM KLIENT MOŻE SIĘ ODRÓŻNIĆ — zdanie na stronę główną:\n\n**„Wykończenia wnętrz w wielkopolskim i lubuskim — wycenę dostajecie do 5 dni roboczych. Rodzinna ekipa: w Niemczech od 2005, w Polsce od 2015.\\\"**\n\nDlaczego akurat to, a nie co innego:\n- Termin wyceny to jedyna twarda liczba, której NIE MA żadna z sześciu sprawdzonych firm. Wszyscy kończą na „darmowa/szybka/niezobowiązująca wycena\\\". Termin daje wyłącznie portal pośredniczący, nie wykonawca. To wyróżnik, którego nikt nie może skopiować bez zmiany sposobu pracy.\n- Dwa województwa: cztery z sześciu firm zamykają się w „Poznań i okolice\\\". Klient z Wolsztyna, Zbąszynia czy Świebodzina nie ma dziś do kogo zadzwonić z własnej okolicy.\n- Dwie daty zamiast „ponad 20 lat doświadczenia\\\": to samo „20 lat + zagranica\\\" ma już LUX-DOM (Norwegia). Liczba lat jest zajęta, daty nie.\n\n⛔ CZYM SIĘ NIE ODRÓŻNI (nie budować na tym strony głównej):\n- „ponad 20 lat doświadczenia\\\" — ROLICZ ma 30 lat i dwa dyplomy mistrzowskie, LUX-DOM ma dokładnie 20.\n- „firma rodzinna\\\" — PK FLIZ pisze „z pokolenia na pokolenie\\\", to frazes bez liczb.\n- „kompleksowo\\\", „solidnie\\\", „terminowo\\\", „indywidualne podejście\\\" — jest u wszystkich, po angielsku i po polsku.\n\nDRUGI WYRÓŻNIK, wart osobnej sekcji (nie hero): nikt na tym rynku nie mówi, co robi z zapytaniem o usługę spoza swojego zakresu. Brief mówi wprost, że nasz klient poleca sprawdzone osoby. To ludzki konkret, którego nie ma żaden konkurent.\n\nOSTRZEŻENIE JAKOŚCIOWE dla naszej roboty — trzy błędy, które widać u konkurencji i których u nas nie może być:\n1. LUX-DOM ma na żywej stronie opinie „Jane Anderson\\\" i „James Head\\\" o firmie „Earthly Elegance\\\" — teksty zastępcze z szablonu. Bramka: zero tekstów zastępczych.\n2. REMPERFEKT ma liczniki statystyk pokazujące „0 +\\\" — animacja nie odpala. Bramka: liczby statyczne, żadnych animowanych liczników.\n3. PK FLIZ i Adam Kundzik mają sekcje „opinie\\\" bez ani jednej opinii, sam link do Map. Bramka: albo przepisujemy 2-3 realne opinie na stronę, albo nie robimy sekcji.\n\nRYZYKO DO ZWERYFIKOWANIA: nie znalazłem ani jednej firmy wykończeniowej z powiatu grodziskiego albo wolsztyńskiego z własną stroną — tylko Facebook i katalogi. Nie mogę wykluczyć, że taka istnieje, a nie wyszła w wyszukiwarce (małe firmy bywają niewidoczne w Google). Oznaczyłem to jako „prawdopodobny\\\", nie „potwierdzony\\\", i nie stawiałbym tego twierdzenia w tekście na stronie."
  }
 },
 {
  "tor": "szukajacy",
  "dane": {
   "tor": "TOR 5 — czego szuka klient końcowy (Firma Ogólnobudowlana Artur Tchórzewski / A.S TCHÓRZEWSKI, Błońsko 46, NIP 9950044465)",
   "fakty": [
    {
     "stwierdzenie": "Zakres usług tej firmy (szpachlowanie, malowanie, łazienki, sucha zabudowa, montaż drzwi i okien) to typowy zestaw prac ETAPU WYKOŃCZENIOWEGO — czyli klient trafia do nich dopiero wtedy, gdy budynek stoi i ma tynki albo gdy stare wnętrze idzie do rozbiórki.",
     "zrodlo": "BRIEF-KLIENTA.md (checklista Adama po rozmowie z klientem, 07.09.2026), sekcja „Zakres usług (słowa klienta)”",
     "pewnosc": "potwierdzony",
     "uzycie": "Podział strony na trzy ścieżki wejścia: „buduję dom / odbieram mieszkanie od dewelopera”, „remontuję to, w czym mieszkam”, „mam jedno konkretne pomieszczenie (łazienka)”."
    },
    {
     "stwierdzenie": "Realne zapytania klientów w tym regionie są formułowane zadaniami i metrami, nie nazwami usług — dosłownie: „Położenie gładzi na gotowo ściany i sufity 3 pomieszczenia około 200m2 plus malowanie”, „Szpachlowanie ścian i sufitow, malowanie na bialo, panele na całości oprócz lazienek”, „Wyrównanie scian, tynkowanie, częsciowe malowanie, plytka podlogowa i scienna”, „Generalny remont pomieszczenia gospodarczego na kuchnię letnią”.",
     "zrodlo": "https://www.oferteo.pl/wykonczenia-wnetrz/swiebodzin (cytaty zleceń klientów, odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Nazwy usług i nagłówki na podstronach pisać językiem zlecenia („gładzie i malowanie całego mieszkania”), a formularz kontaktowy zbudować wokół pól: co za pomieszczenia, ile metrów, co ma być zrobione."
    },
    {
     "stwierdzenie": "Połowa Polaków szuka usługodawcy przez polecenia znajomych, 44% przez wyszukiwarkę Google, 27% przez social media, po 20% przez Mapy Google i portale branżowe — a polecenia są dziś WERYFIKOWANE w internecie.",
     "zrodlo": "Badanie Insight Lab dla WeNet i Polskich ePłatności, opis: https://strefabiznesu.pl/google-zastapilo-sasiadke-tak-polacy-szukaja-dzis-fachowcow/ar/c3p2-29317983",
     "pewnosc": "prawdopodobny",
     "uzycie": "Główna funkcja strony to nie „zdobycie nowego klienta z Google”, tylko POTWIERDZENIE polecenia — ktoś usłyszał nazwisko, wpisuje je w Google i musi w 5 sekund zobaczyć, że firma jest prawdziwa: nazwisko, wieś, numer, twarze, zdjęcia robót."
    },
    {
     "stwierdzenie": "76,1% Polaków miało problemy z fachowcami; najczęściej wskazywane to niezadowalająca jakość wymagająca poprawek (22,9%) i znaczne opóźnienia (22,7%), dalej przekroczenie kosztów, nieobecność w umówionym terminie i dodatkowe opłaty.",
     "zrodlo": "Raport „Doświadczenia Polaków z fachowcami. Edycja 2026” (badanie CAWI, materiał prasowy MondayNews Polska, sierpień 2026), za: https://www.komercja24.pl/wykanczanie-wnetrz-nieruchomosci-ponad-trzy-czwarte-polakow-ma-klopoty-z-fachowcami/",
     "pewnosc": "potwierdzony",
     "uzycie": "Klient wchodzi na stronę z GOTOWYM STRACHEM, nie z ciekawością — sekcja „jak pracujemy” musi wprost odpowiadać na te cztery lęki (termin, poprawki, kosztorys bez niespodzianek, obecność na budowie), a nie chwalić firmę."
    },
    {
     "stwierdzenie": "W starszym badaniu 62,7% osób remontujących deklarowało problemy z ekipami, przy czym wśród szukających przez rodzinę/znajomych było to 74%, a wśród zlecających firmom 50% — czyli problem dotyka też poleceń.",
     "zrodlo": "Opis badania na https://www.budnet.pl/Fachowcy_pod_lupa_Polakow_Klienci_glownie_skarza_sie_na_jakosc_terminy_i_koszty_uslug,Analizy_badania_raporty,152954-czytaj.html oraz https://www.isprzet.pl/pl/jak-remontuja-polacy-raport-2021.html",
     "pewnosc": "prawdopodobny",
     "uzycie": "Argument, że sama „firma z polecenia” nie wystarcza — strona ma pokazać dowody (umowa, gwarancja, zdjęcia zakończonych robót), a nie tylko zaufanie z drugiej ręki."
    },
    {
     "stwierdzenie": "Ocena wyglądu strony powstaje w około 50 milisekund i praktycznie nie zmienia się po dziesięciokrotnie dłuższym oglądaniu (korelacja r = 0,947 między oceną po 50 ms a po 500 ms).",
     "zrodlo": "Lindgaard i in., „Attention web designers: You have 50 milliseconds to make a good first impression!”, Behaviour & Information Technology 25(2), 2006 — https://www.researchgate.net/publication/220208334_Attention_web_designers_You_have_50_milliseconds_to_make_a_good_first_impression_Behaviour_and_Information_Technology_252_115-126",
     "pewnosc": "potwierdzony",
     "uzycie": "Pierwszy ekran na telefonie musi być rozstrzygnięty jednym zdjęciem PRAWDZIWEJ roboty — nie stockiem, nie sloganem. Stock w tej branży czyta się jako „ktoś ściągnął szablon”."
    },
    {
     "stwierdzenie": "W pierwszym ekranie na telefonie klient końcowy szuka czterech rzeczy naraz: CO robicie, GDZIE (moja miejscowość), DOWÓD (zdjęcie/opinie) i JAK SIĘ ODEZWAĆ — przy czym przycisk kontaktu powinien być widoczny cały czas, niezależnie od miejsca na stronie, a przycisk „napisz na WhatsApp” obsługuje tych, którzy przy pierwszym kontakcie wolą napisać niż dzwonić.",
     "zrodlo": "https://cyberfolks.pl/blog/jak-przyciagnac-klientow-do-firmy-remontowej/ oraz https://artnova.com.pl/blog/strona-www-dla-firmy-budowlanej-jak-stworzyc/ (poradniki branżowe, nie badanie)",
     "pewnosc": "prawdopodobny",
     "uzycie": "Sticky pasek na dole ekranu mobilnego: [Zadzwoń 667 434 222] [WhatsApp 882 832 244]. Klient MA osobny numer WhatsApp — to trzeba wykorzystać, bo część ludzi nie zadzwoni nigdy."
    },
    {
     "stwierdzenie": "Klient końcowy w tej branży pyta przede wszystkim o pieniądze i czas: „ile to kosztuje za m²”, „ile kosztuje remont łazienki”, „ile trwa”, „czy w cenie jest materiał” — to dominujący temat wyszukiwań w tej kategorii.",
     "zrodlo": "Tytuły najwyżej rankingujących stron dla tej kategorii: https://www.oferteo.pl/artykuly/koszt-wykonczenia-mieszkania, https://www.lazienkaplus.pl/pl/porady/koszt-remontu-lazienki-440/, https://www.blu.com.pl/blog/post/ile-kosztuje-robocizna-za-zrobienie-lazienki-w-2026-roku-prognoza-stawek-i-przykladowe-wyceny",
     "pewnosc": "potwierdzony",
     "uzycie": "Podstrona „Wycena / Cennik” jest obowiązkowa — nawet bez cen. Ma tłumaczyć, OD CZEGO zależy cena i CO klient dostaje w kosztorysie, bo inaczej wyjdzie szukać tej odpowiedzi u konkurencji."
    },
    {
     "stwierdzenie": "Rynkowe punkty odniesienia, z którymi klient przychodzi na stronę: wykończenie pod klucz ok. 1 600–3 000 zł/m² netto (2026), robocizna remontu łazienki 4–5 m² ok. 10 000–18 000 zł (2026), szpachlowanie i szlifowanie 15–35 zł/m², zabudowa GK ok. 40–60 zł/m².",
     "zrodlo": "https://www.extradom.pl/porady/artykul-ile-kosztuje-wykonczenie-domu-ze-stanu-deweloperskiego-pod-klucz, https://www.blu.com.pl/blog/post/ile-kosztuje-robocizna-za-zrobienie-lazienki-w-2026-roku-prognoza-stawek-i-przykladowe-wyceny, https://gipsowy-remont.pl/sucha-zabudowa-cennik",
     "pewnosc": "prawdopodobny",
     "uzycie": "Tylko jako kontekst dla nas — NIE publikować cudzych stawek jako swoich. Przydaje się do napisania sekcji „od czego zależy wycena” tak, żeby nie kłóciła się z rynkiem."
    },
    {
     "stwierdzenie": "Konkurencja lokalna na tych frazach jest gęsta i zdominowana przez AGREGATORY (Oferteo, Daibau, Muratordom, MamFach, Favore, pkt.pl), a nie przez własne strony firm — sam ranking „Malowanie Grodzisk Wielkopolski” w Oferteo wykazuje 278 firm.",
     "zrodlo": "https://www.oferteo.pl/malarze/grodzisk-wielkopolski (odczyt 07.09.2026), https://www.daibau.pl/firmy/remont_mieszkania/grodzisk_wielkopolski_62-065, https://zlecenia-budowlane.muratordom.pl/remont/wolsztyn",
     "pewnosc": "potwierdzony",
     "uzycie": "Strona nie wygra z agregatorami na ogólne „remonty Wolsztyn”. Wygra na NAZWIE („tchórzewski”, „a.s tchórzewski”) i na wąskich frazach usługa+wieś/gmina — i tak ma być zbudowana architektura podstron."
    },
    {
     "stwierdzenie": "Konkurenci widoczni w tych samych rankingach mają po 7–18 opinii z ocenami 4,6–5,0 (np. AP Krupscy 5,0/5 z 15 opinii, Bud-Paweł 4,78/5 z 18 opinii) — to jest poziom dowodu społecznego, z którym A.S Tchórzewski jest porównywany.",
     "zrodlo": "https://www.oferteo.pl/malarze/grodzisk-wielkopolski (odczyt 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja opinii jest bramką, nie ozdobą — bez niej strona przegrywa porównanie. Jeśli klient nie ma opinii Google, trzeba to uruchomić przy oddaniu strony (i tak robimy Wizytówkę)."
    },
    {
     "stwierdzenie": "Nie znaleziono ŻADNYCH publicznych opinii o firmie A.S Tchórzewski w portalach branżowych ani wyników z jej wizytówki poza samym wpisem w Mapach Google.",
     "zrodlo": "Wyszukiwanie „A.S Tchórzewski Błońsko Rakoniewice opinie firma ogólnobudowlana” (07.09.2026) — zero trafień o tej firmie",
     "pewnosc": "potwierdzony",
     "uzycie": "Odwiedzający, który sprawdza firmę, NIC nie znajdzie poza naszą stroną i FB/IG — więc strona musi sama nieść dowód (zdjęcia realizacji, konkretne miejscowości, dane rejestrowe, gwarancja z umowy)."
    },
    {
     "stwierdzenie": "Współrzędne z podanego linku do wizytówki Google (52,3798 N; 17,4407 E) leżą ok. 85 km na wschód od Błońska w gminie Rakoniewice — czyli pinezka wizytówki NIE stoi pod adresem rejestrowym firmy.",
     "zrodlo": "URL wizytówki podany w zleceniu + obliczenie odległości od Błońska (52,14 N; 16,26 E)",
     "pewnosc": "potwierdzony",
     "uzycie": "🔴 Do sprawdzenia z klientem przed oddaniem strony: jeśli pinezka stoi 85 km od bazy, klient z Wolsztyna/Grodziska widzi w Mapach firmę „z drugiego końca województwa” i nie dzwoni. Naprawa wizytówki jest warta więcej niż połowa strony."
    },
    {
     "stwierdzenie": "Obecne demo mówi „Wolsztyn i okolice” i podaje adres „Błońsko 46, 64-308 Jabłonna”, podczas gdy klient zadeklarował obszar „województwo wielkopolskie i lubuskie”, a w rejestrze figuruje „64-308 Błońsko”.",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (odczyt 07.09.2026) vs BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Na stronie docelowej geografia musi być jednoznaczna i szersza niż w demie — inaczej klient z Sulechowa albo Świebodzina uzna, że firma do niego nie dojedzie i nie zadzwoni."
    },
    {
     "stwierdzenie": "Frazy rodziny „usługa + miasto” są realnie używanymi nazwami kategorii w portalach obsługujących ten teren: „wykończenia wnętrz Świebodzin”, „remonty Wolsztyn”, „remonty Nowy Tomyśl”, „malowanie Grodzisk Wielkopolski”, „wykończenia łazienek Nowy Tomyśl”, „remont mieszkania Grodzisk Wielkopolski”, „malowanie mieszkań Grodzisk Wielkopolski”.",
     "zrodlo": "Tytuły stron kategorii: https://www.oferteo.pl/wykonczenia-wnetrz/swiebodzin, https://www.oferteo.pl/remonty/wolsztyn, https://www.oferteo.pl/remonty/nowy-tomysl, https://www.oferteo.pl/malarze/grodzisk-wielkopolski, https://www.oferteo.pl/wykonczenia-lazienek/nowy-tomysl",
     "pewnosc": "potwierdzony",
     "uzycie": "Wzorzec nazywania podstron i nagłówków H1: <usługa> + <miasto>, a nie „nasza oferta”. Miasta z zasięgu: Wolsztyn, Grodzisk Wielkopolski, Rakoniewice, Nowy Tomyśl, Zbąszyń, Opalenica, Wielichowo, Kamieniec, Babimost, Kargowa, Sulechów, Świebodzin, Zbąszynek, Leszno, Poznań."
    },
    {
     "stwierdzenie": "Gmina Rakoniewice sąsiaduje bezpośrednio z gminami Kamieniec, Wielichowo, Granowo i Rostarzewem — te nazwy występują jako lokalne frazy przy Grodzisku Wielkopolskim.",
     "zrodlo": "https://www.oferteo.pl/malarze/grodzisk-wielkopolski (lista gmin w sekcji lokalnej)",
     "pewnosc": "potwierdzony",
     "uzycie": "Lista miejscowości w stopce i na podstronie „Obszar działania” — dokładnie te nazwy ludzie dopisują do zapytań."
    },
    {
     "stwierdzenie": "Bezpośrednim konkurentem o tym samym profilu w promieniu kilkunastu kilometrów jest m.in. Firma Ogólnobudowlana Tomasz Bańdur (Przyprostynia, gmina Zbąszyń, działa od sierpnia 2011), oferująca malowanie, kompleksowe remonty wnętrz, wykończenia łazienek, płytki, zabudowę GK i szpachlowanie.",
     "zrodlo": "Wynik wyszukiwania kategorii remontowych dla Zbąszynia/Nowego Tomyśla (07.09.2026), opis firmy w portalu branżowym",
     "pewnosc": "prawdopodobny",
     "uzycie": "Przewagi, które trzeba wyeksponować, bo konkurent ich nie ma: 20+ lat i praca w Niemczech od 2005, firma rodzinna, polecanie sprawdzonych fachowców do prac spoza zakresu, godziny 8–20."
    },
    {
     "stwierdzenie": "Klient końcowy oczekuje, że fachowiec „nie powie na dzień dobry, że się nie da”, okaże rachunki i faktury, posprząta po sobie i nie zniszczy niczego w mieszkaniu — to najczęściej powtarzane kryteria wyboru ekipy w poradnikach konsumenckich.",
     "zrodlo": "https://pewnylokal.pl/porady/ekipa-remontowa-na-co-zwrocic-uwage, https://klink.pl/blog/jak-wybrac-ekipe-remontowa.html, https://rynekpierwotny.pl/wiadomosci-mieszkaniowe/jak-znalezc-dobrego-wykonawce/9705/",
     "pewnosc": "prawdopodobny",
     "uzycie": "Cztery konkretne obietnice do sekcji „Jak pracujemy”: faktura VAT, sprzątanie po etapie, zabezpieczenie tego, co zostaje, i pisemna gwarancja. Warte więcej niż jakikolwiek slogan."
    },
    {
     "stwierdzenie": "To, że firma po prostu ODBIERA TELEFON i przyjeżdża w umówionym terminie, jest w tej branży realnym wyróżnikiem — brak kontaktu i znikanie wykonawcy to najczęściej opisywany scenariusz porażki klienta.",
     "zrodlo": "https://www.money.pl/gospodarka/polacy-w-pulapce-remontowej-to-juz-prawdziwa-plaga-6926672020531904a.html (relacje poszkodowanych; artykuł dziennikarski, bez badania) + raport „Doświadczenia Polaków z fachowcami. Edycja 2026”",
     "pewnosc": "prawdopodobny",
     "uzycie": "Godziny 8–20 z briefu to nie detal w stopce, tylko HASŁO pierwszego ekranu: „Odbieramy 8–20, siedem dni w tygodniu” (do potwierdzenia, czy także w weekendy)."
    },
    {
     "stwierdzenie": "Brak jakiejkolwiek informacji o cenie działa na niekorzyść mikrofirmy mocniej niż na niekorzyść dużej marki, bo mała firma musi szybciej udowodnić, że jest konkretna i szanuje czas odbiorcy.",
     "zrodlo": "https://portalmarketingowy.pl/strony-www,ac229/jak-pokazac-ceny-na-stronie-uslugowej-cennik-widelki-pakiety-i-zasady-wyceny-ktore-zwiekszaja-liczbe-zapytan-zamiast-odstraszac-klientow,1242 (opinia branżowa, nie badanie)",
     "pewnosc": "prawdopodobny",
     "uzycie": "Zamiast cennika (klient go nie chce) — „od czego zależy cena” + „co dostajesz w kosztorysie” + ewentualne widełki na jedną usługę wejściową, jeśli klient się zgodzi."
    },
    {
     "stwierdzenie": "Firma deklaruje, że przy usługach, których nie wykonuje, poleca sprawdzone osoby — to zachowanie odpowiada na realną potrzebę klienta, który przy wykończeniu potrzebuje kilku branż naraz (hydraulik, elektryk, glazurnik) i nie chce koordynować ich sam.",
     "zrodlo": "BRIEF-KLIENTA.md, sekcja „Zakres usług (słowa klienta)”: „Pytają o usługi, których nie robią → poleca sprawdzone osoby”",
     "pewnosc": "potwierdzony",
     "uzycie": "Osobny blok na stronie głównej: „Nie robimy wszystkiego — ale wiemy, kto zrobi”. To jest anty-lęk „będę musiał sam zbierać ekipy”, którego konkurencja nie adresuje."
    }
   ],
   "luki": [
    "Ile realnie trwa PIERWSZA odpowiedź na telefon/wiadomość (nie kosztorys)? Bez tego nie da się napisać obietnicy kontaktu, a „wycena do 5 dni” sama w sobie odstrasza.",
    "Czy godziny 8–20 obowiązują siedem dni w tygodniu, czy tylko w dni robocze? Na stronie musi być jedno zdanie bez „ok.”.",
    "Czy numer WhatsApp 882 832 244 jest realnie obsługiwany (ktoś czyta i odpisuje), czy to numer prywatny? Jeśli nie — nie wolno go stawiać jako przycisku.",
    "Czy oględziny i wycena na miejscu są BEZPŁATNE i czy jest limit odległości dojazdu bez opłaty? To pytanie numer jeden przed zadzwonieniem.",
    "Jakie są realne widełki na najczęstsze zlecenie (np. gładzie + malowanie mieszkania 60 m², remont łazienki 5 m²)? Choćby „od X zł” — do decyzji klienta, czy publikujemy.",
    "Ile trwają typowe realizacje: łazienka od zera, gładzie i malowanie całego mieszkania, sucha zabudowa poddasza? Klient szuka terminu, nie tylko ceny.",
    "Jaki jest najbliższy wolny termin / jak daleko naprzód jest zapełniony grafik? Zdanie „wolne terminy od <miesiąc>” zmienia telefon z „pytam” na „rezerwuję”.",
    "Ile wynosi gwarancja z umowy (klient obiecał podać 07.09 wieczorem) i czy obejmuje robociznę, czy też materiał?",
    "Czy pracują u ludzi, którzy MIESZKAJĄ w trakcie remontu (zabezpieczenia, praca etapami, zapylenie)? To odrębna grupa klientów i odrębny lęk.",
    "Czy przyjmują zlecenia od deweloperów / na całe mieszkania w stanie deweloperskim, czy tylko od klientów prywatnych? Rozstrzyga, czy budujemy podstronę pod „odbiór mieszkania od dewelopera”.",
    "Jaka jest minimalna wartość zlecenia (czy jadą pomalować jeden pokój)? Bez tego formularz ściąga zapytania, których firma nie chce.",
    "Czy wystawiają fakturę VAT i czy przyjmują zaliczkę — a jeśli tak, w jakiej wysokości i na jakim etapie? To dwa najczęstsze pytania „bezpieczeństwa”.",
    "Czy firma ma wizytówkę Google pod właściwym adresem? Pinezka z podanego linku stoi ok. 85 km od Błońska — trzeba ustalić, czy to błąd wizytówki, czy inny podmiot.",
    "Ile firma ma dziś opinii Google i czy zgadza się na akcję zbierania opinii po oddaniu strony? Konkurencja w rankingach ma 7–18 opinii przy ocenach 4,6–5,0.",
    "Które miejscowości są PRIORYTETOWE (gdzie naprawdę chcą jeździć), a gdzie jadą tylko przy dużym zleceniu? „Wielkopolskie i lubuskie” to za szeroko, żeby napisać sensowne podstrony lokalne.",
    "Czy sprzątają po zakończeniu prac i wywożą gruz — i czy jest to w cenie? Poradniki konsumenckie stawiają to wysoko na liście kryteriów.",
    "Kto konkretnie z rodziny prowadzi robotę i czy zgadzają się na zdjęcie zespołu na stronie? Twarz przy nazwisku jest najtańszym dowodem prawdziwości firmy z polecenia.",
    "Czym się skończyła i czym była praca w Niemczech od 2005 (rodzaj zleceń, czy nadal tam pracują)? Bez konkretu to zostaje sloganem, a z konkretem jest największą przewagą nad lokalną konkurencją."
   ],
   "materialy": [
    {
     "co": "Logo firmy (obecnie awatar z profilu Facebook użyty w demie)",
     "skad": "Profil FB „A.S Tchórzewski”, pobrany przy budowie dema",
     "czy_na_pewno_ich": "TAK dla profilu — na grafice z tego profilu widnieje numer 667 434 222, zgodny z numerem z briefu Adama. ALE plik logo w jakości do druku/strony docelowej nie został jeszcze dostarczony; klient obiecał go 07.09 wieczorem (BRIEF-KLIENTA.md)."
    },
    {
     "co": "Zdjęcia realizacji (gładzie, łazienki, sucha zabudowa)",
     "skad": "Klient — obiecane 07.09 wieczorem; zapasowo profil FB i Instagram @a.s_tchorzewski",
     "czy_na_pewno_ich": "NIE MAMY ICH W OGÓLE. Galeria w demie to STOCK z Pexels — potwierdzone w BRIEF-KLIENTA.md. Do czasu dostarczenia zdjęć strona nie może być oddana, bo pierwszy ekran musi nieść prawdziwą robotę (Lindgaard: ocena wyglądu w 50 ms)."
    },
    {
     "co": "Dane rejestrowe do stopki i sekcji zaufania (NIP 9950044465, REGON 363138510, Błońsko 46, 64-308)",
     "skad": "BRIEF-KLIENTA.md, sekcja „Adres (rejestr / biała lista VAT)”",
     "czy_na_pewno_ich": "TAK — spisane z rejestru/białej listy VAT. ⚠️ Na fakturze klienta widnieje „64-308 Jabłonna”, w rejestrze „Błońsko” — przed publikacją trzeba wybrać jedną wersję i potwierdzić ją u klienta."
    },
    {
     "co": "Numery kontaktowe: telefon 667 434 222 i WhatsApp 882 832 244",
     "skad": "BRIEF-KLIENTA.md (checklista Adama, 07.09.2026); numer główny dodatkowo widoczny na grafice z profilu FB",
     "czy_na_pewno_ich": "Telefon główny — TAK, dwa niezależne źródła (brief + grafika FB). Numer WhatsApp — tylko brief; nikt nie sprawdził, czy ktoś na tym numerze odpisuje."
    },
    {
     "co": "Realne sformułowania zapytań klientów z regionu (do napisania nagłówków i pól formularza)",
     "skad": "https://www.oferteo.pl/wykonczenia-wnetrz/swiebodzin — cytaty zleceń klientów",
     "czy_na_pewno_ich": "NIE, to CUDZE zapytania z portalu ogłoszeniowego. Używamy ich wyłącznie jako materiału do sformułowań — ⛔ nigdy jako opinii, referencji ani realizacji A.S Tchórzewski."
    },
    {
     "co": "Lista miejscowości i gmin do podstron lokalnych oraz stopki",
     "skad": "https://www.oferteo.pl/malarze/grodzisk-wielkopolski (gminy sąsiednie) + deklaracja klienta „wielkopolskie i lubuskie” z briefu",
     "czy_na_pewno_ich": "Częściowo — geografia jest publiczna i sprawdzalna, ale KTÓRE z tych miejscowości firma realnie obsługuje, nie zostało potwierdzone. Demo mówi tylko „Wolsztyn i okolice”, brief mówi dwa województwa. Sprzeczność do rozstrzygnięcia z klientem."
    },
    {
     "co": "Opinie klientów / dowód społeczny",
     "skad": "—",
     "czy_na_pewno_ich": "BRAK. Wyszukiwanie 07.09.2026 nie znalazło ani jednej publicznej opinii o tej firmie, a wizytówka Google z podanego linku ma pinezkę ok. 85 km od Błońska. To dziś największa dziura w wiarygodności strony."
    }
   ],
   "uwagi": "TRZY RZECZY, KTÓRE ROZSTRZYGAJĄ CAŁY TOR 5:\n\n1) 🔴 „Wycena do 5 dni roboczych” to najgroźniejsze zdanie w całym briefie. 78% klientów wybiera firmę, która odpowie PIERWSZA, a 35% oczekuje reakcji w 30 minut. Trzeba rozdzielić dwa zegary i napisać je osobno: „Odezwiemy się tego samego dnia” (kontakt) oraz „Kosztorys przygotowujemy do 5 dni roboczych, bo liczymy go pod Twoje metry, a nie z cennika” (wycena). W jednym zdaniu „5 dni” brzmi jak „nie odpiszą”; rozdzielone i uzasadnione brzmi jak rzetelność.\n\n2) 🔴 Ta strona nie służy głównie do zdobywania nowych klientów z Google — służy do POTWIERDZANIA POLECEŃ. Połowa Polaków dostaje nazwisko od znajomego i wpisuje je w wyszukiwarkę, żeby sprawdzić. Dziś taka osoba nie znajdzie o A.S Tchórzewski ani jednej publicznej opinii. Priorytet numer jeden na pierwszym ekranie: prawdziwe zdjęcie roboty + nazwisko + wieś + numer + godziny 8–20. Priorytet numer dwa (poza stroną, ale wart więcej niż połowa strony): wizytówka Google — pinezka z podanego linku stoi ok. 85 km na wschód od Błońska, co dla klienta z Wolsztyna oznacza „to firma z drugiego końca województwa”.\n\n3) 🔴 Klient końcowy wchodzi ze STRACHEM, nie z ciekawością — 76,1% Polaków miało problem z fachowcem, na czele jakość wymagająca poprawek (22,9%) i opóźnienia (22,7%). Sekcja „Jak pracujemy” ma odpowiadać punkt po punkcie na te lęki (termin na piśmie, kosztorys bez dopłat, obecność na budowie, gwarancja, faktura, sprzątanie), a nie chwalić firmę przymiotnikami. Deklaracja z briefu „polecamy sprawdzone osoby do prac, których nie robimy” to gotowa, niewykorzystana przewaga — zdejmuje lęk „będę musiał sam zbierać ekipy”.\n\nUCZCIWOŚĆ ŹRÓDEŁ — co jest słabsze, niż wygląda:\n· Frazy wyszukiwania podałem jako WZORZEC nazewnictwa potwierdzony tytułami kategorii w portalach (Oferteo/Daibau/Muratordom), a NIE jako zmierzone wolumeny wyszukiwań — nikt nie sprawdził, ile osób wpisuje „wykończenia wnętrz Rakoniewice”. Jeśli to ma sterować architekturą podstron, warto dołożyć jedno sprawdzenie w Planerze słów kluczowych.\n· Badanie Insight Lab dla WeNet (50%/44%/27%/20%) mam wyłącznie z omówienia prasowego — oryginał (strefabiznesu.pl) zwraca 403. Oznaczyłem „prawdopodobny”.\n· Artykuł money.pl o „pułapce remontowej” NIE zawiera żadnych liczb, mimo że tak wyglądał w wynikach wyszukiwania — sprawdziłem treść. Liczby biorę wyłącznie z raportu „Doświadczenia Polaków z fachowcami. Edycja 2026”.\n· Poradniki o budowie stron dla firm remontowych (cyberfolks, artnova, portalmarketingowy) to OPINIE BRANŻOWE agencji, nie badania. Traktować jako kierunek, nie dowód.\n\nSPRZECZNOŚĆ DO ROZSTRZYGNIĘCIA PRZED PISANIEM TEKSTÓW: demo obiecuje „Wolsztyn i okolice”, brief mówi „wielkopolskie i lubuskie”, adres w demie to „64-308 Jabłonna”, a w rejestrze „64-308 Błońsko”. Trzy różne wersje geografii tej samej firmy. Klient z Sulechowa albo Świebodzina, który zobaczy „Wolsztyn i okolice”, po prostu nie zadzwoni.\n\nI ZASADA REDAKCYJNA, KTÓRA OBOWIĄZUJE WSZĘDZIE: wszystkie teksty w LICZBIE MNOGIEJ („robimy”, „przyjedziemy”, „damy znać”) — wyraźne polecenie klienta z briefu, łamie domyślną regułę silnika. Przy okazji dobrze się zgrywa z „firmą rodzinną”."
  }
 },
 {
  "tor": "wzorce",
  "dane": {
   "tor": "TOR 6 — wzorce branżowe ze świata (firmy wykończeniowe / malarskie / remontowe poza Polską)",
   "fakty": [
    {
     "stwierdzenie": "Build Team (Londyn, przebudowy i wykończenia domów) zbudował całą stronę główną wokół PROCESU i pewności ceny, a nie wokół galerii: trzy karty obietnic to „Fixed Fee Design Packages\", „Payment in Arrears – Protect Your Pounds\", „Build Management – From Design to Build\" oraz „Structural Guarantee – For 3 Years\".",
     "zrodlo": "https://www.buildteam.com/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja „Jak pracujemy\" na stronie głównej Tchórzewskiego: 3–4 kafle obietnic zamiast ogólników. Nasz odpowiednik: wycena do 5 dni roboczych · stała cena po obmiarze · gwarancja (długość czeka na klienta) · jedna ekipa od szpachli po malowanie."
    },
    {
     "stwierdzenie": "Build Team ma osobne, linkowane ze strony głównej narzędzia wyceny pod adresami /online-quote-calculator.html i /build-your-price-start.html — czyli kalkulator jest osobną podstroną, nie widgetem w stopce.",
     "zrodlo": "https://www.buildteam.com/ — linki w kodzie HTML strony głównej",
     "pewnosc": "potwierdzony",
     "uzycie": "Jedna z 5 podstron może być „Wycena\" — formularz obmiaru (metraż, liczba pomieszczeń, zakres) zamiast zwykłego „napisz do nas\". To realnie podnosi liczbę zapytań i pasuje do „wycena do 5 dni roboczych\"."
    },
    {
     "stwierdzenie": "Build Team zamiast liczby lat pokazuje liczbę klientów („zaufało 1 750 londyńskich właścicieli domów\") oraz pasek logotypów mediów (Grand Designs, Channel 4, Good Homes, Ideal Home) i 7 odznak Houzz.",
     "zrodlo": "https://www.buildteam.com/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "U nas ekwiwalentem logotypów prasy są: liczba lat (2005 Niemcy / 2015 Polska), opinie Google z wizytówki i profil FB/IG. Pasek zaufania robimy z tego, co realnie mamy — nie wymyślamy odznak."
    },
    {
     "stwierdzenie": "Build Team zamyka stronę główną wezwaniem z KONKRETNYMI DATAMI: „Book a FREE Design Consultation today\" z listą wolnych terminów (09–21 września) i przyciskiem „Book now\" przy każdej dacie.",
     "zrodlo": "https://www.buildteam.com/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Mocny wzorzec, ale u nas w wersji telefonicznej: „Dzwonimy 8–20\" + numer 667 434 222 jako przycisk + WhatsApp 882 832 244. Konkret godzin działa tak samo jak konkret dat."
    },
    {
     "stwierdzenie": "Build Team używa pary krojów: Mulish (bezszeryfowy, wagi 300/400/700) do całości plus Libre Baskerville tylko w odmianie 400 kursywa — czyli szeryf wchodzi wyłącznie jako akcent, nie jako krój nagłówków.",
     "zrodlo": "https://www.buildteam.com/ — wywołania fonts.googleapis.com w kodzie strony",
     "pewnosc": "potwierdzony",
     "uzycie": "Gotowy, sprawdzony przepis typograficzny na stronę rzemieślniczą: jeden neutralny bezszeryf na wszystko + szeryfowa kursywa wyłącznie na cytat klienta albo jedno zdanie o rodzinie. Zero wersalików."
    },
    {
     "stwierdzenie": "Malerfachbetrieb HEYSE (Isernhagen k. Hanoweru) — firma rodzinna z ponad 80-letnią historią — prowadzi cały przekaz jednym hasłem-obietnicą: „Wunderschöne Wohn(t)räume und Arbeitswelten\" z podpisem „FARBE fühlst Du. HEYSE brauchst Du.\", a nie listą usług.",
     "zrodlo": "https://www.maler-heyse.de/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Hero u Tchórzewskiego: jedno zdanie o EFEKCIE dla klienta („Wykańczamy wnętrza pod klucz…\") plus krótki podpis-obietnica, zamiast wyliczanki „szpachlowanie, malowanie, sucha zabudowa\" na samej górze. Wyliczanka idzie niżej, do sekcji usług."
    },
    {
     "stwierdzenie": "HEYSE opiera dowód społeczny na jednej zewnętrznej platformie: 845 recenzji na ProvenExpert plus status certyfikowanego „Kalkkind-Fachbetrieb\" — bez wklejania cytatów bez źródła.",
     "zrodlo": "https://www.maler-heyse.de/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Nasz odpowiednik = opinie Google z wizytówki (link do profilu, nie przepisane cytaty). Wzorzec do przeniesienia: liczba opinii + link do źródła, żeby dało się sprawdzić."
    },
    {
     "stwierdzenie": "HEYSE zbudował paletę na czerni/bieli z JEDNYM złotym akcentem #AB9044 (i przyciemnioną wersją #726542) — nie ma dużej płaszczyzny jaskrawego koloru.",
     "zrodlo": "https://www.maler-heyse.de/ — wartości kolorów w kodzie strony",
     "pewnosc": "potwierdzony",
     "uzycie": "Dokładnie ten model palety dla Tchórzewskiego: neutralne tło + JEDEN ciepły akcent (przyciski, podkreślenia, ikony). Zgodne z zakazem wielkich jaskrawych płaszczyzn."
    },
    {
     "stwierdzenie": "HEYSE rozbija ofertę nie na „usługi\", tylko na EFEKTY POWIERZCHNI, które klient może sobie wyobrazić: Fugenlose Wände, Betonoptik, Kalkkind/Sumpfkalk, Echtmetalloptik, Rostoptik, Wandbegrünungen.",
     "zrodlo": "https://www.maler-heyse.de/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Przenosimy sam mechanizm, nie te techniki: zamiast suchego „sucha zabudowa\" — „sufity podwieszane, zabudowy wnęk, ścianki działowe\"; zamiast „szpachlowanie\" — „ściany gładkie pod malowanie, bez cieni przy oknie\". Klient kupuje efekt, nie nazwę roboty."
    },
    {
     "stwierdzenie": "Malerboks (Kopenhaga) pokazuje na stronie głównej JAWNE widełki cenowe w kaflach: „Maling 1V od 9 900\", „2V od 13 500\", „3V od 18 900\" — z dopiskiem „inklusiv materialer og moms\" (z materiałami i VAT).",
     "zrodlo": "https://www.malerboks.dk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "⚠️ Klient wprost powiedział „trzeba się skontaktować, wycena bardzo indywidualna\" — więc widełek NIE wstawiamy bez jego zgody. Wzorzec do rozważenia w łagodnej wersji: sekcja „Od czego zależy cena\" (metraż, stan ścian, ile warstw, czy z materiałem) — daje poczucie transparentności bez podawania kwot."
    },
    {
     "stwierdzenie": "Malerboks ma na stronie głównej FAQ z 15 pytaniami (o ceny, przebieg prac, gwarancje, różnice technik malowania) oraz eksponowaną „3 års garanti\" i przynależność do cechu (Danske Malermestre, Københavns Malerlaug).",
     "zrodlo": "https://www.malerboks.dk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "FAQ to najtańsza podstrona, jaką możemy dać Tchórzewskiemu — odsiewa telefony bez sensu i pracuje na Google. Gwarancja wyeksponowana jako osobny element (czekamy na długość od klienta)."
    },
    {
     "stwierdzenie": "Malerboks wymienia usługi ROBOCZO, bardzo blisko naszego zakresu: malowanie ścian i sufitów, szpachlowanie (spartling), montaż filcu, lakierowanie natryskowe drewna, zdejmowanie tapet, naprawa płyt gipsowych, szlifowanie bezpyłowe.",
     "zrodlo": "https://www.malerboks.dk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "„Szlifowanie bezpyłowe\" i „naprawa płyt gipsowych\" to gotowe, konkretne hasła-różnice, którymi warto rozbić nasze cztery ogólne usługi. ⚠️ Wpisujemy tylko to, co Tchórzewski realnie robi — trzeba dopytać."
    },
    {
     "stwierdzenie": "Tony Baert (Belgia, malowanie i dekoracja wnętrz) prowadzi hero hasłem emocjonalnym „Verliefd op je huis\" („zakochany w swoim domu\"), a historię rodzinną podaje jako twardą liczbę pokoleń — piąte pokolenie w firmie.",
     "zrodlo": "https://www.tonybaert.be/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Bezpośredni wzorzec dla „firma rodzinna, ponad 20 lat doświadczenia, od 2005 w Niemczech\": liczba jako bohater sekcji O NAS, a nad nią jedno ludzkie zdanie. Nie „jesteśmy profesjonalni\", tylko „ponad 20 lat, dwa kraje, jedna rodzina\"."
    },
    {
     "stwierdzenie": "Tony Baert zamiast listy cech firmy daje 5 ponumerowanych obietnic: słuchamy potrzeb · uczciwe i fachowe doradztwo · wysokiej jakości materiały, ponadczasowa jakość · unikalne rozwiązania wnętrzarskie · rzemiosło pięciu pokoleń.",
     "zrodlo": "https://www.tonybaert.be/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Ten format 1:1 przenosi się na naszą sekcję „Dlaczego my\" — i naturalnie brzmi w LICZBIE MNOGIEJ, której wymaga klient („słuchamy\", „doradzamy\", „pracujemy\")."
    },
    {
     "stwierdzenie": "Tony Baert dzieli ofertę na 4 filary (schilderwerken & wanddecoratie / raamdecoratie / totaalinterieur / interieuraccessoires), a nie na kilkanaście pozycji.",
     "zrodlo": "https://www.tonybaert.be/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Odpowiada dokładnie naszym 4 kluczowym usługom (szpachlowanie, malowanie, łazienki, sucha zabudowa) — montaż drzwi i okien schodzi do zdania w tekście, bo klient sam mówi, że mniej na tym zarabia."
    },
    {
     "stwierdzenie": "Smeulders Interieurgroep (Holandia, wykończenia wnętrz premium) dostała nominację Awwwards (14.07.2026, agencja Comaxx) za „elegancki design, mocne wizualizacje i czytelną opowieść o rzemiośle\"; stroną główną jest pionowa lista realizacji — każdy projekt to duży kadr, nazwa jako H2 i link „Lees meer over dit project\".",
     "zrodlo": "https://www.awwwards.com/sites/smeulders-interieurgroep oraz https://smeulders-ig.nl/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Najważniejszy wzorzec dla galerii Tchórzewskiego: realizacja = KRÓTKA HISTORIA z nazwą, nie zdjęcie w siatce miniatur. Nawet 4–6 realizacji z podpisem („Łazienka, dom jednorodzinny pod Grodziskiem — płytki, sucha zabudowa, malowanie\") bije 30 anonimowych fotek."
    },
    {
     "stwierdzenie": "Smeulders używa dużych zdjęć tła i animacji GSAP przy przewijaniu, a menu ogranicza do czterech pozycji: Projekten, Over Smeulders, Duurzaamheid, Werken bij.",
     "zrodlo": "https://www.awwwards.com/sites/smeulders-interieurgroep (stack: WordPress, GSAP, responsive, big background images) oraz https://smeulders-ig.nl/",
     "pewnosc": "potwierdzony",
     "uzycie": "Menu na 4–5 pozycji to dokładnie nasz limit (główna + do 5 podstron). Delikatne wejścia elementów przy scrollu — tak; karuzele i „efekty\" — nie."
    },
    {
     "stwierdzenie": "Blakes London rozpisuje współpracę na SIEDEM ponumerowanych etapów, od „Initial Consultation\" do „Installation\", i pokazuje ofertę jako siatkę 2×3 kategorii przestrzeni (kuchnie, garderoby, gabinety, łazienki…), każda ze zdjęciem.",
     "zrodlo": "https://blakeslondon.com/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Siedem etapów to dla nas za dużo — bierzemy 4: kontakt → obmiar i wycena (do 5 dni roboczych) → prace → odbiór i gwarancja. Siatka kategorii ze zdjęciem = układ naszej sekcji usług."
    },
    {
     "stwierdzenie": "Blakes London stoi w całości na jednym kroju Poppins, bez drugiego kroju nagłówkowego.",
     "zrodlo": "https://blakeslondon.com/ — deklaracje font-family w kodzie strony",
     "pewnosc": "potwierdzony",
     "uzycie": "Dowód, że jeden dobrze poprowadzony krój wystarcza na stronę premium. ⛔ Ale Poppins jest w Polsce zajeżdżony przez szablony — u nas raczej Inter/Manrope/Source Sans, albo para jak u Build Team."
    },
    {
     "stwierdzenie": "Dwie strony z tej branży prowadzą główne hasło WERSALIKAMI: Alloy Workshop („ARCHITECT-LED DESIGN BUILD | CHARLOTTESVILLE | VIRGINIA\") i SÒ Interiors („UK SPECIALIST IN SURFACE DESIGN\").",
     "zrodlo": "https://alloyworkshop.com/ oraz https://sointeriorsuk.co.uk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Kontrprzykład — to jest dokładnie ten patent, który klient już odrzucił. Wpisuję go tu jako ostrzeżenie: nagłówki normalną wielkością liter, nawet gdy oryginał robi inaczej."
    },
    {
     "stwierdzenie": "SÒ Interiors (UK, specjaliści od wykończeń powierzchni: microcement, polished plaster, tadelakt) wypisuje usługi jako gołe linki tekstowe, bez zdjęć i ikon, i nie ma na stronie głównej ani opinii, ani procesu.",
     "zrodlo": "https://sointeriorsuk.co.uk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Kontrprzykład drugiego typu: minimalizm bez zdjęć w rzemiośle wykończeniowym nie sprzedaje. Potwierdza, że u Tchórzewskiego zdjęcia realizacji są warunkiem koniecznym, nie ozdobą."
    },
    {
     "stwierdzenie": "Duńskie i belgijskie strony z tej branży, mimo dobrej struktury, stoją na gotowcach: Norh Maler i Malerboks to WordPress + Elementor z krojem Roboto, Alloy Workshop to motyw Divi (ETmodules) z Source Sans Pro/Lato/Alata.",
     "zrodlo": "Kod źródłowy https://www.norhmaler.dk/, https://www.malerboks.dk/, https://alloyworkshop.com/ (meta generator i font-family)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sygnał dla nas: warstwa TREŚCI (proces, FAQ, gwarancja, cennik) jest w tej branży dużo lepiej dopracowana niż warstwa wizualna. Kopiujemy od nich strukturę i argumenty, wygląd budujemy od zera."
    },
    {
     "stwierdzenie": "Norh Maler (Kopenhaga) nie ma na stronie ŻADNEJ galerii realizacji — tylko wzmiankę o filmie z budowy — mimo rozbudowanej sekcji usług i doradztwa kolorystycznego.",
     "zrodlo": "https://www.norhmaler.dk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Kontrprzykład: pokazuje, jak wygląda strona wykończeniowca bez zdjęć własnych prac. Argument do rozmowy z Tchórzewskim, dlaczego jego zdjęcia realizacji są blokerem numer jeden."
    },
    {
     "stwierdzenie": "Norh Maler eksponuje szeroką dostępność jako argument sprzedażowy: godziny pon–pt 07:00–22:00, sob–nd 08:00–21:00 plus hasło o dostępie „24/7\".",
     "zrodlo": "https://www.norhmaler.dk/ (pobrane 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Tchórzewski ma godziny 8–20 (z briefu) — to realna przewaga nad konkurencją, którą warto wystawić w hero i w stopce, a nie chować w zakładce kontakt."
    },
    {
     "stwierdzenie": "Żadnej z tych stron nie oglądałem wizualnie — WebFetch zwraca tekst przekonwertowany na markdown, więc ocena kadrowania zdjęć, proporcji siatek, odstępów i realnej hierarchii wizualnej nie została zweryfikowana.",
     "zrodlo": "metoda pracy w tym torze (WebFetch + curl na kod źródłowy), 07.09.2026",
     "pewnosc": "potwierdzony",
     "uzycie": "Wszystkie powyższe wnioski o UKŁADZIE i TREŚCI są twarde; wnioski o WYGLĄDZIE wymagają przejścia po tych 6 adresach ze zrzutami ekranu przed etapem designu."
    }
   ],
   "luki": [
    "Czy klient zgodzi się na jakąkolwiek transparentność cenową (jak Malerboks: widełki „od X\")? Powiedział „trzeba się skontaktować\" — bez jego zgody nie wstawiamy nawet sekcji „od czego zależy cena\".",
    "Ile dokładnie wynosi gwarancja? Bez tej liczby nie da się zrobić kafla obietnicy w stylu Malerboks („3 lata gwarancji\") — a to jeden z najmocniejszych elementów zaufania w tej branży.",
    "Czy Tchórzewscy robią szlifowanie bezpyłowe, natrysk (agregat), naprawy płyt g-k, zdejmowanie tapet? Duńczycy wygrywają właśnie takimi konkretami — ale wpisujemy tylko to, co realnie robią.",
    "Ile jest osób w ekipie i czy są to członkowie rodziny z imienia? Belgowie i Niemcy budują zaufanie na pokoleniach i nazwiskach — musimy wiedzieć, ile pokoleń/osób możemy pokazać.",
    "Które konkretnie 4–6 realizacji chcemy opowiedzieć jako osobne historie (wzorzec Smeulders)? Potrzebne: rodzaj obiektu, zakres prac, miejscowość — bez tego zostaje anonimowa siatka fotek.",
    "Czy klient chce podstronę „Realizacje\" osobno, czy galeria ma siedzieć na głównej? Przy limicie 5 podstron to realny wybór: Realizacje vs. FAQ vs. Wycena.",
    "Czy wystawiamy WhatsApp 882 832 244 jako osobny przycisk obok telefonu 667 434 222 (Duńczycy i Brytyjczycy dublują kanały kontaktu w hero)?",
    "Jak nazwać na stronie mechanizm „polecamy sprawdzone osoby do usług, których nie robimy\" — żeby brzmiał jak przewaga (kompleksowa obsługa), a nie jak przyznanie się do braków? Żadna z badanych stron tego nie robi, nie mam wzorca."
   ],
   "materialy": [
    {
     "co": "Zrzuty ekranu 6 stron wzorcowych (desktop + mobile) do wewnętrznego moodboardu przed etapem designu",
     "skad": "Do zrobienia — buildteam.com, maler-heyse.de, malerboks.dk, tonybaert.be, smeulders-ig.nl, blakeslondon.com",
     "czy_na_pewno_ich": "⛔ NIE nasze. To cudze strony — zrzuty służą wyłącznie jako materiał roboczy do analizy układu. Żaden piksel, zdjęcie ani tekst z nich nie może trafić na stronę Tchórzewskiego."
    },
    {
     "co": "Przepis typograficzny: jeden bezszeryf na całość + szeryfowa kursywa wyłącznie na cytat/jedno zdanie o rodzinie",
     "skad": "Zweryfikowany wzorzec z buildteam.com (Mulish 300/400/700 + Libre Baskerville 400 italic) — kroje bierzemy własne, nie kopiujemy zestawu",
     "czy_na_pewno_ich": "✅ Sam schemat jest ideą, nie własnością. Konkretne kroje wybieramy z Google Fonts na licencji otwartej — sprawdzone przy publikacji."
    },
    {
     "co": "Paleta: neutralne tło + JEDEN ciepły akcent (wzorzec HEYSE: czerń/biel + złoto #AB9044)",
     "skad": "Kod źródłowy maler-heyse.de",
     "czy_na_pewno_ich": "✅ Kolor nie podlega ochronie. Dobieramy własny odcień akcentu pod logo Tchórzewskiego (awatar FB), nie przepisujemy #AB9044."
    },
    {
     "co": "Zdjęcia realizacji Tchórzewskich — bez nich cały wzorzec „realizacja jako historia\" (Smeulders) jest niewykonalny",
     "skad": "Klient obiecał 07.09 wieczorem; zapasowo profil FB „A.S Tchórzewski\" i Instagram @a.s_tchorzewski przez skill kolejka-sociali/social-foto",
     "czy_na_pewno_ich": "⚠️ Zdjęcia z ich własnego FB/IG = ich. Obecny stock z dema (Pexels) NIE jest ich i musi zniknąć ze strony docelowej — tak stoi w briefie."
    },
    {
     "co": "Logo firmy w pliku",
     "skad": "Klient obiecał 07.09; zapasowo awatar z FB użyty w demie",
     "czy_na_pewno_ich": "⚠️ Awatar FB pochodzi z ich profilu, ale to zapas w niskiej jakości. Do strony płatnej potrzebny plik od klienta — inaczej logo w nagłówku będzie rozmyte."
    }
   ],
   "uwagi": "SZEŚĆ WZORCÓW, KTÓRE POLECAM (i po co każdy):\n1. buildteam.com (UK) — proces i pewność ceny · bierzemy: kafle obietnic, osobna podstrona wyceny, para krojów.\n2. maler-heyse.de (DE) — najbliższy analog: firma rodzinna, dekady stażu, wykończenia · bierzemy: hero-obietnica zamiast wyliczanki, usługi opisane jako EFEKTY, paleta z jednym akcentem, opinie linkowane do źródła.\n3. malerboks.dk (DK) — najbliższy analog zakresem robót · bierzemy: FAQ, gwarancja jako osobny element, konkretne nazwy prac.\n4. tonybaert.be (BE) — pokolenia w firmie rodzinnej · bierzemy: liczba pokoleń jako bohater sekcji O NAS, 5 ponumerowanych obietnic w liczbie mnogiej, 4 filary usług.\n5. smeulders-ig.nl (NL, nominacja Awwwards 07.2026) — najlepszy wzorzec galerii · bierzemy: realizacja = historia z nazwą i podpisem, menu na 4 pozycje, delikatne wejścia przy scrollu.\n6. blakeslondon.com (UK) — proces + siatka kategorii ze zdjęciem · bierzemy: skrócony do 4 kroków.\n\nCZEGO NIE PRZENOSIMY NA RYNEK POLSKI:\n- Jawnych widełek cenowych (Malerboks) — klient wprost tego nie chce, wycena indywidualna do 5 dni.\n- Rezerwacji konsultacji z kalendarzem terminów (Build Team) — mała ekipa z telefonem 8–20 tego nie obsłuży; zamiast tego telefon + WhatsApp.\n- Odznak branżowych i logotypów prasy (Build Team, Alloy: AIA/NARI/LEED) — w PL nie mamy odpowiednika i to wygląda na ściemę. Zastępujemy opiniami Google i latami stażu.\n- Kilkunastu technik dekoracyjnych (HEYSE: betonoptik, tadelakt, kalkkind) — Tchórzewscy zarabiają na szpachli, malowaniu, łazienkach i suchej zabudowie; wciskanie technik premium byłoby kłamstwem.\n- Języka „bespoke / one-of-a-kind / luxury\\\" (Blakes, SÒ) — w wielkopolsko-lubuskim to odstrasza. Ton: rzeczowy, ludzki, w liczbie mnogiej.\n\n⛔ CZEGO PILNUJĘ Z ZAKAZÓW KLIENTA: żadnych wersalików w nagłówkach (Alloy i SÒ robią tak — to kontrprzykład, nie wzór), żadnych wielkich jaskrawych płaszczyzn (wzorzec HEYSE to neutralne tło + jeden akcent), żadnych grubych czarnych ramek.\n\n🔴 OGRANICZENIE METODY: nie widziałem tych stron NA OCZY — WebFetch zwraca tekst, nie obraz. Wszystko, co piszę o układzie, treści, procesie i argumentach, jest oparte na pobranej treści i kodzie źródłowym (potwierdzone). Wszystko o kadrowaniu zdjęć, odstępach i realnej hierarchii wizualnej wymaga jeszcze przejścia po tych 6 adresach ze zrzutami ekranu — to ok. 15 minut w Chrome i zrobiłbym to przed startem designu, jeśli K. da zielone światło.\n\n⚠️ RÓWNANIE W DÓŁ POTWIERDZONE ODWROTNIE NIŻ ZAKŁADALIŚMY: zagraniczne strony w tej branży wcale nie są ładniejsze — Norh, Malerboks i Alloy to Elementor/Divi na Roboto. Przewagę mają w TREŚCI (proces, FAQ, gwarancja, konkretne nazwy prac), nie w wyglądzie. Wygląd musimy zaprojektować sami; od nich bierzemy argumenty."
  }
 },
 {
  "tor": "luki",
  "dane": {
   "tor": "TOR 7 — czego nie wiemy (braki blokujące konkretną stronę + gotowe pytania do właściciela)",
   "fakty": [
    {
     "stwierdzenie": "W demie sekcja „Opinie\" nie zawiera ANI JEDNEJ wypowiedzi klienta — jest tylko tekst zastępczy „Najlepiej mówią za nas mieszkania… Zapytaj o adresy realizacji w okolicy\".",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (odczyt treści 07.09.2026)",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja opinii na stronie docelowej — dziś nie ma czym jej wypełnić; albo zdobywamy 3-5 opinii, albo sekcja wypada z układu."
    },
    {
     "stwierdzenie": "Ani brief, ani demo nie zawierają ŻADNEJ liczby opisującej skalę pracy: ile realizacji rocznie, ile metrów kwadratowych, ile trwa wykończenie mieszkania, ile osób liczy ekipa, żadnej ceny „od\".",
     "zrodlo": "BRIEF-KLIENTA.md (07.09.2026) + https://impulseo-pl.github.io/a-s-tchorzewski/",
     "pewnosc": "potwierdzony",
     "uzycie": "Pasek liczb pod hero i sekcja „Jak pracujemy\" — bez liczb strona będzie brzmiała jak każda inna firma wykończeniowa."
    },
    {
     "stwierdzenie": "Jedyny termin, jaki podał klient, to „wycena do 5 dni roboczych\" — nie ma nigdzie czasu reakcji na telefon/wiadomość (kiedy oddzwaniają, kiedy przyjeżdżają obejrzeć).",
     "zrodlo": "BRIEF-KLIENTA.md, sekcja „Zakres usług\"",
     "pewnosc": "potwierdzony",
     "uzycie": "Hero + sekcja kontaktu: „oddzwaniamy tego samego dnia\" to najmocniejsza obietnica, jaką da się dać w tej branży — dziś nie mamy prawa jej napisać."
    },
    {
     "stwierdzenie": "Demo obiecuje „Bezpłatna wycena\" i „Za obejrzenie placu i policzenie nie bierzemy pieniędzy\" — brief tego NIE potwierdza, mówi tylko o wycenie indywidualnej do 5 dni roboczych.",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ (5 wystąpień „Bezpłatna wycena\") vs BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Wszystkie przyciski CTA — jeśli wycena jednak bywa płatna albo tylko dojazd jest bezpłatny w promieniu X km, to trzeba przepisać KAŻDY przycisk na stronie."
    },
    {
     "stwierdzenie": "Obszar w demie („Wolsztyn i okolice\", „Jabłonna, Zbąszyń, Nowy Tomyśl, Grodzisk Wielkopolski\") jest znacznie węższy niż obszar z briefu („województwo wielkopolskie i lubuskie\").",
     "zrodlo": "https://impulseo-pl.github.io/a-s-tchorzewski/ vs BRIEF-KLIENTA.md",
     "pewnosc": "potwierdzony",
     "uzycie": "Sekcja obszaru działania i teksty pod SEO lokalne — trzeba wiedzieć, które miasta wymieniać z nazwy, bo od tego zależy, na co strona się wypozycjonuje."
    },
    {
     "stwierdzenie": "Gwarancja: klient potwierdził, że jest w umowie, ale długości nie podał (obiecał wieczorem 07.09); demo pisze „Gwarancja na robociznę\" bez żadnej liczby.",
     "zrodlo": "BRIEF-KLIENTA.md, sekcja „Ustalenia redakcyjne\" + demo",
     "pewnosc": "potwierdzony",
     "uzycie": "Odznaka w hero i sekcja FAQ — „gwarancja 3 lata na robociznę\" to liczba, której nie ma żadna konkurencja z okolicy na stronie."
    },
    {
     "stwierdzenie": "Strona docelowa nie ma dziś ŻADNEGO materiału o dwóch rzeczach, które klient sam wskazał jako wyróżniki: firma rodzinna oraz praca w Niemczech od 2005 (demo nie wspomina o Niemczech ani o rodzinie ani razu).",
     "zrodlo": "BRIEF-KLIENTA.md (Historia firmy) vs treść demo",
     "pewnosc": "potwierdzony",
     "uzycie": "Podstrona „O nas\" — bez konkretów (kto, ile osób, jakie roboty w Niemczech) zostanie z tego jedno ogólne zdanie."
    },
    {
     "stwierdzenie": "Data rozpoczęcia działalności w Polsce: 02.12.2015, „FIRMA OGÓLNOBUDOWLANA Artur Tchórzewski\", NIP 9950044465, REGON 363138510, Błońsko 46.",
     "zrodlo": "CEIDG za pośrednictwem agregatorów (wyszukiwanie 07.09.2026: aleo.com / firma.egospodarka.pl) — nie odczytane bezpośrednio z ceidg.gov.pl",
     "pewnosc": "prawdopodobny",
     "uzycie": "Zdanie „od 2015 roku w Polsce\" na stronie O nas — zgodne z briefem, ale przed publikacją warto potwierdzić u klienta jedną liczbą."
    },
    {
     "stwierdzenie": "Pod tym samym adresem (Błońsko 46) figuruje DRUGA firma budowlana o tym samym nazwisku: Firma Ogólnobudowlana Tadeusz Tchórzewski, NIP 7881441770, REGON 330972970, ta sama branża (wykończenia, tynkowanie, malowanie).",
     "zrodlo": "https://aleo.com/pl/firma/firma-ogolnobudowlana-tadeusz-tchorzewski-wolsztyn (dane z CEIDG)",
     "pewnosc": "prawdopodobny",
     "uzycie": "Wątek „firma rodzinna\" na stronie O nas (jeśli to ojciec/brat — mocny, prawdziwy konkret) ORAZ ostrzeżenie: przy weryfikacji opinii i wizytówek łatwo pomylić obie firmy."
    }
   ],
   "luki": [
    "CZAS REAKCJI: Jak szybko oddzwaniacie na nieodebrany telefon albo wiadomość — tego samego dnia, czy do 24 godzin? (potrzebne dosłowne zdanie do nagłówka strony)",
    "CZAS REAKCJI: Ile czasu mija od telefonu do przyjazdu na oględziny — jeszcze w tym tygodniu, czy zwykle dłużej?",
    "CZAS REAKCJI: Godziny 8-20 to godziny odbierania telefonu czy godziny pracy ekipy na budowie?",
    "LICZBA: Ile mieszkań albo domów wykańczacie w ciągu roku?",
    "LICZBA: Ile dni zajmuje Wam wykończenie mieszkania pod klucz, powiedzmy 60 metrów, od gołych ścian?",
    "LICZBA: Ile dni zajmuje remont typowej łazienki, od skuwania do gotowej do użycia?",
    "LICZBA: Ile osób liczy ekipa i ile z nich to rodzina?",
    "LICZBA: Ile lat gwarancji na robociznę daje Wasza umowa? (to jest to, co obiecaliście podać 07.09 wieczorem)",
    "LICZBA: Ile metrów kwadratowych ścian potraficie zaszpachlować i pomalować w jeden dzień pracy agregatem?",
    "CENA: Czy możemy podać na stronie choć jedną cenę orientacyjną — na przykład 'malowanie od X zł za metr' albo 'wykończenie pod klucz od X zł za metr' — czy absolutnie żadnych cen?",
    "CENA: Czy wycena i dojazd na oględziny są bezpłatne? Do ilu kilometrów? (demo obiecuje bezpłatną wycenę — potwierdzacie?)",
    "OPINIE: Możecie podać nam trzech klientów z ostatniego roku, którzy zgodzą się na krótką opinię z imieniem i miejscowością na stronie?",
    "OPINIE: Macie zapisane pochwały na WhatsAppie albo w wiadomościach na Facebooku? Wystarczy zrzut ekranu — przepiszemy i zapytamy o zgodę.",
    "OPINIE: Ile opinii macie na wizytówce Google i czy jesteście jej właścicielami (czy możecie nią zarządzać)?",
    "ZAKRES: Które cztery usługi mają być osobnymi podstronami? Z briefu wychodzi: szpachlowanie i malowanie, łazienki, sucha zabudowa, montaż drzwi i okien — dobrze?",
    "ZAKRES: Robicie prace murarskie i tynki maszynowe, czy to wpisaliśmy w demie na wyrost?",
    "ZAKRES: Bierzecie całe wykończenie pod klucz (z podłogami, hydrauliką, elektryką przez podwykonawców), czy tylko swoje cztery usługi?",
    "OBSZAR: Do których miast realnie dojeżdżacie? Wymieńcie pięć, w których pracujecie najczęściej — chcemy je wpisać z nazwy, żeby ludzie stamtąd Was znajdowali w Google.",
    "OBSZAR: Jak daleko opłaca Wam się jechać i czy przy dalszych robotach doliczacie dojazd?",
    "HISTORIA: Co konkretnie robiliście w Niemczech od 2005 roku i czy nadal tam pracujecie?",
    "HISTORIA: Kto zakłada firmę rodzinną — ojciec, bracia, syn? Czy Tadeusz Tchórzewski spod tego samego adresu to rodzina?",
    "ADRES: Który adres wpisujemy na stronę: Błońsko 46, 64-308 Błońsko (jak w rejestrze) czy 64-308 Jabłonna (jak na fakturze)? Musi być identyczny jak na wizytówce Google.",
    "MATERIAŁY: Czy przy robotach kupujecie materiały na siebie z fakturami, czy klient kupuje sam? (demo obiecuje obie opcje)",
    "TERMIN: Za ile tygodni od podpisania możecie zwykle zacząć większą robotę?"
   ],
   "materialy": [
    {
     "co": "Zdjęcia realizacji — 15-25 sztuk, w tym co najmniej 3 pary „przed i po\" tego samego pomieszczenia",
     "skad": "Od klienta (obiecał 07.09 wieczorem) — telefon właściciela, WhatsApp; zapasowo profil FB „A.S Tchórzewski\" i Instagram @a.s_tchorzewski przez skill social-foto",
     "czy_na_pewno_ich": "Tylko jeśli przyśle je sam albo pochodzą z jego profilu FB/IG (profile potwierdzone: telefon 667 434 222 na ich grafice — zapis w BRIEF-KLIENTA.md). ⛔ Galeria w demie to STOCK z Pexels i na stronie docelowej NIE MOŻE zostać."
    },
    {
     "co": "Logo w pliku (najlepiej wektor lub PNG bez tła)",
     "skad": "Od klienta (obiecane 07.09 wieczorem)",
     "czy_na_pewno_ich": "Zapasowo mamy awatar z ich profilu FB użyty w demie — profil potwierdzony numerem 667 434 222 widocznym na ich grafice. Awatar jest realny, ale to plik niskiej jakości, nie zamiennik logo."
    },
    {
     "co": "Umowa albo jej fragment z zapisem o gwarancji (długość, na co)",
     "skad": "Od klienta",
     "czy_na_pewno_ich": "Brief mówi wprost, że gwarancja jest w ICH umowie i klient obiecał podać długość — potwierdzone przez Adama w rozmowie 07.09.2026."
    },
    {
     "co": "Zrzuty ekranu z pochwałami klientów (WhatsApp, Messenger, komentarze pod postami FB)",
     "skad": "Od klienta + komentarze publiczne pod postami na FB/IG",
     "czy_na_pewno_ich": "Zrzuty z jego telefonu = jego. Komentarze z jego profilu FB — profil potwierdzony numerem telefonu. Każdą opinię przed publikacją potwierdzamy z klientem (zgoda osoby wypowiadającej się)."
    },
    {
     "co": "Liczba i treść opinii z wizytówki Google",
     "skad": "Wizytówka Google „A.S TCHÓRZEWSKI\" (link w briefie) — do odczytania ręcznie w Chrome, bo automat trafia na ścianę zgody Google",
     "czy_na_pewno_ich": "⚠️ NIE POTWIERDZONE. Wizytówka nie została odczytana. Dodatkowe ryzyko: pod tym samym adresem działa druga firma budowlana o tym samym nazwisku (Tadeusz Tchórzewski, NIP 7881441770) — przed użyciem opinii trzeba sprawdzić telefon na wizytówce (musi być 667 434 222)."
    },
    {
     "co": "Zdjęcie właściciela / ekipy przy pracy oraz samochodu firmowego z logo",
     "skad": "Od klienta",
     "czy_na_pewno_ich": "Brak — trzeba poprosić wprost. Bez tego strona firmy RODZINNEJ nie pokaże ani jednej twarzy, a to jest jej główny wyróżnik."
    }
   ],
   "uwagi": "Trzy braki, które przesądzają o tym, czy strona będzie konkretna, czy ogólna: (1) czas reakcji — nie mamy go w ogóle, jedyny termin to „wycena do 5 dni roboczych\\\", a to obietnica ZWŁOKI, nie szybkości; (2) żadnej liczby — ani realizacji, ani metrów, ani dni, ani ceny; (3) zero opinii — sekcja opinii w demie stoi pusta, w katalogach firm opinii brak, a wizytówki Google nie udało się odczytać (Google przekierowuje na ścianę zgody — trzeba otworzyć ręcznie w Chrome na Macu K.). Do tego trzy sprzeczności demo↔brief, które trzeba rozstrzygnąć ZANIM ruszy pisanie tekstów: obszar (Wolsztyn i okolice vs wielkopolskie + lubuskie), zakres usług (demo dodało murarkę i tynki, pominęło drzwi i okna), oraz „bezpłatna wycena\\\" — obiecana w demie pięć razy, nigdzie nie potwierdzona przez klienta. Osobne znalezisko: pod tym samym adresem Błońsko 46 zarejestrowana jest druga firma ogólnobudowlana Tadeusz Tchórzewski (NIP 7881441770, dane z CEIDG przez aleo.com) — prawdopodobnie ta sama rodzina, co byłoby świetnym, prawdziwym materiałem na „O nas\\\", ale najpierw trzeba to potwierdzić u właściciela i uważać, żeby nie pomylić wizytówek i opinii obu firm."
  }
 }
]