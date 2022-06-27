# go to a website and login in that page.and do all of this by using selenium

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

# frist name part
first_name = driver.find_element_by_name('fName')
first_name.send_keys('your_first_name')
first_name.send_keys(Keys.ENTER)

# enter last name
last_name = driver.find_element_by_name('lName')
last_name.send_keys('you_last_name')
last_name.send_keys(Keys.ENTER)

# enter email
email_address = driver.find_element_by_name('email')
email_address.send_keys('your_email')
email_address.send_keys(Keys.ENTER)

# driver.close()