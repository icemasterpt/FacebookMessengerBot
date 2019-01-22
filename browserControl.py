from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import time
import config


class bot:
    def __init__(self):
        self.drive = webdriver.Firefox()
    def exit_panic(self):
        print("Exiting bot! Panic!")
        self.drive.quit()
        
    def getCurrentUrl(self):
        return self.drive.current_url
    def isInPartialURL(self,partialText):
        curr_url = self.getCurrentUrl()
        if partialText in str(curr_url):
            return True
        else:
            return False

        
        

    def loadPage(self,url):
        print("changing url to "+str(url))
        self.drive.get(url)

    def writeonBox(self,xpath,text):
        try:
            k = self.drive.find_element_by_xpath(xpath)
            print("trying to write on " +str(xpath))
            k.send_keys(text)
        except:
            print("error, can't find element")
            self.exit_panic()

    def pressButton(self,xpath):
        try:
            button = self.drive.find_element_by_xpath(xpath)
            print("Clicking on: "+str(xpath))
            button.click()
        except:
            print("Error, button not found! :"+str(xpath))
            self.exit_panic()
        
    def getContactName(self,index):
        xpath = config.cNameLocation
        try:
            print("getting name from xpath: " + xpath)
            a = self.drive.find_element_by_xpath(xpath)
            return str(a.getText())
        except:
            print("Cant find contact with index "+ str(index))
            self.exit_panic()
    
            
    def clickOnContactbyIndex(self,index):
        xpath = config.aNameStart + str(index) + config.aNameEnd
        try:
            print("getting name from xpath: " + xpath)
            a = self.drive.find_element_by_xpath(xpath)
            a.click()
        except:
            print("Cant click "+ str(index))
            self.exit_panic()




    
  
 
    
      
        

            
            



