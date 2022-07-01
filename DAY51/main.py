# a project which get a speedtest of your interrnet connection and tweet it if that is low

from selenium.webdriver.common.by import By
from selenium import webdriver
import time


# internet speed of contract
DOWNLOAD_SPEED_CONTRACT = 1000000000
UPLOAD_SPEED_CONTRACT = 10000000
TWITTER_EMAIL = "kiramtoinmamlekat2@gmail.com"
TWITTER_PASS = "internettestbot"



driver = webdriver.Chrome()
driver.get("https://www.speedtest.net/")

# click on Go button
driver.find_element(by=By.CLASS_NAME, value="start-text").click()

# give 1 min time to programme to test the internet speed
time.sleep(60)

# get data of internet speed
download_speed = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
upload_speed = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

print(download_speed)
print(upload_speed)


# Now we have speed of internet we should check speed of internet with speed of our Contract
if float(download_speed) < DOWNLOAD_SPEED_CONTRACT or float(upload_speed) < UPLOAD_SPEED_CONTRACT:

    driver.get("https://twitter.com/home?lang=en")
    #login_box_twitter = driver.find_element(by=By.CLASS_NAME, value="css-1dbjc4n r-1ets6dv r-z2wwpe r-rs99b7 r-18u37iz")
    #login_box_twitter.send_keys(TWITTER_EMAIL)

    email_element = driver.find_element_by_name('session[username_or_email]')

    # PasswordElement = driver.find_element_by_name('session[password]')

    email_element.send_keys(TWITTER_EMAIL)

    # PasswordElement.send_keys('password_goes_here')



