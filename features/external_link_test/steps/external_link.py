import sys
sys.path.append('features/utils')
import random
from features.utils.environment import *
from features.utils.global_queries import *


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

@given(u'I am on the homepage')
def step_impl(context):
    driver.get("https://voila.id/")
    # raise NotImplementedError(u'STEP: Given I am on the homepage')


@when(u'I click on "appstore"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[1]/div/ul/li[1]/a').click()
    # raise NotImplementedError(u'STEP: When I click on "appstore"')


@then(u'I should be redirected to page associated with "appstore"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "appstore"')


@when(u'I click on "playstore"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[1]/div/ul/li[2]/a').click()
    # raise NotImplementedError(u'STEP: When I click on "playstore"')


@then(u'I should be redirected to page associated with "playstore"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "playstore"')


@when(u'I click on "facebook"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/ul/li[1]/a').click()
    # raise NotImplementedError(u'STEP: When I click on "facebook"')


@then(u'I should be redirected to page associated with "facebook"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "facebook"')


@when(u'I click on "instagram"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/ul/li[2]/a').click()
    # raise NotImplementedError(u'STEP: When I click on "instagram"')


@then(u'I should be redirected to page associated with "instagram"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "instagram"')


@when(u'I click on "tiktok"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/ul/li[3]/a')
    # raise NotImplementedError(u'STEP: When I click on "tiktok"')


@then(u'I should be redirected to page associated with "tiktok"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "tiktok"')


@when(u'I click on "youtube"')
def step_impl(context):
    driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/ul/li[4]/a').click()
    # raise NotImplementedError(u'STEP: When I click on "youtube"')


@then(u'I should be redirected to page associated with "youtube"')
def step_impl(context):
    take_screenshot(driver)
    # raise NotImplementedError(u'STEP: Then I should be redirected to page associated with "youtube"')