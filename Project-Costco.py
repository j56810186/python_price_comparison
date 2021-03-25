#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from pyquery import PyQuery as pq


# In[13]:


ElectronicsRes = requests.get("https://www.costco.com.tw/Electronics/c/1")
ElectronicsDoc = pq(ElectronicsRes.text)
ElectList = ElectronicsDoc(".category-wrapper > .category-node > .category-link")
ElectItemList = []
for eachElectDoc in ElectList.items():
    print("https://www.costco.com.tw/"+eachElectDoc.attr("href"))
    ElectRes = requests.get("https://www.costco.com.tw/"+eachElectDoc.attr("href"))
    ElectDoc = pq(ElectRes.text)
    #爬取Electronics的所有類別
    ElectPage = 0
    NextElectDoc = ElectDoc
    while True:
        Electitem = NextElectDoc("#list-view-id > li")
        #print(len(Electitem), Electitem)
        for eachElectDoc in Electitem.items():
            ElectDict = {}
            ElectDict["title"] = eachElectDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachElectDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                ElectDict["price"] = "請登入Costco網站查詢售價"
            else:
                ElectDict["price"] = eachElectDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            ElectItemList.append(ElectDict)
            #print(ElectDict)
        ElectPage+=1
        if len(Electitem) == 0:
            break
        ElectResurl=ElectRes.url+'?q=%3Aprice-desc&page=0'
        NextElectRes = requests.get(ElectResurl[0:-1]+str(ElectPage))
        NextElectDoc = pq(NextElectRes.text)
    print(ElectItemList)
    ElectItemList = []


# In[14]:


ComputersRes = requests.get("https://www.costco.com.tw/Computers/c/2")
ComputersDoc = pq(ComputersRes.text)
ComList = ComputersDoc(".category-wrapper > .category-node > .category-link")
ComItemList = []
for eachComDoc in ComList.items():
    print("https://www.costco.com.tw/"+eachComDoc.attr("href"))
    ComRes = requests.get("https://www.costco.com.tw/"+eachComDoc.attr("href"))
    ComDoc = pq(ComRes.text)
    #爬取Computers的所有類別
    ComPage = 0
    NextComDoc = ComDoc
    while True:
        Comitem = NextComDoc("#list-view-id > li")
        #print(len(Comitem), Comitem)
        for eachComDoc in Comitem.items():
            ComDict = {}
            ComDict["title"] = eachComDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachComDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                ComDict["price"] = "請登入Costco網站查詢售價"
            else:
                ComDict["price"] = eachComDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            ComItemList.append(ComDict)
            #print(ComDict)
        ComPage+=1
        if len(Comitem) == 0:
            break
        ComResurl=ComRes.url+'?q=%3Aprice-desc&page=0'
        NextComRes = requests.get(ComResurl[0:-1]+str(ComPage))
        NextComDoc = pq(NextComRes.text)
    print(ComItemList)
    ComItemList = []


# In[15]:


AppliancesRes = requests.get("https://www.costco.com.tw/Appliances/c/3")
AppliancesDoc = pq(AppliancesRes.text)
AppList = AppliancesDoc(".category-wrapper > .category-node > .category-link")
AppItemList = []
for eachAppDoc in AppList.items():
    print("https://www.costco.com.tw/"+eachAppDoc.attr("href"))
    AppRes = requests.get("https://www.costco.com.tw/"+eachAppDoc.attr("href"))
    AppDoc = pq(AppRes.text)
    #爬取Appliances的所有類別
    AppPage = 0
    NextAppDoc = AppDoc
    while True:
        Appitem = NextAppDoc("#list-view-id > li")
        #print(len(Appitem), Appitem)
        for eachAppDoc in Appitem.items():
            AppDict = {}
            AppDict["title"] = eachAppDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachAppDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                AppDict["price"] = "請登入Costco網站查詢售價"
            else:
                AppDict["price"] = eachAppDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            AppItemList.append(AppDict)
            #print(AppDict)
        AppPage+=1
        if len(Appitem) == 0:
            break
        AppResurl=AppRes.url+'?q=%3Aprice-desc&page=0'
        NextAppRes = requests.get(AppResurl[0:-1]+str(AppPage))
        NextAppDoc = pq(NextAppRes.text)
    print(AppItemList)
    AppItemList = []


# In[16]:


