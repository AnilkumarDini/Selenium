from selenium import webdriver
# from selenium.webdriver.support.select import Select

# Creating a webdriver instance by specifying path to chrome driver
from selenium.webdriver import Keys

driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com")

# waiting for the page to load
# time.sleep(5)
driver.implicitly_wait(10)
# locate email form by_class_name
username = driver.find_element("id", "session_key")

# send_keys() to simulate keystrokes
username.send_keys('user_email')

# locate password form by_class_name
password = driver.find_element("id", "session_password")

# send_keys() to simulate keystrokes
password.send_keys('user_password')

# following code opens job feed and search for "data entry " jobs in kerala

driver.get("https://linkedin.com/jobs/")
username = driver.find_element("name", "location")
username.clear()
username.send_keys("kerala")
keyword = driver.find_element("name", "keywords")
keyword.clear()
keyword.send_keys("data entry")
keyword.send_keys(Keys.ENTER)



