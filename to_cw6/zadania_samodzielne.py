from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL


def test_task1_dynamic_loading_loader(driver):
    driver.get(f"{INTERNET_URL}/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    wait = WebDriverWait(driver, 10)
    loader = wait.until(EC.visibility_of_element_located((By.ID, "loading")))
    assert loader.is_displayed()

    assert wait.until(EC.invisibility_of_element(loader))
    assert driver.find_element(By.CSS_SELECTOR, "#finish h4").text == "Hello World!"


def test_task2_dynamic_controls_enable_input(driver):
    driver.get(f"{INTERNET_URL}/dynamic_controls")
    driver.find_element(By.CSS_SELECTOR, "#input-example button").click()

    field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
    )
    field.send_keys("Selenium")
    assert field.get_attribute("value") == "Selenium"


def test_task3_prompt_cancelled(driver):
    driver.get(f"{INTERNET_URL}/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.dismiss()

    assert driver.find_element(By.ID, "result").text == "You entered: null"


def test_task4_iframe_tinymce_editor(driver):
    driver.get(f"{INTERNET_URL}/iframe")

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr"))
    )
    text = driver.find_element(By.ID, "tinymce").text
    driver.switch_to.default_content()

    assert text == "Your content goes here."


class ScrollUntilParagraphs:
    def __init__(self, target_count):
        self.target_count = target_count

    def __call__(self, driver):
        paragraphs = driver.find_elements(By.CLASS_NAME, "jscroll-added")
        if len(paragraphs) >= self.target_count:
            return paragraphs
        footer = driver.find_element(By.ID, "page-footer")
        ActionChains(driver).scroll_to_element(footer).perform()
        return False


def test_task5_infinite_scroll_condition_class(driver):
    driver.get(f"{INTERNET_URL}/infinite_scroll")

    paragraphs = WebDriverWait(driver, 15).until(ScrollUntilParagraphs(5))
    assert len(paragraphs) >= 5