from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import pandas as pd
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import csv
from urllib.request import urlopen
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.alert import Alert
def BOT1(request):
    if request.method=="GET":
        return render (request,'index.html')
    else:
        startrange=request.POST.get('startrange1')
        endange=request.POST.get('endrange1')
        print(startrange,endange)
        # return HttpResponse("done")
        
        sheet_url = "https://docs.google.com/spreadsheets/d/1oFRyFMn1L2-yRnspTMocLBDgZMPLOQeK8Vt68SbEjLA/edit#gid=0"
        url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=") 
        df=pd.read_csv(url_1)

        # print(type(df))

        driver=webdriver.Chrome(ChromeDriverManager().install())


        driver.get('http://faltawageexcel.stockexcel.com/pce_WagesEntry.aspx?PageID=DataEntry')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/input').send_keys('shubham')
        driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys('suv@123')
        driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys(Keys.ENTER)
        # for _ in range(3):
        time.sleep(2)
        actions = ActionChains(driver)
        alert = Alert(driver)


        # accept the alert
        alert.accept()

        driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys('suv@123')
        driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys(Keys.ENTER)
        # for i in range(2819,len(df['Buyer'].values.tolist())+1):
        for i in range(int(startrange),int(endange)):
        # for i in range(0,4):
            print(df['Buyer'][i],"index",i)
        
            driver.get('http://faltawageexcel.stockexcel.com/pce_WagesEntry.aspx?PageID=DataEntry')
            driver.maximize_window()

            # selecting buyer code ..
            # time.sleep(4)
            el = driver.find_element_by_id('ContentPlaceHolder1_ddlBuyerCode')
            # el = driver.find_element_by_id('id_of_select')
            for option in el.find_elements_by_tag_name('option'):
                if option.text == '{}'.format(df['Buyer'][i]):
                    option.click() # select() in earlier versions of webdriver
                    break

            time.sleep(4)
            print(int("00")+int(float((df['Order'][i]))),"OOOOOOOOOOOOOOOOOOOOOOOOO")
            # slecting order number code 
            if int(float(df['Order'][i]))<10:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(("00")+str(int(float(df['Order'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break
            elif 10<int(float(df['Order'][i]))<100:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(("0")+str(int(float(df['Order'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break        
            else:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(str(int(float(df['Order'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break        
            # worker code ......
            time.sleep(4)
            try:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlWorkerNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(str(int(float(df['Worker Code'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break
            except:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlWorkerNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(str((df['Worker Code'][i]))):
                        option.click() # select() in earlier versions of webdriver
                        break
                        
            # time.sleep(2)                 '/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[8]/td[1]/table/tbody/tr[1]/td[1]/input
            # driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[8]/td[1]/table/tbody/tr[1]/td[1]/input').send_keys(str(df['Worker Code'][i]))
            #item code.......
            time.sleep(4)
            el = driver.find_element_by_id('ContentPlaceHolder1_lstItem')
            # el = driver.find_element_by_id('id_of_select')
            if int(float(df['Item Code'][i]))<10:
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(("0")+str(int(float(df['Item Code'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break
            else:
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(str(int(float(df['Item Code'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break
                        
        
            # Operation No....
            time.sleep(5)
            el = driver.find_element_by_id('ContentPlaceHolder1_lstOperationNo')
            # el = driver.find_element_by_id('id_of_select')
            try:
                if int(float(df['Operation No'][i]))<10:
                    for option in el.find_elements_by_tag_name('option'):
                        if option.text == '{}'.format(("0")+str(int(float(df['Operation No'][i])))):
                            option.click() # select() in earlier versions of webdriver
                            break
                else:
                    for option in el.find_elements_by_tag_name('option'):
                        if option.text == '{}'.format(str(int(float(df['Operation No'][i])))):
                            option.click() # select() in earlier versions of webdriver
                            break        
            except:
                for option in el.find_elements_by_tag_name('option'):
                        if option.text == '{}'.format(str(df['Operation No'][i])):
                            option.click() # select() in earlier versions of webdriver
                            break       
            
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[7]/td[4]/table/tbody/tr[2]/td[1]/input').send_keys(str(int(float(df['Qty'][i]))))
            #Time taken:(min)......
            # time.sleep(1)                
            driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[7]/td[4]/table/tbody/tr[2]/td[2]/input').send_keys(str(df['Time'][i]))
            # Date......
            # time.sleep(2)
            driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[7]/td[4]/table/tbody/tr[4]/td[1]/input').clear()
            driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[7]/td[4]/table/tbody/tr[4]/td[1]/input').send_keys(str(df['Date'][i]))
            # driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr[7]/td[4]/table/tbody/tr[4]/td[2]/input').click()
            print("done",df['Worker Name'][i])
            time.sleep(4)

        return render (request,'index.html')