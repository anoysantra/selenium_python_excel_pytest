
import pytest
from login_ops import LoginPage

#file_path = "/excel_selenium_pytest/creds_test_data.xlsx"
from read_excel import get_credentials_data

creds_data = get_credentials_data()


@pytest.mark.parametrize("username,password",creds_data)
def test_login(setup, username, password):
    #setup is a fixture that initializes the WebDriver and WebDriverWait, and provides them to the test function
    driver , wait = setup
    print(f"Testing login with username: {username} and password: {password}")
    # Here you would add the actual login test code using Selenium
    login = LoginPage(driver, wait)
    result = login.login(username, password)
    assert result == True, f"Login failed for username: {username} and password: {password}"


