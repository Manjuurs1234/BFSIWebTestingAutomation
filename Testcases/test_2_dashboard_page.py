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

from PageObjes.landing_page import landing
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
        # Search bar must display
    def test_search_common_text(self):
            self.driver.find_element(By.XPATH, dashboard.search_bar).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, dashboard.search_bar).send_keys('TIBIL')  # search name

            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, dashboard.search_bar)
            print("Empty window is displayed:", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
            time.sleep(2)

            self.driver.find_element(By.XPATH, dashboard.search_bar).clear()
    #*******************************************************************************************************************
        # Search bar must display
    def test_search_bar_card_name(self):
        self.driver.find_element(By.XPATH, dashboard.search_bar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.search_bar).send_keys('BFSI')  # search name

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.search_bar)
        print("Project card name displayed :", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)
    #*******************************************************************************************************************
    #     # click on kebab menu
    def test_kebab_menu(self):
        self.driver.find_element(By.XPATH, dashboard.click_kebab_menu).click()

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_kebab_menu)
        print("Kebab menu is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)
    #*******************************************************************************************************************
    # navigate the dashboard page
    def test_navigate_dashboard_page(self):
        # open application
        self.driver.find_element(By.XPATH, dashboard.open_applications).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.click_back_button_browser).click()
        time.sleep(3)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_kebab_menu)
        print("Application Tab name is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Click on read more
    def test_click_read_more(self):
        self.driver.find_element(By.XPATH,dashboard.click_read_more).click()
        time.sleep(2)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_read_more)
        print("Data releated project is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    #*******************************************************************************************************************
    # click read less
    def test_click_read_less(self):
        self.driver.find_element(By.XPATH,dashboard.click_read_less).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_read_more)
        print("Project card go to original state displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    #*******************************************************************************************************************
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
    def test_check_hamburgur_menu_options(self):
        self.driver.find_element(By.XPATH, landing.hamburger_menu_right).click()  # show Hamburger menu
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_dashboard_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_product_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_part_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_resources_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_settings_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.humbuger_menu_product_click).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, landing.hamburger_menu_left).click()  # Hide Hamburger menu
        time.sleep(5)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.hamburger_menu_right)
        print("verify the Humber Menu options:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
# *******************************************************************************************************************
    # click on plus icon check whether it click or not
    def test_check_plus_icon_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.plus_icon).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_product_tab)
        print("Prodect tab must be display:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # click on product tab check whether it click or not
    def test_check_click_on_product_tab_click_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.click_product_tab).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.add_new_product_title_name)
        print("It must navigate the add new prodect page:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    #click on add new product check whether close button working or not
    def test_check_click_on_add_new_product_close_button_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.add_new_product_close_button).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.plus_icon)
        print("It Must be close the add a new product screen:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # click on add new product check whether cancel button working or not
    def test_check_click_on_add_new_product_cancel_button_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.click_product_tab).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.add_new_product_title_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.add_new_product_cancel_button).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.plus_icon)
        print("It Must be cancel the add a new product screen", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    #Check add new product whether Product Name textfield accept the text or not
    def test_check_product_name_text_field_accept_text_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.plus_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.click_product_tab).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.add_new_product_title_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.product_name_text_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.product_name_text_field).send_keys("Internet Browser")
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("Textfield must be accept the text", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    #Check add new product whether Product Status dropdown working or not
    def test_check_product_status_dropdown_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.status_dropdown_click).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("Must be select the dropdown", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Check add new product whether Product Status dropdown options working or not
    def test_check_product_status_dropdown_options_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.options_active_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.status_dropdown_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.options_production_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.status_dropdown_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.options_completed_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.status_dropdown_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.options_development_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.status_dropdown_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.options_active_click).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("Must be select the dropdown options", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # Check add new product whether Product about textfield accept the text or not
    def test_check_product_about_text_field_accept_text_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.product_about_text_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.product_about_text_field).send_keys("Searing the usefull information")
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("Textfield must be accept the text", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Check add new product whether Product Resent activities textfield accept the text or not
    def test_check_product_recent_activities_text_field_accept_text_or_not(self):
            self.driver.find_element(By.XPATH, dashboard.product_recent_activities_text_field).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, dashboard.product_recent_activities_text_field).send_keys(
                "only for testing activities")
            time.sleep(2)
            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
            print("Textfield must be accept the text", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    # *******************************************************************************************************************
    # Check add new product whether app url textfield accept the text or not
    def test_check_product_app_url_text_field_accept_text_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.product_app_url_text_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.product_app_url_text_field).send_keys(
            "https://d.dynoapp.in/#/Dyno/login")
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("Textfield must be accept the text", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Check add new product whether Hash tag textfield accept the text or not
    def test_check_product_hash_tag_text_field_accept_text_or_not(self):
            self.driver.find_element(By.XPATH, dashboard.product_hash_tag_text_field).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, dashboard.product_hash_tag_text_field).send_keys(" #information")
            time.sleep(2)

            # test case verification
            verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
            print("Textfield must be accept the text", verify_tc.is_displayed())
            if verify_tc.is_displayed() == True:
                assert True
            else:
                assert False
    # *******************************************************************************************************************
    # Check whether Product Hash Tag plus icon is click or not
    def test_check_product_hash_tag_icon_click_or_not(self):
        self.driver.find_element(By.XPATH,dashboard.hash_tag_plus_icon).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("click the hash tag plus icon verified", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
    # Check whether Product Hash Tag  delete button is click or not
    def test_check_product_hash_tag_delete_button_click_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.hash_tag_delete_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_name_text_field)
        print("click the hash tag delete icon verified", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

        self.driver.find_element(By.XPATH, dashboard.product_hash_tag_text_field).send_keys("#information")
        time.sleep(2)
    # *******************************************************************************************************************
    # Check whether add new product page is able to click the image button
    def test_check_product_page_click_image_button_or_not(self):
        self.driver.find_element(By.XPATH,dashboard.product_image).click()
        time.sleep(2)
        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.upload_image_title)
        print("It must navigate upload image title page", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # *******************************************************************************************************************
        # Click on Upload Check whether it is working or not
    def test_click_upload_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.file_path).send_keys(
                "/home/manjunath/Pictures/Placeholder_Person.jpg")
        time.sleep(5)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.upload_image_title)
        print("Image Upload sucessfully", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # Check whether upload image cancel batton working or not
    def test_click_upload_image_cancel_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.upload_image_cancel_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.product_image)
        print("Upload image must be cancel", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # Check whether select image is delete or not
    def test_click_upload_image_delete_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.product_image).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.file_path).send_keys(
            "/home/manjunath/Pictures/Placeholder_Person.jpg")
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.image_remove_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.upload_image_title)
        print("Image Upload remove sucessfully", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # Check whether select image is save or not
    def test_click_upload_image_save_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.file_path).send_keys(
            "/home/manjunath/Pictures/Placeholder_Person.jpg")
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.image_save_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.add_new_product_title_name)
        print("Image Upload save sucessfully", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    # ******************************************************************************************************************
    # # Check whether add button is working or not
    def test_check_add_button_working_or_not(self):
        self.driver.find_element(By.XPATH, dashboard.product_add_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, landing.hamburger_menu_right).click()
        print("Products add Sucessfully", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        # ******************************************************************************************************************



