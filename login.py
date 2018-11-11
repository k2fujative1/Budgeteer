from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
##If Driver in Windows location use the following:
#driver = webdriver.Chrome('C:/Users/daniel/Desktop/Bank-Project/chromedriver.exe')
driver = webdriver.Chrome('/mnt/c/Users/daniel/Desktop/Bank-Project/chromedriver.exe')
driver.get("https://www.usaa.com/")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

logon_field = driver.find_element_by_id("usaa-my-profile")
logon_field.send_keys(Keys.RETURN)

username_field = driver.find_element_by_id("usaaNum")
username_field.send_keys("user")

password_field = driver.find_element_by_id("usaaPass")
password_field.send_keys("password")
password_field.send_keys(Keys.RETURN)
wait.until(page_is_loaded)

pin_field = driver.find_element_by_id("pinTextField")
pin_field.send_keys("pin")
pin_field.send_keys(Keys.RETURN)
wait.until(page_is_loaded)

question_field = driver.find_element_by_id("securityQuestionTextField")
question_field.send_keys("Anwser1")
question_field.send_keys(keys.RETURN)
