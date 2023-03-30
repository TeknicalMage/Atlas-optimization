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

f = open('urllist.txt','w')

Posts = []


def access():
    
    options = Options()
    options.page_load_strategy = 'normal'
    

    options.add_argument('--log-level=3')
    #options.add_argument('--disable-dev-shm-usag')
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--disable-buffer-bw-compression")
    options.add_argument("--disable-extensions")
    #options.add_argument("--enable-background-thread-pool")
    #options.add_argument("--in-process-gpu")
    options.add_argument("--mute-audio")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    
    searchq = input()
    #2023|01|19
    site_access = ("https://www.youtube.com/results?search_query={}").format(searchq)
    last_height = driver.execute_script("return document.body.scrollHeight")

    
    action = ActionChains(driver)
    driver.get(site_access)
    
    
    endloop = 0

    iteratem = 1

    #Url iteration
    urlitr = 1
    #Url iteration

    while endloop < 3000:
        endloop+=1
        action.key_down(Keys.PAGE_DOWN).perform()
        print(endloop)

    top = (driver.find_elements(By.XPATH, '//*[@class="yt-simple-endpoint style-scope ytd-video-renderer"]'))
    urlcount = (len(top))
    print(urlcount)
    
    mainvalue = 0

    for mainvalue in range(urlcount):
        linkvar = (driver.find_elements(By.XPATH, '//*[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')[mainvalue]).get_attribute("href")

        #try:
            #id = (driver.find_elements(By.XPATH, '//*[@id="video-title"]')[mainvalue]).get_attribute("aria-label")
            #print(id)
        #except:
            #id = (driver.find_elements(By.XPATH, '//*[@id="video-title"]')[mainvalue]).get_attribute("innerText")
            #print(id)
            #pass


        f.write(linkvar + "\n")
        print(linkvar) 

        
        

    


    
    ########################################################################################

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
access()
print("--- %s seconds ---" % (time.time() - start_time))
print(Posts)

 


