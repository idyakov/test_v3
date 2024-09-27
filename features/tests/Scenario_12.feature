Feature: Test Scenarios for the elements number verification
    All tests flow through the settings menu page
    Background:
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open

    Scenario: User can verify the number of the options
    When Verify the right page opens and contains settings
    When Verify there are 12 options for the settings
    When Verify “connect the company” button is available