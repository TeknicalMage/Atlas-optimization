import sys
import getopt
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

import pymongo
from pymongo import MongoClient

cluster= 
db = cluster ["Youtube-test"]
collection  = db["test"]


  
def full_name():
    first_name = None
  
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "f:")
      
    except:
        print("Error")
  
    for opt, arg in opts:
            first_name = arg
    print(first_name)

    urlstring = str(first_name)

    time.sleep(5)

    Posts = []
    
    options = Options()
   
    

    options.add_argument('--log-level=3')
    options.add_argument('--disable-dev-shm-usag')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-buffer-bw-compression")
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-background-thread-pool")
    options.add_argument("--in-process-gpu")
    options.add_argument("--mute-audio")
    options.add_argument("--process-per-tab")


    driver = webdriver.Chrome(options=options)
    
    
    #2023|01|19
    site_access = (urlstring)
    
    
    action = ActionChains(driver)
    driver.implicitly_wait(6)

    driver.get(site_access)
    
  
    keywords = (driver.find_elements(By.XPATH, '//*[@name="keywords"]')[0]).get_attribute("content")
    Title = (driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-watch-metadata"]/h1')[0]).get_attribute("innerText")
    

    Likes = (driver.find_elements(By.XPATH, '//*[@class="factoid-value style-scope ytd-factoid-renderer"]')[0]).get_attribute("innerText")
    Views = (driver.find_elements(By.XPATH, '//*[@class="factoid-value style-scope ytd-factoid-renderer"]')[1]).get_attribute("innerText")
    Date = (driver.find_elements(By.XPATH, '//*[@class="factoid style-scope ytd-factoid-renderer"]')[2]).get_attribute("aria-label") 
 
    
     

    print(keywords)
    print(Title)
    print(Likes)
    print(Views)
    print(Date)

    #post = {"Keywords": keywords, "Title": Title, "Likes": Likes, "Views": Views, "Date": Date}
    #collection.insert_one(post)



    
    endloop = 1
    driver.implicitly_wait(0.0001)
    while endloop < 4000:
        try:
            action.key_down(Keys.ARROW_DOWN).perform()
            print(endloop)
            endloop+=1
        except:
            pass


    thecomments = (driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-comment-thread-renderer"]//*[@id="content-text"]'))

    totalcount = 0

    listo = (len(thecomments))
    while totalcount < listo:
        
        commenter = (driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-comment-thread-renderer"]//*[@id="author-text"]/span')[totalcount]).get_attribute("innerHTML") 
        valsingular = (driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-comment-thread-renderer"]//*[@id="content-text"]')[totalcount]).get_attribute("innerHTML") 
        #Posts.append(valsingular)
        comment = valsingular.replace(" ", "")
        #print(commenter)
        #print(comment)
        totalcount+=1

        post_comment = {"commenter": commenter, "comment": comment}
        collection.insert_one(post_comment)




  
full_name()    