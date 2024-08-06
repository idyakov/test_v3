Feature: Test Scenarios for open the community page functionality
    Scenario: User able to open and verify the community page
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open
    When Click on Community option
    Then Verify the right_page opens and contains community
    Then Verify “Telegram_english_chat” button is available and clickable
    Then Verify “Telegram_russian_chat” button is available and clickable
    Then Verify “Contact support” button is available and clickable




