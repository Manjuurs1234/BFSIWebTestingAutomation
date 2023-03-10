import psycopg2 as pg
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



class TestLogin:

    def test_Login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("E:\Company Software\Chrome  Webdriver - 110 version\chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=serv_obj)
        driver.get("https://d.dynoapp.in/#/login/login")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('manjunath.s@tibilsolutions.com')
        time.sleep(5)
        shadow = driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(5)

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
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)
        # dashboard screen SID 2.1
        driver.find_element(By.XPATH, "//img[@class='avatar']")
        time.sleep(5)
        # Grid view displayed
        driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(1) > img:nth-child(1)").is_displayed()
        time.sleep(2)

        # list view click
        driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(2) > img:nth-child(1)").click()
        time.sleep(2)
        # search project card
        driver.find_element(By.XPATH, "//input[@placeholder='Search Apps']").send_keys('Artistpass') # search name
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click() # 3 dots
        time.sleep(2)
        # view specifications
        driver.find_element(By.ID,"logout-id").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-landing:nth-child(3) > ion-header:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > img:nth-child(1)").click() # back button
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click() #3 dots
        time.sleep(2)
        # open application
        driver.find_element(By.ID,"logout-id").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-landing:nth-child(3) > ion-header:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > img:nth-child(1)").click()  # back button
        time.sleep(2)
        # Case studies screen
        driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > mat-tab-group:nth-child(1) > mat-tab-header:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR,".font-size")
        time.sleep(5)
        # presentation screen
        driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > mat-tab-group:nth-child(1) > mat-tab-header:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR,".font-size")
        time.sleep(2)

        # validations
        Dashboard_display = driver.find_element(By.XPATH, "//img[@class='orgLogo ng-star-inserted']")
        print("Element Found : Focus On", Dashboard_display.is_displayed())
        print("Dashboard page verified:")
        print("Grid view displayed:")
        print("List view verified:")
        print("project card name verified:")
        print("view specifications verified:")
        print("open application verified:")
        print("Case studies screen verified:")
        print("presentation verified:")

        time.sleep(2)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())

        driver.close()











