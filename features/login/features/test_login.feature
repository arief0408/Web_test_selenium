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