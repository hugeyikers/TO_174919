import pytest
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL

# Oznaczamy całą grupę testów sprawdzających tytuły jako znany DEF-01
@pytest.mark.xfail(reason="DEF-01", strict=True)
@pytest.mark.parametrize("path, expected_title", [
    ("index.php", "SklepTO – Start"),
    ("rejestracja.php", "SklepTO – Rejestracja"),
    ("logowanie.php", "SklepTO – Logowanie"),
    ("kalkulator.php", "SklepTO – Kalkulator"),
    ("zamowienia.php", "SklepTO – Zamówienia"),
    ("kontakt.php", "SklepTO – Kontakt"),
    ("admin.php", "SklepTO – Administracja"),
])
def test_page_titles(driver, path, expected_title):
    """REQ-UI-02"""
    driver.get(f"{SKLEPTO_URL}/{path}")
    assert driver.title == expected_title

def test_logged_out_menu(driver):
    """REQ-UI-01"""
    driver.get(f"{SKLEPTO_URL}/index.php")
    menu_text = driver.find_element(By.TAG_NAME, "nav").text
    assert "Zaloguj" in menu_text or "Logowanie" in menu_text

def test_footer_version(driver):
    """REQ-UI-06"""
    driver.get(f"{SKLEPTO_URL}/index.php")
    footer_text = driver.find_element(By.TAG_NAME, "footer").text
    assert "Wersja 1.0" in footer_text