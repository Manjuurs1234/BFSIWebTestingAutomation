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
        # Cards are must be display in grid view
    def test_grid_view(self):
        self.driver.find_element(By.XPATH, dashboard.grid_view_click).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.grid_view_click).click() # click again

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.grid_view_click)
        print("Grid view is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(3)
    #*******************************************************************************************************************
        # click on kebab menu
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
    # View specification and open application tab must be display
    def test_application_tab(self):
        self.driver.find_element(By.XPATH, dashboard.view_specifications).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.click_back_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_kebab_menu)
        print("Application Tab is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
    #*******************************************************************************************************************
    # navigate the dashboard page
    def test_navigate_dashboard_page(self):
        self.driver.find_element(By.XPATH, dashboard.click_kebab_menu).click()
        time.sleep(2)
        # open application
        self.driver.find_element(By.XPATH, dashboard.open_applications).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.click_back_button_browser).click()
        time.sleep(3)

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.view_application_tab_name)
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
        # Click on list view
    def test_click_list_view(self):
        self.driver.find_element(By.XPATH, dashboard.click_list_view).click()

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_list_view)
        print("Cards are view in list view verified:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)
    #*******************************************************************************************************************
        # click kebab menu in list view
    def test_click_kebab_menu_list_view(self):
        self.driver.find_element(By.XPATH, dashboard.click_kebab_list_view).click()

    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.click_kebab_list_view)
        print("View specification and open application tab is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False
        time.sleep(2)
    #*******************************************************************************************************************
        # Click on view specification in list view
    def test_click_view_specification(self):
        self.driver.find_element(By.XPATH, dashboard.view_specifications).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.click_back_button).click()
        time.sleep(2)

        # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.view_application_tab_name)
        print("view specification in list view is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    #*******************************************************************************************************************
        # Click on Open application in list view
    def test_click_on_open_application(self):
        self.driver.find_element(By.XPATH, dashboard.click_kebab_list_view).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, dashboard.open_applications).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, dashboard.click_back_button_browser).click()
        time.sleep(2)
    # test case verification
        verify_tc = self.driver.find_element(By.XPATH, dashboard.view_application_tab_name)
        print("Open application in list view is displayed:", verify_tc.is_displayed())
        if verify_tc.is_displayed() == True:
            assert True
        else:
            assert False

    #*******************************************************************************************************************
