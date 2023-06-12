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
from PageObjes.dashboard_page import dashboard
from PageObjes.landing_page import landing
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

    # *******************************************************************************************************************
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

    # *******************************************************************************************************************
    # enter the valid otp (From database)
    def test_valid_otp(self):
        otp = self.test_fetch_otp()
        digit = otp
        self.driver.find_element(By.XPATH, Login.otp_textfield).send_keys(digit)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR, Login.next_button)
        shadow1.click()

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, Login.otp_textfield)
        print("Valid otp is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(5)

    # *******************************************************************************************************************
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

    # *******************************************************************************************************************
    # Check whether Hamburger menu name is displayed in header (Landing page)
    def test_check_hamburgur_menu(self):
        self.driver.find_element(By.XPATH, landing.hamburger_menu_right).click()  # show Hamburger menu
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.hamburger_menu_left).click()  # Hide Hamburger menu
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.hamburger_menu_right)
        print("Hamburger menu name display on header verified:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # *******************************************************************************************************************
    # Check whether header drop down is working
    def test_check_drop_down(self):
        self.driver.find_element(By.XPATH, landing.bfsi_card).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, landing.drop_down_right).click()  # once click
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.drop_down_right).click()  # for folders view
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.drop_down_right)
        print("Dropdown related folders is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # ******************************************************************************************************************
    # Click on the search icon and check whether search bar is displaying
    def test_check_search_icon_and_search_bar(self):
        self.driver.find_element(By.XPATH, landing.search_bar)
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
        print("search bar is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # ******************************************************************************************************************
    # # Click on plus icon check whether related data displaying
    # def test_click_plus_icon_and_related_data_display(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_new_menu)
    #     print("It is related data is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False

    # ******************************************************************************************************************
    # # Click on folder Check whether Add new folder tab is opening
    # def test_click_folder_check_and_new_folder_tab(self):
    #     self.driver.find_element(By.XPATH, landing.click_folder).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     print("new folder tab is opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    # # *******************************************************************************************************************
    # # Check whether accepting without text folder is saveing or not
    # def test_check_accepting_without_text_folder_is_save(self):
    #     shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #     shadow.click()
    #     time.sleep(5)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.invalid_credentials_msg)
    #     print("Invalid credentials messages is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    #     self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #     time.sleep(5)
    #
    # # *******************************************************************************************************************
    # # Check whether Title textfield is accepting the text or not
    # def test_check_title_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_folder).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.title_name).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("dn10")
    #     time.sleep(3)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_name)
    #     print("Title textfield is accepting the text:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    # # *******************************************************************************************************************
    # def test_check_description_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
    #     print("Description textfield is accepting the text: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
    # # Click on the Change icon Check whether folder are displaying
    # def test_click_on_change_icon_folder(self):
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
    #     print("Folders root is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Click on cancel button Check whether working
    # def test_click_on_cancel_button_is_working(self):
    #     self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.search_bar)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
    #     print("Add new folder tab to be cancel:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #  #*******************************************************************************************************************
    # #Click on save button Check whether working
    # def test_click_on_save_button_is_working(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_folder).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("dn10")
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
    #     time.sleep(3)
    #     shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #     shadow.click()
    #     time.sleep(5)
    #
    #      # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
    #     print("new folder is save:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #  #*******************************************************************************************************************
    # # Click on vision Check whether Add new vision tab is opening
    # def test_click_on_vision_tab_is_open(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_vision).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.vision_popup_title)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
    #     print("Add new vision tab opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Check whether Title textfield is accepting the text or not
    # def test_check_vision_title_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.XPATH, landing.title_name).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("master15")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
    #     print("Vision Title textfield is accepting the text:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # def test_check_vision_description_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
    #     print("Description textfield is accepting the text: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Click on the Change icon Check whether folder are displaying
    # def test_click_on_change_icon_vision_folder(self):
    #         self.driver.find_element(By.XPATH, landing.change_button).click()
    #         time.sleep(3)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
    #         print("vision Folders root is displayed:", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #*******************************************************************************************************************
    # # Click on cancel button Check whether working
    # def test_click_on_cancel_button_is_working_vision_folder(self):
    #     self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.search_bar)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
    #     print("Add new folder tab to be cancel for vision folder:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # def test_click_on_save_button_is_working_vision_folder(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_vision).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("space17")
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
    #     time.sleep(3)
    #     shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #     shadow.click()
    #     time.sleep(5)
    #
    #      # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
    #     print("new vision folder is save:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #  #*******************************************************************************************************************
    # #Click on story Check whether Add new story tab is opening or not
    # def test_click_on_story_tab_is_open(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_story).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.story_popup_title)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.story_popup_title)
    #     print("Add new story tab opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Title textfield is accepting the text or not
    # def test_check_story_title_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.XPATH, landing.title_name).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr15")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
    #     print("Vision Title textfield is accepting the text:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # def test_check_story_description_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
    #     print("Description textfield is accepting the text: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Click on the Change icon Check whether folder are displaying
    # def test_click_on_change_icon_story_folder(self):
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
    #     print("vision Folders root is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #     # *******************************************************************************************************************
    #     # Click on cancel button Check whether working
    # def test_click_on_cancel_button_is_working_story_folder(self):
    #     self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.search_bar)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
    #     print("Add new folder tab to be cancel for story folder:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #     #*******************************************************************************************************************
    # def test_click_on_save_button_is_working_story_folder(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_story).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.folder_popup_title)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("space12")
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
    #     time.sleep(3)
    #     shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #     shadow.click()
    #     time.sleep(5)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
    #     print("new story folder is save:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
    #     # Click on user interface  Check whether Add new user interface tab is opening or not
    # def test_click_on_user_interface_tab_is_open(self):
    #         self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_user_interface).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
    #         time.sleep(2)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
    #         print("Add new userinteface tab opened:", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    #     # *******************************************************************************************************************
    #     # Check whether Title textfield is accepting the text or not
    # def test_check_user_interface_title_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.XPATH, landing.title_name).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr9")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
    #     print("user interface Title textfield is accepting the text:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    #     # *******************************************************************************************************************
    # def test_check_user_interface_description_textfield_is_accepting_the_text(self):
    #         self.driver.find_element(By.TAG_NAME, landing.description_text).click()
    #         time.sleep(3)
    #         self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #             "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #         time.sleep(3)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
    #         print("Description textfield is accepting the text: ", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    #     # *******************************************************************************************************************
    #     # Click on the Change icon Check whether folder are displaying
    # def test_click_on_change_icon_user_inteface_folder(self):
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
    #     print("User inteface Folders root is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
    # # Click on cancel button Check whether working
    # def test_click_on_cancel_button_is_working_user_interface_folder(self):
    #     self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.search_bar)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
    #     print("Add new folder tab to be cancel for user interace folder:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # def test_click_on_save_button_is_working_User_interface_folder(self):
    #         self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_user_interface).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.title_name).send_keys("test12")
    #         time.sleep(3)
    #         self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #             "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #         time.sleep(3)
    #         self.driver.find_element(By.XPATH, landing.change_button).click()
    #         time.sleep(3)
    #         self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
    #         time.sleep(3)
    #         shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #         shadow.click()
    #         time.sleep(5)
    #
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
    #         print("new interface folder is save:", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #*******************************************************************************************************************
    # def test_click_specification_tab_is_open(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_Specification).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.specification_popup_title)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.specification_popup_title)
    #     print("specification tab opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Check whether Title textfield is accepting the text or not
    # def test_check_specification_title_textfield_is_accepting_the_text(self):
    #         self.driver.find_element(By.XPATH, landing.title_name).click()
    #         time.sleep(3)
    #         self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr7")
    #         time.sleep(3)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
    #         print("specification Title textfield is accepting the text:", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #*******************************************************************************************************************
    # def test_check_specification_description_textfield_is_accepting_the_text(self):
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
    #     print("Description textfield is accepting the text: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #******************************************************************************************************************
    # # Click on the Change icon Check whether folder are displaying
    # def test_click_on_change_icon_specification_folder(self):
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
    #     print("specification Folders root is displayed:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Click on cancel button Check whether working
    # def test_click_on_cancel_button_is_working_specifications_folder(self):
    #         self.driver.find_element(By.XPATH, landing.cancel_button).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.search_bar)
    #         time.sleep(2)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
    #         print("Add new folder tab to be cancel for specifications folder:", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #*******************************************************************************************************************
    # def test_click_on_save_button_is_working_specifications_folder(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_Specification).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.specification_popup_title)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.title_name).send_keys("test11")
    #     time.sleep(3)
    #     self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
    #         "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.change_button).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
    #     time.sleep(3)
    #     shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
    #     shadow.click()
    #     time.sleep(5)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
    #     print("new interface folder is save:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
    # Click on Part  Check whether Add a Part tab is open
    # def test_click_part_tab_is_open(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_a_part_popup_title)
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_a_part_popup_title)
    #     print("part tab opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # #Check whether Add a new Part tab is opening
    # def test_add_a_new_part_tab_is_open(self):
    #     self.driver.find_element(By.XPATH, landing.button_add_a_new_part).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_add_a_new_part)
    #     print("Add new part tab to be opened:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # #Check whether Part Name textfield is accepting the text or not
    # def test_add_part_name_textfield_accepting_text(self):
    #     self.driver.find_element(By.XPATH, landing.part_name_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.part_name_text_field).send_keys("SKILL-UP")
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.part_name_text_field)
    #     print("Textfield must be accept the text in part name:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Part about textfield is accepting the text or not
    # def test_add_part_about_textfield_accepting_text(self):
    #     self.driver.find_element(By.XPATH, landing.part_about_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.part_about_text_field).send_keys("SkillUp Online is a future-focused learning platform with a single. goal; to close the tech skills gap and enable professionals and. organizations "
    #                                                                                 "to thrive using emerging technologies. We're achieving this by providing today's learners with the. job-aligned future skills and practical experience employers need to.")
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.part_about_text_field)
    #     print("Textfield must be accept the text in part about:", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Part service type dropdown is click or not
    # def test_service_dropdown_click_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.service_type_button).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.front_end_dropdown)
    #     print("Service type Dropdown is show", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    # #*******************************************************************************************************************
    # # Check whether Part service type dropdown option accept or not
    # def test_service_dropdown_option_accept_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.front_end_dropdown).click()  # check frontend drop down
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.service_type_button).click()  # click again service drop down button
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.back_end_drop_down).click()  # click back end drop down button
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.service_type_button).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.front_end_dropdown).click()  # check frontend drop down
    #     time.sleep(3)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.service_type_button)
    #     print("Service type Dropdown is accept the option", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Reuseable Part type dropdown is click or not
    # def test_reuseable_part_type_dropdown_click_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.reuseable_part_select_type).click()  # check reuseable part select type drop down
    #     time.sleep(3)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.reuseable_yes_option)
    #     print("Select Part type Dropdown is click", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #
    # #*******************************************************************************************************************
    # # Check whether yes Reuseable option type dropdown options is select or not
    # def test_reuseable_part_type_dropdown_options_select_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.reuseable_yes_option).click() # select YES reuseable option
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH,landing.reuseable_part_select_type).click()  # check reuseable part select type drop down
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.reuseable_no_option).click()  # select NO reuseable option
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH,landing.reuseable_part_select_type).click()  # check reuseable part select type drop down
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.reuseable_yes_option).click()  # select YES reuseable option
    #     time.sleep(3)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.reuseable_yes_option)
    #     print("dropdown options is must be selected ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # #Check whether Part Repo URL textfield is accepting the text or not
    # def test_part_repo_url_textfield_accept_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.part_repo_url_textfield).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH,landing.part_repo_url_textfield).send_keys("https://github.com/Manjuurs1234/BFSIWebTestingAutomation")
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.part_repo_url_textfield)
    #     print("Textfield accept the Repo URL", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # *******************************************************************************************************************
    # Check whether Programming Language plus icon is click or not
    # def test_program_language_plus_icon_working_or_not(self):
    #     self.driver.find_element(By.XPATH,landing.pgm_plus_icon).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_language_tab)
    #     print("Add Language tab open", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Add language Tab Cancel button is working or not
    # def test_program_language_cancel_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH,landing.language_cancel_button).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_add_a_new_part)
    #     print("Add Language tab is show", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether add language Tech Name textfield is accepting the text or not
    # def test_add_language_tech_name_accepting_text_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.pgm_plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_language_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_language_text_field).send_keys("C Programming")
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_language_text_field)
    #     print("Name Textfield be accept the text", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Check whether add language SVG URL textfield is accepting the text or not
    #     self.driver.find_element(By.XPATH, landing.add_svg_url_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_svg_url_text_field).send_keys("https://commons.wikimedia.org/wiki/File:C_Programming_Language.svg")
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_svg_url_text_field)
    #     print("SVG Textfield accept the text", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Add language Tab Cancel button is working or not
    # def test_program_language_cancel_button_inside_working_or_not(self):
    #     self.driver.find_element(By.XPATH,landing.language_cancel_button).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_add_a_new_part)
    #     print("Add new part tab must be open", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Add language Tab Add button is working or not
    # def test_program_language_add_button_inside_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.pgm_plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_language_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_language_text_field).send_keys("C Programming")
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_svg_url_text_field).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_svg_url_text_field).send_keys("https://commons.wikimedia.org/wiki/File:C_Programming_Language.svg")
    #     time.sleep(2)
    #
    #     self.driver.find_element(By.XPATH,landing.add_language_add_button).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_add_a_new_part)
    #     print("Add new part tab must be open", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #*******************************************************************************************************************
    #  Check whether select language dropdown is working or not
    # def test_select_language_dropdown_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.select_language_dropdown).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.select_language_options)
    #     print("Select Language Dropdown is Click", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #        assert False
    # #*******************************************************************************************************************
    #     #  Check whether select language dropdown is working or not
    # def test_select_language_cancel_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.select_language_cancel_button).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.title_add_a_new_part)
    #     print("Select Language Dropdown is Click", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Select language Check box is Check or not
    # def test_select_language_check_box_select_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.select_language_dropdown).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language1).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language2).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language3).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language4).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language5).click()
    #     time.sleep(1)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.select_language_options)
    #     print("Check box is select", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    # # Check whether Select language Check box is un Check or not
    # def test_select_language_check_box_un_select_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language1).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language2).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language3).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language4).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language5).click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, landing.select_language_checkbox_language5).click() # again click the check box to select language
    #     time.sleep(1)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.select_language_options)
    #     print("dropdown options is must be selected ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #*******************************************************************************************************************
    #     # Check whether Select language OK button is working or not
    # def test_select_language_ok_button_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.select_language_ok_button).click()
    #         time.sleep(2)
    #         # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.select_language_dropdown)
    #         print("dropdown options is must be selected ", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #*******************************************************************************************************************
    # # Click on Add a Existing Part  Check whether Add Assosiated Part tab is opening
    # def test_Add_Assosiated_Part_Must_be_open(self):
    #         self.driver.find_element(By.XPATH, landing.add_button).click()
    #         time.sleep(2)
            # test case verification
    #         verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
    #         print(" Add Assosiated Part Must be open", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # # ****************************************************************************************************************
    # # Click on Add a Existing Part  Check whether Add Assosiated Part tab is opening
    # def test_Add_Assosiated_Part_Must_be_open(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_add_existing_part).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_associated_part_title)
    #     print("  Add Assosiated Part Must be open", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # #  Check whether in Add Assosiated Part tab Select part is click or not
    # def test_Add_Assosiated_Part_tab_select_part_click(self):
    #     self.driver.find_element(By.XPATH, landing.project_select_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.project_select_emas_card).click()
    #     time.sleep(2)
    #
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.add_associated_part_title)
    #     print("Add Assosiated Part view", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #****************************************************************************************************************
    # #  Check whether in Add Assosiated Part tab Select part cancel button is working or not
    # def test_Add_Assosiated_Part_tab_select_part_cancel_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.part_cancel_button).click()
    #     time.sleep(2)
    #     # test case verification
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
    #     print("Select Part is cancel", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Check whether in Add Assosiated Part tab Select part add button is working or not
    # def test_Add_Assosiated_Part_tab_select_part_add_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.plus_icon).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.add_new_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_add_existing_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.project_select_part).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.project_select_emas_card).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.part_add_button).click()
    #     time.sleep(5)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
    #     print("Select Part is added", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #****************************************************************************************************************
    # Click on Kebab menu Check whether it is working or not
    def test_click_on_kebab_menu_working_or_not(self):
        self.driver.find_element(By.XPATH, landing.click_testing_folder).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH, landing.dots_menu).click()
        # time.sleep(2)
        # verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu_options)
        # print("It must be display Documents,People,Tags,Linked item and Folder", verify_tc.is_displayed())
        # if verify_tc.is_displayed() == True:
        #     assert True
        # else:
        #     assert False
    # # ****************************************************************************************************************
    # # Click on Documents Check whether documents are displaying or not
    # def test_check_documents_displaying_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.click_documents).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.documents_name_title)
    #     print("Documents must be display", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Click on Cancel Check whether close button working or not
    # def test_check_close_button_working_or_not(self):
    #     self.driver.find_element(By.CSS_SELECTOR, landing.close_option).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu)
    #     print("Documents must be display", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #****************************************************************************************************************
    # # Click on pin in Check whether it is working or not
    # def test_check_on_pin_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_documents).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_pin).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.documents_name_title)
    #     print("Documents tab must be comes at left of the screen", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #****************************************************************************************************************
    # # Click on People Check whether people releated data are displaying or not
    # def test_check_people_displaying_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_people).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.people_name_title)
    #     print("People related data must be display", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    #     # Click on Cancel Check whether close button working or not
    # def test_check_people_close_button_working_or_not(self):
    #         self.driver.find_element(By.CSS_SELECTOR, landing.close_option).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu)
    #         print("Documents must be display", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #****************************************************************************************************************
    # # Click on pin in Check whether it is working or not
    # def test_check_on_people_tab_pin_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_people).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_pin).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.documents_name_title)
    #     print("people tab must be comes at left of the screen", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    #     # Click on Tags Check whether Tags are displaying or not
    # def test_check_Tags_displaying_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_tags).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.tags_name_title)
    #     print("Tags releated  must be display : ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # #****************************************************************************************************************
    # # Click on Cancel Check whether close button working or not
    # def test_check_Tags_close_button_working_or_not(self):
    #     self.driver.find_element(By.CSS_SELECTOR, landing.close_option).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu)
    #     print("Tags tab must be cancel.: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    #     # Click on pin in Check whether it is working or not
    # def test_check_on_tags_tab_pin_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_tags).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_pin).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.tags_name_title)
    #         print("Tags tab must be comes at left of the screen", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # #****************************************************************************************************************
    # # Click on linked item Check whether Linked Itams are displaying or not
    # def test_check_Linked_item_displayed_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_linked_items).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.linked_items_tag_names)
    #     print("Linked item releated  must be display : ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #     # ****************************************************************************************************************
    #     # Click on Cancel Check whether close button working or not
    # def test_check_linked_item_close_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.linked_items_close).click()
    #     time.sleep(2)
    #     verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu)
    #     print("Linked Items tab must be cancel.: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    #     # Click on pin in Check whether it is working or not
    # def test_check_on_Linked_Item_pin_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_linked_items).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_pin).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.linked_items_tag_names)
    #     print("Linked Item tab must be comes at left of the screen", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Click on Check whether folder are displaying or not
    # def test_folder_displayed_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_folder_part).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.linked_items_close).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.linked_items_tag_names)
    #         print("Folder releated  must be display : ", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # # ****************************************************************************************************************
    # Click on Kebab menu Check whether it is  working or not
    # def test_kubeb_menu_working_or_not(self):
        self.driver.find_element(By.XPATH, landing.edit_pancel_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.dots_menu).click()
        time.sleep(2)
    #     verify_tc = self.driver.find_element(By.XPATH, landing.dots_menu_options)
    #     print("Upload Documents,Add People,Add Tag,Link items, Change Folder must be display: ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Click on Upload Documents Check whether upload documents tab are displaying or not
    # def test_upload_documents_tab_displaying_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.click_documents).click()
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.documents_name_title)
    #     print("Upload Documents tab must be display: ",verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Check whether Title textfield is accepting the text or not
    # def test_upload_documents_title_text_field_accepting_the_text_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.upload_doc_text).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.upload_doc_text).send_keys("demo_test")
    #     time.sleep(2)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.upload_doc_text)
    #     print("Upload Textfield must be accept the text ", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # ****************************************************************************************************************
    # # Click on Upload Check whether it is working or not
    # def test_click_upload_working_or_not(self):
    #     self.driver.find_element(By.XPATH, landing.file_path).send_keys(
    #         "/home/manjunath/Pictures/Placeholder_Person.jpg")
    #     time.sleep(5)
    # #*******************************************************************************************************************
    # # Click on uploaded Doucuments drop down Check whether it is working or not.
    # def test_upload_documents_dropdown_working_or_not(self):
    #     self.driver.find_element(By.CSS_SELECTOR, landing.upload_doc_caret_dropdown).click() # to view the upload docs
    #     time.sleep(3)
    #
    #     verify_tc = self.driver.find_element(By.XPATH, landing.upload_doc_title)
    #     print("Uploaded documents must be display", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    #     self.driver.find_element(By.CSS_SELECTOR, landing.upload_doc_caret_up_dropdown).click()  # to hide the upload docs
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, landing.file_path).send_keys(
    #         "/home/manjunath/Documents/Selenium links")
    #     time.sleep(5)
    #
    # # *******************************************************************************************************************
    # def test_upload_documents_cancel_button_working_or_not(self):
    #     self.driver.find_element(By.XPATH,landing.upload_doc_cancel_button).click()
    #     time.sleep(3)
    #     verify_tc = self.driver.find_element(By.XPATH,landing.plus_icon)
    #     print("Edit icon must be display.", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
    # def test_upload_documents_save_button_working_or_not(self):
    #
    #     self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.click_documents).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.upload_doc_text).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.upload_doc_text).send_keys("demo_test")
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, landing.file_path).send_keys(
    #         "/home/manjunath/Pictures/Placeholder_Person.jpg")
    #     time.sleep(5)
    #     self.driver.find_element(By.CSS_SELECTOR, landing.upload_doc_caret_dropdown).click()  # to view the upload docs
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, landing.upload_doc_caret_dropdown).click()  # to view the upload docs
    #     time.sleep(3)
    #
    #     self.driver.find_element(By.XPATH,landing.upload_doc_save_button).click()
    #     time.sleep(3)
    #     verify_tc = self.driver.find_element(By.XPATH,landing.plus_icon)
    #     print("Uploaded documents must be save.", verify_tc.is_displayed())
    #     if verify_tc.is_displayed() == True:
    #         assert True
    #     else:
    #         assert False
    # # *******************************************************************************************************************
