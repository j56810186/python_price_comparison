#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\User\pytest\chromedriver.exe")


# In[2]:


driver.get('https://online.carrefour.com.tw/tw/%E6%9C%80%E6%96%B0%E5%9E%8B%E9%8C%84%E5%95%86%E5%93%81')


# In[3]:


SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# In[12]:


html = driver.find_element_by_css_selector("*").get_attribute("outerHTML")
doc = pq(html)
dataList = []
titleDoc = doc("#proList > div.container > div > div.col-md-10.col-sm-12.col-xs-12 > div.display-type > div.theme-wrap.theme1.list-or-block.active > div > div > div > div > ul div > div.rank-right.pull-left.overflow-visible.clearfix > div:nth-child(1) > a")
specDoc = doc("#proList > div.container > div > div.col-md-10.col-sm-12.col-xs-12 > div.display-type > div.theme-wrap.theme1.list-or-block.active > div > div > div > div > ul div > div.rank-right.pull-left.overflow-visible.clearfix > div.margin-bottom-10.list-item > div.list-item-sub > div:nth-child(2) > span")
priceDoc = doc("#proList > div.container > div > div.col-md-10.col-sm-12.col-xs-12 > div.display-type > div.theme-wrap.theme1.list-or-block.active > div > div > div > div > ul div > div.rank-right.pull-left.overflow-visible.clearfix > div.margin-bottom-10.list-item > div.item-action > div.item-price.inline-block > div.discount-price.inline-block.vertical-middle")
i = 0
for eachTitle in titleDoc.items():
    itemDict = {}
    t = 0
    i += 1
    for eachSpec in specDoc.items():
        t += 1
        if (t == i):
            specString = eachSpec.text()
            break
    itemDict["title"] = eachTitle.text() + " " + specString

    j = 0
    for eachPrice in priceDoc.items():
        j += 1
        if (j == i):
            itemDict["price"] = float(eachPrice.text().replace("$",""))
            break
    dataList.append(itemDict)


# In[13]:


dataList


# In[ ]:




