Feature: Test Scenarios for verification of the titles
    Scenario: User able to open and verify the titles
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open
    When Click on User Guide option
    Then Verify the right page user_guide opens and contains user-guide
    Then Verify all lesson videos contain titles
