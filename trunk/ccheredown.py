#!/usr/bin/python

# download all the data from one ccthere thread
# input: maxpage for page number
#        threadnum for the thread
# output: each page is a single html file with everything except image

from selenium import webdriver
import codecs
import time 

maxpage = 248 
threadnum = "3109684"
linkaddr = "http://www.ccthere.com/thread/"

driver = webdriver.Firefox()

# this does not work, it will hang the procedure
# at the first page
# from selenium.webdriver import FirefoxProfile
# fp = FirefoxProfile()
# fp.set_preference("webdriver.load.strategy", "fast")
# driver = webdriver.Firefox(fp)

for i in range(1, maxpage+1):
  forumlink = linkaddr+threadnum+"/"+str(i)
  driver.get(forumlink) 
  f = codecs.open(str(i)+".html", 'w', "utf-8")
  f.write(driver.page_source)
  f.close()
  time.sleep(3)
driver.quit()
