from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class landing:
    side_menu_bar = "//div[contains(@class,'sideMenuBar ng-star-inserted sm')]"
    hamburger_menu_right = "//img[@class='rightArrow']"
    hamburger_menu_left = "//img[@class='leftArrow']"
    kebab_menu = "(//img[@class='mat-menu-trigger dot'])[1]"
    bfsi_card = "//ion-label[contains(text(),'BFSI')]"
    drop_down_right = "(//img[@class='vectorDown'])[2]"
    search_bar = "(//input[contains(@placeholder,'Search')])[3]"
    plus_icon = "(//img[contains(@class,'addImg')])[3]"
    add_new_menu = "//ion-label[contains(normalize-space(),'Add a new')]"
    click_folder = "//ion-label[contains(normalize-space(),'Folder')]"
    folder_popup_title = "//div[@class='popupTitle']"
    save_button = '.add-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated'
    cancel_button = "//ion-button[normalize-space()='Cancel']"
    invalid_credentials_msg = "//div[@class='error-messages']"
    title_name = "//ion-input[contains(@formcontrolname,'title')]/input"
    description_text = "textarea"
    change_button = "//img[contains(@class,'change-logo')]"
    plan_radio_button = "//span[contains(@class,'mat-radio-inner-circle')][1]"
    plan_window = "//span[contains(text(),'Plan')]"
    click_vision = "//ion-label[contains(text(),'Vision')]"
    vision_popup_title = "//div[@class='popupTitle']"
    story_popup_title = "//div[@class='popupTitle']"
    click_story = "//ion-label[contains(text(),'Story')]"
    user_interface_popup_title = "//div[@class='popupTitle']"
    click_user_interface = "//ion-label[contains(text(),'User Interface')]"
    click_Specification = "//ion-label[contains(text(),'Specification')]"
    specification_popup_title = "//div[@class='popupTitle']"