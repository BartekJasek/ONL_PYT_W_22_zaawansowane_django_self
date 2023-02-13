## Zadanie 1

* Dodaj widok logowania, wraz z odpowiednim formularzem (możesz użyć kodu z zajęć). 
* Widok powinien być udostępniony pod adresem `/login`/. 
* Po udanym zalogowaniu powinniśmy zostać przeniesieni na stronę `/products/`.


## Zadanie 2

* Zabezpiecz aplikację w taki sposób, by widoki edycji towaru i kategorii były dostępne tylko dla użytkowników,
kótrzy mają przyznane prawa do odpowiednich akcji:
    * "add\_product",
    * "add\_category",
    * "edit\_product",
    * itp.
* Powyższe uprawnienia powinny dotyczyć odpowiednich modeli.


## Zadanie 3

* Zabezpiecz szablony tak, by linki do odpowiednich akcji (dodaj produkt, modyfikuj produkt, itp.) 
pojawiały się tylko użytkownikom mającym odpowiednie uprawnienia.


## Zadanie 4

* Dodaj modele stworzone podczas pracy domowej do panelu **admina**. 
W tym celu napisz własne modele dziedziczące po `admin.ModelAdmin`
* Zapewnij czytelność panelu administracyjnego przez odpowiednie nadpisanie metody `__str__()` 
(powinny pojawiać się tylko nazwy produktów i kategorii). 
* Zapewnij łatwość użytkowania dodając odpowiednie pola dla wyżej wspomnianych modeli.
