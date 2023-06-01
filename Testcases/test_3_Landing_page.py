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
        print("search bas is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # ******************************************************************************************************************
    # Click on plus icon check whether related data displaying
    def test_click_plus_icon_and_related_data_display(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.add_new_menu)
        print("It is related data is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # ******************************************************************************************************************
    # Click on folder Check whether Add new folder tab is opening
    def test_click_folder_check_and_new_folder_tab(self):
        self.driver.find_element(By.XPATH, landing.click_folder).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.folder_popup_title)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.folder_popup_title)
        print("new folder tab is opened:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # *******************************************************************************************************************
    # Check whether accepting without text folder is saveing or not
    def test_check_accepting_without_text_folder_is_save(self):
        shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
        shadow.click()
        time.sleep(5)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.invalid_credentials_msg)
        print("Invalid credentials messages is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

        self.driver.find_element(By.XPATH, landing.cancel_button).click()
        time.sleep(5)

    # *******************************************************************************************************************
    # Check whether Title textfield is accepting the text or not
    def test_check_title_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_folder).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.folder_popup_title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.title_name).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("dn10")
        time.sleep(3)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.title_name)
        print("Title textfield is accepting the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    # *******************************************************************************************************************
    def test_check_description_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.TAG_NAME, landing.description_text).click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
        print("Description textfield is accepting the text: ", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Click on the Change icon Check whether folder are displaying
    def test_click_on_change_icon_folder(self):
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
        print("Folders root is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Click on cancel button Check whether working
    def test_click_on_cancel_button_is_working(self):
        self.driver.find_element(By.XPATH, landing.cancel_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.search_bar)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
        print("Add new folder tab to be cancel:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
     #*******************************************************************************************************************
    #Click on save button Check whether working
    def test_click_on_save_button_is_working(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_folder).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.folder_popup_title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("dn10")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
        time.sleep(3)
        shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
        shadow.click()
        time.sleep(5)

         # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
        print("new folder is save:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
     #*******************************************************************************************************************
    # Click on vision Check whether Add new vision tab is opening
    def test_click_on_vision_tab_is_open(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_vision).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.vision_popup_title)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
        print("Add new vision tab opened:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
        # Check whether Title textfield is accepting the text or not
    def test_check_vision_title_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.XPATH, landing.title_name).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("master15")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
        print("Vision Title textfield is accepting the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    def test_check_vision_description_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.TAG_NAME, landing.description_text).click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
        print("Description textfield is accepting the text: ", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
        # Click on the Change icon Check whether folder are displaying
    def test_click_on_change_icon_vision_folder(self):
            self.driver.find_element(By.XPATH, landing.change_button).click()
            time.sleep(3)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
            print("vision Folders root is displayed:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    #*******************************************************************************************************************
    # Click on cancel button Check whether working
    def test_click_on_cancel_button_is_working_vision_folder(self):
        self.driver.find_element(By.XPATH, landing.cancel_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.search_bar)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
        print("Add new folder tab to be cancel for vision folder:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    def test_click_on_save_button_is_working_vision_folder(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_vision).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.folder_popup_title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("space17")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
        time.sleep(3)
        shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
        shadow.click()
        time.sleep(5)

         # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
        print("new vision folder is save:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
     #*******************************************************************************************************************
    #Click on story Check whether Add new story tab is opening or not
    def test_click_on_story_tab_is_open(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_story).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.story_popup_title)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.story_popup_title)
        print("Add new story tab opened:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Check whether Title textfield is accepting the text or not
    def test_check_story_title_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.XPATH, landing.title_name).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr15")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.vision_popup_title)
        print("Vision Title textfield is accepting the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    def test_check_story_description_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.TAG_NAME, landing.description_text).click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
        print("Description textfield is accepting the text: ", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Click on the Change icon Check whether folder are displaying
    def test_click_on_change_icon_story_folder(self):
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
        print("vision Folders root is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        # *******************************************************************************************************************
        # Click on cancel button Check whether working
    def test_click_on_cancel_button_is_working_story_folder(self):
        self.driver.find_element(By.XPATH, landing.cancel_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.search_bar)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
        print("Add new folder tab to be cancel for story folder:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        #*******************************************************************************************************************
    def test_click_on_save_button_is_working_story_folder(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_story).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.folder_popup_title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("space12")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
        time.sleep(3)
        shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
        shadow.click()
        time.sleep(5)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
        print("new story folder is save:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Click on user interface  Check whether Add new user interface tab is opening or not
    def test_click_on_user_interface_tab_is_open(self):
            self.driver.find_element(By.XPATH, landing.plus_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.add_new_menu).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.click_user_interface).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
            time.sleep(2)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
            print("Add new userinteface tab opened:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False

        # *******************************************************************************************************************
        # Check whether Title textfield is accepting the text or not
    def test_check_user_interface_title_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.XPATH, landing.title_name).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr9")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
        print("user interface Title textfield is accepting the text:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

        # *******************************************************************************************************************
    def test_check_user_interface_description_textfield_is_accepting_the_text(self):
            self.driver.find_element(By.TAG_NAME, landing.description_text).click()
            time.sleep(3)
            self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
                "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
            time.sleep(3)
            # test case verification
            verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
            print("Description textfield is accepting the text: ", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False

        # *******************************************************************************************************************
        # Click on the Change icon Check whether folder are displaying
    def test_click_on_change_icon_user_inteface_folder(self):
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
        print("User inteface Folders root is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Click on cancel button Check whether working
    def test_click_on_cancel_button_is_working_user_interface_folder(self):
        self.driver.find_element(By.XPATH, landing.cancel_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.search_bar)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
        print("Add new folder tab to be cancel for user interace folder:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    def test_click_on_save_button_is_working_User_interface_folder(self):
            self.driver.find_element(By.XPATH, landing.plus_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.add_new_menu).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.click_user_interface).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.title_name).send_keys("test12")
            time.sleep(3)
            self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
                "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
            time.sleep(3)
            self.driver.find_element(By.XPATH, landing.change_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
            time.sleep(3)
            shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
            shadow.click()
            time.sleep(5)

            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
            print("new interface folder is save:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    #*******************************************************************************************************************
    def test_click_specification_tab_is_open(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_Specification).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.specification_popup_title)
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.specification_popup_title)
        print("specification tab opened:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
        # Check whether Title textfield is accepting the text or not
    def test_check_specification_title_textfield_is_accepting_the_text(self):
            self.driver.find_element(By.XPATH, landing.title_name).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, landing.title_name).send_keys("mtr7")
            time.sleep(3)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, landing.user_interface_popup_title)
            print("specification Title textfield is accepting the text:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    #*******************************************************************************************************************
    def test_check_specification_description_textfield_is_accepting_the_text(self):
        self.driver.find_element(By.TAG_NAME, landing.description_text).click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.TAG_NAME, landing.description_text)
        print("Description textfield is accepting the text: ", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #******************************************************************************************************************
    # Click on the Change icon Check whether folder are displaying
    def test_click_on_change_icon_specification_folder(self):
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.change_button)
        print("specification Folders root is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
        # Click on cancel button Check whether working
    def test_click_on_cancel_button_is_working_specifications_folder(self):
            self.driver.find_element(By.XPATH, landing.cancel_button).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, landing.search_bar)
            time.sleep(2)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, landing.search_bar)
            print("Add new folder tab to be cancel for specifications folder:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    #*******************************************************************************************************************
    def test_click_on_save_button_is_working_specifications_folder(self):
        self.driver.find_element(By.XPATH, landing.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.add_new_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.click_Specification).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.specification_popup_title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, landing.title_name).send_keys("test11")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, landing.description_text).send_keys(
            "To be concrete, descriptive writing has to offer specifics the reader can envision. Rather than “Her eyes were the color of blue rocks” (Light blue? Dark blue? Marble? Slate?), try instead, “Her eyes sparkled like sapphires in the dark.")
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.change_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, landing.plan_radio_button).click()
        time.sleep(3)
        shadow = self.driver.find_element(By.CSS_SELECTOR, landing.save_button)
        shadow.click()
        time.sleep(5)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.plan_window)
        print("new interface folder is save:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************

