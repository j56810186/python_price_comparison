#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from pyquery import PyQuery as pq


# In[2]:


HomeRes = requests.get("https://www.rt-mart.com.tw/direct/")
# HomeRes.text
HomeDoc = pq(HomeRes.text)


# In[8]:


dataList=[]
CateList=HomeDoc(".footerNavContent>ul>li>h3>a")
for Eachcast in CateList.items():
    print(Eachcast.attr("href"))
    CateRes = requests.get(Eachcast.attr("href"))
# HomeRes.text
    CateDoc = pq(CateRes.text)
    CateList2=CateDoc(".classify_title>a")
    for Eachcast2 in CateList2.items():
        if Eachcast2.attr("href")=="javascript: void(0);":
            continue
#         print(Eachcast2.attr("href"))
        CateRes2 = requests.get(Eachcast2.attr("href"))
        CateDoc2 = pq(CateRes2.text)
        #part2
        pg=1
        nextPgDoc=CateDoc2
        while True:
    #         print(len(CateDoc2(".indexProList")))
            itemLi=nextPgDoc(".indexProList")
##           print(len(itemLi),CateRes2.url+"&prod_size=&p_data_num=18&usort=auto_date%2CDESC&page={}".format(pg))
            for eachItemDoc in itemLi.items():
                dataDict={}
                dataDict["title"]=eachItemDoc("h5").text()
                dataDict["price"]=eachItemDoc(".for_pricebox").text()
                dataList.append(dataDict)
    #             print(eachItemDoc("h5").text())
    #             print(eachItemDoc(".for_pricebox").text())
            pg+=1
            if len(itemLi)==0:
                break
            nextPgRes = requests.get(CateRes2.url+"&prod_size=&p_data_num=18&usort=aut            o_date%2CDESC&page={}".format(pg))
            nextPgDoc = pq(nextPgRes.text)


            


# In[9]:


dataList


# In[ ]:




