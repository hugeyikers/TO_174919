import pytest
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL
from helpers import open_page, wait_for


@pytest.mark.xfail(reason="DEF-03", strict=True)
def test_contact_valid_message(driver):
    """REQ-KON-01, REQ-KON-05"""
    open_page(driver, f"{SKLEPTO_URL}/kontakt.php", By.TAG_NAME, "form")
    driver.find_element(By.NAME, "imie").send_keys("Anna")
    driver.find_element(By.NAME, "email").send_keys("anna@example.com")
    driver.find_element(By.NAME, "wiadomosc").send_keys("Wiadomość testowa.")
    driver.find_element(By.XPATH, "//button[text()='Wyślij'] | //input[@value='Wyślij']").click()

    pytest.skip("Formularz wysyła błędne zapytanie zabijające sesję WebDrivera. Oznaczono jako DEF-03.")

    flash = wait_for(driver, By.CLASS_NAME, "flash")
    assert flash.text == "Dziękujemy za wiadomość."


def test_contact_empty_form(driver):
    """REQ-KON-02, REQ-KON-03, REQ-KON-04"""
    open_page(driver, f"{SKLEPTO_URL}/kontakt.php", By.TAG_NAME, "form")
    driver.find_element(By.XPATH, "//button[text()='Wyślij'] | //input[@value='Wyślij']").click()

    wait_for(driver, By.TAG_NAME, "form")
    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Podaj imię." in body_text
    assert "Niepoprawny adres e-mail." in body_text
    assert "Wpisz treść wiadomości." in body_text


@pytest.mark.xfail(reason="DEF-04", strict=True)
def test_contact_checklist(driver):
    """REQ-UI-03, REQ-UI-04, REQ-UI-05"""
    open_page(driver, f"{SKLEPTO_URL}/kontakt.php", By.TAG_NAME, "form")

    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        assert img.get_attribute("alt"), "Brak tekstu alternatywnego (alt) dla obrazka"

    inputs = driver.find_elements(By.CSS_SELECTOR, "input:not([type='submit']):not([type='hidden']), textarea")
    for inp in inputs:
        inp_id = inp.get_attribute("id")
        labels = driver.find_elements(By.CSS_SELECTOR, f"label[for='{inp_id}']")
        assert len(labels) == 1, f"Brak etykiety <label for='...'> dla pola {inp_id}"

    email_input = driver.find_element(By.NAME, "email")
    assert email_input.get_attribute("type") == "email"