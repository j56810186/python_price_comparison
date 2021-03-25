import time
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
import tkinter as tk

def crawlCarrefour():
    driver = webdriver.Chrome(r"C:\Users\User\pytest\chromedriver.exe")
    driver.get('https://online.carrefour.com.tw/tw/%E6%9C%80%E6%96%B0%E5%9E%8B%E9%8C%84%E5%95%86%E5%93%81')
    
    # 捲螢幕
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
    driver.quit()
    return dataList

def crawlRTMart():
    HomeRes = requests.get("https://www.rt-mart.com.tw/direct/")
    # HomeRes.text
    HomeDoc = pq(HomeRes.text)

    dataList=[]
    CateList=HomeDoc(".footerNavContent>ul>li>h3>a")
    for Eachcast in CateList.items():
        CateRes = requests.get(Eachcast.attr("href"))
    # HomeRes.text
        CateDoc = pq(CateRes.text)
        CateList2=CateDoc(".classify_title>a")
        for Eachcast2 in CateList2.items():
            if Eachcast2.attr("href")=="javascript: void(0);":
                continue
    #         print(Eachcast2.attr("href"))
            try:
                CateRes2 = requests.get(Eachcast2.attr("href"))
            except requests.exceptions.ConnectionError:
                r.status_code = "Connection refused"
            CateDoc2 = pq(CateRes2.text)
            #part2
            pg=1
            nextPgDoc=CateDoc2
            while True:
                itemLi=nextPgDoc(".indexProList")
        ##      print(len(itemLi),CateRes2.url+"&prod_size=&p_data_num=18&usort=auto_date%2CDESC&page={}".format(pg))
                for eachItemDoc in itemLi.items():
                    dataDict={}
                    dataDict["title"]=eachItemDoc("h5").text()
                    dataDict["price"]=float(eachItemDoc(".for_pricebox").text().replace('$', ''))
                    dataList.append(dataDict)
        #             print(eachItemDoc("h5").text())
        #             print(eachItemDoc(".for_pricebox").text())
                pg+=1
                if len(itemLi)==0:
                    break
                try:
                    nextPgRes = requests.get(CateRes2.url+"&prod_size=&p_data_num=18&usort=auto_date%2CDESC&page={}".format(pg))
                except requests.exceptions.ConnectionError:
                    r.status_code = "Connection refused"
                nextPgDoc = pq(nextPgRes.text)
    return dataList

