from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#This program is using Firefox as a webdriver
#This program only works on English Instagram Accounts, change the ''Log In''(#55236) and ''Not Now''(#66954) innerTexts to the language of your Instagram's account If it's not English.
driver = webdriver.Firefox()
driver.get("https://www.instagram.com")

user=input('Enter your username:')
passw=input('Enter your password:')
target=input("Enter the target's username:")

#Class names might change from Instagram's end, check them and restart the program if an error occurs
followerButtonClass='_acan _acap _acas'
followersContainerClass='_aano'


element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username = driver.find_element_by_name("username")
username.clear()
username.send_keys(user)


password= driver.find_element_by_name("password")
password.clear()
password.send_keys(passw)

#55236
submit=driver.find_element_by_xpath("//div[contains(text(),\
'Log In')]")
submit.click()

#66954
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),\
'Not Now')]")))  
    
driver.get("https://www.instagram.com/{}/followers/".format(target))

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='{}']".format(followerButtonClass))))
followers= driver.find_elements_by_xpath("//button[@class='{}']".format(followerButtonClass))

def scrolldown():
    
    blank=driver.find_element_by_xpath("//div[@class='{}']".format(followersContainerClass))
    blank.click()
    blank.send_keys(Keys.PAGE_DOWN)

    t.sleep(5)
    global followers
    followers= driver.find_elements_by_xpath("//button[@class='{}']".format(followerButtonClass))
    
    
    follow()

times=0
def follow():

  global times
  print(followers)
  for i in range(6):
    
    x=randint(1,3)
    follower= followers[i]
    t.sleep(x)
    follower.click()
    times+=1
    print('\n', times,'\n')
    if times==5:
        times=0
        scrolldown()
        

follow()
fp=input()