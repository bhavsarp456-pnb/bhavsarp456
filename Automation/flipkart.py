from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\OneDrive\\Desktop\\chromedriver.exe")
products = []
prices = []
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content = driver.page_source
par_con = BeautifulSoup(content, "html.parser")
for a in par_con.findAll('a', href={True}, attrs={'class':'_1fQZEK'}):
    name = a.find('div',attrs = {'class':'_4rR01T'})
    price = a.find('div',attrs = {'class':'_30jeq3 _1_WHN1'})
    products.append(name.text)
    prices.append(price.text)
df = pd.DataFrame({"Product":products,"Prices":prices})
df.to_excel("C:\\Users\\Dell\\OneDrive\\Desktop\\laptops_list.xlsx", index=False, encoding="UTF-8")