def crawlCostco():
    costcoList = []
    
    # electronics
    ElectronicsRes = requests.get("https://www.costco.com.tw/Electronics/c/1")
    ElectronicsDoc = pq(ElectronicsRes.text)
    ElectList = ElectronicsDoc(".category-wrapper > .category-node > .category-link")
    ElectItemList = []
    for eachElectDoc in ElectList.items():
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
                    ElectDict["price"] = float(eachElectDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                ElectItemList.append(ElectDict)
                #print(ElectDict)
            ElectPage+=1
            if len(Electitem) == 0:
                break
            ElectResurl=ElectRes.url+'?q=%3Aprice-desc&page=0'
            NextElectRes = requests.get(ElectResurl[0:-1]+str(ElectPage))
            NextElectDoc = pq(NextElectRes.text)
    costcoList += ElectItemList
    
    # computers
    ComputersRes = requests.get("https://www.costco.com.tw/Computers/c/2")
    ComputersDoc = pq(ComputersRes.text)
    ComList = ComputersDoc(".category-wrapper > .category-node > .category-link")
    ComItemList = []
    for eachComDoc in ComList.items():
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
                    ComDict["price"] = float(eachComDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                ComItemList.append(ComDict)
                #print(ComDict)
            ComPage+=1
            if len(Comitem) == 0:
                break
            ComResurl=ComRes.url+'?q=%3Aprice-desc&page=0'
            NextComRes = requests.get(ComResurl[0:-1]+str(ComPage))
            NextComDoc = pq(NextComRes.text)
    costcoList += ComItemList
    
    # appliance
    AppliancesRes = requests.get("https://www.costco.com.tw/Appliances/c/3")
    AppliancesDoc = pq(AppliancesRes.text)
    AppList = AppliancesDoc(".category-wrapper > .category-node > .category-link")
    AppItemList = []
    for eachAppDoc in AppList.items():
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
                    AppDict["price"] = float(eachAppDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                AppItemList.append(AppDict)
                #print(AppDict)
            AppPage+=1
            if len(Appitem) == 0:
                break
            AppResurl=AppRes.url+'?q=%3Aprice-desc&page=0'
            NextAppRes = requests.get(AppResurl[0:-1]+str(AppPage))
            NextAppDoc = pq(NextAppRes.text)
    costcoList += AppItemList
    
    # health
    HealthBeautyRes = requests.get("https://www.costco.com.tw/Health-Beauty/c/7")
    HealthBeautyDoc = pq(HealthBeautyRes.text)
    HealthList = HealthBeautyDoc(".category-wrapper > .category-node > .category-link")
    HealthItemList = []
    for eachHealthDoc in HealthList.items():
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
                    HealthDict["price"] = float(eachHealthDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                HealthItemList.append(HealthDict)
                #print(HealthDict)
            HealthPage+=1
            if len(Healthitem) == 0:
                break
            HealthResurl=HealthRes.url+'?q=%3Aprice-desc&page=0'
            NextHealthRes = requests.get(HealthResurl[0:-1]+str(HealthPage))
            NextHealthDoc = pq(NextHealthRes.text)
    costcoList += HealthItemList
    
    # baby
    BabyKidsToysRes = requests.get("https://www.costco.com.tw/Baby-Kids-Toys/c/12")
    BabyKidsToysDoc = pq(BabyKidsToysRes.text)
    BabyList = BabyKidsToysDoc(".category-wrapper > .category-node > .category-link")
    BabyItemList = []
    for eachBabyDoc in BabyList.items():
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
                    BabyDict["price"] = float(eachBabyDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                BabyItemList.append(BabyDict)
                #print(BabyDict)
            BabyPage+=1
            if len(Babyitem) == 0:
                break
            BabyResurl=BabyRes.url+'?q=%3Aprice-desc&page=0'
            NextBabyRes = requests.get(BabyResurl[0:-1]+str(BabyPage))
            NextBabyDoc = pq(NextBabyRes.text)
    costcoList += BabyItemList
    
    # food
    FoodRes = requests.get("https://www.costco.com.tw/Food/c/8")
    FoodDoc = pq(FoodRes.text)
    FoodList = FoodDoc(".category-wrapper > .category-node > .category-link")
    FoodItemList = []
    for eachFoodDoc in FoodList.items():
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
                    FoodDict["price"] = float(eachFoodDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                FoodItemList.append(FoodDict)
                #print(FoodDict)
            FoodPage+=1
            if len(Fooditem) == 0:
                break
            FoodResurl=FoodRes.url+'?q=%3Aprice-desc&page=0'
            NextFoodRes = requests.get(FoodResurl[0:-1]+str(FoodPage))
            NextFoodDoc = pq(NextFoodRes.text)
    costcoList += FoodItemList
    
    # house
    HouseholdPetSuppliesRes = requests.get("https://www.costco.com.tw/Household-Pet-Supplies/c/14")
    HouseholdPetSuppliesDoc = pq(HouseholdPetSuppliesRes.text)
    HouseList = HouseholdPetSuppliesDoc(".category-wrapper > .category-node > .category-link")
    HouseItemList = []
    for eachHouseDoc in HouseList.items():
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
                    HouseDict["price"] = float(eachHouseDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                HouseItemList.append(HouseDict)
                #print(HouseDict)
            HousePage+=1
            if len(Houseitem) == 0:
                break
            HouseResurl=HouseRes.url+'?q=%3Aprice-desc&page=0'
            NextHouseRes = requests.get(HouseResurl[0:-1]+str(HousePage))
            NextHouseDoc = pq(NextHouseRes.text)
    costcoList += HouseItemList
    
    # kitchen
    HomeKitchenRes = requests.get("https://www.costco.com.tw/Home-Kitchen/c/6")
    HomeKitchenDoc = pq(HomeKitchenRes.text)
    HomeList = HomeKitchenDoc(".category-wrapper > .category-node > .category-link")
    HomeItemList = []
    for eachHomeDoc in HomeList.items():
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
                    HomeDict["price"] = float(eachHomeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                HomeItemList.append(HomeDict)
                #print(HomeDict)
            HomePage+=1
            if len(Homeitem) == 0:
                break
            HomeResurl=HomeRes.url+'?q=%3Aprice-desc&page=0'
            NextHomeRes = requests.get(HomeResurl[0:-1]+str(HomePage))
            NextHomeDoc = pq(NextHomeRes.text)
    costcoList += HomeItemList
    
    # clothing
    ClothingAccessoriesLuggageRes = requests.get("https://www.costco.com.tw/Clothing-Accessories-Luggage/c/9")
    ClothingAccessoriesLuggageDoc = pq(ClothingAccessoriesLuggageRes.text)
    ClothingList = ClothingAccessoriesLuggageDoc(".category-wrapper > .category-node > .category-link")
    ClothingItemList = []
    for eachClothingDoc in ClothingList.items():
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
                    ClothingDict["price"] = float(eachClothingDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                ClothingItemList.append(ClothingDict)
                #print(ClothingDict)
            ClothingPage+=1
            if len(Clothingitem) == 0:
                break
            ClothingResurl=ClothingRes.url+'?q=%3Aprice-desc&page=0'
            NextClothingRes = requests.get(ClothingResurl[0:-1]+str(ClothingPage))
            NextClothingDoc = pq(NextClothingRes.text)
    costcoList += ClothingItemList
    
    # furniture
    FurnitureBeddingRes = requests.get("https://www.costco.com.tw/Furniture-Bedding/c/5")
    FurnitureBeddingDoc = pq(FurnitureBeddingRes.text)
    FurnitureList = FurnitureBeddingDoc(".category-wrapper > .category-node > .category-link")
    FurnitureItemList = []
    for eachFurnitureDoc in FurnitureList.items():
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
                    FurnitureDict["price"] = float(eachFurnitureDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                FurnitureItemList.append(FurnitureDict)
                #print(FurnitureDict)
            FurniturePage+=1
            if len(Furnitureitem) == 0:
                break
            FurnitureResurl=FoodRes.url+'?q=%3Aprice-desc&page=0'
            NextFurnitureRes = requests.get(FurnitureResurl[0:-1]+str(FurniturePage))
            NextFurnitureDoc = pq(NextFurnitureRes.text)
    costcoList += FurnitureItemList
    
    # homeImprove
    HomeImprovementRes = requests.get("https://www.costco.com.tw/Home-Improvement/c/13")
    HomeImprovementDoc = pq(HomeImprovementRes.text)
    HomeImproList = HomeImprovementDoc(".category-wrapper > .category-node > .category-link")
    HomeImproItemList = []
    for eachHomeImproDoc in HomeImproList.items():
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
                    HomeImproDict["price"] = float(eachHomeImproDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                HomeImproItemList.append(HomeImproDict)
                #print(HomeImproDict)
            HomeImproPage+=1
            if len(HomeImproitem) == 0:
                break
            HomeImproResurl=HomeImproRes.url+'?q=%3Aprice-desc&page=0'
            NextHomeImproRes = requests.get(HomeImproResurl[0:-1]+str(HomeImproPage))
            NextHomeImproDoc = pq(NextHomeImproRes.text)
    costcoList += HomeImproItemList
    
    # auto
    AutomotiveTireRes = requests.get("https://www.costco.com.tw/Automotive-Tire/c/18")
    AutomotiveTireDoc = pq(AutomotiveTireRes.text)
    AutoList = AutomotiveTireDoc(".category-wrapper > .category-node > .category-link")
    AutoItemList = []
    for eachAutoDoc in AutoList.items():
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
                    AutoDict["price"] = float(eachAutoDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
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
    costcoList += AutoItemList
    
    # fitness
    SportFitnessRes = requests.get("https://www.costco.com.tw/Sport-Fitness/c/11")
    SportFitnessDoc = pq(SportFitnessRes.text)
    SportList = SportFitnessDoc(".category-wrapper > .category-node > .category-link")
    SportItemList = []
    for eachSportDoc in SportList.items():
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
                    SportDict["price"] = float(eachSportDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                SportItemList.append(SportDict)
                #print(SportDict)
            SportPage+=1
            if len(Sportitem) == 0:
                break
            SportResurl=SportRes.url+'?q=%3Aprice-desc&page=0'
            NextSportRes = requests.get(SportResurl[0:-1]+str(SportPage))
            NextSportDoc = pq(NextSportRes.text)
    costcoList += SportItemList
    
    # garden
    LawnGardenRes = requests.get("https://www.costco.com.tw/Lawn-Garden/c/4")
    LawnGardenDoc = pq(LawnGardenRes.text)
    LawnList = LawnGardenDoc(".category-wrapper > .category-node > .category-link")
    LawnItemList = []
    for eachLawnDoc in LawnList.items():
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
                    LawnDict["price"] = float(eachLawnDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                LawnItemList.append(LawnDict)
                #print(LawnDict)
            LawnPage+=1
            if len(Lawnitem) == 0:
                break
            LawnResurl=LawnRes.url+'?q=%3Aprice-desc&page=0'
            NextLawnRes = requests.get(LawnResurl[0:-1]+str(LawnPage))
            NextLawnDoc = pq(NextLawnRes.text)
    costcoList += LawnItemList
    
    # office
    OfficeSuppliesBooksRes = requests.get("https://www.costco.com.tw/Office-Supplies-Books/c/17")
    OfficeSuppliesBooksDoc = pq(OfficeSuppliesBooksRes.text)
    OfficeList = OfficeSuppliesBooksDoc(".category-wrapper > .category-node > .category-link")
    OfficeItemList = []
    for eachOfficeDoc in OfficeList.items():
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
                    OfficeDict["price"] = float(eachOfficeDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                OfficeItemList.append(OfficeDict)
                #print(OfficeDict)
            OfficePage+=1
            if len(Officeitem) == 0:
                break
            OfficeResurl=OfficeRes.url+'?q=%3Aprice-desc&page=0'
            NextOfficeRes = requests.get(OfficeResurl[0:-1]+str(OfficePage))
            NextOfficeDoc = pq(NextOfficeRes.text)
    costcoList += OfficeItemList
    
    # gift
    GiftsTicketsFloralRes = requests.get("https://www.costco.com.tw/Gifts-Tickets-Floral/c/16")
    GiftsTicketsFloralDoc = pq(GiftsTicketsFloralRes.text)
    GiftsList = GiftsTicketsFloralDoc(".category-wrapper > .category-node > .category-link")
    GiftsItemList = []
    for eachGiftsDoc in GiftsList.items():
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
                    GiftsDict["price"] = float(eachGiftsDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                GiftsItemList.append(GiftsDict)
                #print(GiftsDict)
            GiftsPage+=1
            if len(Giftsitem) == 0:
                break
            GiftsResurl=GiftsRes.url+'?q=%3Aprice-desc&page=0'
            NextGiftsRes = requests.get(GiftsResurl[0:-1]+str(GiftsPage))
            NextGiftsDoc = pq(NextGiftsRes.text)
    costcoList += GiftsItemList
    
    # jewel
    JewelryWatchesOpticalsRes = requests.get("https://www.costco.com.tw/Jewelry-Watches-Opticals/c/10")
    JewelryWatchesOpticalsDoc = pq(JewelryWatchesOpticalsRes.text)
    JewelryList = JewelryWatchesOpticalsDoc(".category-wrapper > .category-node > .category-link")
    JewelryItemList = []
    for eachJewelryDoc in JewelryList.items():
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
                    JewelryDict["price"] = float(eachJewelryDoc(".product-info-wrapper >.price-panel >.product-price >.original-price >span:nth-child(1)").text().replace('$', ''))
                JewelryItemList.append(JewelryDict)
                #print(JewelryDict)
            JewelryPage+=1
            if len(Jewelryitem) == 0:
                break
            JewelryResurl=JewelryRes.url+'?q=%3Aprice-desc&page=0'
            NextJewelryRes = requests.get(JewelryResurl[0:-1]+str(JewelryPage))
            NextJewelryDoc = pq(NextJewelryRes.text)
    costcoList += JewelryItemList
    
    # 終於弄完了XD
    return costcoList

def startToCrawl():
    global carrefourList
    global costcoList
    global RTMartList
    carrefourList = crawlCarrefour()
    costcoList = crawlCostco()
    RTMartList = crawlRTMart()
    main()

def main():
    
    # define mainSearch()
    def mainSearch():
        
        # define retry() and end()
        def retry():
            mainWindow.destroy()
            main()
        def end():
            mainWindow.destroy()
        
        target = searchEntry.get()
        
        # search carrefour
        carrefourAfterSearch = []
        for carrefour in carrefourList:
            if(target in carrefour['title']):
                carrefourAfterSearch.append(carrefour)
        
        # search RT-mart
        RTMartAfterSearch = []
        for RTMart in RTMartList:
            if(target in RTMart['title']):
                RTMartAfterSearch.append(RTMart)
        
        # search costco
        costcoAfterSearch = []
        for costco in costcoList:
            try:
                if(target in costco['title']):
                    costcoAfterSearch.append(costco)
            except TypeError:
                continue
        
        # carrefour frame
        carrefourFrame = tk.Frame(mainWindow)
        carrefourFrame.configure(width=250)
        carrefourFrame.pack(side=tk.LEFT)
        carrefourMessage = tk.Message(carrefourFrame, text='家樂福')
        carrefourMessage.pack()
        lowestPrice = []
        for i in range(5):
            mini = 900000000
            miniTitle = ''
            for each in carrefourAfterSearch:
                if (each['price'] < mini):
                    mini = each['price']
                    miniTitle = each['title']
            for each in carrefourAfterSearch:
                if (each['title'] == miniTitle):
                    lowestPrice.append(each.copy())
                    each['price'] = 900000000
                    break
        carrefourAfterSearch = []
        for each in lowestPrice:
            frame = tk.Frame(carrefourFrame)
            frame.pack()
            titleMessage = tk.Message(frame, text=each['title'])
            titleMessage.pack(side=tk.LEFT)
            priceMessage = tk.Message(frame, text=each['price'])
            priceMessage.pack(side=tk.RIGHT)
            del titleMessage, priceMessage, frame
        
        # RT-mart frame
        RTMartFrame = tk.Frame(mainWindow)
        RTMartFrame.configure(width=250)
        RTMartFrame.pack(side=tk.LEFT)
        RTMartMessage = tk.Message(RTMartFrame, text='大潤發')
        RTMartMessage.pack()
        lowestPrice = []
        for i in range(5):
            mini = 900000000
            miniTitle = ''
            for each in RTMartAfterSearch:
                if (each['price'] < mini):
                    mini = each['price']
                    miniTitle = each['title']
            for each in RTMartAfterSearch:
                if (each['title'] == miniTitle):
                    lowestPrice.append(each.copy())
                    each['price'] = 900000000
                    break
        RTMartAfterSearch = []
        for each in lowestPrice:
            frame = tk.Frame(RTMartFrame)
            frame.pack()
            titleMessage = tk.Message(frame, text=each['title'])
            titleMessage.pack(side=tk.LEFT)
            priceMessage = tk.Message(frame, text=each['price'])
            priceMessage.pack(side=tk.RIGHT)
            del titleMessage, priceMessage, frame
        
        # costco frame
        costcoFrame = tk.Frame(mainWindow)
        costcoFrame.configure(width=250)
        costcoFrame.pack(side=tk.LEFT)
        costcoMessage = tk.Message(costcoFrame, text='Costco')
        costcoMessage.pack()
        lowestPrice = []
        for i in range(5):
            mini = 900000000
            miniTitle = ''
            for each in costcoAfterSearch:
                try:
                    if (each['price'] < mini):
                        mini = each['price']
                        miniTitle = each['title']
                except TypeError:
                    continue
            for each in costcoAfterSearch:
                try:
                    if (each['title'] == miniTitle):
                        lowestPrice.append(each.copy())
                        each['price'] = 900000000
                        break
                except TypeError:
                    continue
        costcoAfterSearch = []
        for each in lowestPrice:
            frame = tk.Frame(costcoFrame)
            frame.pack()
            titleMessage = tk.Message(frame, text=each['title'])
            titleMessage.pack(side=tk.LEFT)
            priceMessage = tk.Message(frame, text=each['price'])
            priceMessage.pack(side=tk.RIGHT)
            del titleMessage, priceMessage, frame
        
        # button frame
        buttonFrame = tk.Frame(mainWindow)
        buttonFrame.pack()
        retryButton = tk.Button(buttonFrame, text='再來一次', command=retry)
        retryButton.pack(side=tk.LEFT)
        endButton = tk.Button(buttonFrame, text='結束', command=end)
        endButton.pack(side=tk.RIGHT)
    
    # mainWindow
    mainWindow = tk.Tk()
    mainWindow.title('家樂福、大潤發、Costco比價 - 爬取完成')
    mainWindow.geometry('800x700')
    mainWindow.configure(background='white')

    mainMessage = tk.Message(mainWindow, text='已成功完成資料爬取！')
    mainMessage.configure(width=400, font=36)
    mainMessage.pack()

    # searchFrame
    searchFrame = tk.Frame(mainWindow)
    searchFrame.pack()
    searchLabel = tk.Label(searchFrame, text='欲搜尋之商品名：')
    searchLabel.configure(font=36)
    searchLabel.pack(side=tk.LEFT)
    searchEntry = tk.Entry(searchFrame)
    searchEntry.pack(side=tk.RIGHT)

    mainButton = tk.Button(mainWindow, text='開始比價！', command=mainSearch)
    mainButton.configure(font=36)
    mainButton.pack()
    mainWindow.mainloop()

# crawlWindow
crawlWindow = tk.Tk()
crawlWindow.title('家樂福、大潤發、Costco比價 - 爬取頁面')
crawlWindow.geometry('800x600')
crawlWindow.configure(background='white')

# Title
title = tk.Message(crawlWindow, text='家樂福、大潤發、Costco比價')
title.configure(width=400, font=44)
title.pack()

# How to use
howToUse = tk.Message(crawlWindow, text='按下"開始爬蟲"按鈕開始爬資料，請靜待爬取完畢(總耗時約20~30分鐘)。                                接下來便可輸入欲查詢之商品名稱，我們會把商品資料呈現出來，供使用者參考。                                重要注意事項：                                \n                                \n1.使用前請務必確認webdriver檔案位置是否正確。                                2.使用前請確認網路連線狀況良好，否則可能因連線問題導致執行失敗。')
howToUse.configure(width=750, font=36)
howToUse.pack()

startButton = tk.Button(crawlWindow, text='開始爬蟲', command=startToCrawl)
startButton.configure(font=36)
startButton.pack()

crawlWindow.mainloop()