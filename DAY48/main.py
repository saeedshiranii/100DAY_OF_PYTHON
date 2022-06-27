# main project : a bot to play cookikilicker
from selenium import webdriver
import time



# create a webdriver 
driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")


# find Main cookie
BIG_COOKIE = driver.find_element_by_id("cookie")
id_list = ["buyElder Pledge", "buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma", "buyCursor"]

# create a buffer time 
one_min = time.time() + 5
total_time = 0


# click on cookie and stuff of store
while total_time < 300:
    
    BIG_COOKIE.click()


    if one_min <= time.time():

        for item in id_list:

            try:
                i = driver.find_element_by_id(item)
                i.click()

            except: 
                continue

        one_min = time.time() + 5
        total_time += 5


coocki_per_sce = driver.find_element_by_id("money").text

print(F"{coocki_per_sce} cookies per sec")
driver.close()