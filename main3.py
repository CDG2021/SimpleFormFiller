from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriverPath = "G:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element_by_name("fName")
name.send_keys("Bob")

lName = driver.find_element_by_name("lName")
lName.send_keys("May")

emailA = driver.find_element_by_name("email")
emailA.send_keys("Bob@56.com")

signUp = driver.find_element_by_class_name("btn")
signUp.click()
    
sleep(5)
driver.quit()