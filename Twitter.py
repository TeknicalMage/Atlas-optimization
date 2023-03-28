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
    
    options = Options()
    options.page_load_strategy = 'normal'
    

    options.add_argument('--log-level=3')
    options.add_argument('--disable-dev-shm-usag')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-buffer-bw-compression")
    options.add_argument("--enable-background-thread-pool")
    options.add_argument("--in-process-gpu")
    options.add_argument("--mute-audio")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    

    #2023|01|19
    site_access = ("https://twitter.com/search?q=%23{}&src=trend_click&vertical=trends").format('TrumpArrest')
    last_height = driver.execute_script("return document.body.scrollHeight")

    
    action = ActionChains(driver)
    driver.get(site_access)

    endloop = 0

    iteratem = 1

    #Url iteration
    urlitr = 1
    #Url iteration
    time.sleep(1)

    Biglist = []

    while endloop < 400:
        endloop+=1
        val = 0
        while val < 10:
            action.key_down(Keys.ARROW_DOWN).perform()
            action.key_down(Keys.ARROW_DOWN).perform()
            action.key_down(Keys.ARROW_DOWN).perform()
            val+=1
           
        try:
            action.key_down(Keys.ESCAPE).perform() 
            itr64 = 0
            while True:
                doc = (driver.find_elements(By.XPATH, '//*[@class="css-1dbjc4n r-eqz5dr r-16y2uox r-1wbh5a2"]//*[@class="css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')[itr64]).get_attribute("innerHTML")
                #print(doc)
                itr64+=1

                try:
                    doc = doc.replace('<span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('</span>', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<div class="css-1dbjc4n r-xoduu5">', '')
                except:
                    pass
                try:
                    doc = doc.replace('<a dir="ltr" href="/Gartner_inc" role="link" class="css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1cvl2hr r-1loqt21 r-poiln3 r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<span class="r-18u37iz">', '')
                except:
                    pass
                try:
                    doc = doc.replace('<span class="r-18u37iz"><a dir="ltr"', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<span class="css-901oao css-16my406 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0"><a dir="ltr"', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<a dir="ltr"', '' )
                except:
                    pass
                try:
                    doc = doc.replace('class="css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1cvl2hr r-1loqt21 r-poiln3 r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('class="css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1cvl2hr r-1loqt21 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<span class="css-901oao css-16my406 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('class="r-4qtqp9 r-dflpy8 r-sjv1od r-zw8f10 r-10akycc r-h9hxbl">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('<span aria-hidden="true" class="css-901oao css-16my406 r-poiln3 r-hiw28u r-qvk6io r-bcqeeo r-qvutc0">', '' )
                except:
                    pass
                try:
                    doc = doc.replace('</a>', '' )
                except:
                    pass
                try:
                    doc = doc.replace('</a>', '' )
                except:
                    pass
                


            
                if doc in Biglist:
                    pass
                    
                else:
                    Biglist.append(doc)
                    print(doc)

                

                

        except:
            pass

        print(endloop)
            


    time.sleep(1)
    print(Biglist)
    

   
    
    


start_time = time.time()
access()
print("--- %s seconds ---" % (time.time() - start_time))
print()

 


