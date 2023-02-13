## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

W katalogu z zadaniami znajdziesz plik **logo.png**.

* Utwórz i skonfiguruj katalog plików statycznych.
* Skopiuj plik **logo.png** do katalogu plików statycznych.
* Do szablonu bazowego szkoły dodaj obrazek **logo.png**.


## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Napisz formularz wyszukiwania ucznia. Formularz powinien wyświetlać jedno pole: **nazwisko**.
* Napisz widok, który:
    * po wejściu metodą **GET** wyświetli formularz wyszukiwania ucznia,
    * po wejściu metodą **POST**, odbierze dane następnie, 
    * wyszuka dane w bazie danych, używając modelu (wystarczy wprowadzić fragment nazwiska,
     program powinien wyszukać wszystkich uczniów, których nazwiska pasują do wzorca),
     po czym przekaże je do szablonu i wyświetli wyniki na stronie,
    * widok udostępnij pod adresem URL: `/student_search`.


## Zadanie 2

* Napisz formularz, który przyjmuje 3 parametry: imię, nazwisko i klasę, do której uczęszcza uczeń. 
Pole z klasą ucznia powinno przyjmować wartości, które znajdują się w stałej `SCHOOL_CLASS`.
* Napisz widok, który udostępnisz pod adresem `/add_student`.  
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST odbierze dane z formularza i doda ucznia do bazy,
    po czym przekieruje użytkownika na stronę metryczki danego ucznia.


## Zadanie 3

Zmodyfikuj widok, model i/lub formularz z poprzedniego zadania. Do modelu dodaj pole `year_of_birth`, 
które będzie przechowywało wartość typu **integer**. Pozwól użytkownikowi dodać tę wartość przy pomocy formularza.


## Zadanie 4

* Napisz formularz konwersji walut. Formularz powinien mieć następujące pola:
    * `currency1`: pole przyjmujące liczbę zmiennoprzecinkową,
    * `currency2`: pole przyjmujące liczbę zmiennoprzecinkową,
    * `conversion`: dropdown przyjmujący jedną z dwóch wartości: **PLNtoUSD** i **USDtoPLN**.
* Napisz widok, który udostępnisz pod adresem `/exchange`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST przeliczy waluty ze złotówek na dolary 
    (lub odwrotnie, zależy to od wartości pola `conversion`) i wyświetli wynik.

Dla chętnych:
 
Przerób widok w ten sposób, żeby wynik wyświetlał się w drugim z pól formularza.
Przykładowo, jeśli wypełnimy pole currency1 (PLN) i klikniemy PLNtoUSD, to program uzupełni pole currency2 (USD)
odpowiednią wartością.


## Zadanie 5

* Napisz formularz, który pozwoli dodać oceny uczniowi. Formularz powinien zawierać następujące pola:
    * student: pole z nazwiskiem ucznia,
    * subject: pole z nazwą przedmiotu, 
    * grade: pole ze stopniem. Pole powinno przybierać tylko wartości znajdujące się w stałej `GRADES`. 

* Napisz widok, który udostępnisz pod adresem `/add_grade`. Widok powinien definiować następujące funkcjonalności:
    * po wejściu metodą GET, powinien wyświetlić pusty formularz,
    * po wejściu metodą POST, powinien:
        * odebrać dane z formularza,
        * sprawdzić, czy dany uczeń istnieje w bazie danych, jeśli nie &ndash; wyświetlić komunikat: 
        "Nie ma takiego ucznia!",
        * sprawdzić, czy dany przedmiot istnieje w bazie danych, jeśli nie &ndash; wyświetlić komunikat:
        "Nie ma takiego przedmiotu!", 
        * jeśli dane są poprawne, dopisać uczniowi stopień z danego przedmiotu i zapisać do bazy,
        * przekierować użytkownika do strony z danymi ucznia. 

Dla chętnych:

Przerób formularz w ten sposób, aby przedmiot był wybierany z listy dostępnych przedmiotów.

---

Podpowiedź: różne typy pól formularza poznasz w dalszej części prezentacji. 
Przydatne pola: 
* `forms.CharField`
* `forms.IntegerField`
* `forms.ChoiceField`
* `forms.FloatField`

Więcej na ten temat znajdziesz w dokumentacji: https://docs.djangoproject.com/en/4.0/ref/forms/fields/


## Zadanie 1 &ndash; wykonywane razem z wykładowcą.

* Napisz formularz, który będzie pozwalał skomponować dodatki do pizzy.
* Powinien mieć tylko jedno pole, za to wielokrotnego wyboru. Wartości, które będzie można wybrać, to:
    * oliwki,
    * pomidory,
    * dodatkowy ser,
    * anchovies,
    * cebula.
* Napisz widok, który po wejściu metodą **GET**, wyświetli formularz.
* Zmień widget pola na `CheckboxSelectMutiple` i porównaj różnice.

W LMS znajdziesz artykuł "Snippets", który zawiera gotowe modele do tego zadania.


## Zadanie 2

* Napisz model `PresenceList`, który będzie przechowywał listę obecności ucznia na lekcjach. 
Model powinien mieć następujące pola:
    * student: klucz obcy do modelu `Student`,
    * day: pole typu date (tylko data) &ndash; dzień lekcyjny,
    * present: wartość logiczna, powinna pozwalać na brak wartości (null).

* Napisz formularz, który będzie zawierał dane, jak w powyższym modelu,

