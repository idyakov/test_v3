Feature: Test Scenarios for the User that can open Whatsapp and Telegram communities
    All tests flow through the settings menu page
    Background:
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open

    Scenario: User can access Whatsapp and Telegram communities
    When Click on support option
    When Switch to the new tab
    When Verify the right tab page opens and contains api.whatsapp.com
    Then Go back
    Then Click on news option
    When Verify the right tab telegram page opens and contains t.me