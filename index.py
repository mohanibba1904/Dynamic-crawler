

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from xlwt import *

# workbook = Workbook(encoding = 'utf-8')
# table = workbook.add_sheet('data')
# table.write(0, 0, 'S.no')
# table.write(0, 1, 'Names')
# table.write(0, 2, 'Prices')
# table.write(0, 3, '10-Dec-2021')
# table.write(0, 4, '09-Dec-2021')
urlsList = [
    'https://www.moneycontrol.com/commodity/',
    'https://www.mcxindia.in/'
]

def urlFunction(url):
    driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(url)

    # this is just to ensure that the page is loaded
    time.sleep(5)

    html = driver.page_source
    print(driver.get(url))
    soup = BeautifulSoup(html, "html.parser")
    driver.close()
    all_divs = soup.find('td',{
            'class': "commonopen"
        })
    print(soup)
    return  all_divs.text




def specificUrl(index):
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(urlsList[index])

    # this is just to ensure that the page is loaded
    time.sleep(5)

    html = driver.page_source
    namesList = ['gold', 'silver', 'cotton', 'crudeoil', 'naturalgas', 'aluminium', 'copper', 'nickel', 'lead', 'zinc', 'menthaoil']
    soup = BeautifulSoup(html, "html.parser")
    driver.close()
    if(index==0): 
        all_divs = soup.find('div',{
            'class': "scrollBar scrolacMark jspScrollable"
        }).find_all('a')
        all_prices = soup.find('div',{
            'class': "scrollBar scrolacMark jspScrollable"
        }).find_all('tr')
        prices = []
        for my in all_prices:
            k = 0
            for y in my:
                if(k==3):
                    prices.append(y.text)
                k +=1

        anchorUrls = []
        names = []
        newlist = []
        for k in all_divs:
            names.append(k.text)
        for l in names:
            v = len(l)
            low = l[0:v-11]
            newlist.append(low.lower().strip())        
        
        return (prices)


    elif(index==1):
        # all_divs = soup.find_all('table',{
        #     'class': "home-table"
        # })
        # prices  = soup.find_all('span',{
        #     'class': "indexprice"
        # })  
        
        all_anchors = soup.find('div',{
            'class': "grid col-940 centertext"
        }).find_all('a')
        anchorUrls = []
        # for i in all_anchors:
        #     anchorUrls.append(i['href'])

        # url = 'https://www.mcxindia.in/mcx/mcx-gold'
        print(namesList)
        for ym in namesList:
            url = 'https://www.mcxindia.in/mcx/mcx-' + ym
            fun = urlFunction(url)
            print(fun)
        names = []
        priceslist = []

        # for i in all_divs:
        #     line = i.tbody.tr.td.h2.text
        #     prefix = "MCX"
        #     line_new = line.removeprefix(prefix)
        #     names.append(line_new.strip())
        # for l in prices:
        #     priceslist.append(l.text.strip())

        return (names,priceslist)





#url of the page we want to scrape


# url = "https://www.mcxindia.in/"
# url = 'https://www.moneycontrol.com/commodity/'


# all_divs = soup.find_all('table',{
#     'class': "home-table"
# })
# prices  = soup.find_all('span',{
#     'class': "indexprice"
# })

for i in range(len(urlsList)):
    print(specificUrl(i))




# all_anchors = soup.find('div',{
#     'class': "grid col-940 centertext"
# }).find_all('a')
# anchorUrls = []
# for i in all_anchors:
#     all_anchors.append(i['href'])


# row = 1
# names = []
# priceslist = []
# for i in all_divs:
#     line = i.tbody.tr.td.h2.text
#     prefix = "MCX"
#     line_new = line.removeprefix(prefix)
#     names.append(line_new.strip())
# for l in prices:
#     priceslist.append(l.text.strip())

# lengths = len(all_divs)
# for index in range(lengths):
#     v1 = names[index]
#     v2 = priceslist[index]
#     table.write(row, 0, row)
#     table.write(row, 1, v1) 
#     table.write(row, 2, v2)    
#     row+=1  
# workbook.save('MCX.xls')  

 # closing the webdriver
