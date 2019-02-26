from behave import *
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("/home/mandar/Downloads/python-projects/flask-blog-post/chromedriver")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://127.0.0.1:5000")

# TO check Register functionality
@given(u'user navigates to http://localhost:5000 and click on register link')
def step_impl(context):
    # driver.implicitly_wait(30)
    # driver.maximize_window()
    # driver.get("http://127.0.0.1:5000")
    driver.get("http://127.0.0.1:5000")

# when user enters wrong email
@when(u'user click on register link and enter username "mandar2" and enter mailid as "mandargmailcom" and enter password as "mandar1712" and enter confirm_password as "mandar1712"')
def step_impl(context):
    search_field = driver.find_element_by_name("Register")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    assert search_field.text == "Register"
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("username").send_keys("mandar2")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("email").send_keys("mandagmailcom")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("confirm_password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(100000)

@then(u'User should get error message "Invalid email address"')
def step_impl(context):
    l_link = driver.find_element_by_name("if-email").text
    print(l_link)
    assert l_link == "Invalid email address."

# when user enter password and password should not match
@when(u'user click on register link and enter username "mandar2" and enter mailid as "mandar2@gmail.com" and enter password as "mandar1712" and enter confirm_password as "mandar17"')
def step_impl(context):
    search_field = driver.find_element_by_name("Register")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    assert search_field.text == "Register"
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("username").send_keys("mandar2")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("email").send_keys("mandagmailcom")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("confirm_password").send_keys("mandar17")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(100000)

@then(u'User should get error message "Field must be equal to password"')
def step_impl(context):
    l_link = driver.find_element_by_name("if-con-password").text
    print(l_link)
    assert l_link == "Field must be equal to password."

# If user enters username which is already exist then he will get error msg "username already taken"
@when(u'user click on register link and enter username "mandar2" and enter mailid as "mandar2@gmail.com" and enter password as "mandar1712" and enter confirm_password as "mandar1712"')
def step_impl(context):
    search_field = driver.find_element_by_name("Register")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    assert search_field.text == "Register"
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("username").send_keys("mandar2")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("email").send_keys("mandar2@gmail.com")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("confirm_password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'User should get error message "That username is taken.Please choose a different one."')
def step_impl(context):
    l_link = driver.find_element_by_name("if-username").text
    print(l_link)
    assert l_link == "That username is taken. Please choose a different one."

# Login test
# If user enters worng mailid then user will get error "Invalid email Id"
@when(u'user logs in using Username as "mandar2@gm.com" and Password "mandar1712"')
def step_impl(context):
    search_field = driver.find_element_by_name("Login")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("email").send_keys("mandar.com")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(5000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')

@then(u'page should get error message "Invalid email address"')
def step_impl(context):
    l_link = driver.find_element_by_name("email-err").text
    print(l_link)
    assert l_link == "Invalid email address."

# If user enters worng password then user will get error "Login Unsuccessful"
@when(u'user logs in using Username as "mandar2@gmail.com" and Password "mandar17"')
def step_impl(context):
    search_field = driver.find_element_by_name("Login")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("email").send_keys("mandar2@gmail.com")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar17")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(5000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'page should get error message "Login Unsuccessful. Please check email and password"')
def step_impl(context):
    l_link = driver.find_element_by_class_name("alert-danger").text
    print(l_link)
    assert l_link == "Login Unsuccessful. Please check email and password"

# When user enters correct email and password
@when(u'user logs in using Username as "mandar2@gmail.com" and Password "mandar1712"')
def step_impl(context):
    search_field = driver.find_element_by_name("Login")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("email").send_keys("mandar2@gmail.com")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(5000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'page should contain Logout link!')
def step_impl(context):
    l_link = driver.find_element_by_name("Logout").text
    print(l_link)
    assert l_link == "Logout"

# About link
@when(u'user click on About link')
def step_impl(context):
    driver.find_element_by_name("About").click()
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'User should contain a About page blank!')
def step_impl(context):
    l_link = driver.find_element_by_name("Logout").text
    assert l_link == "Logout"
    # driver.quit()

# Account details
@when(u'user click on account link')
def step_impl(context):
    driver.find_element_by_name("Account").click()
    driver.implicitly_wait(100000)


@then(u'User should contain a page with account details of user!')
def step_impl(context):
    l_link = driver.find_element_by_tag_name("h2").text
    assert l_link == "mandar2"
    l_link1 = driver.find_element_by_tag_name("p").text
    assert l_link1 == "mandar2@gmail.com"
    # driver.quit()

# Account - when user wants to update username and if it is already exist then throw error.
@when(u'user click on account link and try to update username')
def step_impl(context):
    driver.find_element_by_name("Account").click()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("mandar")
    driver.find_element_by_name("submit").submit()
    driver.implicitly_wait(100000)


@then(u'User should contain a error page with error "username already taken"')
def step_impl(context):
    l_link = driver.find_element_by_name("acc-username").text
    print(l_link)
    assert l_link == "That username is taken. Please choose a different one."
    # driver.quit()

# Account - when user wants to update email and if it is already exist then throw error.
@when(u'user click on account link and try to update email')
def step_impl(context):
    driver.find_element_by_name("Account").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("mandar@gmail.com")
    driver.find_element_by_name("submit").submit()
    driver.implicitly_wait(100000)


@then(u'User should contain a error page with error "Email already taken"')
def step_impl(context):
    l_link = driver.find_element_by_name("acc-email").text
    print(l_link)
    assert l_link == "That email is taken. Please choose a different one."
    # driver.quit()

# Add new post
@when(u'user click on newpost link and enter title "mypost4" and enter content as "Python virtual environment" and submit')
def step_impl(context):
    search_field = driver.find_element_by_name("Newpost")
    # enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    # assert search_field.text == "NewPost"
    search_field.click()
    driver.implicitly_wait(5000)
    driver.find_element_by_name("title").send_keys("mypost4")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("content").send_keys("Python virtual environment")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'new post will be added with title {"mypost4"}')
def step_impl(context):
    l_link1 = driver.find_element_by_tag_name("h2").text
    print(l_link1)
    assert l_link1 == "mypost4"
    # driver.quit()

# Home link
@when(u'user click on Home link')
def step_impl(context):
    driver.find_element_by_name("Home").click()
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'User should contain a page with last Post of last user!')
def step_impl(context):
    l_link1 = driver.find_element_by_tag_name("h2").text
    print(l_link1)
    assert l_link1 == "mypost4"
    # driver.quit()

