Feature: Order

  Background:
    Given I am on the Automation Practice page


  @ORDER
  Scenario: Order express
    Given I am logged with valid user
    And I go to "WOMEN" category
    When I select the clothes "Faded Short Sleeve T-shirts"
    And I press "Add to Cart"
    And I press "Proceed to checkout"
    And I check Summary and proceed to checkout
    And I check the delivery address data and proceed to checkout
    And I accept the terms of service and proceed to checkout
    And I select the payment method "bank wire"
    And I confirm my order
    Then I see the "Your order on My Store is complete." message