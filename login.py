#####################################################################################
##Author: Daniel Brown
##Purpose: An automated budgeting program because I'm tired of manually clicking crap
##         in google sheets >:(
##Please work!!
##Date: 10NOV18
#####################################################################################

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
##Specify the files that contain the key data for logging in:
user_file_handle=open("/mnt/c/Users/Daniel/Desktop/Authentication/user.txt")
userRead=user_file_handle.read()
pass_file_handle=open("/mnt/c/Users/Daniel/Desktop/Authentication/pass.txt")
passRead=pass_file_handle.read()
pin_file_handle=open("/mnt/c/Users/Daniel/Desktop/Authentication/pin.txt")
pinRead=pin_file_handle.read()


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
##If Driver in Windows location use the following:
#driver = webdriver.Chrome('C:/Users/daniel/Desktop/Bank-Project/chromedriver.exe')
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.usaa.com/")
wait = ui.WebDriverWait(driver, 5)
wait.until(page_is_loaded)

#def printFile(fileObject):
#    print fileObject.read()
#    fileObject.close()

logon_field = driver.find_element_by_id("usaa-my-profile")
#logon_field.send_keys(Keys.RETURN)

username_field = driver.find_element_by_id("usaaNum")
username_field.send_keys(userRead)
username_field.send_keys(Keys.TAB)

#password_field = driver.find_element_by_id("usaaPass")
password_field.send_keys(passRead)
#password_field.send_keys(Keys.RETURN)
wait.until(page_is_loaded)

pin_field = driver.find_element_by_id("pinTextField")
pin_field.send_keys(pinRead)
#pin_field.send_keys(Keys.RETURN)
wait.until(page_is_loaded)

user_file_handle.close()
pass_file_handle.close()
pin_file_handle.close()

question_field = driver.find_element_by_id("securityQuestionTextField")
question_field.send_keys("Anwser1")
#question_field.send_keys(keys.RETURN)
