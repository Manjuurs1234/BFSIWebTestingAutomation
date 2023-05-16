from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class Login:
    URL = "https://d.dynoapp.in/#/Dyno/login"
    email = "manjunath.s@tibilsolutions.com"
    next_button = ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated"

    title = "//div[@class='titleStyle']"
    sub_title = "//p[text()='Sales Enabler & Solution Accelerator']"

    # Google Sign in
    click_google_signin_button = "//ion-button[contains(text(),'Sign In With Google')]"
    google_email_textfield = '//*[@id="identifierId"]'
    google_email_next_button = '//*[@id="identifierNext"]/div/button/span' # email next button
    google_password_textfield = '//*[@id="password"]/div[1]/div/div[1]/input'
    google_pwd_next_button = "//span[normalize-space()='Next']" # password next button
    profile_img = "//img[@class='avatar']"


    email_textfield = "//input[@placeholder='Email']"
    error_message = ".error-message"
    otp_textfield = "//input[@placeholder='Enter OTP']"
    error_text = "error-message"
    wrong_otp_ok_button = "//span[@class='alert-button-inner sc-ion-alert-md'] = ok button"
    invalid_mail_id_ok_button = "//span[@class='alert-button-inner sc-ion-alert-md']"

    # logout
    img = ".avatar"
    logout = "//button[2]//div[1]"


    def __init__(self, driver):
        self.driver = driver

    def get_subtitle(self):
        sub_title = self.driver.find_element(By.XPATH, self.sub_title).text
        return sub_title

    def get_subtitle_center(self):
        sub_title_center = self.driver.find_element(By.XPATH, self.sub_title).text
        return sub_title_center

    def click_google_sign_in(self):
        click_google_sign_in = self.driver.find_element(By.XPATH, Login.profile_img)
        return click_google_sign_in

    def dashboard_page(self):
        dashboard_page = self.driver.find_element(By.XPATH, Login.profile_img)
        return dashboard_page


    def get_next_button(self):
        next_button = self.driver.find_element(By.CSS_SELECTOR, Login.next_button).click
        return next_button

    def get_error_msg(self):
        error_msg = self.driver.find_element(By.CSS_SELECTOR, Login.error_message).text
        return error_msg

    def valid_mail_id(self):
        valid_mail_id = self.driver.find_element(By.XPATH, Login.email_textfield).text
        return valid_mail_id

    def img_button(self):
       img_button = self.driver.find_element(By.CSS_SELECTOR, self.img).click()
       return img_button

    def logout_button(self):
        logout_button = self.driver.find_element(By.XPATH,self.logout).click()
        return logout_button

    def otp_field(self):
        otp_field = self.driver.find_element(By.XPATH, self.otp_textfield).text
        return otp_field

