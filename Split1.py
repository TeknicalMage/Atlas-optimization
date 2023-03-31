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

import pymongo
from pymongo import MongoClient

import re


cluster= MongoClient("mongodb+srv://macrollcofficial:IrytsrNRSTaQestB@macrocluster.wqpdnof.mongodb.net/?retryWrites=true&w=majority")
db = cluster ["Youtube-test"]
collection  = db["test"]

commentstack = {

    }
    
  
def full_name():

    
    first_name = None
  
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "l:")
      
    except:
        print("Error")
  
    for opt, arg in opts:
            first_name = arg
    print(first_name)

    urlstring = str(first_name)

    time.sleep(3)

    Posts = []
    
    options = Options()
   
    

    options.add_argument('--log-level=3')
    #options.add_argument('--disable-dev-shm-usag')
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--disable-buffer-bw-compression")
    options.add_argument("--disable-extensions")
    #options.add_argument("--enable-background-thread-pool")
    #options.add_argument("--in-process-gpu")
    options.add_argument("--mute-audio")
    options.add_argument("--start-maximized")

    #options.add_argument("--process-per-tab")


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

    
    
    dicton_vid_info = {"keywords" : keywords, "Title" : Title, "Likes" : Likes, "Views" : Views, "Date" : Date} 
    commentstack.update(dicton_vid_info)
    
    endloop = 0
     
    driver.implicitly_wait(0.0)
    while endloop < 3500:
        try:
            action.key_down(Keys.END).perform()
            print(endloop)
            endloop+=1
            
        except:
            pass

    
    totalcount = 0

    


    thecomments = (driver.find_elements(By.XPATH, '//*[@class="style-scope ytd-comment-thread-renderer"]//*[@id="content-text"]'))
    
 
    listo = (len(thecomments))
    while totalcount != listo:
        macrovar = (driver.find_elements(By.XPATH, '//ytd-item-section-renderer[@section-identifier="comment-item-section"]/div[@id="contents"]//*[@id="body"]//div[@id="main"]//div[@id="comment-content"]')[totalcount]).get_attribute("innerHTML")  
        

        macrovar = (macrovar.replace('<span dir="auto" class="style-scope yt-formatted-string">', ''))
        macrovar = (macrovar.replace('</span>', ''))
        macrovar = (macrovar.replace('slot="content" split-lines="" user-input="" class="style-scope ytd-comment-renderer">', ''))
        macrovar = (macrovar.replace('<a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false">', ''))
        macrovar = (macrovar.replace('<tp-yt-paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" style-target="host" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->', ''))
        macrovar = (macrovar.replace('<span class="less-button style-scope ytd-comment-renderer" slot="less-button">Show less', ''))
        macrovar = (macrovar.replace('</tp-yt-paper-button>', ''))
        macrovar = (macrovar.replace('<tp-yt-paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" hidden="" style-target="host" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->', ''))
        macrovar = (macrovar.replace('<span class="more-button style-scope ytd-comment-renderer" slot="more-button">Read more', ''))
        macrovar = (macrovar.replace('</tp-yt-paper-button>', ''))
        #macrovar = (macrovar.replace('</yt-formatted-string>', ''))
        #macrovar = (macrovar.replace('</ytd-expander>', ''))


        s = macrovar
        start = '<yt-formatted-string id="content-text'
        end = '</span></yt-formatted-string>'
        macrovar = (s[s.find(start)+len(start):s.rfind(end)])
        
        macrovar = "\n".join([ll.rstrip() for ll in macrovar.splitlines() if ll.strip()])
        dummyval = str(totalcount)


        dicton_commentstack = {dummyval : macrovar}
        commentstack.update(dicton_commentstack) 

        print(totalcount)
        print(macrovar)

        totalcount+=1

        commentstack.update(dicton_commentstack) 

        

    print("Pushing Comments")
    collection.insert_one(commentstack)
        




  
full_name()    

