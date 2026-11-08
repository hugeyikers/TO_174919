import pytest
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL
from helpers import open_page, wait_for


def log_in(driver, login, password):
    """Fills in the login form; returns the #flash message."""
    open_page(driver, f"{SKLEPTO_URL}/logowanie.php", By.ID, "form-logowanie")
    driver.find_element(By.ID, "login").send_keys(login)
    driver.find_element(By.ID, "haslo").send_keys(password)
    driver.find_element(By.ID, "zaloguj").click()
    return wait_for(driver, By.ID, "flash")


@pytest.mark.xfail(reason="DEF-02", strict=True)
def test_valid_login(driver):
    """REQ-LOG-02"""
    assert log_in(driver, "jan", "Haslo123").text == "Zalogowano jako jan."
    menu_elements = driver.find_elements(By.CSS_SELECTOR, "nav a")
    menu_texts = [el.text for el in menu_elements]
    assert "Zalogowano: jan" in menu_texts


@pytest.mark.parametrize("login, password, expected_flash", [
    ("jan", "ZleHaslo", "Błędny login lub hasło. Pozostało prób: 2."),
    ("nieznany", "ZleHaslo", "Błędny login lub hasło."),
    ("zablokowany", "Haslo123", "Konto jest zablokowane. Skontaktuj się z administratorem."),
    ("", "", "Błędny login lub hasło.")
])
def test_invalid_login(driver, clean_db, login, password, expected_flash):
    """REQ-LOG-03, REQ-LOG-05, REQ-LOG-06"""
    flash = log_in(driver, login, password)
    assert flash.text == expected_flash


def test_logout(driver):
    """REQ-LOG-07"""
    log_in(driver, "jan", "Haslo123")
    driver.find_element(By.LINK_TEXT, "Wyloguj").click()
    flash = wait_for(driver, By.ID, "flash")
    assert flash.text == "Wylogowano."


def test_account_lockout(driver, clean_db):
    """REQ-LOG-04, REQ-LOG-08"""
    log_in(driver, "anna", "Zle1")
    log_in(driver, "anna", "Zle2")
    flash = log_in(driver, "anna", "Zle3")
    assert flash.text == "Konto zostało zablokowane po 3 nieudanych próbach."

    open_page(driver, f"{SKLEPTO_URL}/admin.php", By.TAG_NAME, "table")
    locked_cell = driver.find_elements(By.XPATH, "//td[text()='anna']/following-sibling::td[text()='LOCKED']")
    assert len(locked_cell) > 0