from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class Loginpage:
# locators

    chrome = '../Driver/chromedriver'
    URL = "https://d.dynoapp.in/#/Dyno/login"
    email = "manjunath.s@tibilsolutions.com"
    next = ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated"
    textbox_mailid_xpath = "//input[@placeholder='Email']"
    img = ".avatar"
    logout = "//button[2]//div[1]"

    def __init__(self,driver):
        self.driver = driver


    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options, executable_path='../Driver/chromedriver')
        self.driver.set_window_size(3860, 2160)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print('window size :', self.driver.get_window_size())
        print("Current session is {}".format(self.driver.session_id))

        return self.driver
    # actions methods

    # mail id

    def setmailid(self,mailid):
        mailid = self.driver.find_element(By.XPATH,self.textbox_mailid_xpath)
        mailid.send_keys(mailid)

    # img action
    def img_button(self):
       self.driver.find_element(By.CSS_SELECTOR, self.img).click()

    def logout_button(self):

      # logout button
        self.driver.find_element(By.XPATH,self.logout).click()