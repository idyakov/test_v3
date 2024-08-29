Feature: Test Scenarios for the password change functional verification
    Scenario: User able to open password related page and change
    Given Open the main_page
    And Log in to the main page
    When Click on continue button
    When Click on settings open
    When Click on change password
    Then Verify the right page "set-new-password" opens and contains set-new-password
    Then Add some test password to the input fields
    Then Verify the “Change password” button is available
