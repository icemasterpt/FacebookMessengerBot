import selenium.common
import selenium.webdriver
import browserControl
import os
import config
import time
clear = lambda: os.system('cls')



def main():
    f = 1

    bot = browserControl.bot()
    time.sleep(2)
    bot.loadPage(config.facebookLoginPage)
    time.sleep(2)
    curr_url = bot.getCurrentUrl()
    print("Current url is: " +curr_url)
    print("Let's try to login..")
    bot.writeonBox(config.xpath_login_email,config.bot_email)
    time.sleep(2)
    bot.writeonBox(config.xpath_login_passwrd,config.bot_password)
    print("done, let's do the rest")
    time.sleep(2)
    print("now we are going to press the login button and wait")
    bot.pressButton(config.xpath_login_button)
    while not bot.isInPartialURL(config.messengerPage):
        print("not in messenger page, changing....")
        bot.loadPage(config.messengerPage)
    while bot.isInPartialURL(config.messengerPage):
        print("we are in messenger page...")
        #wait few seconds
        time.sleep(2)
       
        #get all active conversations
        if f < 10:
            print("clicking on index " + str(f))
            bot.clickOnContactbyIndex(f)
            #name = bot.getContactName(f)
            #print("N: " +name)
            f += 1
        if f == 10:
            f = 1
        #Scan for new messages
        


        


main()