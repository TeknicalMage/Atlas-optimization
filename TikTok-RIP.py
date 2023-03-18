import time
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.action_chains import ActionChains

import subprocess

import random
import os

Posts = []


def access():
    
    chrome_options = Options() 
    
        
    driver = webdriver.Chrome()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usag')
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-buffer-bw-compression")
    chrome_options.add_argument("--enable-background-thread-pool")
    chrome_options.add_argument("--in-process-gpu")
    chrome_options.add_argument("--mute-audio")

   
    #2023|01|19
    site_access = ("https://www.tiktok.com/tag/{}?lang=en").format("Elon")


    
    action = ActionChains(driver)
    driver.get(site_access)
    
    time.sleep(1)

  
    #print(posturl_var + "\n" + Titlename_tags)
    driver.find_elements(By.XPATH, '//*[@class="tiktok-yz6ijl-DivWrapper e1cg0wnj1"]/a')[0].click()
    while True: 
        internali = 0
        hashtagL = []
        try:
            while True:
                
                hashtag = (driver.find_elements(By.XPATH, '//*[@class="tiktok-ml44fi-DivText e1mzilcj1"]//a')[internali].get_attribute("href"))
                internali+=1
                hashtag = hashtag.replace("https://www.tiktok.com/tag/", "")
                hashtag = hashtag.replace("?lang=en", "")
                hashtagL.append(hashtag)

        except:
            pass

        likes = (driver.find_element(By.XPATH, '//*[@data-e2e="browse-like-count"]').get_attribute("innerText"))
        comments = (driver.find_element(By.XPATH, '//*[@data-e2e="browse-comment-count"]').get_attribute("innerText"))
        username = (driver.find_element(By.XPATH, '//*[@data-e2e="browser-nickname"]').get_attribute("innerText"))
        date = (driver.find_elements(By.XPATH, '//*[@data-e2e="browser-nickname"]/span')[1].get_attribute("innerText"))
        
        print("_")
        print(username)
        print(date)
        print(driver.current_url)
        print(hashtagL)
        print(likes)
        print(comments)
        print("_")
        action.key_down(Keys.ARROW_DOWN).perform() 
    
           
       
   
    
   
    
    

access()

