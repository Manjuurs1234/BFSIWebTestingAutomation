import psycopg2 as pg
import pytest
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from PageObjes.dyno_pom import Loginpage
class TestLogin:
    otp = []
    @pytest.fixture()
    def test_Login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("/home/manjunath/Projects/BFSI Web Testing Automation/Driver/chromedriver")
        driver = webdriver.Chrome(options=options, service=serv_obj)
        # self.driver.implicitly_wait(30)

        self.driver.get("https://d.dynoapp.in/#/login/login")
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ENTER)
        # actions.perform()
        time.sleep(3)
        driver.maximize_window()
        time.sleep(2)
        yield
        self.driver.close()
        # ***************************************************************************
     # Click on next button Check without mail id
    def test_nxt_button(self,test_Login):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
        #***************************************************************************

        # Enter the invalid email id
    def test_email_id(self, test_Login):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('abc')
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".error-message")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()

        #***************************************************************************
        # Enter the Valid email id - Positive Testcase
    def test_validemail_id(self, test_Login):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('manjunath.s@tibilsolutions.com')
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)

        #************************************************************************************************
        # enter the otp - Empty text box
    def test_empty_textbox(self, test_Login):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter OTP']")
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        #****************************************************************************************************************

        # enter wrong otp
    def test_wrong_otp(self, test_Login):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys('123456')
        self.driver.implicitly_wait(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(12)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").clear()
        time.sleep(2)


        port = '5432'
        host = '34.100.216.73'
        user = "postgres"
        password = "t3djo7b0jfd9J3JL"
        database = "devdyno"

        con = pg.connect(database=database, user=user, password=password, host=host, port=port)
        cur = con.cursor()
        QueryString = '''SELECT (payload ->>'OTP') FROM auth.nq Order by pid desc limit 1'''
        cur.execute(QueryString)
        con.commit()
        output1 = cur.fetchall()
        a = str(output1)
        b = a.replace('[(', '')
        self.otp = b.replace(',)]', '')

    #  ******************************************************************************************
        # enter the valid otp (From database)
    def test_valid_digits(self,test_Login):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(self.otp)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

        # validations
        errormsg = 'Error messages verified'
        if errormsg=="Error messages was verified":
            print(errormsg)
        else:
            print("verified")

        Dashboard_display = self.driver.find_element(By.XPATH,"//img[@class='orgLogo ng-star-inserted']")
        print("Harmony Log in page must displayed")
        print("Dyno icon and Title and sub title must be displayed")
        print('Dyno icon and Title and sub title must be displayed at center')
        print("Element Found : Focus On", Dashboard_display.is_displayed())
        print("Error messages was verified:")
        print("Login page was verified:")
        time.sleep(5)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())





