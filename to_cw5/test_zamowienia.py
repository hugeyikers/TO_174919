import pytest
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL
from helpers import open_page


def zaloguj(driver, login, haslo):
    """Pomocnicza funkcja do logowania przed testami zamówień."""
    open_page(driver, f"{SKLEPTO_URL}/logowanie.php", By.ID, "form-logowanie")
    driver.find_element(By.ID, "login").send_keys(login)
    driver.find_element(By.ID, "haslo").send_keys(haslo)
    driver.find_element(By.ID, "zaloguj").click()


def test_zamowienia_wymaga_logowania(driver, no_cookies):
    """REQ-ZAM-01: Dostęp tylko dla zalogowanych."""
    driver.get(f"{SKLEPTO_URL}/zamowienia.php")

    # Niezalogowany użytkownik powinien zostać zablokowany/przekierowany
    wynik = driver.find_element(By.TAG_NAME, "body").text
    assert "Zaloguj się, aby zobaczyć" in wynik or driver.title == "SklepTO – Logowanie"


def test_zamowienia_zalogowany_widzi_swoje(driver, clean_db):
    """REQ-ZAM-02: Użytkownik widzi tylko swoje zamówienia."""
    zaloguj(driver, "jan", "Haslo123")
    driver.get(f"{SKLEPTO_URL}/zamowienia.php")

    wynik = driver.find_element(By.TAG_NAME, "body").text.lower()

    # Jan powinien widzieć tabelę ze swoimi zamówieniami
    assert "jan" in wynik, "Brak zamówień Jana na liście"
    # Jan absolutnie NIE MOŻE widzieć zamówień innych użytkowników (np. anny)
    assert "anna" not in wynik, "LUKA W ZABEZPIECZENIACH: Jan widzi zamówienia Anny!"