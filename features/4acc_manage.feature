Feature: Test account-management Functionality
    Scenario: when user login user will get a account link to manage account details
        When user click on account link
        Then User should contain a page with account details of user!

    Scenario: when user wants to update username and if it is already exist then throw error
        When user click on account link and try to update username
        Then User should contain a error page with error "username already taken"

    Scenario: when user wants to update email and if it is already exist then throw error
        When user click on account link and try to update email
        Then User should contain a error page with error "Email already taken"
