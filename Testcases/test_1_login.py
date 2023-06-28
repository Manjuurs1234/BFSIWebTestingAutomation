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
from PageObjes.login_page import Login
from utilities.readProperties import ReadConfig

baseURL = ReadConfig.getApplicationURL


@pytest.mark.usefixtures("browser")
class TestLogin:
    otp = []

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser


    # Enter the Harmony url in Browser search bar
    def test_Url(self):
        self.driver.get(Login.URL)
        time.sleep(3)

    # test case verification
        act_title = self.driver.title
        if act_title == "Dyno":
            assert True
        else:
            assert False

    #*******************************************************************************************************************
    # Check whether Dyno icon and Title and subtitle is displaying or not

    def test_icon(self):
        lp = Login(self.driver)
        act_title = lp.get_subtitle()
        time.sleep(2)

    # test case verification
        if act_title == "Sales Enabler & Solution Accelerator":
            assert True
        else:
            assert False

    #*******************************************************************************************************************
       # Dyno icon and Title and subtitle must be displayed at center

    def test_title_subtitle_center(self):
        lp = Login(self.driver)
        act_title = lp.get_subtitle_center()
        time.sleep(2)

    # test case verification
        if act_title == "Sales Enabler & Solution Accelerator":
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Dyno icon and Title and subtitle not displayed at center
    def test_title_subtitle_not_center(self):
        self.driver.find_element(By.XPATH, Login.sub_title_not_center)
        time.sleep(2)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.sub_title)
        print("Dyno icon is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    #*******************************************************************************************************************
        # Enter the special characters
    def test_invalid_characters(self):
            self.driver.find_element(By.XPATH, Login.email_textfield).send_keys('ertfyt')
            time.sleep(2)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, Login.email_textfield)
            print("The next button should be hidden and Invalid credentials message must be displayed:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
            self.driver.find_element(By.XPATH, Login.email_textfield).clear()

    # #*******************************************************************************************************************
    # Enter the special characters
    def test_special_characters(self):
        self.driver.find_element(By.XPATH, Login.email_textfield).send_keys('[];?_!')
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.email_textfield)
        print("Login is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        self.driver.find_element(By.XPATH,Login.email_textfield).clear()
   #  #*******************************************************************************************************************
        # Enter the invalid email id
    def test_invalid_email_id(self):
            self.driver.find_element(By.XPATH, Login.email_textfield).send_keys('narayan.sk@tibilsolutions.com')
            time.sleep(2)
            shadow = self.driver.find_element(By.CSS_SELECTOR, Login.next_button)
            shadow.click()
            time.sleep(12)

    # test case verification
            verify_tc = self.driver.find_element(By.XPATH, Login.invalid_credentias)
            print("invalid email is displayed:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
            self.driver.find_element(By.XPATH, Login.email_textfield).clear()
    #*******************************************************************************************************************
    # Enter the Valid email id
    def test_validemail_id(self):
        self.driver.find_element(By.XPATH, Login.email_textfield).send_keys('manjunath.s@tibilsolutions.com')
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR, Login.next_button)
        shadow.click()

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.otp_textfield)
        print("Valid email is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)

    # *******************************************************************************************************************
       # enter the otp - Empty text box
    def test_empty_textbox(self):
        self.driver.find_element(By.XPATH, Login.otp_textfield)
        time.sleep(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR, Login.next_button)
        shadow.click()

    # test case verification
        txt3 = self.driver.find_element(By.CSS_SELECTOR, Login.error_message).text
        if txt3 == "Please enter otp":
            assert True
        else:
            assert False

        time.sleep(2)
    #*******************************************************************************************************************
    # enter wrong otp
    def test_wrong_otp(self):
        self.driver.find_element(By.XPATH, Login.otp_textfield).send_keys('123456')
        self.driver.implicitly_wait(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR,Login.next_button)
        shadow.click()
        time.sleep(13)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH,Login.otp_textfield)
        print("Wrong is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

        self.driver.find_element(By.XPATH,Login.otp_textfield).clear()
        time.sleep(2)
    #*******************************************************************************************************************
    def test_fetch_otp(self):

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
            return self.otp

    #*******************************************************************************************************************
        # enter the valid otp (From database)
    def test_valid_otp(self):
        otp = self.test_fetch_otp()
        digit = otp
        self.driver.find_element(By.XPATH, Login.otp_textfield).send_keys(digit)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR,Login.next_button)
        shadow1.click()

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.otp_textfield)
        print("Valid otp is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)
    #*******************************************************************************************************************
        # Login page mustbe navigate to dashboard page
    def test_login(self):
        self.driver.find_element(By.XPATH, Login.profile_img)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.profile_img)
        print("Dashboard is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)

    #*******************************************************************************************************************
    # logout from the dashboard
    def test_logout_from_dahboard(self):
        self.driver.find_element(By.CSS_SELECTOR, Login.img).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Login.logout).click()

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.profile_img)
        print("Login is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)
   #********************************************************************************************************************
    # Sign in using google
    def test_signin_google(self):
        self.driver.find_element(By.XPATH,Login.click_google_signin_button).click()  # Signin
        time.sleep(2)
        # email
        self.driver.find_element(By.XPATH, Login.google_email_textfield).send_keys("manjunath.s@tibilsolutions.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, Login.google_email_next_button).click()
        time.sleep(2)
        # password
        self.driver.find_element(By.XPATH, Login.google_password_textfield).send_keys("tibilsolutions")
        time.sleep(2)
        self.driver.find_element(By.XPATH, Login.google_pwd_next_button).click()
        time.sleep(2)
        # verify profile img avatar in dashboard
        self.driver.find_element(By.CSS_SELECTOR, Login.img)
        time.sleep(4)
        self.driver.find_element(By.XPATH, Login.profile_img).is_displayed()
        time.sleep(3)

    # test case verification
        verify_tc= self.driver.find_element(By.XPATH, Login.profile_img)
        print("Profile image is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

        self.driver.close()
    #*******************************************************************************************************************