import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui

#---------------------------BeautifulSoup--------------------------------#

r=requests.get("http://www.nisb.in")
soup=BeautifulSoup(r.text,'html.parser')
img=[]
img=soup.findAll("img",{"class":"img-thumbnail col-md-4"})
for link in img:
    image=link.get("src")
    imgname=os.path.split(image)[1]
    qm=imgname.find("?")
    imgname=imgname[:qm]
    # r2=requests.get(image)
    # with open(imgname,"wb") as f:
    #     f.write(r2.read)
    # f.close()
    print(imgname)

#---------------------------Selenium--------------------------------#

    driver=webdriver.Firefox()
    driver.get(image)
    time.sleep(5)
    actionChains = ActionChains(driver)
    search=driver.find_element_by_xpath("/html/body/img")
    actionChains.context_click(search).perform()

#---------------------------pyautogui--------------------------------#

    pyautogui.FAILSAFE = True
    pyautogui.typewrite(['down','down','down','enter'])
    time.sleep(3)
    pyautogui.moveTo(410,60,duration=2)
    pyautogui.click(410,60)
    location="C:\\users\\raish\\desktop\\python\\nisbinaug\\images"
    pyautogui.typewrite(location,0.25)
    time.sleep(2)
    pyautogui.typewrite(['enter'])
    time.sleep(3)
    pyautogui.moveTo(895,570,duration=2)
    pyautogui.click(895,570)
    #pyautogui.typewrite(['enter'])
    time.sleep(2)
    #pyautogui.typewrite(['enter'])
    driver.close()
    time.sleep(2)
