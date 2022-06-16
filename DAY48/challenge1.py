from selenium import webdriver


driver = webdriver.Chrome("/usr/local/bin/chromedriver")


driver.get('https://www.python.org/')


upcoming_events_xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/h2'
upcoming = driver.find_element_by_xpath(upcoming_events_xpath).text


events_time = driver.find_elements_by_css_selector(".event-widget time")
events_name = driver.find_elements_by_css_selector(".event-widget li a")

events_dict = {}
for i in range(len(events_time)):

    events_dict[i]= {
        "time": events_time[i].text,
        "name": events_name[i].text, }


print(events_dict)
driver.quit()