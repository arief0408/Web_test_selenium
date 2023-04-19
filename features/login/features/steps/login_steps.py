import sys
sys.path.append('features/login/features/utils')
import random
from features.login.features.utils.environment import *
from features.login.features.utils.global_queries import *
# from behave import *
# import allure,random
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

# driver.get("https://voila.id/collections/live-sale/products/dellest-city-medium-shoulder-bag-gotica-black")
# sleep(3)
# driver.find_element("xpath",'//*[@id="product_form_7945757786355"]/div[1]/div[2]/button').click()
# sleep(3)
# driver.find_element("partial link text",'BELI').click()
# sleep(3)
# @given("I am on the login page")
# def step_impl(context):
#     driver.get("https://voila.id/account/login/")
#     take_screenshot(driver)

# @when("I enter my email in email field and password in password field")
# def step_impl(context):
#     element_id_login_email(driver).send_keys(data_email())

# @when('I click the login button')
# def step_impl(context):
#     element_id_login_password(driver).send_keys(data_password())

# @then("I Should be redirected to voila.id/account")
# def step_impl(context):
#     element_class_login_button(driver).click()
#     wait_webdriver_url(driver,"https://voila.id/account")
#     current_url = get_current_url(driver)
#     if current_url == "https://voila.id/account":
#         take_screenshot(driver)
#     else:
#         raise NotImplementedError(u'STEP: I Should be redirected to voila.id/account')
    


# @given(u'I am on the homepage of voila.id')
# def step_impl(context):
#     driver.get("https://voila.id/")
#     try:
#         driver.find_element("css selector",'button[aria-label="close"]').click()
#     except:
#         print("No Pop Up Deals")
#     current_url = get_current_url(driver)
#     if current_url == "https://voila.id/":
#         take_screenshot(driver)
#     else:
#         raise NotImplementedError(u'STEP: Given I am on the homepage of voila.id')

# @when(u'I clicked on one of the product listed')
# def step_impl(context):
#     try:
#         wait_webdriver_element_clickable(driver,"css selector",'a[tabindex="0"]')
#         click_me = driver.find_elements("css selector",'a[tabindex="0"]')
#         click_random = random.choice(click_me)
#         link_of_click = click_random.get_attribute("href")
#         click_random.click()
#         context.link_of_click = link_of_click
#     except:
#         raise NotImplementedError(u'It redirect to the page of the product')


# @then(u'It redirect to the page of the product')
# def step_impl(context):
#     print(context.link_of_click)
#     current_url = get_current_url(driver)
#     clicked_url = context.link_of_click
#     if current_url == clicked_url:
#         take_screenshot(driver)
#     else:
#         raise NotImplementedError(u'STEP: Then It redirect to the page of the product')
#     context.clicked_url = clicked_url


# @given(u'I am on the page of selected product')
# def step_impl(context):
#     try:
#         take_screenshot(driver)
#     except:
#         raise NotImplementedError(u'STEP: Given I am on the page of selected product')


# @when(u'I click + Keranjang')
# def step_impl(context):
#     sleep(5)
#     driver.find_element("css selector",'button[data-type="addtocart"]').click()


# @then(u'I should have an popped up windows of Produk berhasil ditambah!')
# def step_impl(context):
#     check_modal = driver.find_element("class name","tt-modal-messages")
#     if check_modal != "":
#         take_screenshot(driver)
#     else:
#         raise NotImplementedError(u'STEP: Then I should have an popped up windows of Produk berhasil ditambah!')

# @given(u'I am on the popped up page of Produk berhasil ditambah!')
# def step_impl(context):
#     try:
#         take_screenshot(driver)
#     except:   
#         raise NotImplementedError(u'STEP: Given I am on the popped up page of Produk berhasil ditambah!')


# @when(u'I click on Beli')
# def step_impl(context):
#     try:
#         driver.find_element("partial link text",'BELI').click()
#     except:
#         raise NotImplementedError(u'STEP: When I click on Beli')


