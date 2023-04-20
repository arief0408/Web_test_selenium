import sys
sys.path.append('features/login/features/utils')
import random
from features.login.features.utils.environment import *
from features.login.features.utils.global_queries import *


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

@given("I am on the login page")
def step_impl(context):
    driver.get("https://voila.id/account/login/")
    take_screenshot(driver)

@when("I enter my email in email field and password in password field")
def step_impl(context):
    element_id_login_email(driver).send_keys(data_email())
    element_id_login_password(driver).send_keys(data_password())

@when('I click the login button')
def step_impl(context):
    element_class_login_button(driver).click()

@then("I Should be redirected to voila.id/account")
def step_impl(context):
    wait_webdriver_url(driver,"https://voila.id/account")
    current_url = get_current_url(driver)
    if current_url == "https://voila.id/account":
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: I Should be redirected to voila.id/account')
    


@given(u'I am on the homepage of voila.id')
def step_impl(context):
    sleep(10)
    try:
        driver.find_element("css selector",'button[aria-label="close"]').click()
    except:
        print("No Pop Up Deals")
    driver.find_element('xpath','/html/body/div[3]/header/div[2]/div[1]/div/div/div[1]/a').click() 
    
    current_url = get_current_url(driver)
    if current_url == "https://voila.id/":
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Given I am on the homepage of voila.id')

@when(u'I clicked on one of the product listed')
def step_impl(context):
    # try:
    driver.find_element('xpath','//*[@id="main-menu"]/div/div/nav/ul/li[4]/a').click()
    first_product = driver.find_element('xpath','//*[@id="shopify-section-collection-template-boost-pfs-filter"]/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[1]/a')
    # wait_webdriver_element_clickable(driver,"css selector",'a[tabindex="0"]')
    # click_me = driver.find_elements("css selector",'a[tabindex="0"]')
    # click_random = random.choice(click_me)
    link_of_click = first_product.get_attribute("href")
    first_product.click()
    # click_random.click()
    context.link_of_click = link_of_click
    # except:
    #     raise NotImplementedError(u'It redirect to the page of the product')


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
    sleep(5)
    driver.find_element("css selector",'button[data-type="addtocart"]').click()


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
        driver.find_element("partial link text",'BELI').click()
    except:
        raise NotImplementedError(u'STEP: When I click on Beli')


@then(u'I should be redirected to checkouts page')
def step_impl(context):
    try:
        driver.find_element("css selector",'h2.n8k95w1._1fragema3.n8k95w3')
    except:
        raise NotImplementedError(u'STEP: Then I should be redirected to checkouts page')


@given(u'I am on the checkout page')
def step_impl(context):
    try:
        take_screenshot(driver)
        # driver.get("https://voila.id/checkouts/c/c8d5ca3f72ce06a5911422f13e4d9953/information?_ga=2.16386294.1789729160.1681838703-1173728324.1681838620")
    except:
        raise NotImplementedError(u'STEP: Given I am on the checkout page')


@when(u'I type Arief in Nama Depan field')
def step_impl(context):
    try:
        login_again = driver.find_element('css selector','a.s2kwpi1._1fragema3._1fragemah._1fragemap.s2kwpi2._1fragemaa')
        login_again.click()
        element_id_login_email(driver).send_keys(data_email())
        element_id_login_password(driver).send_keys(data_password())
        element_class_login_button(driver).click()
    except:
        print("Already logged in and not logged out in the middle")
    try:
        first_name = driver.find_element("id",'TextField1') 
        first_name.clear()
        first_name.send_keys(data_first_name())
    except:
        raise NotImplementedError(u'STEP: When I type Arief in Nama Depan field')



@when(u'I type Chaerudin in Nama Belakang field')
def step_impl(context):
    try:
        last_name = driver.find_element("id",'TextField2')
        last_name.clear()
        last_name.send_keys(data_last_name())
    except:
        raise NotImplementedError(u'STEP: When I type Chaerudin in Nama Belakang field')


