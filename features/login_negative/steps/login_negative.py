import sys
sys.path.append('features/utils')
import random,keyboard
from features.utils.environment import *
from features.utils.global_queries import *


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

@given(u'I am on the login page')
def step_impl(context):
    driver.get("https://voila.id/account/login")
    # raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I enter my Email and Password')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[2]/input').send_keys(data_email())
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[3]/input').send_keys(data_password())
    # raise NotImplementedError(u'STEP: When I enter my Email and Password')


@when(u'I click the login button')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[4]/div[1]/div/button').click()
    # raise NotImplementedError(u'STEP: When I click the login button')


@then(u'I should be redirected to account page')
def step_impl(context):
    current_url = get_current_url(driver)
    if current_url == "https://voila.id/account":
        take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to account page')


@when(u'I press enter on my keyboard')
def step_impl(context):
    keyboard.press_and_release('enter')
    # raise NotImplementedError(u'STEP: When I press enter on my keyboard')


@when(u'I enter the wrong Email but correct Password')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[2]/input').send_keys(data_email())
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[3]/input').send_keys("{}123".format(data_password()))
    # raise NotImplementedError(u'STEP: When I enter the wrong Email but correct Password')


@then(u'I should seen an error message')
def step_impl(context):
    print("Warning message dissapear")
    # raise NotImplementedError(u'STEP: Then I should seen an error message')


@when(u'I enter the correct Email but wrong Password')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[2]/input').send_keys("test_{}".format(data_email()))
    driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[3]/input').send_keys(data_password())
    # raise NotImplementedError(u'STEP: When I enter the correct Email but wrong Password')


@when(u'I enter the correct Email but wrong Password for 5 times')
def step_impl(context):
    for i in range(5):
        driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[2]/input').send_keys(data_email())
        driver.find_element('xpath','/html/body/div[6]/div/div/div/div/div[2]/div/div[1]/div/form/div[3]/input').send_keys("{}123".format(data_password()))
        sleep(5)    
    # raise NotImplementedError(u'STEP: When I enter the correct Email but wrong Password for 5 times')


@then(u'I should seen an error message of account locked')
def step_impl(context):
    print("feature not implemented")
    raise NotImplementedError(u'STEP: Then I should seen an error message of account locked')