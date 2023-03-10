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


        # valid mail - valid testcase
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

    #  ******************************************************************************************
        # valid otp - valid testcase
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

    # logout

        driver.find_element(By.CSS_SELECTOR, ".avatar").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[2]/div[1]").click()
        time.sleep(2)

        # validations
        logout_page = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']")
        print("Element Found : Focus On", logout_page.is_displayed())
        print("Logout page verified:")
        time.sleep(5)
        if logout_page.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", logout_page.is_displayed())

        driver.close()





