from selenium import webdriver 
#import Keys
from selenium.webdriver.common.keys import Keys
#import time
from time import sleep
browser = webdriver.Chrome(executable_path="C:\\Users\\Dell\\OneDrive\\Desktop\\chromedriver.exe")
website = "https://www.youtube.com"
browser.maximize_window()
browser.get(website)
sleep(5)
search_box = browser.find_element_by_xpath('//input[@id="search"]')
search_box.send_keys(f'baps  {Keys.ENTER}')
song = browser.find_element_by_partial_link_text('Pramukh Swami Maharaj: Transforming ').click()
