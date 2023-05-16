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
    grid_view_click = "(//img[@class='viewLogo'])[1]"
    click_kebab_menu = "(//img[@id='3dotMenugridv'])[1]"
    view_specifications = "//div[text()='View Specifications']"
    click_back_button = "//ion-col[@class='ion-align-self-center justifyContent logocol md hydrated']//img[@class='orgLogo']"
    open_applications = "//div[text()='Open Application']"
    click_back_button_browser = "//img[@class='orgLogo ng-star-inserted']"
    view_application_tab_name = "//span[@class='tabiconname ng-star-inserted']"
    click_read_more = "(//a[@class='ng-star-inserted'])[1]"
    click_read_less = "//a[normalize-space()='Read Less']"
    click_list_view = "(//img[@class='viewLogo'])[2]"
    click_kebab_list_view ="(//img[@id='3dotmenulistv'])[1]"