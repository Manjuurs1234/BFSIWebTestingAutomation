from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class dashboard:
    cards = "//ion-row[@class='align-row ng-star-inserted md hydrated']"
    search_bar = "//input[@type='search']"
    click_kebab_menu = "(//img[contains(@class,'mat-menu-trigger dot')])[1]"
    click_back_button = "(//img[@class='orgLogo'])[2]"
    open_applications = "//div[text()='Open Application']"
    click_back_button_browser = "//img[@class='orgLogo ng-star-inserted']"
    click_read_more = "(//a[@class='ng-star-inserted'])[1]"
    click_read_less = "//a[normalize-space()='Read Less']"
    humbuger_menu_dashboard_click = "//label[contains(text(),'Dashboard')]"
    humbuger_menu_product_click = "//label[contains(text(),'Product')]"
    humbuger_menu_part_click = "//label[contains(text(),'Part')]"
    humbuger_menu_resources_click = "//label[contains(text(),'Resources')]"
    humbuger_menu_settings_click = "//label[contains(text(),'Settings')]"
    plus_icon = "//img[@class='addImg']"
    click_product_tab = "//ion-label[contains(text(),'Product')]"
    add_new_product_title_name = "//label[contains(text(),'Add New Product')]"
    add_new_product_close_button = "//img[contains(@alt,'remove')]"
    add_new_product_cancel_button = "//ion-button[contains(text(),'Cancel')]"
    product_name_text_field = "//ion-input[contains(@formcontrolname,'name')]//input"
    status_dropdown_click = '//mat-select'
    options_active_click = "//span[contains(text(),'Active')]"
    options_production_click = "//span[contains(text(),'Production')]"
    options_completed_click = "//span[contains(text(),'Completed')]"
    options_development_click = "//span[contains(text(),'Development')]"
    product_about_text_field = "//ion-input[@formcontrolname='about']//input"
    product_recent_activities_text_field = "//ion-input[contains(@formcontrolname,'recentActivities')]//input"
    product_app_url_text_field= "//ion-input[contains(@formcontrolname,'appUrl')]//input"
    product_hash_tag_text_field ="//ion-row[contains(@formarrayname,'hashTag')]//input"
    hash_tag_plus_icon = "//img[contains(@class,'addHash')]"
    hash_tag_delete_button = "//img[@class='deleteHash']"
    product_image = "//img[contains(@alt,'select Product Image')]"
    upload_image_title = "//ion-label[contains(text(),'Upload Image')]"
    file_path = "//input[@type='file']"
    upload_image_cancel_button = "//button[starts-with(text(),'Cancel')]"
    image_remove_button = "//img[contains(@class,'removeButton')]"
    image_save_button = "//button[contains(text(),'Save')]"
    product_add_button = "//ion-button[contains(text(),'Add')]"
    dots_click = "(//img[contains(@aria-haspopup,'true')])[2]"
    new_product_card_menu = "//img[contains(@class,'mat-menu-trigger dot')]"
    new_product_card_delete = "//div[contains(text(),'Delete')]"