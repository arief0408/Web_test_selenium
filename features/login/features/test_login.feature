Feature: Login as ariefchaerudin
    As a user
    Who have an account
    I want to Login

Scenario: Successful login
    Given I am on the login page
    When I enter my email in email field and password in password field
    And I click the login button
    Then I Successfully login