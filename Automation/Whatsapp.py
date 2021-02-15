from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
from time import sleep
browser = webdriver.Chrome(executable_path="C:\\Users\\Dell\\OneDrive\\Desktop\\chromedriver.exe")
browser.get("https://web.whatsapp.com/")
target = "'PYTHON DAILY RY 27/10/20'"
string1 = sys.argv[1]
#x_arg = '//span[contains(@title=target)]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/div[1]/span' + target + ')]'
selector = "//*[contains(@title=target]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span"
wait = WebDriverWait(browser, 600)
group_title = wait.until(ec.presence_of_all_elements_located((By.XPATH, selector)))
print(group_title)
sleep(5)
group_title.click()
message = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
count = int(input("count:"))
for i in range(count):
    message.send_keys(string1)
    sendbutton = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')[0]
    sendbutton.click()
browser.close()