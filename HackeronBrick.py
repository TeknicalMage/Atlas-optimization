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
    
    searchq = input()
    start_time = time.time()
    #2023|01|19
    site_access = ("https://hackerone.com/opportunities/all/search?bbp=&vdp=&private=&high_response_efficiency=&managed=&offers_retesting=&bounty_splitting=&credentials=&new=&updated=&category=&active_campaign=&gold_standard=&tech=&industries=&asset_types=&ordering=Newest+programs&search=&minimum_low_checked=&minimum_medium_checked=&minimum_high_checked=&minimum_critical_checked=&minimum_low_value=&minimum_medium_value=&minimum_high_value=&minimum_critical_value=")
    last_height = driver.execute_script("return document.body.scrollHeight")

    
    
    driver.get(site_access)
    
    
    number = 1
    
    while number < 2000:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")
        except:
            pass
        if new_height == last_height:
            pass
        last_height = new_height
        number+=1 
        print(number)

    ########################################################################################

    time.sleep(1)
    iter = 1
    while True: 
        try:
            posturl_var = (driver.find_elements(By.XPATH, '//*[@class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"]/div/div/div/a')[iter]).get_attribute("href")
            subredditname_var = (driver.find_elements(By.XPATH, '//*[@data-testid="subreddit-name"]')[iter]).get_attribute("href")
            username_var = (driver.find_elements(By.XPATH, '//*[@class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE"]')[iter]).get_attribute("href")
            
            votes_var = (driver.find_elements(By.XPATH, '//*[@class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"]')[iter]).get_attribute("innerHTML")
            
            edit = votes_var.replace('<span class="_vaFo96phV6L5Hltvwcox">', '' )
            votes_var = edit.replace("</span>", "")
            edit = votes_var.replace('<span class="_vaFo96phV6L5Hltvwcox">', "")
            votes_var = edit.replace('<span class="_vaFo96phV6L5Hltvwcox">', "")
            
            iter+=1
            thelist = [posturl_var, subredditname_var, username_var, votes_var]
            
            Posts.append(thelist)
            
            print(posturl_var + "\n" + subredditname_var + "\n" + username_var)
            print(votes_var)
        except:
            break
   
    
   
    
    

start_time = time.time()
start_time = time.time()
access()
print("--- %s seconds ---" % (time.time() - start_time))
print(Posts)

 


