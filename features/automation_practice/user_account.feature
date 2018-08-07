Feature: User account

  Background:
    Given I am on the Automation Practice page

  @USER_ACCOUNT
  Scenario: Create an account with valid values
    Given I go to the Sign in page
    When I insert valid "Email address" in "CREATE AN ACCOUNT" section
    And I click on "Create an account" button
    Then I see the "CREATE AN ACCOUNT" form to complete
    When I insert valid "First name" in "YOUR PERSONAL INFORMATION" section
    And I insert valid "Last name" in "YOUR PERSONAL INFORMATION" section
    And I insert valid "Password" in "YOUR PERSONAL INFORMATION" section
    And I insert valid "Address" in "YOUR ADDRESS" section
    And I insert valid "City" in "YOUR ADDRESS" section
    And I select an state
    And I insert valid "Zip/Postal Code" in "YOUR ADDRESS" section
    And I insert valid "Mobile phone" in "YOUR ADDRESS" section
    And I insert valid "Address alias" in "YOUR ADDRESS" section
    And I click on "Register" button
    Then I see "My account - My Store" page
    And I see "Juan Perez" user logged