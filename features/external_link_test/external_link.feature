Feature: External link check
  I want to make sure
  That every link of social media or appstore is working well
  Also check whether it went to the correct page

Scenario Outline: Click on "<external_link>"
  Given I am on the homepage
  When I click on "<external_link>"
  Then I should be redirected to page associated with "<external_link>"

  Examples:
    | external_link |
    | appstore      |
    | playstore     |
    | facebook      |
    | instagram     |
    | tiktok        |
    | youtube       |
