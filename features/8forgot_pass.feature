Feature: Forgot Password
    Scenario: User want to login but user forgot the password
        When user clicks on forgot_password link
        Then User should get reset password form

    Scenario: User want to reset password
        When user enters email ID to get link of password reset when he enter mail ID and submit reset password button
        Then User should get message "An email has been sent with instructions to reset your password!"
