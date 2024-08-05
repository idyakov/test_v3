Feature: Test Scenarios for open the community page functionality
    Scenario: can open the community page
    When Open the main_page
    When Log in to the main page
    When Click on_continue button
    When Click on settings open
    When Click on Community option
    Then Verify the right_page opens and contains community
    Then Verify “Contact support” button is available and clickable




