Feature: Project functionality execution
  Scenario: User able add a project via the settings menu
    Given Open soft.reelly main page
    And Login to the page
    And Click on continue button
    And Click on settings open__
    And Click on Add a project
    And Add test information to the input fields
    And Verify the right information is present for rabochiy_krestyanin@gmail.com
    Then Verify _Send an application_ button is available and clickable
