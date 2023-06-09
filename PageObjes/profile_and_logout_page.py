from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



from selenium.webdriver.support.wait import WebDriverWait


class profile:
    click_profile_image = "//img[contains(@class,'avatar')]"
    my_profile = "//div[contains(text(),'My Profile')]"
    edit_button = "//div[contains(@class,'end-item small-end saveCancel-end')]"
    first_name_label = "//ion-label[contains(text(),'First Name')]"
    last_name_label = "//ion-label[contains(text(),'Last Name')]"
    edit_cancel_button = "(//img[contains(@class,'sveimg')])[2]"
    first_name_textfield = "//ion-input[@formcontrolname='firstname']//input"
    last_name_text_field = "//ion-input[@formcontrolname='lastname']//input"
    click_profile_picture = "//div[@class='img-div']"
    upload_profile_title_name = "//ion-label[contains(text(),'Upload Profile')]"
    upload_profile_cancel_button = "//button[contains(text(),'Cancel')]"
    click_upload_image = "//img[@class='uploadImg']"
    file_upload = "(//input[@type='file'])[2]"
    image_remove_button = "//img[contains(@class,'removeButton')]"
    save_profile_image = "//button[contains(text(),'Save')]"
    profile_save_button = "(//img[contains(@class,'sveimg')])[1]"
    left_arrow_button = "//img[contains(@src,'assets/icon/left-arrow.png')]"
    logout = "//div[contains(text(),'Logout')]"
    emalil_text_field = "//input[@placeholder='Email']"
