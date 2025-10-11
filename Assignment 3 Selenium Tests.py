import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSuite():
    def __init__(self, driver, weblink):
        self.driver = driver
        self.driver.get(weblink)

        self.email = "Oscar.Peer247@gmail.com" #use an actual email
        self.password = "Happy_Hacker"
        self.phone = "0449570899"

    def set_current_url(self):
        self.current_url = self.driver.current_url

    def test3(self):
        menu_options = self.driver.find_element(by = By.CLASS_NAME, value = "mz-pure-drawer")
    
    def wait(self, seconds):
        try:
            time.sleep(seconds)
        except:
            pass
    
    def save_screenshot(self, screenshot_name = "screenshot.png"):
        self.driver.save_screenshot(screenshot_name)

    def element_by_id(self, id):
        try:
            return self.driver.find_element(by = By.ID, value = id)
        except Exception as e:
            raise e

    def element_by_name(self, name):
        try:
            return self.driver.find_element(by = By.NAME, value = name)
        except Exception as e:
            raise e

    def element_by_css(self, css):
        try:
            return self.driver.find_element(by = By.CSS_SELECTOR, value = css)
        except Exception as e:
            raise e

    def element_by_class(self, class_name):
        try:
            return self.driver.find_element(by = By.CLASS_NAME, value = class_name)
        except Exception as e:
            raise e

    def test_registration(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        input_fname = self.element_by_name("firstname")
        input_fname.send_keys("John")
        input_lname = self.element_by_name("lastname")
        input_lname.send_keys("Smith")
        self.wait(2)
        input_email = self.element_by_name("email")
        input_email.send_keys(self.email)
        input_phone = self.element_by_name("telephone")
        input_phone.send_keys(self.phone)
        self.wait(1)
        input_password = self.element_by_name("password")
        input_password.send_keys(self.password)
        input_password_confirm = self.element_by_name("confirm")
        input_password_confirm.send_keys(self.password)
        self.wait(1)
        chk_agree = self.element_by_id("input-agree")
        print(chk_agree)
        driver.execute_script("arguments[0].click();", chk_agree)
        btn_submit = self.element_by_css("input.btn.btn-primary")
        btn_submit.click()
        

        successful_login_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/success"
        self.set_current_url()
        self.save_screenshot("login.png")
        assert self.current_url == successful_login_url, f"❌ URL mismatch: expected {successful_login_url}, got {self.current_url} \nThis means the login was unsuccessful"
        print("✅ URL is correct!")
        self.wait(3)

    def run_tests(self):
        self.test_registration()
        #self.test3()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    testsuite = TestSuite(driver, "https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
    testsuite.run_tests()
    driver.quit()
