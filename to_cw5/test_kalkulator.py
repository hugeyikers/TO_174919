import time
import pytest
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL
from helpers import open_page


def wypelnij_kalkulator(driver, wartosc, karta, kod, dostawa):
    open_page(driver, f"{SKLEPTO_URL}/kalkulator.php", By.TAG_NAME, "form")

    pole_wartosc = driver.find_element(By.XPATH, "//input[contains(@name, 'wartosc') or contains(@id, 'wartosc')]")
    pole_wartosc.clear()
    pole_wartosc.send_keys(str(wartosc))

    pole_karta = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    if karta != pole_karta.is_selected():
        pole_karta.click()

    pole_kod = driver.find_element(By.XPATH, "//input[contains(@name, 'kod') or contains(@id, 'kod')]")
    pole_kod.clear()
    pole_kod.send_keys(kod)

    wartosc_dla_html = dostawa.lower().replace('ó', 'o').split()[0]
    radio_xpath = f"//input[@type='radio' and contains(translate(@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{wartosc_dla_html}')]"
    driver.find_element(By.XPATH, radio_xpath).click()

    driver.find_element(By.XPATH, "//button[contains(text(), 'Oblicz')] | //input[@value='Oblicz']").click()
    time.sleep(0.5)


@pytest.mark.xfail(reason="DEF-06", strict=True)
def test_kalkulator_przyklad(driver):
    """REQ-KAL-08"""
    wypelnij_kalkulator(driver, "150.00", True, "student10", "Kurier")
    wynik = driver.find_element(By.TAG_NAME, "body").text
    assert "15%" in wynik
    assert "0.00 zł" in wynik
    assert "127.50 zł" in wynik


# Tu zostaje TYLKO ta jedna kombinacja, która faktycznie źle liczy rabat (daje 20% zamiast 15%)
@pytest.mark.xfail(reason="DEF-07", strict=True)
@pytest.mark.parametrize("wartosc, karta, kod, dostawa, oczekiwany_rabat, oczekiwana_dostawa, oczekiwana_kwota", [
    ("100", True, "STUDENT10", "Odbiór osobisty", "15%", "0.00 zł", "85.00 zł"),
])
def test_kalkulator_kombinacje_oblewajace(driver, wartosc, karta, kod, dostawa, oczekiwany_rabat, oczekiwana_dostawa,
                                          oczekiwana_kwota):
    """REQ-KAL-03, REQ-KAL-04, REQ-KAL-05, REQ-KAL-06, REQ-KAL-07"""
    wypelnij_kalkulator(driver, wartosc, karta, kod, dostawa)
    wynik = driver.find_element(By.TAG_NAME, "body").text
    assert oczekiwany_rabat in wynik
    assert oczekiwana_dostawa in wynik
    assert oczekiwana_kwota in wynik


# Wszystkie pozostałe kombinacje aplikacja liczy poprawnie!
@pytest.mark.parametrize("wartosc, karta, kod, dostawa, oczekiwany_rabat, oczekiwana_dostawa, oczekiwana_kwota", [
    ("100", False, "", "Kurier", "0%", "15.00 zł", "115.00 zł"),
    ("100", True, "", "Kurier", "10%", "0.00 zł", "90.00 zł"),
    ("100", False, "STUDENT10", "Paczkomat", "10%", "10.00 zł", "100.00 zł"),
    ("200", False, "", "Kurier", "0%", "0.00 zł", "200.00 zł")
])
def test_kalkulator_kombinacje_poprawne(driver, wartosc, karta, kod, dostawa, oczekiwany_rabat, oczekiwana_dostawa,
                                        oczekiwana_kwota):
    wypelnij_kalkulator(driver, wartosc, karta, kod, dostawa)
    wynik = driver.find_element(By.TAG_NAME, "body").text
    assert oczekiwany_rabat in wynik
    assert oczekiwana_dostawa in wynik
    assert oczekiwana_kwota in wynik


# Aplikacja poprawnie wyświetla błędy dla tych wartości! (Brak DEF-08)
@pytest.mark.parametrize("wartosc", ["0", "10000.01", "abc"])
def test_kalkulator_niepoprawne_wartosci(driver, wartosc):
    """REQ-KAL-02"""
    wypelnij_kalkulator(driver, wartosc, False, "", "Kurier")
    wynik = driver.find_element(By.TAG_NAME, "body").text
    assert "Wartość zamówienia musi być liczbą z zakresu 0,01–10000,00." in wynik