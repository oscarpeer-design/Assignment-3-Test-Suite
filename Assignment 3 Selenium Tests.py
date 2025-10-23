import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class TestSuite():
    def __init__(self, driver, weblink):
        self.driver = driver
        self.driver.get(weblink)

        self.email = "peeroscar.personal@gmail.com" #use an actual email
        self.password = "Happy_Hacker"
        self.phone = "0449570899"

    def set_current_url(self):
        self.current_url = self.driver.current_url

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
        self.driver.execute_script("arguments[0].click();", chk_agree)
        btn_submit = self.element_by_css("input.btn.btn-primary")
        btn_submit.click()
        
        successful_registration_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/success"
        self.set_current_url()
        self.save_screenshot("login.png")
        assert self.current_url == successful_registration_url, f"❌ URL mismatch: expected {successful_registration_url}, got {self.current_url} \nThis means the login was unsuccessful"
        print("✅ URL is correct!")
        self.wait(3)

    def test_login_valid(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        input_email = self.element_by_name("email")
        input_email.send_keys(self.email)
        input_password = self.element_by_id("input-password")
        input_password.send_keys(self.password)
        self.wait(2)
        btn_login = self.element_by_css("input[value='Login']")
        self.driver.execute_script("arguments[0].click();", btn_login)
        self.wait(3)
        successful_login_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/account"
        self.set_current_url()
        assert self.current_url == successful_login_url, f"❌ URL mismatch: expected {successful_login_url}, got {self.current_url} \nThis means the login was unsuccessful"
        print("✅ Login was successful!")

    def test_login_invalid_email(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        input_email = self.element_by_name("email")
        input_email.send_keys("John.Smith@gmail.com.au")
        input_password = self.element_by_id("input-password")
        input_password.send_keys(self.password)
        self.wait(2)
        btn_login = self.element_by_css("input[value='Login']")
        self.driver.execute_script("arguments[0].click();", btn_login)
        self.wait(3)
        successful_login_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/account"
        self.set_current_url()
        assert self.current_url != successful_login_url, f"❌ URL mismatch: expected {successful_login_url}, got {self.current_url} \nThis means the login was unsuccessful"
        print("✅ Login was unsuccessful. The user shouldn't log in with an incorrect email address")

    def test_login_invalid_password(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        input_email = self.element_by_name("email")
        input_email.send_keys(self.email)
        input_password = self.element_by_id("input-password")
        input_password.send_keys("Unhappy_Hacker")
        self.wait(2)
        btn_login = self.element_by_css("input[value='Login']")
        self.driver.execute_script("arguments[0].click();", btn_login)
        self.wait(3)
        successful_login_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/account"
        self.set_current_url()
        assert self.current_url != successful_login_url, f"❌ URL mismatch: expected {successful_login_url}, got {self.current_url} \nThis means the login was unsuccessful"
        print("✅ Login was unsuccessful. The user shouldn't log in with an incorrect password")

    def click(self, wait, locators):
        for by in locators:
            try:
                el = wait.until(EC.element_to_be_clickable(by))
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                el.click(); return
            except:
                raise RuntimeError("cannot click any locator")

    def test_blog_review(self):
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1280,900")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")

        try:
            wait = WebDriverWait(self.driver, 15)
            self.click(wait, [
                (By.LINK_TEXT, "Blog"),
                (By.PARTIAL_LINK_TEXT, "Blog"),
                (By.CSS_SELECTOR, "a[title='Blog']"),
                (By.CSS_SELECTOR, "a[href*='blog']"),
            ])

            wait.until(EC.presence_of_element_located((
                By.XPATH, "//*[contains(translate(.,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LATEST ARTICLES')]"
            )))
            cards = driver.find_elements(By.CSS_SELECTOR, "a[href*='article_id']")
            assert len(cards) >= 1

            el = cards[0]
            driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
            el.click()
        
            wait.until(EC.url_contains("article_id"))
            assert ("article" in driver.current_url) or ("article_id" in driver.current_url)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1 | //h2[contains(@class,'title') or contains(@class,'heading')]")))
        finally:
            self.wait(3)
            self.set_current_url()
            #check the correct title of the web page exists
            try:
                title = self.driver.find_element(By.XPATH, "//h1[text()='amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus']")
                print("✅ Blog review was successful")
            except:
                raise Exception("❌ The wrong title was displayed, meaning the blog review failed to navigate to the correct page")

    def run_tests(self):
        #self.test_registration()
        #self.test_login_invalid_email()
        #self.test_login_invalid_password()
        self.test_login_valid()
        self.test_blog_review()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    testsuite = TestSuite(driver, "https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
    testsuite.run_tests()
    driver.quit()