# user wants to update or delete his/her post
@when(u'user click on Home link and user wants to update his/her post')
def step_impl(context):
    driver.find_element_by_name("Home").click()
    l_link = driver.find_element_by_tag_name("h2").text
    print(l_link)
    assert l_link == "mypost4"
    driver.find_element_by_tag_name("h2").find_element_by_tag_name("a").click()
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'User should contain a page with two buttons "Update" or "Delete"')
def step_impl(context):
    heading = driver.find_element_by_class_name("mr-2").text
    assert heading == "mandar2"
    l_link1 = driver.find_element_by_name("Delete").text
    l_link2 = driver.find_element_by_name("Update").text
    assert l_link1 == "Delete"
    assert l_link2 == "Update"

# when user clicks on update button he can update post title or content
@when(u'user click on update link and user update his/her post')
def step_impl(context):
    driver.find_element_by_name("Update").click()
    driver.implicitly_wait(100000)
    # raise NotImplementedError(u'STEP: When user logs in using Username as "mandar@gmail.com" and Password "mandar1712"')


@then(u'User should contain a page with post button and title as update post')
def step_impl(context):
    heading = driver.find_element_by_tag_name("heading").text
    assert heading == "Update Post"

# Logout
@when(u'user clicks on logout link')
def step_impl(context):
    driver.find_element_by_name("Logout").click()# enter search keyword and submit
    driver.implicitly_wait(100000)


@then(u'User should contain a Login and register link!')
def step_impl(context):
    l_link = driver.find_element_by_name("Login").text
    assert l_link == "Login"

# Reset Password
@when(u'user clicks on forgot_password link')
def step_impl(context):
    driver.find_element_by_name("Login").click()
    driver.find_element_by_name("Forgot-Pass").click()
    driver.implicitly_wait(100000)

@then(u'User should get reset password form')
def step_impl(context):
    l_link = driver.find_element_by_tag_name("legend").text
    print(l_link)
    assert l_link == "Reset Password"

# Reset Password- get reset password link
@when(u'user enters email ID to get link of password reset when he enter mail ID and submit reset password button')
def step_impl(context):
    driver.find_element_by_name("email").send_keys("waghemandar1712@gmail.com")
    driver.find_element_by_name("submit").submit()
    driver.implicitly_wait(100000)

@then(u'User should get message "An email has been sent with instructions to reset your password!"')
def step_impl(context):
    l_link = driver.find_element_by_class_name("alert-info").text
    print(l_link)
    assert l_link == "An email has been sent with instructions to reset your password."
    # driver.quit()
