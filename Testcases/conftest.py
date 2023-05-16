import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():

    serv_obj = Service("/home/manjunath/Projects/Harmony And Dyno Automation/Testcases/chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

