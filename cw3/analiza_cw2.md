# Analiza Klas Równoważności (EP) i Wartości Brzegowych (AWB)

## 1. `grade_from_percent(percent)`

### Tabela klas równoważności (EP)
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
| :--- | :--- | :--- | :--- | :--- |
| OC-K1 | 0–50 | poprawna | 25 | 2.0 |
| OC-K2 | 51–60 | poprawna | 55 | 3.0 |
| OC-K3 | 61–70 | poprawna | 65 | 3.5 |
| OC-K4 | 71–80 | poprawna | 75 | 4.0 |
| OC-K5 | 81–90 | poprawna | 85 | 4.5 |
| OC-K6 | 91–100 | poprawna | 95 | 5.0 |
| OC-N1 | < 0 | niepoprawna (wartość) | -5 | ValueError |
| OC-N2 | > 100 | niepoprawna (wartość) | 105 | ValueError |
| OC-N3 | typ != int (float) | niepoprawna (typ) | 75.5 | TypeError |
| OC-N4 | typ != int (str) | niepoprawna (typ) | "pięć" | TypeError |
| OC-N5 | typ != int (None) | niepoprawna (typ) | None | TypeError |
| OC-N6 | typ != int (bool) | niepoprawna (typ) | True | TypeError |

### Tabela wartości brzegowych (AWB)
**Precyzja:** 1 punkt procentowy (liczba całkowita)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
| :--- | :--- | :--- | :--- |
| Min. pkt / Max. dla < 0 | -1, 0 | 1 | ValueError, 2.0, 2.0 |
| Max. dla 2.0 | 50, 51 | 49 | 2.0, 3.0, 2.0 |
| Max. dla 3.0 | 60, 61 | 59 | 3.0, 3.5, 3.0 |
| Max. dla 3.5 | 70, 71 | 69 | 3.5, 4.0, 3.5 |
| Max. dla 4.0 | 80, 81 | 79 | 4.0, 4.5, 4.0 |
| Max. dla 4.5 | 90, 91 | 89 | 4.5, 5.0, 4.5 |
| Max. pkt / Min. dla > 100| 100, 101 | 99 | 5.0, ValueError, 5.0 |

**Elementy pokrycia:** 14 elementów dla 2p, 7 elementów dla 3p.

---

## 2. `parking_fee(minutes)`

### Tabela klas równoważności (EP)
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
| :--- | :--- | :--- | :--- | :--- |
| PK-K1 | 0–15 (0 zł) | poprawna | 10 | 0.0 |
| PK-K2 | 16–60 (5 zł) | poprawna | 30 | 5.0 |
| PK-K3 | 61–120 (10 zł) | poprawna | 90 | 10.0 |
| PK-K4 | 121–180 (15 zł) | poprawna | 150 | 15.0 |
| PK-K5 | 181–1440 (20 zł) | poprawna | 300 | 20.0 |
| PK-N1 | < 0 | niepoprawna (wartość) | -10 | ValueError |
| PK-N2 | > 1440 | niepoprawna (wartość) | 1500 | ValueError |
| PK-N3 | typ != int (float) | niepoprawna (typ) | 15.5 | TypeError |
| PK-N4 | typ != int (str) | niepoprawna (typ) | "sto" | TypeError |
| PK-N5 | typ != int (bool) | niepoprawna (typ) | False | TypeError |

### Tabela wartości brzegowych (AWB)
**Precyzja:** 1 minuta (liczba całkowita)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
| :--- | :--- | :--- | :--- |
| Min. czas / Max. dla < 0 | -1, 0 | 1 | ValueError, 0.0, 0.0 |
| Max. dla 0 zł | 15, 16 | 14 | 0.0, 5.0, 0.0 |
| Max. dla 5 zł | 60, 61 | 59 | 5.0, 10.0, 5.0 |
| Max. dla 10 zł | 120, 121 | 119 | 10.0, 15.0, 10.0 |
| Max. dla 15 zł | 180, 181 | 179 | 15.0, 20.0, 15.0 |
| Max. czas / Min. dla > 1440 | 1440, 1441 | 1439 | 20.0, ValueError, 20.0 |

**Elementy pokrycia:** 12 elementów dla 2p, 6 elementów dla 3p.

---

## 3. `validate_password(password)`

