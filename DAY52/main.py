from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

INSTA_ENDPOINT = "https://www.instagram.com/accounts/login/" # login address at instagram website
TARGET_ACCOUNT = "benstogram"  # A moterfucker well known chef
INSTA_EMAIL = ""
INSTA_PASS = ""



class InstagramFollower():
    def __init__(self):
    
        self.browser = webdriver.Chrome()
        self.browser.get(INSTA_ENDPOINT)

    def login(self):
        # enter the email
        time.sleep(10)
        usr = self.browser.find_element(by=By.XPATH, value= '//*[@id="loginForm"]/div/div[1]/div/label/input')
        usr.send_keys(INSTA_EMAIL) 

        # enter the password
        time.sleep(13)
        pas = self.browser.find_element(by=By.XPATH, value= '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pas.send_keys(INSTA_PASS)


        # hit the login 
        time.sleep(9)
        login_button = self.browser.find_element(by=By.XPATH, value="//button[@type = 'submit']") 
        login_button.send_keys(Keys.ENTER)


        # hit the not now
        time.sleep(9)
        not_now = self.browser.find_element(by=By.XPATH, value="//button[text()= 'Not Now']") 
        not_now.send_keys(Keys.ENTER)
        self.browser.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        time.sleep(5)


    def target_finder(self):
        # find target account at insta
        """
        time.sleep(10)
        search_box = self.browser.find_element(by=By.XPATH, value="//input[@type = 'text']")
        search_box.send_keys(TARGET_ACCOUNT)"""
        
        time.sleep(5)
        self.browser.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers/")
        time.sleep(5)


    def follower(self):
        all_buttons = self.browser.find_elements(by=By.XPATH, value="//button[@type= 'button']")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
               # cancel_button = self.browser.find_element(by=By.CLASS_NAME, value='_aacl _aaco _aacw _aad6 _aade"')
                #cancel_button.click()  
                pass                             

    
w = InstagramFollower()
w.login()
w.target_finder()
w.follower()