@when(u'I type [Arief Chaerudin]-[Candidate QA] in Alamat field')
def step_impl(context):
    try:
        address = driver.find_element("id",'TextField3')
        address.clear()
        address.send_keys(data_address())
    except:
        raise NotImplementedError(u'STEP: When I type [Arief Chaerudin]-[Candidate QA] in Alamat field')


@when(u'I type [Arief Chaerudin]-[Candidate QA] in Kota Kecamatan field')
def step_impl(context):
    try:
        city_state = driver.find_element("id",'TextField5')
        city_state.clear()
        city_state.send_keys(data_address())
    except:
        raise NotImplementedError(u'I type [Arief Chaerudin]-[Candidate QA] in Kota Kecamatan field')


@when(u'I type 13950 in Kode Pos field')
def step_impl(context):
    try:
        zip_code_field = driver.find_element("id","TextField6") 
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code())
    except:
        raise NotImplementedError(u'I type 13950 in Kode Pos field')


@when(u'I click the dropdown and select Daerah Khusus Ibukota Jakarta')
def step_impl(context):
    # try:
    select_value = Select(driver.find_element("name","zone"))
    select_value.select_by_value(data_region())
    # except:
    #     raise NotImplementedError(u'I click the dropdown and select Daerah Khusus Ibukota Jakarta')


@when(u'I type 089672300149 in No Handphone field')
def step_impl(context):
    try:
        phone_number = driver.find_element("id","TextField7")
        phone_number.clear()
        phone_number.send_keys(data_phone_number())
    except:
        raise NotImplementedError(u'I type 089672300149 in No Handphone field')


@when(u'I click lanjut ke pengiriman')
def step_impl(context):
    try:
        driver.find_element("css selector",'button[type="submit"]').click()
    except:
        raise NotImplementedError(u'I click lanjut ke pengiriman')


@then(u'The Nama Depan textbox changed to Arief')
def step_impl(context):
    try:
        value_confirmation(driver,'id','TextField1',data_first_name())
    except:
        raise NotImplementedError(u'STEP: Then The Nama Depan textbox changed to Arief')


@then(u'The Nama Belakang textbox changed to Chaerudin')
def step_impl(context):
    try:
        value_confirmation(driver,'id','TextField2',data_last_name())
    except:
        raise NotImplementedError(u'STEP: Then The Nama Belakang textbox changed to Chaerudin')


@then(u'The Alamat textbox changed to [Arief Chaerudin]-[Candidate QA]')
def step_impl(context):
    try:
        value_confirmation(driver,'id','TextField3',data_address())
    except:
        raise NotImplementedError(u'STEP: Then The Alamat textbox changed to [Arief Chaerudin]-[Candidate QA]')


@then(u'The Kota Kecamatan textbox changed to [Arief Chaerudin]-[Candidate QA]')
def step_impl(context):
    # try:
    value_confirmation(driver,'id','TextField5',data_address())
    # except:
    #     raise NotImplementedError(u'STEP: Then The Kota Kecamatan textbox changed to [Arief Chaerudin]-[Candidate QA]')


@then(u'The Kode Pos textbox changed to 13950')
def step_impl(context):
    try:
        value_confirmation(driver,'id','TextField6',zip_code())
    except:
        raise NotImplementedError(u'STEP: Then The Kode Pos textbox changed to 13950')


@then(u'The Dropdown value changed to Daerah Khusus Ibukota Jakarta')
def step_impl(context):
    try:
        value_confirmation(driver,'name','zone',data_region())
    except:
        raise NotImplementedError(u'STEP: Then The Dropdown value changed to Daerah Khusus Ibukota Jakarta')


