import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def setup():
    print("Setting up the test environment")
    # You can add any setup code here, such as initializing a database connection or starting a web server
    # Example: Initialize a Selenium WebDriver
    options = Options()
    options.add_argument("--headless=new")  # Runs without a visible window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    yield driver,wait
    # You can add any teardown code here, such as closing a database connection or stopping a web server
    print("Tearing down the test environment")
    driver.quit()
    