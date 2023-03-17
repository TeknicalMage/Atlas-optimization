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



def access():


    
    chrome_options = Options() 
    
        
    driver = webdriver.Chrome()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usag')
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-buffer-bw-compression")
    chrome_options.add_argument("--enable-background-thread-pool")
    chrome_options.add_argument("--in-process-gpu")
    
    
    #2023|01|19
    site_access = ("https://www.reddit.com/r/AskReddit/comments/11r9k9u/whats_the_best_comedy_movie_you_have_ever_watched/")
    last_height = driver.execute_script("return document.body.scrollHeight")

    
    
    driver.get(site_access)
    
    
    number = 1
    
    while number < 300:
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

    
    iter = 1
    while True: 
        try:
            texthandle = (driver.find_elements(By.XPATH, '//*[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]')[iter]).get_attribute("innerHTML")
            username = (driver.find_elements(By.XPATH, '//*[@class="wM6scouPXXsFDSZmZPHRo DjcdNGtVXPcxG0yiFXIoZ _23wugcdiaj44hdfugIAlnX "]')[iter]).get_attribute("href")
            x1 = texthandle.replace('<p class="_1qeIAgB0cPwnLhDF9XSiJM">', '' )
            texthandle = x1.replace('</p class="_1qeIAgB0cPwnLhDF9XSiJM">', '' )
            x1 = texthandle.replace('</p>', '' )
            texthandle = x1.replace('<p>', '' )
            iter+=1
            print(username + "\n" + texthandle + "\n")
        except:
            break
   
    
   
    
    

start_time = time.time()
access()
print("--- %s seconds ---" % (time.time() - start_time))



 