@then(u'The No Handphone textbox changed to 089672300149')
def step_impl(context):
    # try:0896-7230-0149
    phone_parse = data_phone_number()
    phone_parse = phone_parse[:4] + "-" + phone_parse[4:8] + "-" + phone_parse[8:]
    value_confirmation(driver,'id','TextField7',phone_parse)
    # except:
    #     raise NotImplementedError(u'STEP: Then The No Handphone textbox changed to 089672300149')


@then(u'Redirected to shipping page')
def step_impl(context):
    shipment_method = driver.find_element('css selector','section[aria-label="Metode pengiriman"]')
    if shipment_method !="":
        print(shipment_method)
    else:
        raise NotImplementedError(u'STEP: Then Redirected to shipping page')


@given(u'I am on the shipping page')
def step_impl(context):
    try:
        take_screenshot(driver)
    except:
        raise NotImplementedError(u'STEP: I am on the shipping page')

@when(u'I click radio button value JNT in metode pengiriman')
def step_impl(context):
    # try:
    shipment_radio = driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div/div[1]/section/div/div[2]/fieldset/div[2]/div[2]/label/div/div[2]/div[1]/p')
    shipment_radio.click() 
    # except:
    #     raise NotImplementedError(u'STEP: I click radio button value JNT in metode pengiriman')

@when(u'I click Lanjut ke Pembayaran')
def step_impl(context):
    try:
        driver.find_element("css selector",'button[type="submit"]').click()
    except:
        raise NotImplementedError(u'STEP: I click Lanjut ke Pembayaran')


@then(u'I saw the radio button value switched to JNT')
def step_impl(context):
    radio_button_JNT = driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div/div[1]/section/div/div[2]/fieldset/div[2]/div[2]/label/div/div[2]/div[1]/p')
    if radio_button_JNT.is_selected():
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Then I saw the radio button value switched to JNT')

@then(u'I get redirected to payment page')
def step_impl(context):
    payment_page = driver.find_element('css selector','section[aria-label="Pembayaran"]')
    if payment_page !="":
        print(payment_page)
    else:
        raise NotImplementedError(u'STEP: Then I get redirected to payment page')

@given(u'I am on the payment page')
def step_impl(context):
    try:
        take_screenshot(driver)
    except:
        raise NotImplementedError(u'STEP: Given I am on the payment page')


@when(u'I click the radio button value bank transfer')
def step_impl(context):
    try:
        driver.find_element('id','basic-customManualPayment-61481550008').click()
        total_price = driver.find_element('xpath','//*[@id="app"]/div/div/div/div[1]/div/aside/div[2]/div/div/div/section/div[2]/div[3]/div[2]/div/div/strong').get_attribute()
        total_price = re.sub("[^0-9]", "", total_price)
        context.total_price = total_price
    except:
        raise NotImplementedError(u'STEP: When I click the radio button value bank transfer')


@when(u'I click the Selesaikan Pesanan button')
def step_impl(context):
    try:
        driver.find_element("css selector",'button[type="submit"]').click()
    except:
        raise NotImplementedError(u'STEP: When I click the Selesaikan Pesanan button')


@then(u'I saw the radio button value switched to bank transfer')
def step_impl(context):
    try:
        radio_button_payment = driver.find_element('id','basic-customManualPayment-61481550008')
        if radio_button_payment.is_selected():
            take_screenshot(driver)
    except:    
        raise NotImplementedError(u'STEP: Then I saw the radio button value switched to bank transfer')

@then(u'I get redirected to thank you page with the right amount')
def step_impl(context):
    thank_you_page = driver.find_element('class name','thank-you__additional-content')
    final_total_price = driver.find_element('class name','payment-due__price skeleton-while-loading--lg')
    final_total_price.get_attribute()
    final_total_price = re.sub("[^0-9]", "", final_total_price)
    compare_total_price = context.total_price
    if thank_you_page != '' and compare_total_price == final_total_price:
        take_screenshot(driver)
    else:
        raise NotImplementedError(u'STEP: Then I get redirected to thank you page')