Feature: Test Scenarios for the User that can open Subscription & payments page
    All tests flow through the settings menu page
    Background:
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open

    Scenario: User can open Subscription & payments page
    When Click on Subscription & payments option
    Then Verify the right page Subscription & payments opens and contains subscription
    When Verify the “Subscription & payments” title is visible
    Then Verify “back” and “upgrade plan” buttons are available