#     # Click on Add people Check whether Add people tab are displaying or not
#     def test_click_add_people_whether_add_people_tab_displaying_or_not(self):
#         self.driver.find_element(By.XPATH, landing.click_add_prople_tab).click()
#         time.sleep(2)
#         verify_tc = self.driver.find_element(By.XPATH, landing.add_people_title)
#         print("Add People tab must be display.", verify_tc.is_displayed())
#         if verify_tc.is_displayed() == True:
#             assert True
#         else:
#             assert False
#     #*******************************************************************************************************************
#     # Check whether Add people drop down is working or not
#     def test_click_add_people_whether_add_people_dropdown_working_or_not(self):
#         self.driver.find_element(By.XPATH, landing.add_people_drop_down).click()
#         time.sleep(2)
#         verify_tc = self.driver.find_element(By.XPATH, landing.click_add_prople_check_box)
#         print("People names check box must be display.", verify_tc.is_displayed())
#         if verify_tc.is_displayed() == True:
#             assert True
#         else:
#             assert False
#     # *******************************************************************************************************************
#     # Check whether Add people drop down select the check box is working or not
#     def test_click_add_people_whether_add_people_select_the_check_box_working_or_not(self):
#         self.driver.find_element(By.XPATH, landing.click_add_prople_check_box).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH,landing.add_people_select_name_click).click()
#         time.sleep(2)
#
#         verify_tc = self.driver.find_element(By.XPATH, landing.add_people_title)
#         print("Add people drop down is names  must be display", verify_tc.is_displayed())
#         if verify_tc.is_displayed() == True:
#             assert True
#         else:
#             assert False
#     # *******************************************************************************************************************
#         # Check whether Add people cancel button is working or not
#     def test_click_add_people_whether_add_people_cancel_button_working_or_not(self):
#             self.driver.find_element(By.XPATH, landing.add_people_cancel_button).click()
#             time.sleep(2)
#
#             verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
#             print("Add people drop down is names Must be cancel ", verify_tc.is_displayed())
#             if verify_tc.is_displayed() == True:
#                 assert True
#             else:
#                 assert False
# # *******************************************************************************************************************
#     #Check whether Add people Save button is working or not
#     def test_click_add_people_whether_add_people_save_button_working_or_not(self):
#         self.driver.find_element(By.XPATH, landing.dots_menu).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, landing.click_add_prople_tab).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, landing.add_people_drop_down).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, landing.click_add_prople_check_box).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, landing.add_people_select_name_click).click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, landing.add_people_Save_button).click()
#         time.sleep(2)
#
#         verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
#         print("Add people drop down is names Must be save ", verify_tc.is_displayed())
#         if verify_tc.is_displayed() == True:
#             assert True
#         else:
#             assert False
#     # *******************************************************************************************************************
        # Click on Add people Check whether Add tag tab are displaying or not
    # def test_click_add_people_whether_add_tag_tab_displaying_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.click_add_prople_tags).click()
    #         time.sleep(2)
    #         verify_tc = self.driver.find_element(By.XPATH, landing.add_people_tags_title)
    #         print("Add tag tab must be display.", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    #     # *******************************************************************************************************************
    #     # Check whether Add tags drop down is working or not
    # def test_click_add_people_whether_add_tag_dropdown_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.add_people_drop_down).click()
    #         time.sleep(2)
    #         verify_tc = self.driver.find_element(By.XPATH, landing.click_add_prople_check_box)
    #         print("People tagsnames check box must be display.", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    #     # *******************************************************************************************************************
    #     # Check whether Add tags drop down select the check box is working or not
    # def test_click_add_people_whether_add_tags_select_the_check_box_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.click_add_prople_check_box).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH,landing.add_people_tags_title).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.add_people_tags_title)
    #         print("Add people drop down is names  must be display", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    # #     # *******************************************************************************************************************
    #     # Check whether Add tags cancel button is working or not
    # def test_click_add_people_whether_add_tags_cancel_button_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.add_people_cancel_button).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
    #         print("Add people drop down is names Must be cancel ", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    #
    # #     # *******************************************************************************************************************
    # #     # Check whether Add people Save button is working or not
    # def test_click_add_people_whether_add_tags_save_button_working_or_not(self):
    #         self.driver.find_element(By.XPATH, landing.dots_menu).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_add_prople_tags).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.add_people_drop_down).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.click_add_prople_check_box).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.add_people_tags_title).click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, landing.add_people_Save_button).click()
    #         time.sleep(2)
    #
    #         verify_tc = self.driver.find_element(By.XPATH, landing.plus_icon)
    #         print("Add tags drop down is names Must be save ", verify_tc.is_displayed())
    #         if verify_tc.is_displayed() == True:
    #             assert True
    #         else:
    #             assert False
    # *******************************************************************************************************************
    # Click on Linked Items Check whether Add Link item  are displaying or not
    def test_click_add_people_whether_linked_items_displaying_or_not(self):
        self.driver.find_element(By.XPATH, landing.dots_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_linked_items_tab).click()
        time.sleep(2)
        verify_tc = self.driver.find_element(By.XPATH, landing.click_linked_items_tab)
        print("Linked Items tab must be display", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
