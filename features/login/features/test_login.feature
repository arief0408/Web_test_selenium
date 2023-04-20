Feature: Login as ariefchaerudin
    As a user
    Who have an account
    I want to Login
    And browse for a product
    And finally bought it

Scenario: Successful login
    Given I am on the login page
    When I enter my email in email field and password in password field
    And I click the login button
    Then I Should be redirected to voila.id/account

Scenario: Select a product from collections
    Given I am on the homepage of voila.id
    When I clicked on one of the product listed
    Then It redirect to the page of the product

Scenario: Bought the selected product
    Given I am on the page of selected product
    When I click + Keranjang
    Then I should have an popped up windows of Produk berhasil ditambah!

Scenario: I checked all the details and ready to buy
    Given I am on the popped up page of Produk berhasil ditambah!
    When I click on Beli
    Then I should be redirected to checkouts page
Scenario: Fill all the form in checkout page and click submit button so it be redirected to shipping page
    Given I am on the checkout page
    When I type Arief in Nama Depan field
    And I type Chaerudin in Nama Belakang field
    And I type [Arief Chaerudin]-[Candidate QA] in Alamat field
    And I type [Arief Chaerudin]-[Candidate QA] in Kota Kecamatan field
    And I type 13950 in Kode Pos field
    And I click the dropdown and select Daerah Khusus Ibukota Jakarta
    And I type 089672300149 in No Handphone field
    And I click lanjut ke pengiriman
    Then The Nama Depan textbox changed to Arief
    And The Nama Belakang textbox changed to Chaerudin
    And The Alamat textbox changed to [Arief Chaerudin]-[Candidate QA]
    And The Kota Kecamatan textbox changed to [Arief Chaerudin]-[Candidate QA]
    And The Kode Pos textbox changed to 13950
    And The Dropdown value changed to Daerah Khusus Ibukota Jakarta
    And The No Handphone textbox changed to 089672300149
    And Redirected to shipping page

Scenario: I want to select metode pengiriman
    Given I am on the shipping page
    When I click radio button value JNT in metode pengiriman
    And I click Lanjut ke Pembayaran
    Then I saw the radio button value switched to JNT
    And I get redirected to payment page


Scenario: Select bank transfer as payment method
    Given I am on the payment page
    When I click the radio button value bank transfer
    And I click the Selesaikan Pesanan button
    Then I saw the radio button value switched to bank transfer
    And I get redirected to thank you page with the right amount