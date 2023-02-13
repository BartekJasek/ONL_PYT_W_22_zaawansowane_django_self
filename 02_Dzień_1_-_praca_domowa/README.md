## Zadanie 1

W folderze **3_Django** znajduje się projekt **coderslab**. Wewnątrz projektu są dwie aplikacje:
* **exercises_app** - przeznaczona do pracy na zajęciach,
* **homework_app** - przeznaczona do rozwiązywania zadań domowych.

Upewnij się, czy projekt jest odpowiednio skonfigurowany. W szczególności zwróć uwagę:
* czy obie aplikacje są dodane do `settings.py`,
* czy baza danych istnieje i jest podpięta do projektu,
* czy jest skonfigurowany odpowiedni język szablonów,
* czy szablony są pobierane z odpowiedniego katalogu (katalog `templates` wewnątrz aplikacji).


## Zadanie 2

Wyobraź sobie oprogramowanie sklepu internetowgo. Sklep może sprzedawać dowolny towar, zatem będzie potrzebna 
struktura danych przechowująca informację na temat towaru oraz kategorii. Każdy towar może posiadać wiele kategorii.
Każda kategoria może zwierać wiele towarów.
Kategorie mają być definiowane przez użytkownika, zatem muszą być przechowywane w bazie danych.

Zdefiniuj następujące modele: 

* `Category` - przechowujący dane na temat kategorii, a w nim następujące pola:
    * `category_name` string o max długości 64 znaki,
    * `slug` string o max długości 64 znaki, unikalny.

Slug to pole, które przechowuje identyfikator znakowy kategorii. 
Może zawierać tylko małe litery, cyfry i znak `-` zamiast spacji. Powinien być unikalny.

* `Product` - trzymający dane na temat produktu, a w nim następujące pola:
    * `name`: nazwa towaru, string o maksymalnej długości 128 znaków,
    * `description`: opis, string o nieograniczonej liczbie znaków,
    * `price`: cena netto towaru, liczba zmiennoprzecinkowa (zignorujmy niedoskonałości typu float),
    * `vat`: podatek VAT, może przyjmować wartości liczbowe: 0.23, 0.08, 0.05, 0,
    * `stock`: liczba produktów w magazynie, integer,
    * `categories`: relacja typu "wiele do wielu" między `Product`, a `Category`.

Wypełnij modele danymi: zdefiniuj kilka dowolnych kategorii, dodaj do kategorii kilka produktów.


## Zadanie 3

* Zdefiniuj szablon bazowy, po którym będą dziedziczyć wszystkie inne szablony w aplikacji.
Szablon powinien mieć nazwę `base.html`.

* Napisz widok, który udostępnisz pod adresem `/categories`. 
Widok powinien pokazać listę wszystkich kategorii w porządku alfabetycznym.
Każda kategoria powinna być linkiem (na razie pustym), który w przyszłości będzie prowadził do listy produktów
z danej kategorii.


## Zadanie 4

Napisz widok, który udostępnisz pod adresem `/category/{slug}` gdzie {slug} to identyfikator tekstowy kategorii. 
W widoku pobierz dane o produktach z tej kategorii, następnie wyświetl informacje o produktach w kolejności 
alfabetycznej. Dane, które mają być widoczne na ekranie:
* **nazwa produktu** - powinna być linkiem, który prowadzi do strony `/product/{id}`,
 gdzie `{id}` to klucz główny produktu. Szczegółowy widok produktu stworzysz później.
* **cena brutto** - cena produktu powiększona o kwotę podatku **VAT**.


## Zadanie 5

Napisz widok, który udostępnisz pod adresem `/product/{id}`, gdzie {id} to identyfikator (klucz główny) produktu. 
Widok ma wyświetlać metryczkę (wszystkie dane) na temat produktu.
