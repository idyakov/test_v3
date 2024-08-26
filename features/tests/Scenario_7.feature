Feature: Test Scenarios for open the Contact_us page functionality
    Scenario: User able to open and verify the Contact page
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open
    When Click on Contact us option
    Then Verify the right page opens and contains contact-us
    Then Verify there are at least 4 social media icons
    Then Verify “Connect the company” button is available and clickable




