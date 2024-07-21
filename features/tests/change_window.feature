Feature: Test Scenarios for Search functionality of soft.reelly page

  Scenario: User login main page and verify switch page functionality
    Given Open soft.reelly main page
    And Login to the main page
    And Click on continue button__
    And Store original window page
    And Click on “Connect the company” button
    And Switch to new window page
    And Verify the right tab open page
    And Close the current main page and switch back

