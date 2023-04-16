import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def data_email():
    return "ariefchaerudin@gmail.com"

def data_password():
    return "Arief311065!"

def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

def element_id_login_email(driver):
    return driver.find_element("id","loginInputName")

def element_id_login_password(driver):
    return driver.find_element("id","loginInputEmail")