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

import pandas as pd




import subprocess

import random
import os










def access():

    chrome_options = Options() 
    
    chrome_options.add_argument('--user-data-dir=H:/Projects/NYTRIP/User Data')
    chrome_options.add_argument('--profile-directory=Profile 3')
    
    driver = webdriver.Chrome()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usag')
    
    #Gets rid of errors \ selenium hook log bs
    
    #Makes it go Slightly faster, I  


    #Makes it go Slightly faster, I think
    
    
     
    #Search Filter
    #query = "immigration" # Query 
    
    #query = "Poland%3B+asylum"
    
    #end_date = "20230119" #Year | #Month | #Day 
    #End Date
    #start_date = "20170819" #Year | #Month | #Day
    
    #end_date = EndDateInput
    #start_date = StartDateInput
    #2023|01|19
    #site_access = ("https://www.nytimes.com/search?dropmab=false&endDate={}&query={}&sort=oldest&startDate={}".format(end_date, query, start_date))
    
    site_access = "https://twitter.com/explore/tabs/trending"
    
    print(site_access)
    driver.get(site_access)
    time.sleep(200)
    
    veri = 1
    s = 0
    article_grab = 0
    
    spreadsheetcont = 0
    
    
    print('terminate')

access()

