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

from PageObjes.profile_and_logout_page import profile
from PageObjes.login_page import Login
from PageObjes.dashboard_page import dashboard
from utilities.readProperties import ReadConfig

baseURL = ReadConfig.getApplicationURL


@pytest.mark.usefixtures("browser")
class TestLogin:
    otp = []

class TestMethod():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser

    # Enter the Harmony url in Browser search bar
    def test_Url(self):
        self.driver.get(Login.URL)
        time.sleep(3)

        # verification
        act_title = self.driver.title
        if act_title == "Dyno":
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Enter the Valid email id
    def test_validemail_id(self):
            self.driver.find_element(By.XPATH, Login.email_textfield).send_keys('manjunath.s@tibilsolutions.com')
            time.sleep(2)
            shadow = self.driver.find_element(By.CSS_SELECTOR, Login.next_button)
            shadow.click()
            time.sleep(2)
    # test case verification
            verify_tc = self.driver.find_element(By.XPATH, Login.otp_textfield)
            print("valid mail id is accepted:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
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

    #******************************************************************************************************************
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
        print("Valid OTP is accepted :", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)

    #*******************************************************************************************************************
        # Card alignment must be proper
    def test_dashboard(self):
        self.driver.find_element(By.XPATH, dashboard.cards).is_displayed()
        time.sleep(2)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.cards)
        print("cards is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)
    #*******************************************************************************************************************
    # Check whether profile button click  or not
    def test_profile_image_click_or_not(self):
        self.driver.find_element(By.XPATH, profile.click_profile_image).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.my_profile)
        print("Must be click profile Image:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Check whether profile button click or not
    def test_profile_button_click_or_not(self):
        self.driver.find_element(By.XPATH, profile.my_profile).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.edit_button)
        print("Must be open profile page:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Check whether profile button click or not
    def test_profile_edit_button_click_or_not(self):
        self.driver.find_element(By.XPATH, profile.edit_button).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.first_name_label)
        print("Must be click on edit button:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Check whether cancel button click or not
    def test_profile_cancel_button_click_or_not(self):
        self.driver.find_element(By.XPATH, profile.edit_cancel_button).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.first_name_label)
        print("It must cancel the edit related data:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    #Check whether First Name textfield is clear the text or not
    def test_check_whether_first_name_clear_text_or_not(self):
        self.driver.find_element(By.XPATH, profile.edit_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, profile.first_name_textfield).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,profile.first_name_textfield).clear()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.first_name_label)
        print("Textfield must be clear the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Check whether First Name textfield is accepting the text or not
    def test_check_whether_first_name_textfield_is_accepting_text_or_not(self):
        self.driver.find_element(By.XPATH, profile.first_name_textfield).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, profile.first_name_textfield).send_keys("manju")
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.first_name_label)
        print("Textfield mustbe accept the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    def test_check_whether_last_name_clear_text_or_not(self):

        self.driver.find_element(By.XPATH, profile.last_name_text_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,profile.last_name_text_field).clear()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.last_name_label)
        print("Textfield must be clear the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Check whether First Name textfield is accepting the text or not
    def test_check_whether_last_name_textfield_is_accepting_text_or_not(self):
        self.driver.find_element(By.XPATH, profile.last_name_text_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, profile.last_name_text_field).send_keys("tibil")
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, profile.last_name_label)
        print("Textfield mustbe accept the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # # Check whether Profile picture button click or not
    # def test_check_profile_picture_button_click_or_not(self):
    #     self.driver.find_element(By.XPATH,profile.click_profile_picture).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, profile.upload_profile_title_name)
    #     print("Must be click on profile picture:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ******************************************************************************************************************
    # # Check whethe Profile picture cancel button click or not
    # def test_check_profile_cancel_button_click_or_not(self):
    #     self.driver.find_element(By.XPATH, profile.upload_profile_cancel_button).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, profile.first_name_label)
    #     print("Must be cancel on upload  profile picture:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ******************************************************************************************************************
    # #Check whether upload image button is clicking or not
    # def test_check_uplod_image_button_click_or_not(self):
    #     self.driver.find_element(By.XPATH, profile.click_profile_picture).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH,profile.file_upload).send_keys(
    #         "/home/manjunath/Pictures/Placeholder_Person.jpg")
    #     time.sleep(5)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, profile.upload_profile_title_name)
    #     print("Image Upload sucessfully", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ******************************************************************************************************************
    # # Check whether select image is delete or not
    # def test_check_uplod_image_delete_or_not(self):
    #     self.driver.find_element(By.XPATH, profile.image_remove_button).click()
    #     time.sleep(2)
    #     verify_tc = self.driver.find_element(By.XPATH, profile.upload_profile_title_name)
    #     print("Image Upload remove sucessfully : ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ******************************************************************************************************************
    # # Check whether select image is save or not
    # def test_click_upload_profile_image_save_or_not(self):
    #     self.driver.find_element(By.XPATH, profile.file_upload).send_keys(
    #         "/home/manjunath/Pictures/Placeholder_Person.jpg")
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, profile.save_profile_image).click()
    #     time.sleep(2)
    #     #
    #     # # test case verification
    #     # verify_tc = self.driver.find_element(By.XPATH, dashboard.add_new_product_title_name)
    #     # print("Image Upload save sucessfully", verify_tc.is_displayed())
    #     # if verify_tc.is_displayed() == True:
    #     #     assert True
    #     # else:
    #     #     assert False
    # ******************************************************************************************************************
    # Check whether profile save button is  working or not
    def test_check_whether_profile_save_button_or_not(self):
        self.driver.find_element(By.XPATH, profile.profile_save_button).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, profile.left_arrow_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, profile.click_profile_image)
        time.sleep(2)

        verify_tc = self.driver.find_element(By.XPATH, profile.click_profile_image)
        print("Come back to home page :", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # Logout from the Dyno URL
    def test_check_whether_logout_from_application_or_not(self):
        self.driver.find_element(By.XPATH, profile.click_profile_image).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, profile.logout).click()
        time.sleep(2)
        verify_tc = self.driver.find_element(By.XPATH, profile.emalil_text_field)
        print(" It Must be Logout from the application:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************

