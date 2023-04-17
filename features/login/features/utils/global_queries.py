from utils.global_queries import *
from behave import *
import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def element_class_login_button(driver):
    return driver.find_element("xpath","/html/body/div[4]/div/div/div/div/div[2]/div/div[1]/div/form/div[4]/div[1]/div/button")

def element_xpath_shoes(driver):
    return driver.find_element("xpath","/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[7]/div/div[1]/a")

def get_current_url(driver):
    return driver.current_url

def wait_webdriver_url(driver,val):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.url_to_be(val))

def wait_webdriver_element(driver,type_of,value):
    element = WebDriverWait(driver, 10)
    return element.until(EC.presence_of_element_located((type_of,value)))

def check_class_exist(driver,classname):
    checked_class = driver.find_element("class name",classname)
    if len(checked_class)>0:
        return True
    else:
        return False

