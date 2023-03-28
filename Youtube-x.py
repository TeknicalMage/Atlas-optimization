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




def access():
    
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
    options.add_argument("--start-maximized")
    options.add_argument("--process-per-tab")


    driver = webdriver.Chrome(options=options)
    
    
    #2023|01|19
    site_access = ("https://www.youtube.com/watch?v=mU7s16OJs4o")
    
    
    action = ActionChains(driver)
    driver.implicitly_wait(4)

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



    
    endloop = 1
    driver.implicitly_wait(0.1)
    while endloop < 3000:
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
        valsingular = valsingular.replace(" ", "")
        print(commenter)
        print(valsingular)
        totalcount+=1

        
         
    print(Posts)
    
   
             
6
        

            
          


             
        

    


    
    ########################################################################################

    
   
    
   
    
    


start_time = time.time()
access()
print("--- %s seconds ---" % (time.time() - start_time))


 


