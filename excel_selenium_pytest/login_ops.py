
from helper import BasePage
from locators_website import Locators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    """Page Object Model for the SauceDemo login page."""
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def login(self, username, password):
        """Perform login action with given credentials."""
        try:
            self.send_text(Locators.USERNAME_INPUT, username)
            self.send_text(Locators.PASSWORD_INPUT, password)
            self.click_element(Locators.LOGIN_BUTTON)
            try: 
                self.wait.until(EC.url_contains("inventory.html"))
                return True  # Login successful
            except:
                return False  # Login failed, likely due to error message   
            
        except Exception as e:
            print(f"An error occurred during login: {type(e).__name__}")
            return False

        
    