Feature: Test Login Functionality
    Scenario: User clicks on login button and enter wrong email address
        When user logs in using Username as "mandar2@gm.com" and Password "mandar1712"
        Then page should get error message "Invalid email address"
    Scenario: User clicks on login button and enter wrong password
      	When user logs in using Username as "mandar2@gmail.com" and Password "mandar17"
      	Then page should get error message "Login Unsuccessful. Please check email and password"
    Scenario: User clicks on login button
      	When user logs in using Username as "mandar2@gmail.com" and Password "mandar1712"
      	Then page should contain Logout link!