HealthBeautyRes = requests.get("https://www.costco.com.tw/Health-Beauty/c/7")
HealthBeautyDoc = pq(HealthBeautyRes.text)
HealthList = HealthBeautyDoc(".category-wrapper > .category-node > .category-link")
HealthItemList = []
for eachHealthDoc in HealthList.items():
    print("https://www.costco.com.tw/"+eachHealthDoc.attr("href"))
    HealthRes = requests.get("https://www.costco.com.tw/"+eachHealthDoc.attr("href"))
    HealthDoc = pq(HealthRes.text)
    #爬取HealthBeauty的所有類別
    HealthPage = 0
    NextHealthDoc = HealthDoc
    while True:
        Healthitem = NextHealthDoc("#list-view-id > li")
        #print(len(Healthitem), Healthitem)
        for eachHealthDoc in Healthitem.items():
            HealthDict = {}
            HealthDict["title"] = eachHealthDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachHealthDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                HealthDict["price"] = "請登入Costco網站查詢售價"
            else:
                HealthDict["price"] = eachHealthDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            HealthItemList.append(HealthDict)
            #print(HealthDict)
        HealthPage+=1
        if len(Healthitem) == 0:
            break
        HealthResurl=HealthRes.url+'?q=%3Aprice-desc&page=0'
        NextHealthRes = requests.get(HealthResurl[0:-1]+str(HealthPage))
        NextHealthDoc = pq(NextHealthRes.text)
    print(HealthItemList)
    HealthItemList = []


# In[17]:


BabyKidsToysRes = requests.get("https://www.costco.com.tw/Baby-Kids-Toys/c/12")
BabyKidsToysDoc = pq(BabyKidsToysRes.text)
BabyList = BabyKidsToysDoc(".category-wrapper > .category-node > .category-link")
BabyItemList = []
for eachBabyDoc in BabyList.items():
    print("https://www.costco.com.tw/"+eachBabyDoc.attr("href"))
    BabyRes = requests.get("https://www.costco.com.tw/"+eachBabyDoc.attr("href"))
    BabyDoc = pq(BabyRes.text)
    #爬取BabyKidsToys的所有類別
    BabyPage = 0
    NextBabyDoc = BabyDoc
    while True:
        Babyitem = NextBabyDoc("#list-view-id > li")
        #print(len(Babyitem), Babyitem)
        for eachBabyDoc in Babyitem.items():
            BabyDict = {}
            BabyDict["title"] = eachBabyDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachBabyDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                BabyDict["price"] = "請登入Costco網站查詢售價"
            else:
                BabyDict["price"] = eachBabyDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            BabyItemList.append(BabyDict)
            #print(BabyDict)
        BabyPage+=1
        if len(Babyitem) == 0:
            break
        BabyResurl=BabyRes.url+'?q=%3Aprice-desc&page=0'
        NextBabyRes = requests.get(BabyResurl[0:-1]+str(BabyPage))
        NextBabyDoc = pq(NextBabyRes.text)
    print(BabyItemList)
    BabyItemList = []


# In[18]:


FoodRes = requests.get("https://www.costco.com.tw/Food/c/8")
FoodDoc = pq(FoodRes.text)
FoodList = FoodDoc(".category-wrapper > .category-node > .category-link")
FoodItemList = []
for eachFoodDoc in FoodList.items():
    print("https://www.costco.com.tw/"+eachFoodDoc.attr("href"))
    FoodRes = requests.get("https://www.costco.com.tw/"+eachFoodDoc.attr("href"))
    FoodDoc = pq(FoodRes.text)
    #爬取Food的所有類別
    FoodPage = 0
    NextFoodDoc = FoodDoc
    while True:
        Fooditem = NextFoodDoc("#list-view-id > li")
        #print(len(Fooditem), Fooditem)
        for eachFoodDoc in Fooditem.items():
            FoodDict = {}
            FoodDict["title"] = eachFoodDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachFoodDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                FoodDict["price"] = "請登入Costco網站查詢售價"
            else:
                FoodDict["price"] = eachFoodDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            FoodItemList.append(FoodDict)
            #print(FoodDict)
        FoodPage+=1
        if len(Fooditem) == 0:
            break
        FoodResurl=FoodRes.url+'?q=%3Aprice-desc&page=0'
        NextFoodRes = requests.get(FoodResurl[0:-1]+str(FoodPage))
        NextFoodDoc = pq(NextFoodRes.text)
    print(FoodItemList)
    FoodItemList = []


# In[19]:


