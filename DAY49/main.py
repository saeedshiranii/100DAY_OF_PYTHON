# an automatic linkedin applyer for job using python and selenium
# to work with this program you should already have an account

from selenium import webdriver

# go on a search page of linkdin  
driver = webdriver.Chrome()
driver.get(" ")

# email and password off your linkdin
# remember its better to did not be loged in linkdin in your browser
LINKDIN_PASS = " "
LINKDIN_EMAIL = " "



# and now click on sign in button
driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]").click()

# input username and pass
usr = driver.find_element_by_id("username")
usr.send_keys(LINKDIN_EMAIL)

pass_word = driver.find_element_by_id("password")
pass_word.send_keys(LINKDIN_PASS)

# hit sing in button again
driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
