Feature: Test Register-User functionality
    Scenario: when user enter url he will get a register link to register user
       Given user navigates to http://localhost:5000 and click on register link
            When user click on register link and enter username "mandar2" and enter mailid as "mandargmailcom" and enter password as "mandar1712" and enter confirm_password as "mandar1712"
            Then User should get error message "Invalid email address"

    Scenario: when user enter url he will get a register link to register user
             When user click on register link and enter username "mandar2" and enter mailid as "mandar2@gmail.com" and enter password as "mandar1712" and enter confirm_password as "mandar17"
             Then User should get error message "Field must be equal to password"

    Scenario: If user enters username which is already exist then he will get error msg "username already taken"
              When user click on register link and enter username "mandar2" and enter mailid as "mandar2@gmail.com" and enter password as "mandar1712" and enter confirm_password as "mandar1712"
              Then User should get error message "That username is taken.Please choose a different one."
