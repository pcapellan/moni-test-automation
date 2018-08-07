Feature: Login

  Background:
    Given I am on the Automation Practice page

  @LOGIN
  Scenario: Login with valid credentials
    Given I go to the Sign in page
    When I insert valid credentials
    And I click on "Sign in" button
    Then I see "My account - My Store" page
    And I see "Juan Perez" user logged