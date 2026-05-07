from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators:
    """Centralized locators for the SauceDemo website."""
    # Login Page
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")