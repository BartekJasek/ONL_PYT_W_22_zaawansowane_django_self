## Zadanie 1

* Napisz formularz dodający kategorie produktów do bazy danych. Udostępnij go pod adresem URL `/add_category/`. 
    * po wejściu metodą **GET** powinien wyświetlić się pusty formularz, w którym można dodać nową kategorię,
    * po wejściu metodą **POST** kaegoria, powinna zostać zapisana do bazy danych, 
    * po dodaniu nowej kategorii powinniśmy zostać przekierowani pod adres `/categories/`.
    
* Dodaj widok edycji kategorii: 
    * widok powinien umożliwiać zmianę danych kategorii oraz zapisanie tej zmiany do bazy danych, 
    * formularz edycji kategorii powinien być udostępniony pod adresem `/edit_category/{slug}/`,
    * po zmianie danych powinniśmy zostać przekierowani pod adres `/categories/`.

* Zmodyfikuj widok z listą wszystkich kategorii (URL `/categories/`) w następujący sposób:
    * przy opisie każdej kategorii dodaj link: **modyfikuj**, 
    link powinien przekierowywać do adresu `/edit_category/{slug}/`
    * na dole listy kategorii dodaj link: **dodaj kategorię**,
    link powinien przekierowywać do adresu `/add_category/`,


## Zadanie 2

* Napisz formularz dodawania towarów do bazy danych. Dodaj widoki:

    * lista produktów (udostępniony pod adresem `/products/`):
        * wyświetla listę **wszystkich** produktów, niezależnie od kategorii
        (możesz w tym celu zmodyfikować widok `/category/`),
        * przy opisie każdego produktu posiada link do edycji - `/edit_product/{product_id}/`
        * na dole listy produktów ma link **dodaj produkt** prowadzący do adresu `/add_product/`,

    * edycja produktu (udostępniony pod adresem `/edit_product/{product_id}`:
        * po wejściu na link do edycji wyświetla formularz edycji produktu,
        * umożliwia zmianę danych produktu i ich zapisanie,
        * po zmianie danych przekierowuje na stronę z wszystkimi produktami (`/products/`),

    * dodawanie produktu (udostępniony pod adresem `/add_product/`:
        * po wejściu w link **dodaj produkt**, wyświetla pusty formularz,
        * umożliwia dodanie nowego towaru i zapisanie go,
        * po dodaniu nowego produktu przekierowuje na stronę z wszystkimi produktami (`/products/`).

Zadania 1 i 2 z dnia 2, spróbuj rozwiązać używając ModelForms i/lub widoków generycznych.


## Zadanie 3 (*).

* Dodaj formularz wyszukiwania. Powinien mieć tylko jedno pole: szukaj.
* Jeśli formularz został wypełniony poprawnie, powinien wyszukać wpisaną frazę w nazwach produktów **oraz** kategorii 
i zwrócić znalezione wyniki. 
* Utwórz widok, który zaprezentuje wyniki wyszukiwania. 
* Widok powinien być udostępniony pod adresem `/search/`.
