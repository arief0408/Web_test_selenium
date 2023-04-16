# import sys
# sys.path.append('/CATALYS_QA_TEST/features/login/utils')
from utils.global_queries import *
from behave import *
import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@given("I am on the login page")
def step_impl(context):
    driver.get("https://voila.id/account/login")
    take_screenshot(driver)

@when("I enter my email in email field and password in password field")
def step_impl(context):
    element_id_login_email(driver).send_keys(data_email())
@when('I click the login button')
def step_impl(context):
    element_id_login_password(driver).send_keys(data_password())
@then("I Successfully login")
def step_impl(context):
    sleep(5)
    take_screenshot(driver)
