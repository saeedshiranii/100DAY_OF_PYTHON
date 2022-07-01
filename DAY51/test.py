
from selenium.webdriver.common.by import By
from selenium import webdriver

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "kiramtoinmamlekat2@gmail.com"
TWITTER_PASSWORD = "internettestbot"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.get("https://www.speedtest.net/")
        self.find_element(by=By.CLASS_NAME, value="start-text").click()
        self.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text


    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()