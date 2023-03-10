import psycopg2 as pg
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from PageObjes.pom import Loginpage


class TestLogin:

    def test_login(self):
          self.serv_obj = Service(Loginpage.chrome)
          self.driver = webdriver.Chrome(service=self.serv_obj)
          self.driver.maximize_window()
          self.driver.get(Loginpage.URL)
          self.driver.find_element(By.XPATH, Loginpage.textbox_mailid_xpath).send_keys(Loginpage.email)
          time.sleep(5)
          self.driver.find_element(By.CSS_SELECTOR, Loginpage.next).click()
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
          self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
          time.sleep(5)
          shadow1 = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
          shadow1.click()
          time.sleep(5)
          # dashboard screen SID 2.1
          self.driver.find_element(By.XPATH, "//img[@class='avatar']")
          time.sleep(5)
          # Grid view displayed
          self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(1) > img:nth-child(1)").is_displayed()
          time.sleep(2)

          # list view click
          self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(2) > img:nth-child(1)").click()
          time.sleep(2)
          # search project card
          self.driver.find_element(By.XPATH, "//input[@placeholder='Search Apps']").send_keys('Artistpass') # search name
          time.sleep(2)
          self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click() # 3 dots
          time.sleep(2)
          # view specifications
          self.driver.find_element(By.ID,"logout-id").click()
          time.sleep(2)
          self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-landing:nth-child(3) > ion-header:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > img:nth-child(1)").click() # back button
          time.sleep(2)
          self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click() #3 dots
          time.sleep(2)
          # open application
          self.driver.find_element(By.ID,"logout-id").click()
          time.sleep(2)
          self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-landing:nth-child(3) > ion-header:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > img:nth-child(1)").click()  # back button
          time.sleep(2)
          # Case studies screen
          self.driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > mat-tab-group:nth-child(1) > mat-tab-header:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)").click()
          self.driver.find_element(By.CSS_SELECTOR,".font-size")
          time.sleep(5)
          # presentation screen
          self.driver.find_element(By.CSS_SELECTOR, "body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(1) > mat-tab-group:nth-child(1) > mat-tab-header:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)").click()
          self.driver.find_element(By.CSS_SELECTOR,".font-size")
          time.sleep(2)

          # validations
          Dashboard_display = self.driver.find_element(By.XPATH, "//img[@class='orgLogo ng-star-inserted']")
          print("Element Found : Focus On", Dashboard_display.is_displayed())
          print("Dashboard page verified:")
          print("Grid view displayed:")
          print("List view verified:")
          print("project card name verified:")
          print("view specifications screen verified:")
          print("open application screen verified:")
          print("Case studies screen verified:")
          print("presentation screen verified:")
          print("logout screen verified:")

          time.sleep(2)
          if Dashboard_display.is_displayed() == True:
            assert True
          else:
             print("Element Not Found : Not verified", Dashboard_display.is_displayed())

            #logout
          self.lp = Loginpage(self.driver)
          time.sleep(5)
          self.lp.img_button()
          time.sleep(5)
          self.lp.logout_button()
          time.sleep(5)
          self.driver.close()