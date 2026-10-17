# Plan testów – KinoTO

| | |
|---|---|
| Identyfikator planu | PT-KinoTO-01 |
| Wersja / data | 1.0 / 2026-10-16 |
| Autor | Adrian Skamarski 174919 |
| Status | szkic |

## 1. Kontekst testowania

### 1.1 Przedmiot testów (elementy testowe)
Symulator systemu rezerwacji biletów kinowych (KinoTO) w postaci arkusza kalkulacyjnego. Testom podlegają interfejs formularza rezerwacji oraz wbudowany kalkulator cen biletów i zniżek.

### 1.2 Zakres testów
- **W zakresie:** Walidacja poprawności wprowadzanych danych w formularzu oraz weryfikacja logiki wyliczania całkowitej ceny rezerwacji w oparciu o cennik bazowy i zniżki, w tym limity biletów na transakcję.
- **Poza zakresem:** Testy wydajnościowe, testy integracji z systemami płatności oraz testy interfejsu użytkownika.

### 1.3 Podstawa testów
Specyfikacja wymagań dla modułu rezerwacji KinoTO.

### 1.4 Założenia i ograniczenia
Testy wykonywane są wyłącznie w trybie manualnym. Aplikacja dostępna jest jedynie jako symulator w pliku Excel. Czas na realizację pełnego procesu testowego ograniczony jest do ram czasowych ćwiczeń.

### 1.5 Interesariusze
Prowadzący zajęcia, zespół deweloperski odpowiedzialny za poprawki logiki.

## 2. Komunikacja
Wyniki testów będą dokumentowane na bieżąco w dedykowanych arkuszach pliku Excel. Po zakończeniu sesji zostanie przygotowany zbiorczy "Raport z wykonania testów", zawierający ocenę kryteriów wyjścia oraz podsumowanie znalezionych błędów, który zostanie przekazany Prowadzącemu.

## 3. Rejestr ryzyk

| ID | Ryzyko (produktowe / projektowe) | Prawdopodobieństwo (1–3) | Wpływ (1–3) | Poziom (P×W) | Działanie ograniczające |
|---|---|---|---|---|---|
| R1 | Błędy w logice sumowania zniżek obniżą dochody firmy (Produktowe) | 3 | 3 | 9 | Dokładne przetestowanie kombinacji zniżek i wartości brzegowych w module kalkulacyjnym. |
| R2 | Brak czasu na wykonanie wszystkich testów w trakcie zajęć (Projektowe) | 2 | 2 | 4 | Priorytetyzacja przypadków testowych – rozpoczęcie od ścieżek krytycznych i głównych funkcjonalności. |

## 4. Strategia testów

### 4.1 Poziomy i typy testów
Testy funkcjonalne na poziomie systemowym. Wykonywane będą wyłącznie testy manualne.

### 4.2 Techniki projektowania testów
Podział na klasy równoważności, analiza wartości brzegowych, a także testowanie eksploracyjne.

### 4.3 Kryteria wejścia
Udostępnienie działającego pliku symulatora z formularzami oraz zatwierdzona specyfikacja wymagań biznesowych dotycząca cen biletów i reguł rezerwacji.

### 4.4 Kryteria wyjścia (ukończenia)
Wykonanie 100% przypadków testowych o statusie "Wysoki", pokrycie wszystkich zdefiniowanych wymagań co najmniej jednym przypadkiem testowym oraz brak otwartych, nierozwiązanych defektów o priorytecie krytycznym. 

### 4.5 Kryteria zawieszenia i wznowienia
Zawieszenie testów nastąpi, jeśli wykryty zostanie defekt całkowicie uniemożliwiający wprowadzanie danych lub gdy formuły pliku ulegną nieodwracalnemu uszkodzeniu. Wznowienie nastąpi po udostępnieniu naprawionego symulatora.

### 4.6 Dane testowe i środowisko
Testy wykonywane lokalnie w programie MS Excel. Pomiędzy poszczególnymi testami należy ręcznie czyścić komórki wprowadzania danych, aby zachować niezależność przypadków testowych. 

### 4.7 Retesty i testy regresji
Po dostarczeniu poprawionej wersji symulatora przeprowadzone zostaną retesty dla wszystkich zgłoszonych defektów w celu weryfikacji ich naprawy, a także uproszczone testy regresji dla kluczowych modułów kalkulacji cen.

### 4.8 Metryki
- Pokrycie wymagań przypadkami testowymi.
- Odsetek przypadków testowych wykonanych.
- Liczba zgłoszonych defektów w podziale na priorytet i dotkliwość.

### 4.9 Produkty testowania (testalia)
Plan testów, zbiór przypadków testowych, karta sesji eksploracyjnej, rejestr defektów oraz raport podsumowujący wykonanie testów.

## 5. Działania testowe i harmonogram

| Działanie | Kto | Termin / czas | Produkt |
|---|---|---|---|
| Analiza wymagań i specyfikacji | Adrian Skamarski | Tydzień 1 | Wytypowane warunki testowe |
| Projektowanie przypadków testowych | Adrian Skamarski | Tydzień 1 | Arkusz "Przypadki testowe" |
| Wykonanie testów + Sesja eksploracyjna | Adrian Skamarski | Tydzień 2 | Arkusze i zebrane Defekty |
| Raportowanie i podsumowanie testów | Adrian Skamarski | Tydzień 2 | Raport z wykonania |

## 6. Role i odpowiedzialności
- **Tester (Adrian Skamarski):** Planowanie testów, analiza wymagań, projektowanie i wykonanie przypadków testowych, zgłaszanie defektów oraz sporządzenie raportu końcowego.
- **Prowadzący:** Zatwierdzenie planu testów, ocena zgłoszonych defektów i końcowego raportu.

## 7. Zatwierdzenie

| Rola | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Autor | Adrian Skamarski | 2026-10-16 | Skamarski |
| Zatwierdzający | | | |