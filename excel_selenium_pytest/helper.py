from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    """Utility wrapper for common Selenium interactions."""
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def click_element(self, locator):
        """Wait for presence then click via JavaScript (bypasses overlays)."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_visible(self, locator):
        """Wait for visibility then click via JavaScript."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_text(self, locator, text):
        """Clear field and send keys."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def locate_element(self, locator):
        """Return element once present in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible_element(self, locator):
        """Return element once visible on UI."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_option(self, locator, option_text):
        """Select from a <select> dropdown by visible text."""
        dropdown_element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)