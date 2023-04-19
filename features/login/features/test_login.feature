Feature: Login as ariefchaerudin
    As a user
    Who have an account
    I want to Login
    And browse for a product
    And finally bought it

# Scenario: Successful login
#     Given I am on the login page
#     When I enter my email in email field and password in password field
#     And I click the login button
#     Then I Should be redirected to voila.id/account

# Scenario: Select a product from collections
#     Given I am on the homepage of voila.id
#     When I clicked on one of the product listed
#     Then It redirect to the page of the product

# Scenario: Bought the selected product
#     Given I am on the page of selected product
#     When I click + Keranjang
#     Then I should have an popped up windows of Produk berhasil ditambah!

# Scenario: I checked all the details and ready to buy
#     Given I am on the popped up page of Produk berhasil ditambah!
#     When I click on Beli
#     Then I should be redirected to checkouts page

Scenario: I want to type text in field Nama Depan
    Given I am on the checkout page
    When I type Arief in Nama Depan field
    Then I saw the field text changed to Arief

Scenario: I want to type text in field Nama Belakang
    Given I am on the checkout page
    When I type Chaerudin in Nama Belakang field
    Then I saw the field text changed to Chaerudin

Scenario: I want to type text in field Alamat
    Given I am on the checkout page
    When I type [Arief Chaerudin]-[Candidate QA] in Alamat field
    Then I saw the field text changed to [Arief Chaerudin]-[Candidate QA]

Scenario: I want to type text in field Kota dan kecamatan
    Given I am on the checkout page
    When I type [Arief Chaerudin]-[Candidate QA] in Alamat field
    Then I saw the field text changed to [Arief Chaerudin]-[Candidate QA]

Scenario: I want to type text in field Kode Pos
    Given I am on the checkout page
    When I type 13950 in Kode Pos field
    Then I saw the field text changed to 13950

Scenario: I want to select jakarta from the provinsi drop down button
    Given I am on the checkout page
    When I click the dropdown and select Daerah Khusus Ibukota Jakarta
    Then I saw the dropdown value changed to Daerah Khusus Ibukota Jakarta

Scenario: I want to type text in field No Handphone
    Given I am on the checkout page
    When I type 089672300149 in No Handphone field
    Then I saw the field text changed to 089672300149

Scenario: I want to proceed the form of checkout
    Given I am on the checkout page with all the form filled
    When I click lanjut ke pengiriman
    Then I get redirected to shipping page

Scenario: I want to select metode pengiriman
    Given I am on the shipping page
    When I click radio button value JNT in metode pengiriman
    Then I saw the radio button value switched to JNT

Scenario: I want to proceed to payment
    Given I am on the shipping page
    When I click Lanjut ke Pembayaran
    Then I get redirected to payment page

Scenario: Select bank transfer as payment method
    Given I am on the payment page
    When I click the radio button value bank transfer
    Then I saw the radio button value switched to bank transfer

Scenario: Submit the form of payment by clicking selesaikan pesanan
    Given i am on the payment page
    When I click the Selesaikan Pesanan button
    Then I get redirected to thank you page
