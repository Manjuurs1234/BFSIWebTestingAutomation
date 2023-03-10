import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import validators

class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("E:\Company Software\Chrome  Webdriver - 110 version\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://d.dynoapp.in/#/Dyno/login")
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, '.alignment.md.button.button-solid.ion-activatable.ion-focusable.hydrated').click()  # Signin
        time.sleep(2)
        #email
        self.driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("manjunath.s@tibilsolutions.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
        time.sleep(2)
        #password
        self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("tibilsolutions")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
        time.sleep(2)
        # verify profile img avatar in dashboard
        Dashboard_dis = self.driver.find_element(By.CSS_SELECTOR, ".avatar")
        print("Dashboard Displayed  status:", Dashboard_dis.is_displayed())
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//img[@class='avatar']").is_displayed()
        time.sleep(3)
        # verify the Logo of Organization
        Logo_dis = self.driver.find_element(By.XPATH, "//img[@class='orgLogo']")
        print("Logo Displayed  status:", Logo_dis.is_displayed())
        # see the left pane with options


        # validations
        # Plan_dis = self.driver.find_element(By.CSS_SELECTOR, ".default-image")
        # print("Pan Window Displayed status:", Plan_dis.is_displayed())
        # time.sleep(5)
        # if Plan_dis.is_displayed() == True:
        #     assert True
        # else:
        #     print("Pan Window Displayed status:", Plan_dis.is_displayed())
        self.driver.close()

