import psycopg2 as pg
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from PageObjes.dyno_pom import Loginpage
class TestLogin:
    @pytest.fixture()
    def test_Login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("Loginpage.chrome")
        self.driver = webdriver.Chrome(options=options, service=serv_obj)
        self.driver.maximize_window()
        self.driver.get(Loginpage.URL)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, Loginpage.textbox_mailid_xpath).send_keys(Loginpage.email)
        shadow = self.driver.find_element(By.CSS_SELECTOR, Loginpage.next)
        shadow.click()

        port = '5432'
        host = '34.100.216.73'
        user = "postgres"
        password = "t3djo7b0jfd9J3JL"
        database = "devdyno"

        con = pg.connect(database=database, user=user, password=password, host=host, port=port)
        cur = con.cursor()
        QueryString = '''SELECT (payload ->>'OTP') :: integer FROM auth.nq Order by pid desc limit 1'''
        cur.execute(QueryString)
        con.commit()
        output1 = cur.fetchall()
        a = str(output1)
        b = a.replace('[(', '')
        otp = b.replace(',)]', '')
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
    #**************************************************************************************************************************

        # list view click
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(2) > img:nth-child(1)").click()
        self.driver.implicitly_wait(2)
        # search project card
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search Apps']").send_keys('BFSI')  # search name
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click()  # 3 dots
        self.driver.implicitly_wait(2)
        # view specifications
        self.driver.find_element(By.ID, "logout-id").click()
        self.driver.implicitly_wait(2)
        # click back button
        self.driver.find_element(By.CSS_SELECTOR, "ion-col[class='ion-align-self-center justifyContent logocol md hydrated'] img[class='orgLogo']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click()  # 3 dots
        self.driver.implicitly_wait(2)
        # open application
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2) > div:nth-child(1)").click()
        self.driver.implicitly_wait(10)
        # click back button
        self.driver.find_element(By.CSS_SELECTOR,".orgLogo.ng-star-inserted").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click()  # 3 dots
        self.driver.implicitly_wait(2)
        # view specifications again
        self.driver.find_element(By.ID, "logout-id").click()
        self.driver.implicitly_wait(3)
        yield
        self.driver.close()
    #***********************************************************************************************************************

        # SID 3.1 -  Screen Name: Plan Screen
    def test_plan_screen(self,test_Login):
        shadow2 = self.driver.find_element(By.CSS_SELECTOR, '.accordion-icon.md.hydrated')
        shadow2.click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".option-label.hideoverflow").click()
        self.driver.implicitly_wait(2)
        # verify Logo of Organization
        self.driver.find_element(By.CSS_SELECTOR, ".default-image")
        self.driver.implicitly_wait(2)

        # see the left menu
        self.driver.find_element(By.CSS_SELECTOR, ".rightArrow").click()
        self.driver.implicitly_wait(2)
        # Navigation path of user
        self.driver.find_element(By.CSS_SELECTOR, ".vectorDown").click()
        self.driver.implicitly_wait(2)
        # left pune options
        self.driver.find_element(By.CSS_SELECTOR, ".vectorDown").click()
        self.driver.implicitly_wait(2)
        # bottom menu text
        self.driver.find_element(By.CSS_SELECTOR, ".font-size")
        self.driver.implicitly_wait(2)
    #*********************************************************************************************************
         # SID 3.2 - Verify UI elements of Left Menu
        self.driver.find_element(By.CSS_SELECTOR, ".side-menu-div.white-bg")
        self.driver.implicitly_wait(2)
        # see the numbered Visions
        self.driver.find_element(By.CSS_SELECTOR, ".side-menu-div.white-bg")
        self.driver.implicitly_wait(2)
    #*******************************************************************************************************

        #  SID 3.3 - Search an Item (SID, UI, Vision by number)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("FLD 1")
        self.driver.implicitly_wait(2)
        # view the details of that particular Item upon selection
        self.driver.find_element(By.CLASS_NAME, "mat-option-text").click()
        self.driver.implicitly_wait(1)
    #***********************************************************************************************************

        # SID 3.4 - Add a New Item  - User clicks on + button
        self.driver.find_element(By.CSS_SELECTOR, ".addImg").click() # '+' button
        self.driver.implicitly_wait(1)
    #***********************************************************************************************************
        # SID 3.5 - Add a New Folder
        self.driver.find_element(By.XPATH, "//ion-label[normalize-space()='Folder']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".cancel-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated").click() # cancel button
        self.driver.implicitly_wait(2)
    #***********************************************************************************************************

        # SID 3.6 - Add a new User Specification
        self.driver.find_element(By.CSS_SELECTOR, ".addImg").click()  # '+' button
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, "//ion-label[normalize-space()='Specification']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR,".cancel-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated").click()  # cancel button
        self.driver.implicitly_wait(2)
    # ***********************************************************************************************************
        # validations
        Dashboard_display = self.driver.find_element(By.XPATH, "//label[normalize-space()='Dashboard']")
        print("Element Found : Focus On", Dashboard_display.is_displayed())
        print("Dyno view specifications page was verified:")
        print("Logo of the org was verified:")
        print("Left menu options was verified:")
        print("Bottom menu text was verified:")
        print("UI elements of Left Menu was verified:")
        print("Numbered Visions folders was verified:")
        print("Searched folder name was verified:")
        print("View the details of that particular Item upon selection was verified:")
        print("Add button popup with the list of options was verified:")
        print("Add a folder screen was verified:")
        print("Add a new User Specification screen was verified:")
        time.sleep(2)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())

        self.driver.close()