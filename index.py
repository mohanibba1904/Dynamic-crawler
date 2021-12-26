

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#url of the page we want to scrape
url = "https://www.mcxindia.in/"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all('span')

count = 0
print(all_divs)
	

driver.close() # closing the webdriver
