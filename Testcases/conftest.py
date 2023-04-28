import pytest
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def browser():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("/home/manjunath/Downloads/chromedriver_linux64")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    yield driver
    driver.quit()