HouseholdPetSuppliesRes = requests.get("https://www.costco.com.tw/Household-Pet-Supplies/c/14")
HouseholdPetSuppliesDoc = pq(HouseholdPetSuppliesRes.text)
HouseList = HouseholdPetSuppliesDoc(".category-wrapper > .category-node > .category-link")
HouseItemList = []
for eachHouseDoc in HouseList.items():
    print("https://www.costco.com.tw/"+eachHouseDoc.attr("href"))
    HouseRes = requests.get("https://www.costco.com.tw/"+eachHouseDoc.attr("href"))
    HouseDoc = pq(HouseRes.text)
    #爬取HouseholdPetSupplies的所有類別
    HousePage = 0
    NextHouseDoc = HouseDoc
    while True:
        Houseitem = NextHouseDoc("#list-view-id > li")
        #print(len(Houseitem), Houseitem)
        for eachHouseDoc in Houseitem.items():
            HouseDict = {}
            HouseDict["title"] = eachHouseDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachHouseDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                HouseDict["price"] = "請登入Costco網站查詢售價"
            else:
                HouseDict["price"] = eachHouseDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            HouseItemList.append(HouseDict)
            #print(HouseDict)
        HousePage+=1
        if len(Houseitem) == 0:
            break
        HouseResurl=HouseRes.url+'?q=%3Aprice-desc&page=0'
        NextHouseRes = requests.get(HouseResurl[0:-1]+str(HousePage))
        NextHouseDoc = pq(NextHouseRes.text)
    print(HouseItemList)
    HouseItemList = []


# In[20]:


HomeKitchenRes = requests.get("https://www.costco.com.tw/Home-Kitchen/c/6")
HomeKitchenDoc = pq(HomeKitchenRes.text)
HomeList = HomeKitchenDoc(".category-wrapper > .category-node > .category-link")
HomeItemList = []
for eachHomeDoc in HomeList.items():
    print("https://www.costco.com.tw/"+eachHomeDoc.attr("href"))
    HomeRes = requests.get("https://www.costco.com.tw/"+eachHomeDoc.attr("href"))
    HomeDoc = pq(HomeRes.text)
    #爬取HomeKitchen的所有類別
    HomePage = 0
    NextHomeDoc = HomeDoc
    while True:
        Homeitem = NextHomeDoc("#list-view-id > li")
        #print(len(Homeitem), Homeitem)
        for eachHomeDoc in Homeitem.items():
            HomeDict = {}
            HomeDict["title"] = eachHomeDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachHomeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                HomeDict["price"] = eachHomeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(2)").text()
            else:
                HomeDict["price"] = eachHomeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            HomeItemList.append(HomeDict)
            #print(HomeDict)
        HomePage+=1
        if len(Homeitem) == 0:
            break
        HomeResurl=HomeRes.url+'?q=%3Aprice-desc&page=0'
        NextHomeRes = requests.get(HomeResurl[0:-1]+str(HomePage))
        NextHomeDoc = pq(NextHomeRes.text)
    print(HomeItemList)
    HomeItemList = []


# In[21]:


ClothingAccessoriesLuggageRes = requests.get("https://www.costco.com.tw/Clothing-Accessories-Luggage/c/9")
ClothingAccessoriesLuggageDoc = pq(ClothingAccessoriesLuggageRes.text)
ClothingList = ClothingAccessoriesLuggageDoc(".category-wrapper > .category-node > .category-link")
ClothingItemList = []
for eachClothingDoc in ClothingList.items():
    print("https://www.costco.com.tw/"+eachClothingDoc.attr("href"))
    ClothingRes = requests.get("https://www.costco.com.tw/"+eachClothingDoc.attr("href"))
    ClothingDoc = pq(ClothingRes.text)
    #爬取ClothingAccessoriesLuggage的所有類別
    ClothingPage = 0
    NextClothingDoc = ClothingDoc
    while True:
        Clothingitem = NextClothingDoc("#list-view-id > li")
        #print(len(Clothingitem), Clothingitem)
        for eachClothingDoc in Clothingitem.items():
            ClothingDict = {}
            ClothingDict["title"] = eachClothingDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachClothingDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                ClothingDict["price"] = "請登入Costco網站查詢售價"
            else:
                ClothingDict["price"] = eachClothingDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            ClothingItemList.append(ClothingDict)
            #print(ClothingDict)
        ClothingPage+=1
        if len(Clothingitem) == 0:
            break
        ClothingResurl=ClothingRes.url+'?q=%3Aprice-desc&page=0'
        NextClothingRes = requests.get(ClothingResurl[0:-1]+str(ClothingPage))
        NextClothingDoc = pq(NextClothingRes.text)
    print(ClothingItemList)
    ClothingItemList = []


