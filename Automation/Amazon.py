from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\OneDrive\\Desktop\\chromedriver.exe")
products = []
prices = []

driver.get("https://www.amazon.in/s?k=Mobile&ref=nb_sb_noss_2")
content = driver.page_source
par_con = BeautifulSoup(content, "html.parser")
for a in par_con.findAll('a', href = {True}, attrs={'class':'a-link-normal a-text-normal'}):
    name = a.find('span', attrs = {'class':'//span[contains(@class="a-size-medium a-color-base a-text-normal")]'})
    price= a.find('span', attrs = {'class':'//span[contains(@class="a-price-whole")]'})
    products.append(name)
    prices.append(price)
print(products)
print(prices)
df = pd.DataFrame({"Products":products,"Prices":prices})
df.to_excel("C:\\Users\\Dell\\OneDrive\\Desktop\\Amazon_list.xlsx", index=False, encoding="UTF-8")


#//span[contains(@class="a-price-whole")]