"""Shared fixtures for all tests (conftest.py)."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import SKLEPTO_URL


def reset_database(driver):
    """Restores SklepTO initial data (jan, anna, zablokowany + orders)."""
    driver.get(f"{SKLEPTO_URL}/install.php?reset=1")
    status = driver.find_element(By.ID, "install-status").text
    assert status == "OK", "Database reset failed is MySQL running?"


@pytest.fixture(scope="session")
def driver():
    """One Chrome browser for the whole session + initial data."""
    drv = webdriver.Chrome()
    drv.implicitly_wait(0)
    reset_database(drv)
    yield drv
    drv.quit()


# once, before the first test
@pytest.fixture(autouse=True)
def no_cookies(driver):
    """Every test starts as a logged-out user (new PHP session)."""
    driver.delete_all_cookies()


@pytest.fixture
def clean_db(driver):
    """On request: reset right before the test."""
    reset_database(driver)