# In[22]:


FurnitureBeddingRes = requests.get("https://www.costco.com.tw/Furniture-Bedding/c/5")
FurnitureBeddingDoc = pq(FurnitureBeddingRes.text)
FurnitureList = FurnitureBeddingDoc(".category-wrapper > .category-node > .category-link")
FurnitureItemList = []
for eachFurnitureDoc in FurnitureList.items():
    print("https://www.costco.com.tw/"+eachFurnitureDoc.attr("href"))
    FurnitureRes = requests.get("https://www.costco.com.tw/"+eachFurnitureDoc.attr("href"))
    FurnitureDoc = pq(FurnitureRes.text)
    #爬取FurnitureBedding的所有類別
    FurniturePage = 0
    NextFurnitureDoc = FurnitureDoc
    while True:
        Furnitureitem = NextFurnitureDoc("#list-view-id > li")
        #print(len(Furnitureitem), Furnitureitem)
        for eachFurnitureDoc in Furnitureitem.items():
            FurnitureDict = {}
            FurnitureDict["title"] = eachFurnitureDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachFurnitureDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                FurnitureDict["price"] = eachFurnitureDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(2)").text()
            else:
                FurnitureDict["price"] = eachFurnitureDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            FurnitureItemList.append(FurnitureDict)
            #print(FurnitureDict)
        FurniturePage+=1
        if len(Furnitureitem) == 0:
            break
        FurnitureResurl=FoodRes.url+'?q=%3Aprice-desc&page=0'
        NextFurnitureRes = requests.get(FurnitureResurl[0:-1]+str(FurniturePage))
        NextFurnitureDoc = pq(NextFurnitureRes.text)
    print(FurnitureItemList)
    FurnitureItemList = []


# In[23]:


HomeImprovementRes = requests.get("https://www.costco.com.tw/Home-Improvement/c/13")
HomeImprovementDoc = pq(HomeImprovementRes.text)
HomeImproList = HomeImprovementDoc(".category-wrapper > .category-node > .category-link")
HomeImproItemList = []
for eachHomeImproDoc in HomeImproList.items():
    print("https://www.costco.com.tw/"+eachHomeImproDoc.attr("href"))
    HomeImproRes = requests.get("https://www.costco.com.tw/"+eachHomeImproDoc.attr("href"))
    HomeImproDoc = pq(HomeImproRes.text)
    #爬取HomeImprovement的所有類別
    HomeImproPage = 0
    NextHomeImproDoc = HomeImproDoc
    while True:
        HomeImproitem = NextHomeImproDoc("#list-view-id > li")
        #print(len(HomeImproitem), HomeImproitem)
        for eachHomeImproDoc in HomeImproitem.items():
            HomeImproDict = {}
            HomeImproDict["title"] = eachHomeImproDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachHomeImproDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                HomeImproDict["price"] = "請登入Costco網站查詢售價"
            else:
                HomeImproDict["price"] = eachHomeImproDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            HomeImproItemList.append(HomeImproDict)
            #print(HomeImproDict)
        HomeImproPage+=1
        if len(HomeImproitem) == 0:
            break
        HomeImproResurl=HomeImproRes.url+'?q=%3Aprice-desc&page=0'
        NextHomeImproRes = requests.get(HomeImproResurl[0:-1]+str(HomeImproPage))
        NextHomeImproDoc = pq(NextHomeImproRes.text)
    print(HomeImproItemList)
    HomeImproItemList = []


# In[27]:


AutomotiveTireRes = requests.get("https://www.costco.com.tw/Automotive-Tire/c/18")
AutomotiveTireDoc = pq(AutomotiveTireRes.text)
AutoList = AutomotiveTireDoc(".category-wrapper > .category-node > .category-link")
AutoItemList = []
for eachAutoDoc in AutoList.items():
    print("https://www.costco.com.tw/"+eachAutoDoc.attr("href"))
    AutoRes = requests.get("https://www.costco.com.tw/"+eachAutoDoc.attr("href"))
    AutoDoc = pq(AutoRes.text)
    #爬取AutomotiveTire的所有類別
    AutoPage = 0
    NextAutoDoc = AutoDoc
    while True:
        Autoitem = NextAutoDoc("#list-view-id > li")
        #print(len(Autoitem), Autoitem)
        for eachAutoDoc in Autoitem.items():
            AutoDict = {}
            AutoDict["title"] = eachAutoDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachAutoDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                AutoDict["price"] = "請登入Costco網站查詢售價"
            else:
                AutoDict["price"] = eachAutoDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            AutoItemList.append(AutoDict)
            #print(AutoDict)
        AutoPage+=1
        if len(Autoitem) == 0:
            break
        AutoResurl=AutoRes.url+'?q=%3Aprice-desc&page=0'
        NextAutoRes = requests.get(AutoResurl[0:-1]+str(AutoPage))
        NextAutoDoc = pq(NextAutoRes.text)
    if AutoItemList == []:
        AutoItemList.append("請進入Costco網站依規格或車輛資訊查詢售價")
        print(AutoItemList)
    else:
        print(AutoItemList)
    AutoItemList = []