# @then(u'I should be redirected to checkouts page')
# def step_impl(context):
#     try:
#         driver.find_element("css selector",'h2.n8k95w1._1fragema3.n8k95w3')
#     except:
#         raise NotImplementedError(u'STEP: Then I should be redirected to checkouts page')
    
@given(u'I am on the checkout page')
def step_impl(context):
    try:
        driver.get("https://voila.id/checkouts/c/c8d5ca3f72ce06a5911422f13e4d9953/information?_ga=2.16386294.1789729160.1681838703-1173728324.1681838620")
    except:
        raise NotImplementedError(u'STEP: Given I am on the checkout page')


@when(u'I type Arief in Nama Depan field')
def step_impl(context):
    try:
        driver.find_element("id",'TextField1').send_keys(data_first_name())
    except:
        raise NotImplementedError(u'STEP: When I type Arief in Nama Depan field')


@then(u'I saw the field text changed to Arief')
def step_impl(context):
    try:
        confirm_first_name = driver.find_element("id",'TextField1').get_attribute("value")
        if confirm_first_name == data_first_name():
            print(confirm_first_name)
        else:
            raise NotImplementedError(u'STEP: Then I saw the field text changed to Arief')
    except:    
        raise NotImplementedError(u'STEP: Then I saw the field text changed to Arief')


@when(u'I type Chaerudin in Nama Belakang field')
def step_impl(context):
    try:
        driver.find_element("id",'TextField2').send_keys(data_last_name())
    except:
        raise NotImplementedError(u'STEP: When I type Chaerudin in Nama Belakang field')


@then(u'I saw the field text changed to Chaerudin')
def step_impl(context):
    try:
        confirm_last_name = driver.find_element("id",'TextField2').get_attribute("value")
        if confirm_last_name == data_last_name():
            print(confirm_last_name)
        else:
            raise NotImplementedError(u'STEP: Then I saw the field text changed to Chaerudin')
    except:
        raise NotImplementedError(u'STEP: Then I saw the field text changed to Chaerudin')


@when(u'I type [Arief Chaerudin]-[Candidate QA] in Alamat field')
def step_impl(context):
    try:
        driver.find_element("id",'TextField3').send_keys(data_address())
    except:
        raise NotImplementedError(u'STEP: When I type [Arief Chaerudin]-[Candidate QA] in Alamat field')


@then(u'I saw the field text changed to [Arief Chaerudin]-[Candidate QA]')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I saw the field text changed to [Arief Chaerudin]-[Candidate QA]')


@when(u'I type 13950 in Kode Pos field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type 13950 in Kode Pos field')


@then(u'I saw the field text changed to 13950')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I saw the field text changed to 13950')


@when(u'I click the dropdown and select Daerah Khusus Ibukota Jakarta')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the dropdown and select Daerah Khusus Ibukota Jakarta')


@then(u'I saw the dropdown value changed to Daerah Khusus Ibukota Jakarta')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I saw the dropdown value changed to Daerah Khusus Ibukota Jakarta')


@when(u'I type 089672300149 in No Handphone field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type 089672300149 in No Handphone field')


@then(u'I saw the field text changed to 089672300149')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I saw the field text changed to 089672300149')


@given(u'I am on the checkout page with all the form filled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the checkout page with all the form filled')


@when(u'I click lanjut ke pengiriman')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click lanjut ke pengiriman')


@then(u'I get redirected to shipping page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get redirected to shipping page')


@given(u'I am on the shipping page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the shipping page')


@when(u'I click radio button value JNT in metode pengiriman')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click radio button value JNT in metode pengiriman')


@then(u'I saw the radio button value switched to JNT')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I saw the radio button value switched to JNT')


@when(u'I click Lanjut ke Pembayaran')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Selesaikan Pesanan button')


@then(u'I get redirected to thank you page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get redirected to thank you page')