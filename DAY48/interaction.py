# Challenge 2

from selenium import webdriver


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://en.wikipedia.org/wiki/Main_Page')


numberof_articles_xpath = '//*[@id="articlecount"]/a[1]'
number_of_articles = driver.find_element_by_xpath(numberof_articles_xpath).text
print(number_of_articles)





driver.quit()