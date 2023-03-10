from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class Loginpage:
# locators

    chrome = "E:\Company Software\Chrome  Webdriver - 110 version\chromedriver.exe"
    URL = "https://d.dynoapp.in/#/Dyno/login"
    email = "manjunath.s@tibilsolutions.com"
    next = ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated"
    textbox_mailid_xpath = "//input[@placeholder='Email']"
    img = ".avatar"
    logout = "//button[2]//div[1]"

    def __init__(self,driver):
        self.driver = driver

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