### Tabela klas równoważności (EP)
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
| :--- | :--- | :--- | :--- | :--- |
| HS-K1 | dł. 8-20, ma literę i cyfrę | poprawna | "Haslo123" | True |
| HS-K2 | dł. 8-20, litera, cyfra, inne znaki | poprawna | "Haslo!23 " | True |
| HS-N1 | długość < 8 | niepoprawna (wartość) | "Has1" | False |
| HS-N2 | długość > 20 | niepoprawna (wartość) | "BardzoDlugieHaslo12345" | False |
| HS-N3 | skład: brak cyfry | niepoprawna (wartość) | "TylkoLitery" | False |
| HS-N4 | skład: brak litery | niepoprawna (wartość) | "123456789" | False |
| HS-N5 | typ != str (int) | niepoprawna (typ) | 12345678 | TypeError |
| HS-N6 | typ != str (list) | niepoprawna (typ) | ['A','a','1','2','3'] | TypeError |

### Tabela wartości brzegowych (AWB)
**Precyzja:** 1 znak (dla wymiaru długości hasła)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
| :--- | :--- | :--- | :--- |
| Min. długość (8 znaków) | 7, 8 | 9 | False, True, True |
| Max. długość (20 znaków) | 20, 21 | 19 | True, False, True |

*(Uwaga: Granice składu hasła – minimum 1 litera / 1 cyfra – testuje się klasami abstrakcyjnymi z EP, AWB stosujemy tu dla mierzalnej długości)*

**Elementy pokrycia:** 4 elementy dla 2p, 2 elementy dla 3p.

---

## 4. `ticket_price(age)`

### Tabela klas równoważności (EP)
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
| :--- | :--- | :--- | :--- | :--- |
| BL-K1 | 0–6 (bezpłatny, 0 zł) | poprawna | 5 | 0.0 |
| BL-K2 | 7–18 (ulg. rozłączna 1, 10 zł) | poprawna | 15 | 10.0 |
| BL-K3 | 19–64 (normalny, 20 zł) | poprawna | 30 | 20.0 |
| BL-K4 | 65–120 (ulg. rozłączna 2, 10 zł)| poprawna | 70 | 10.0 |
| BL-N1 | < 0 | niepoprawna (wartość) | -5 | ValueError |
| BL-N2 | > 120 | niepoprawna (wartość) | 125 | ValueError |
| BL-N3 | typ != int (float) | niepoprawna (typ) | 18.5 | TypeError |
| BL-N4 | typ != int (str) | niepoprawna (typ) | "dziesięć" | TypeError |
| BL-N5 | typ != int (None) | niepoprawna (typ) | None | TypeError |

### Tabela wartości brzegowych (AWB)
**Precyzja:** 1 rok (liczba całkowita)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
| :--- | :--- | :--- | :--- |
| Min. wiek / Max. dla < 0 | -1, 0 | 1 | ValueError, 0.0, 0.0 |
| Max. dla 0 zł | 6, 7 | 5 | 0.0, 10.0, 0.0 |
| Max. dla ulgi 1 (10 zł) | 18, 19 | 17 | 10.0, 20.0, 10.0 |
| Max. dla normalnego (20 zł) | 64, 65 | 63 | 20.0, 10.0, 20.0 |
| Max. wiek / Min. dla > 120 | 120, 121 | 119 | 10.0, ValueError, 10.0 |

**Elementy pokrycia:** 10 elementów dla 2p, 5 elementów dla 3p.

# Defekty

### DEF-01
| Pole | Treść |
| :--- | :--- |
| ID, tytuł | DEF-01 „grade_from_percent() nie zgłasza TypeError dla niepoprawnych typów” |
| Wymaganie | OC-4 |
| Kroki | Wywołanie funkcji z wartościami `75.5` (float), `"pięć"` (str) oraz `True` (bool) |
| Oczekiwany / rzeczywisty | Oczekiwano: `TypeError`. Rzeczywisty: brak wyjątku (`DID NOT RAISE`) dla float/bool, natomiast dla str rzuca `ValueError`. (Oczekiwany wynik zgadza się ze specyfikacją). |
| Test, ważność | `test_ep_wrong_type[float]`, `[str]`, `[bool]`; wysoka |