* Napisz widok, który udostępnisz pod adresem `/class_presence/{student_id}/{date}`, 
gdzie {student_id} to identyfikator ucznia, a {date} to dzień w szkole. 
    * po wejściu metodą GET, widok powinien wyświetlić formularz dla daty podanej w parametrze. 
    Pole `day` powinno być ukryte (użyj widgetu `HiddenInput`),
    * po wejściu metodą POST, widok powinien zapisać dane o obecności ucznia.
 

## Zadanie 3.

* Napisz formularz z jednym polem: `background_color`. Pole to powinno pozwalać na wpisanie 5 wartości:
black, white, red, yellow i blue.

* Napisz widok, który udostępnisz pod adresem `/set_color`. 
    * po wejściu metodą GET, widok  powinien pokazać formularz. 
    Pole `background_color` powinno używać widgetu `RadioSelect`,
    * po wejściu metodą POST, widok powinien pokazać powyższy formularz. 
    Dodatkowo powinno zmienić się tło na kolor wybrany przez użytkownika.


## Zadanie 4

* Napisz formularz logowania z dwoma polami: `login` i `password`. 
Pole `password` powinno używać widgetu `PasswordInput`. 
* Napisz widok, który udostępnisz pod adresem `/login`. 
Widok po wejściu metodą GET ma wyświetlić pusty formularz logowania.
* Napisz metodę `post()` do poprzedniego zadania, która:
    * odbierze dane z formularza, 
    * sprawdzi, czy użytkownik to **root**,
    * sprawdzi, czy hasło to **very\_secret**. 
    Jeśli tak, pokaże na ekranie przeglądarki: "Miło Cię widzieć". W przeciwnym wypadku wyświetli: "A sio, hackerze!".


## Zadanie 1 &ndash; wykonywane razem z wykładowcą.
* Napisz formularz, który przyjmie od użytkownika następujące pola:
    * imię,
    * nazwisko,
    * mail,
    * ulubiona strona www.
* Pola mail i www, niech będą walidowane odpowiednimi walidatorami 
(sprawdź w dokumentacji pod adresem: [https://docs.djangoproject.com/en/4.0/ref/validators/#emailvalidator](https://docs.djangoproject.com/en/4.0/ref/validators/#emailvalidator)).
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e1`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. 
    W przypadku poprawnych danych niech je pokaże w przeglądarce. 


## Zadanie 2

* Napisz walidator, który sprawdzi, czy walidowana liczba jest w zakresie 2000 - 2004. 
* Użyj tego walidatora, aby sprawdzić poprawność danych w formularzu z zadania 3 z działu **1_Formularze**.


## Zadanie 3

* Napisz formularz, który pozwoli Ci wprowadzić imię i nazwisko.
* Do formularza dodaj walidator, który sprawdzi, czy imię jest żeńskie. Jeśli nie, poinformuj o błędzie użytkownika. 
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e3`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. 
    W przypadku poprawnych danych niech je pokaże w przeglądarce.
 
##### Podpowiedź: Przyjmij, że żeńskie imiona to te, które kończą się literą "a". Wyjątki (np. Barnaba, Kuba) 
##### możesz zignorować.


## Zadanie 4
* Napisz formularz, zawierający dwa pola, przyjmujące odpowiednio **liczbę** i **string**,
* Do formularza dodaj walidator, który sprawdzi, czy liczba jest z zakresu 1 - 100.
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e4`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. 
    W przypadku poprawnych danych wypisze string tyle razy, ile wynosi wprowadzona w drugim polu liczba.


## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Napisz formularz dziedziczący po klasie ModelForm, który pozwoli na dodanie przedmiotu do bazy danych.
* Napisz widok, który:
    * Po wejściu metodą GET, wyświetli pusty formularz,
    * Po wejściu metodą POST, zapisze dane bazy danych (używając modelu powiązanego z formularzem).


## Zadanie 2

* Napisz model `Message`, który będzie reprezentował maila do nauczyciela danego przedmiotu. 
Model powinien mieć następujące pola:
    * `subject`: pole tekstowe, max. 256 znaków,
    * `content`: pole tekstowe o nieograniczonej liczbie znaków,
    * `to`: klucz obcy do nauczyciela,
    * `from`: klucz obcy do ucznia,
    * `date_sent`: pole typu datetime, automatycznie uzupełniane przy zapisie.

* Napisz formularz dziedziczący po klasie ModelForm, który będzie pozwalał na obsługę modelu `Message`. 
Formularz ma udostępniać wszystkie pola oprócz `date_sent`.

* Napisz widok (udostępnij pod URL-em `/send_message`), który:
    * po wejściu metodą GET, wyświetli formularz,
    * po wejściu metodą POST, zapisze maila do bazy.


## Zadanie 3

* Napisz model `StudentNotice`, który będzie reprezentował uwagi od nauczycieli dla uczniów. 
Model powinien mieć następujące pola:
    `from`: klucz obcy do nauczyciela,
    `to`: klucz obcy do ucznia,
    `content`: pole tekstowe o nieograniczonej liczbie znaków.

* Napisz formularz dziedziczący po klasie ModelForm, który będzie pozwalał na obsługę modelu `StudentNotice`.

* Napisz widok, który udostępnisz pod adresem `/notices/{student_id}`, gdzie id to identyfikator ucznia. 
Widok powinien wyciągnąć z bazy wszystkie uwagi dla danego ucznia i zaprezentować je na stronie. 
W szablonie umieść też odpowiednie linki dla nauczyciela do dodawania i usuwania istniejących uwag.


## Zadanie 4.

* Napisz widoki, dziedziczące po widokach generycznych, które umożliwią dodanie i usunięcie uwagi dla ucznia.
