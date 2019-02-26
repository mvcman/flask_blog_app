import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of IEDriverServer
# dir = os.path.dirname("/home/mandar/Download")
# chrome_driver_path = dir + "/chromedriver"

# create a new Internet Explorer session
driver = webdriver.Chrome("/home/mandar/Downloads/python-projects/flask-blog-post/chromedriver")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://127.0.0.1:5000")

# Navigate to the application home page
def test_registration():
    search_field = driver.find_element_by_name("Register")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.click()
    driver.implicitly_wait(2500)
    driver.find_element_by_name("username").send_keys("mandarwaghe")
    driver.find_element_by_name("email").send_keys("waghemandar1712@gmail.com")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(5000)
    driver.find_element_by_name("confirm_password").send_keys("mandar1712")
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(2500)

# get the search textbox
def test_login():
    search_field = driver.find_element_by_name("Login")# enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.click()
    print(search_field)
    driver.implicitly_wait(5000)
    driver.find_element_by_name("email").send_keys("mandar@gmail.com")
    driver.implicitly_wait(3500)
    driver.find_element_by_name("password").send_keys("mandar1712")
    driver.implicitly_wait(2500)
    driver.find_element_by_name("submit").submit()
    # lists= driver.find_elements_by_class_name("r")
    driver.implicitly_wait(5000)
    # driver.quit()

def test_add_post():
    driver.find_element_by_name("Newpost").click()
    driver.implicitly_wait(10000)
    driver.find_element_by_name("title").send_keys("My Title 4")
    driver.implicitly_wait(10000)
    driver.find_element_by_name("content").send_keys("My fourth post is about introsuction to virtual environment")
    driver.implicitly_wait(10000)
    driver.find_element_by_name("submit").submit()
    driver.implicitly_wait(10000)


def test_account():
    driver.find_element_by_name("Account").click()


def test_logout():
    search_field = driver.find_element_by_name("Logout")
    search_field.click()
# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
def test_forgot_password():
    driver.find_element_by_name("Login").click()
    search_field = driver.find_element_by_name("Forgot-Pass")
    search_field.click()
    driver.find_element_by_name("email").send_keys("waghemandar1712@gmail.com")
    driver.find_element_by_name("submit").submit()
    # driver.quit()

# def test_pass_confirmation():
#     driver.get("https://mail.google.com/mail/u/0/#inbox")

# get the number of elements found
# print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

# i=0
# for listitem in lists:
#    print (listitem.get_attribute("innerHTML"))
#    i=i+1
#    if(i>10):
#       break

# close the browser window