**Analiza porażki:** Defekt leży w kodzie testowanego programu (sut). Błąd został wykryty za pomocą techniki **EP** (klasy niepoprawne – niewłaściwy typ). Technika AWB nie wykryłaby go, ponieważ bada ona liczbowe granice dziedziny, a nie obsługę nieprawidłowych typów zmiennych.

---

### DEF-02
| Pole | Treść |
| :--- | :--- |
| ID, tytuł | DEF-02 „grade_from_percent(90) zwraca 5.0 zamiast 4.5” |
| Wymaganie | OC-2 |
| Kroki | Wywołanie `grade_from_percent(90)` |
| Oczekiwany / rzeczywisty | Oczekiwano: `4.5`. Rzeczywisty: `5.0`. (Oczekiwany wynik zgadza się ze specyfikacją). |
| Test, ważność | `test_bva_2p[bound_90]`; wysoka |

**Analiza porażki:** Defekt leży w kodzie programu (prawdopodobnie użyto `>=` zamiast `>`). Błąd wykryła technika **AWB 2p** (bezpośredni brzeg). Technika EP mogłaby go przeoczyć (dla bezpiecznej wartości ze środka klasy, np. 85, funkcja działa poprawnie), podobnie jak AWB 3p, które badało punkty obok (89 i 91).

---

### DEF-03
| Pole | Treść |
| :--- | :--- |
| ID, tytuł | DEF-03 „parking_fee(1) nalicza opłatę 5.0 zamiast 0.0” |
| Wymaganie | PK-2 |
| Kroki | Wywołanie `parking_fee(1)` |
| Oczekiwany / rzeczywisty | Oczekiwano: `0.0`. Rzeczywisty: `5.0`. (Oczekiwany wynik zgadza się ze specyfikacją). |
| Test, ważność | `test_bva_3p_extra[bound_1]`; wysoka |

**Analiza porażki:** Defekt programu na początku przedziału (błędna obsługa 1. minuty). Błąd wykryła wyłącznie technika **AWB 3p** (wewnętrzna strona pierwszego przedziału). EP (np. testowane 10 min) oraz AWB 2p (testujące precyzyjnie 0 i 15 min) dały wynik pozytywny i nie zdołały wyłapać tej anomalii.

---

### DEF-04
| Pole | Treść |
| :--- | :--- |
| ID, tytuł | DEF-04 „validate_password() odrzuca poprawne hasła z polskimi znakami, spacją i znakami specjalnymi” |
| Wymaganie | HS-3, HS-4 |
| Kroki | Wywołanie `validate_password("Za żółć 1")` oraz `validate_password("H@slo!23#")` |
| Oczekiwany / rzeczywisty | Oczekiwano: `True`. Rzeczywisty: `False`. (Oczekiwany wynik zgadza się ze specyfikacją). |
| Test, ważność | `test_ep_valid[polish_letters_and_spaces]`, `[special_chars]`; wysoka |

**Analiza porażki:** Defekt programu (zbyt restrykcyjna walidacja znaków). Błąd wykryty przez **EP** (klasy poprawne dla dozwolonych układów znaków). Zastosowane dla tej funkcji AWB nie wykryłoby defektu, ponieważ dotyczyło wyłącznie weryfikacji długości łańcucha znaków, a nie jego zawartości.

---

### DEF-05
| Pole | Treść |
| :--- | :--- |
| ID, tytuł | DEF-05 „ticket_price(119) i (120) rzuca ValueError zamiast zwrócić cenę biletu” |
| Wymaganie | BL-1, BL-2 |
| Kroki | Wywołanie `ticket_price(119)` oraz `ticket_price(120)` |
| Oczekiwany / rzeczywisty | Oczekiwano: `10.0`. Rzeczywisty: wyjątek `ValueError: wiek spoza obsługiwanego zakresu`. (Oczekiwany wynik zgadza się ze specyfikacją). |
| Test, ważność | `test_bva_3p_extra[bound_119]`, `test_bva_2p[bound_120]`; średnia |

**Analiza porażki:** Defekt programu (ustawiono zbyt niski limit maksymalnego wieku `MAX_AGE`). Błąd wykryty przez techniki **AWB 2p** oraz **AWB 3p** sprawdzające górną granicę dziedziny. EP miałoby szansę to wykryć tylko pod warunkiem "wylosowania" nietypowego reprezentanta dla klasy wiekowej +65 (np. gdyby ktoś jawnie wybrał wiek 120 lat, a nie bezpieczne 70 lat).