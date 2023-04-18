# import sys
# sys.path.append('/CATALYS_QA_TEST/features/login/utils')
from utils.global_queries import *
import sys
sys.path.append('features/login/features/utils')
import environment,random

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

@then("I Should be redirected to voila.id/account")
def step_impl(context):
    element_class_login_button(driver).click()
    wait_webdriver_url(driver,"https://voila.id/account")
    current_url = get_current_url(driver)
    if current_url == "https://voila.id/account":
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: I Should be redirected to voila.id/account')
    


@given(u'I am on the homepage of voila.id')
def step_impl(context):
    driver.get("https://voila.id/")
    current_url = get_current_url(driver)
    if current_url == "https://voila.id/":
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Given I am on the homepage of voila.id')

@when(u'I clicked on one of the product listed')
def step_impl(context):
    try:
        wait_webdriver_element_clickable(driver,"css selector",'a[tabindex="0"]')
        click_me = driver.find_elements("css selector",'a[tabindex="0"]')
        click_random = random.choice(click_me)
        link_of_click = click_random.get_attribute("href")
        click_random.click()
        context.link_of_click = link_of_click
    except:
        raise NotImplementedError(u'It redirect to the page of the product')


@then(u'It redirect to the page of the product')
def step_impl(context):
    print(context.link_of_click)
    current_url = get_current_url(driver)
    clicked_url = context.link_of_click
    if current_url == clicked_url:
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Then It redirect to the page of the product')
    context.clicked_url = clicked_url


@given(u'I am on the page of selected product')
def step_impl(context):
    try:
        take_screenshot(driver)
    except:
        raise NotImplementedError(u'STEP: Given I am on the page of selected product')


@when(u'I click + Keranjang')
def step_impl(context):
    try:
        wait_webdriver_element_clickable(driver,"class name",'addtocart-js')
        beli_button = driver.find_element("class name","addtocart-js")
        beli_button.click()
    except:
        raise NotImplementedError(u'STEP: When I click + Keranjang')


@then(u'I should have an popped up windows of Produk berhasil ditambah!')
def step_impl(context):
    check_modal = driver.find_element("class name","tt-modal-messages")
    if check_modal != "":
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Then I should have an popped up windows of Produk berhasil ditambah!')

@given(u'I am on the popped up page of Produk berhasil ditambah!')
def step_impl(context):
    try:
        take_screenshot(driver)
    except:   
        raise NotImplementedError(u'STEP: Given I am on the popped up page of Produk berhasil ditambah!')


@when(u'I click on Beli')
def step_impl(context):
    try:
        driver.find_element("css selector",'a[href="/checkout"]')
    except:
        raise NotImplementedError(u'STEP: When I click on Beli')


@then(u'I should be redirected to checkouts page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to checkouts page')