# a project which get a speedtest of your interrnet connection and tweet it if that is low

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


# The upload and download speed mentioned in the contract
PROMISED_DOWN = 200
PROMISED_UP = 50

# email and pass of bot twitter account
TWITTER_EMAIL = "kiramtoinmamlekat2@gmail.com"
TWITTER_PASSWORD = "kirtotwitter"


# a class for create several web driver in separate pages
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0


    # get internet speed
    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        time.sleep(90) # Low internet speed
        self.down = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text



    # login and tweet
    def tweet_at_provider(self):
        print("88")
        self.driver.get("https://twitter.com/")
        print("888")
        time.sleep(40)
        
        # click on sing in button
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()

        # enter email
        time.sleep(40)
        email_box = self.driver.find_element(by=By.NAME, value='text')
        email_box.send_keys(TWITTER_EMAIL)

        # click on next 
        time.sleep(30)             
        self.driver.find_element_by_xpath("//*[contains(text(), 'Next')]").click()



        try:
            time.sleep(30)
            usrbox = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')   
            usrbox.send_keys("internettestbot")        
            usrbox.send_keys(Keys.ENTER)    

        except:
            pass

        try:
            time.sleep(30)
            pass_box = self.driver.find_element(by=By.XPATH, value="//input[@type='password']")
            pass_box.send_keys(TWITTER_PASSWORD)
            pass_box.send_keys(Keys.ENTER)

        except:
            pass


        # send twitte
        time.sleep(5)
        tweet_compose_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        tweet_compose = self.driver.find_element_by_xpath(tweet_compose_xpath)

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        tweet_button = self.driver.find_element_by_xpath(tweet_button_xpath)
        tweet_button.click()


# now start measurement
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

print(bot.up, bot.down)

if float(bot.down) < PROMISED_DOWN or float(bot.up) > PROMISED_UP:
    
    bot.tweet_at_provider()