# In[28]:


SportFitnessRes = requests.get("https://www.costco.com.tw/Sport-Fitness/c/11")
SportFitnessDoc = pq(SportFitnessRes.text)
SportList = SportFitnessDoc(".category-wrapper > .category-node > .category-link")
SportItemList = []
for eachSportDoc in SportList.items():
    print("https://www.costco.com.tw/"+eachSportDoc.attr("href"))
    SportRes = requests.get("https://www.costco.com.tw/"+eachSportDoc.attr("href"))
    SportDoc = pq(SportRes.text)
    #爬取SportFitness的所有類別
    SportPage = 0
    NextSportDoc = SportDoc
    while True:
        Sportitem = NextSportDoc("#list-view-id > li")
        #print(len(Sportitem), Sportitem)
        for eachSportDoc in Sportitem.items():
            SportDict = {}
            SportDict["title"] = eachSportDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachSportDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                SportDict["price"] = "請登入Costco網站查詢售價"
            else:
                SportDict["price"] = eachSportDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            SportItemList.append(SportDict)
            #print(SportDict)
        SportPage+=1
        if len(Sportitem) == 0:
            break
        SportResurl=SportRes.url+'?q=%3Aprice-desc&page=0'
        NextSportRes = requests.get(SportResurl[0:-1]+str(SportPage))
        NextSportDoc = pq(NextSportRes.text)
    print(SportItemList)
    SportItemList = []


# In[29]:


LawnGardenRes = requests.get("https://www.costco.com.tw/Lawn-Garden/c/4")
LawnGardenDoc = pq(LawnGardenRes.text)
LawnList = LawnGardenDoc(".category-wrapper > .category-node > .category-link")
LawnItemList = []
for eachLawnDoc in LawnList.items():
    print("https://www.costco.com.tw/"+eachLawnDoc.attr("href"))
    LawnRes = requests.get("https://www.costco.com.tw/"+eachLawnDoc.attr("href"))
    LawnDoc = pq(LawnRes.text)
    #爬取LawnGarden的所有類別
    LawnPage = 0
    NextLawnDoc = LawnDoc
    while True:
        Lawnitem = NextLawnDoc("#list-view-id > li")
        #print(len(Lawnitem), Lawnitem)
        for eachLawnDoc in Lawnitem.items():
            LawnDict = {}
            LawnDict["title"] = eachLawnDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachLawnDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                LawnDict["price"] = "請登入Costco網站查詢售價"
            else:
                LawnDict["price"] = eachLawnDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            LawnItemList.append(LawnDict)
            #print(LawnDict)
        LawnPage+=1
        if len(Lawnitem) == 0:
            break
        LawnResurl=LawnRes.url+'?q=%3Aprice-desc&page=0'
        NextLawnRes = requests.get(LawnResurl[0:-1]+str(LawnPage))
        NextLawnDoc = pq(NextLawnRes.text)
    print(LawnItemList)
    LawnItemList = []


# In[30]:


OfficeSuppliesBooksRes = requests.get("https://www.costco.com.tw/Office-Supplies-Books/c/17")
OfficeSuppliesBooksDoc = pq(OfficeSuppliesBooksRes.text)
OfficeList = OfficeSuppliesBooksDoc(".category-wrapper > .category-node > .category-link")
OfficeItemList = []
for eachOfficeDoc in OfficeList.items():
    print("https://www.costco.com.tw/"+eachOfficeDoc.attr("href"))
    OfficeRes = requests.get("https://www.costco.com.tw/"+eachOfficeDoc.attr("href"))
    OfficeDoc = pq(OfficeRes.text)
    #爬取OfficeSuppliesBooks的所有類別
    OfficePage = 0
    NextOfficeDoc = OfficeDoc
    while True:
        Officeitem = NextOfficeDoc("#list-view-id > li")
        #print(len(Officeitem), Officeitem)
        for eachOfficeDoc in Officeitem.items():
            OfficeDict = {}
            OfficeDict["title"] = eachOfficeDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachOfficeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                OfficeDict["price"] = "請登入Costco網站查詢售價"
            else:
                OfficeDict["price"] = eachOfficeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            OfficeItemList.append(OfficeDict)
            #print(OfficeDict)
        OfficePage+=1
        if len(Officeitem) == 0:
            break
        OfficeResurl=OfficeRes.url+'?q=%3Aprice-desc&page=0'
        NextOfficeRes = requests.get(OfficeResurl[0:-1]+str(OfficePage))
        NextOfficeDoc = pq(NextOfficeRes.text)
    print(OfficeItemList)
    OfficeItemList = []


# In[31]:


GiftsTicketsFloralRes = requests.get("https://www.costco.com.tw/Gifts-Tickets-Floral/c/16")
GiftsTicketsFloralDoc = pq(GiftsTicketsFloralRes.text)
GiftsList = GiftsTicketsFloralDoc(".category-wrapper > .category-node > .category-link")
GiftsItemList = []
for eachGiftsDoc in GiftsList.items():
    print("https://www.costco.com.tw/"+eachGiftsDoc.attr("href"))
    GiftsRes = requests.get("https://www.costco.com.tw/"+eachGiftsDoc.attr("href"))
    GiftsDoc = pq(GiftsRes.text)
    #爬取GiftsTicketsFloral的所有類別
    GiftsPage = 0
    NextGiftsDoc = GiftsDoc
    while True:
        Giftsitem = NextGiftsDoc("#list-view-id > li")
        #print(len(Giftsitem), Giftsitem)
        for eachGiftsDoc in Giftsitem.items():
            GiftsDict = {}
            GiftsDict["title"] = eachGiftsDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachGiftsDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                GiftsDict["price"] = "請登入Costco網站查詢售價"
            else:
                GiftsDict["price"] = eachGiftsDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            GiftsItemList.append(GiftsDict)
            #print(GiftsDict)
        GiftsPage+=1
        if len(Giftsitem) == 0:
            break
        GiftsResurl=GiftsRes.url+'?q=%3Aprice-desc&page=0'
        NextGiftsRes = requests.get(GiftsResurl[0:-1]+str(GiftsPage))
        NextGiftsDoc = pq(NextGiftsRes.text)
    print(GiftsItemList)
    GiftsItemList = []


# In[34]:


JewelryWatchesOpticalsRes = requests.get("https://www.costco.com.tw/Jewelry-Watches-Opticals/c/10")
JewelryWatchesOpticalsDoc = pq(JewelryWatchesOpticalsRes.text)
JewelryList = JewelryWatchesOpticalsDoc(".category-wrapper > .category-node > .category-link")
JewelryItemList = []
for eachJewelryDoc in JewelryList.items():
    print("https://www.costco.com.tw/"+eachJewelryDoc.attr("href"))
    JewelryRes = requests.get("https://www.costco.com.tw/"+eachJewelryDoc.attr("href"))
    JewelryDoc = pq(JewelryRes.text)
    #爬取JewelryWatchesOpticals的所有類別
    JewelryPage = 0
    NextJewelryDoc = JewelryDoc
    while True:
        Jewelryitem = NextJewelryDoc("#list-view-id > li")
        #print(len(Jewelryitem), Jewelryitem)
        for eachJewelryDoc in Jewelryitem.items():
            JewelryDict = {}
            JewelryDict["title"] = eachJewelryDoc(".product-info-wrapper >.product-list-details >.product-name-container >a:nth-child(1)").text()
            if eachJewelryDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text() == "":
                JewelryDict["price"] = "請登入Costco網站查詢售價"
            else:
                JewelryDict["price"] = eachJewelryDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text()
            JewelryItemList.append(JewelryDict)
            #print(JewelryDict)
        JewelryPage+=1
        if len(Jewelryitem) == 0:
            break
        JewelryResurl=JewelryRes.url+'?q=%3Aprice-desc&page=0'
        NextJewelryRes = requests.get(JewelryResurl[0:-1]+str(JewelryPage))
        NextJewelryDoc = pq(NextJewelryRes.text)
    print(JewelryItemList)
    JewelryItemList = []


# In[ ]:




