# Raport z defektów - aplikacja SklepTO

## Defekt 1 (DEF-01)
* **Wymaganie:** REQ-UI-02
* **Kroki do reprodukcji:** Otwarcie dowolnej podstrony aplikacji
* **Oczekiwany rezultat:** Tytuł strony (element `<title>`) ma postać „SklepTO – <nazwa strony>”
* **Rzeczywisty rezultat:** Tytuł wyświetlany w przeglądarce nie zgadza się ze specyfikacją
* **Test, który wykrył błąd:** `test_page_titles` w pliku `test_ui.py`

## Defekt 2 (DEF-02)
* **Wymaganie:** REQ-UI-01
* **Kroki do reprodukcji:** Poprawne zalogowanie się na konto użytkownika
* **Oczekiwany rezultat:** W menu pojawia się tekst „Zalogowano: jan” oraz odnośnik „Wyloguj”, a odnośnik „Logowanie” znika
* **Rzeczywisty rezultat:** Po zalogowaniu menu nie zmienia się
* **Test, który wykrył błąd:** `test_valid_login` w pliku `test_login.py`

## Defekt 3 (DEF-03)
* **Wymaganie:** REQ-KON-05
* **Kroki do reprodukcji:** Wypełnienie formularza kontaktowego prawidłowymi danymi i kliknięcie „Wyślij”
* **Oczekiwany rezultat:** Wyświetla się komunikat „Dziękujemy za wiadomość.”, a wiadomość jest zapisywana
* **Rzeczywisty rezultat:** Wysłanie formularza wiesza stronę lub przerywa połączenie, co skutkuje zamknięciem połączenia z przeglądarką. Brak komunikatu zwrotnego
* **Test, który wykrył błąd:** `test_contact_valid_message` w pliku `test_kontakt.py`

## Defekt 4 (DEF-04)
* **Wymaganie:** REQ-UI-03
* **Kroki do reprodukcji:** Otwarcie strony kontakt.php i weryfikacja kodu HTML obrazków
* **Oczekiwany rezultat:** Każdy obrazek posiada niepusty atrybut `alt`
* **Rzeczywisty rezultat:** Brakuje tekstu alternatywnego dla obrazka na stronie
* **Test, który wykrył błąd:** `test_contact_checklist` w pliku `test_kontakt.py`

## Defekt 6 (DEF-06)
* **Wymaganie:** REQ-KAL-08
* **Kroki do reprodukcji:** Obliczenie kosztu dla: 150 zł, zaznaczona karta, kod student10, dostawa kurier
* **Oczekiwany rezultat:** Rabat 15%, dostawa 0.00 zł, do zapłaty 127.50 zł
* **Rzeczywisty rezultat:** Aplikacja błędnie nalicza 20% rabatu
* **Test, który wykrył błąd:** `test_kalkulator_przyklad` w pliku `test_kalkulator.py`

## Defekt 7 (DEF-07)
* **Wymaganie:** REQ-KAL-04, REQ-KAL-05
* **Kroki do reprodukcji:** Wpisanie wartości 100 zł, zaznaczenie karty stałego klienta i wpisanie kodu STUDENT10
* **Oczekiwany rezultat:** Zniżka maksymalna to 15%, do zapłaty 85.00 zł
* **Rzeczywisty rezultat:** Aplikacja sumuje zniżki matematycznie, dając 20% rabatu
* **Test, który wykrył błąd:** `test_kalkulator_kombinacje_oblewajace` w pliku `test_kalkulator.py`