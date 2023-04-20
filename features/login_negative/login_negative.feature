Feature: Login test functionality
As a user who have registered
I need to login to the website
So that i can use the website

  Scenario: Login Successful with login button
  Given I am on the login page
  When I enter my Email and Password
  And I click the login button
  Then I should be redirected to account page
  
  Scenario: Login Successful with ENTER
  Given I am on the login page
  When I enter my Email and Password
  And I press enter on my keyboard
  Then I should be redirected to account page
  
  Scenario: Incorrect Email
  Given I am on the login page
  When I enter the wrong Email but correct Password
  And I press enter on my keyboard
  Then I should seen an error message

  Scenario: Incorrect Password
  Given I am on the login page
  When I enter the correct Email but wrong Password
  And I press enter on my keyboard
  Then I should seen an error message
  
  Scenario: Incorrect Password 5 times
  Given I am on the login page
  When I enter the correct Email but wrong Password for 5 times
  And I press enter on my keyboard
  Then I should seen an error message of account locked