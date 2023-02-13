## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Używając `./manage.py` dodaj superużytkownika.
* Napisz widok, który udostępnisz pod adresem `/list_users/`. Po wejściu metodą GET:
    * pobierz dane wszystkich użytkowników z bazy,
    * wyświetl ich loginy i nazwiska na stronie.


## Zadanie 2
* Napisz widok `/login/`, który:
    * po wejściu metodą GET, wyświetli formularz logowania. Powinien zawierać pola: **nazwa użytkownika** i **hasło**,
    * po wejściu metodą POST, przeprowadzi uwierzytelnianie i logowanie.
        * W razie błędów, poinformuje o tym użytkownika. 

* Napisz widok `/logout/`, który wyloguje użytkownika. 

* Utwórz widok bazowy, który:
    * w stopce będzie pokazywał aktualnie zalogowanego użytkownika.
    * w zależności od tego, czy jakiś użytkownik jest zalogowany, czy nie pokaże link do widoku `/login/` lub `/logout/`,
    * widok udostępnij pod adresem `/`.


## Zadanie 3
* Napisz widok dodawania użytkownika. Udostępnijk go pod adresem URL `/add_user/`. Widok powinien:
    * po wejściu metodą GET, wyświetlić formularz dodawania użytkownika. Pola do wypełnienia:
        * login,
        * hasło (pamiętaj o odpowiednim widgecie),
        * powtórzone hasło,
        * imię,
        * nazwisko,
        * email,
    * po wejściu metodą POST, sprawdzić poprawność formularza:
        * czy login jest już zajęty,
        * czy hasło i powtórzone hasło są takie same,
        * czy email jest poprawny,
    * jeśli dane są poprawne &ndash; założyć konto użytkownika,
    * jeśli dane są błędne &ndash; poinformować użytkownika o błędzie.


## Zadanie 4
* Napisz widok resetowania hasła. Udostępnij go pod adresem URL `/reset_password/{id}`,
gdzie id to identyfikator użytkownika. Widok powinien:
    * po wejściu metodą GET, wyświetlić formularz zmiany hasła użytkownika. Pola do wypełnienia:
        * wprowadź nowe hasło,
        * ponownie wprowadź nowe hasło,
    * po wejściu metodą POST, sprawdzić poprawność formularza:
        * czy nowe hasło i ponowne hasło są takie same,

    * jeśli dane są poprawne &ndash; zmienić hasło użytkownika,
    * jeśli dane są błędne &ndash; poinformować użytkownika o błędzie.

Pamiętaj o odpowiednich widgetach.


## Zadanie 1 &ndash; rozwiązywane z wykładowcą.
Zmodyfikuj zadanie 4 z poprzedniego rozdziału tak, aby tylko użytkownik posiadający uprawnienie "change_user"
mógł wejść do tego widoku.


## Zadanie 2

W aplikacji masz widok udostępniony pod adresem `/notices/`, który napisałeś kilka dni temu.
Zmodyfikuj ten widok (lub template) tak, aby tylko użytkownik z uprawnieniem `add_studentnotice` mógł wysłać uwagę do ucznia.

Następnie dodaj zwykłego użytkownika do aplikacji i nadając / usuwając odpowiednie uprawnienia, przetestuj ten widok.
Wykorzystaj widok do logowania, który napisałeś w  poprzednim rozdziale, aby się zalogować na konto tego użytkownika.


## Zadanie 3
* Dodaj ręcznie grupę "teachers", która będzie miała prawa do dodawania notatek i sprawdzania obecności.
* Dodaj ręcznie zwykłego użytkownika, którego dodasz do grupy "teachers".
* Dodaj ręcznie zwykłego użytkownika, który nie będzie dodany do wyżej wymienionej grupy 
i nie będzie miał wyżej wymienionych uprawnień.

Przetestuj uprawnienia użytkowników.
