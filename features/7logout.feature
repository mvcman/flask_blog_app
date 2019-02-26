# check logout functioanlity
Feature: Test Logout Functionality
    Scenario: User want to logout then he will click on logout button
        When user clicks on logout link
        Then User should contain a Login and register link!
