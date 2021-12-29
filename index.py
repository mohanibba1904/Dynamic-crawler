

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from xlwt import *

workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'S.no')
table.write(0, 1, 'Names')
table.write(0, 2, 'Investing')
table.write(0, 3, 'Mcx')

urlsList = [
    'https://in.investing.com/commodities/',
    'https://www.mcxindia.in/mcx/mcx-'
]


def urlFunction(url,index):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
        }
    strval = ''
    if(index==0):      
        status = requests.get(url,headers=headers,allow_redirects=False)
        strval = str(status)
    elif(index==1):
        status = requests.get(url) 
        strval = str(status)  
    print(status)
    if('<Response [200]>'==strval):
        driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
        driver.get(url) 
        # this is just to ensure that the page is loaded
        
        time.sleep(5)

        html = driver.page_source
        
        soup = BeautifulSoup(html, "html.parser")

        driver.close()
        if(index==0):
            all_divs = soup.find('bdo',{
                    'class': "last-price-value js-streamable-element"
                })
            v = all_divs.text
            return v
        elif(index==1):
            all_divs = soup.find('td',{
                    'class': "commonopen"
                })

            return  all_divs.text
    else:
        # headers = {
        # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
        # }
        # driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
        # time.sleep(5)
        # driver.get(url)
        # html = driver.page_source
        
        # soup = BeautifulSoup(html, "html.parser")
        # driver.close()
        # # status = requests.get(url,headers=headers)
        # # soup = BeautifulSoup(status.content, 'lxml')
        # all_divs = soup.find('bdo',{
        #             'class': "last-price-value js-streamable-element"
        #         })
        return None
        




def specificUrl(index):
    # initiating the webdriver. Parameter includes the path of the webdriver.
    # driver = webdriver.Chrome(r'C:\Users\Nagababu\Downloads\chromedriver_win32\chromedriver.exe')
    # driver.get(urlsList[index])

    # this is just to ensure that the page is loaded
    # time.sleep(5)

    # html = driver.page_source
    # namesList = ['gold', 'silver', 'cotton', 'crudeoil', 'naturalgas', 'aluminium', 'copper', 'nickel', 'lead', 'zinc', 'menthaoil']
    
    # searchProducts = ['gold', 'gold mini', 'silver', 'silver mini', 'silver micro', 'crude oil', 'crude oil mini', 'natural gas', 'copper','cotton', 'crudeoil', 'copper mini', 'aluminium', 'aluminium mini', 'lead', 'lead  mini', 'nickel', 'nickel mini', 'zinc', 'zinc mini', 'mentha oil']
    searchProducts = ['gold',  'silver',  'crude oil',  'natural gas','cotton', 'crudeoil', 'aluminium',  'lead', 'tin',  'mentha oil']

    # soup = BeautifulSoup(html, "html.parser")
    # driver.close()
    if(index==0):
        investingPrice = []
        for ym in searchProducts:
            Urls = urlsList[index] + ym.replace(' ','-')
            fun = urlFunction(Urls,index)
            if(fun==None):
                investingPrice.append('-')
            else:
                investingPrice.append(fun)
            
        # all_divs = soup.find('div',{
        #     'class': "scrollBar scrolacMark jspScrollable"
        # }).find_all('a')
        # all_prices = soup.find('div',{
        #     'class': "scrollBar scrolacMark jspScrollable"
        # }).find_all('tr')
        # prices = []
        # for my in all_prices:
        #     k = 0
        #     for y in my:
        #         if(k==3):
        #             prices.append(y.text)
        #         k +=1

        # anchorUrls = []
        # names = []
        # newlist = []
        # for k in all_divs:
        #     names.append(k.text)
        # for l in names:
        #     v = len(l)
        #     low = l[0:v-11]
        #     newlist.append(low.lower().strip())        
        
        return investingPrice


    elif(index==1):
        # all_divs = soup.find_all('table',{
        #     'class': "home-table"
        # })
        # # prices  = soup.find_all('span',{
        # #     'class': "indexprice"
        # # })  
        
        # all_anchors = soup.find('div',{
        #     'class': "grid col-940 centertext"
        # }).find_all('a')
        # anchorUrls = []
        # for i in all_anchors:
        #     anchorUrls.append(i['href'])

        # # url = 'https://www.mcxindia.in/mcx/mcx-gold'

        priceslist = []
        for ym in searchProducts:
            Urls = urlsList[index] + ym.replace(' ','-')
            fun = urlFunction(Urls,index)
            if(fun==None):
                priceslist.append('-')
            else:
                priceslist.append(fun.strip())

        names = []
        # for i in all_divs:
        #     line = i.tbody.tr.td.h2.text
        #     prefix = "MCX"
        #     line_new = line.removeprefix(prefix)
        #     names.append(line_new.strip())
        # for l in prices:
        #     priceslist.append(l.text.strip())

        return priceslist





#url of the page we want to scrape


# url = "https://www.mcxindia.in/"
# url = 'https://www.moneycontrol.com/commodity/'


# all_divs = soup.find_all('table',{
#     'class': "home-table"
# })
# prices  = soup.find_all('span',{
#     'class': "indexprice"
# })
result =  ['gold',  'silver',  'crude oil',  'natural gas','cotton', 'crudeoil', 'aluminium',  'lead', 'tin',  'mentha oil']

# [[['gold', 'silver', 'cotton', 'crudeoil', 'naturalgas', 'aluminium', 'copper', 'nickel', 'lead', 'zinc', 'menthaoil'], ['47,955.00', '62,553.00', '33,130.00', '5,688.00', '295.40', '223.50', '759.00', '1,546.50', '190.35', '283.05', '992.10']],
#  [['Gold', 'Gold Mini', 'Silver', 'Silver Mini', 'Silver Micro', 'Crude Oil', 'Crude Oil Mini', 'Natural Gas', 'Copper', 'Copper Mini', 'Aluminium', 'Aluminium Mini', 'Lead', 'Lead Mini', 'Nickel', 'Nickel Mini', 'Zinc', 'Zinc Mini', 'Mentha Oil'], ['47991', '47816', '62370', '62657', '62370', '5676', '0', '309.5', '762.9', '0', '221.15', '212.4', '190.35', '189.25', '1535.5', '0', '281.85', '281.7', '281.85', '281.85']]]

row = 1
finalresult = []
for i in range(len(urlsList)):
    finalresult.append(specificUrl(i))
for my in range(len(result)-1):
        name = result[my]
        v1 = finalresult[0][my]
        v2 = finalresult[1][my]
        table.write(row, 0, row)
        table.write(row, 1, name) 
        table.write(row, 2, v1) 
        table.write(row, 3, v2)    
        row+=1 
workbook.save('MulipleUrlsScrapying.xls')  




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


 # closing the webdriver
