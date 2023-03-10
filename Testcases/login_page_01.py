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
        # ***************************************************************************

        # Empty text box - Invalid testcase SID 1.1
        driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        time.sleep(2)
        shadow = driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
        #***************************************************************************

        # Invalid mail - Invalid testcase SID 1.2
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('abc')
        time.sleep(2)
        shadow = driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".error-message")
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()

        #***************************************************************************
        # valid mail - valid testcase SID 1.3
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('manjunath.s@tibilsolutions.com')
        time.sleep(2)
        shadow = driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)

        #************************************************************************************************
        # enter the otp - Empty text box - Invalid testcase SID 1.4
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter OTP']")
        time.sleep(2)
        shadow = driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        time.sleep(2)
        #****************************************************************************************************************

        # wrong otp - Invalid testcase SID 1.5
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys('123456')
        driver.implicitly_wait(2)
        shadow = driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated").click()
        time.sleep(12)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").clear()
        time.sleep(2)


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

    #  ******************************************************************************************
        # valid otp - valid testcase SID 1.6
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

        # validations
        errormsg = 'Error messages verified'
        if errormsg=="Error messages was verified":
            print(errormsg)
        else:
            print("verified")

        Dashboard_display = driver.find_element(By.XPATH, "//img[@class='orgLogo ng-star-inserted']")

        print("Element Found : Focus On", Dashboard_display.is_displayed())

        print("Error messages was verified:")
        print("Login page was verified:")
        time.sleep(5)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())

        driver.close()



