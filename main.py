from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from pynput.keyboard import Key, Controller
keyboard = Controller() 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) 

driver = webdriver.Chrome(options=chrome_options)
body = driver.find_element(By.TAG_NAME,"body")
driver.get("https://www.monkeytype.com")
time.sleep(2)
accept_all = driver.find_element(by=By.CSS_SELECTOR,value=".active.acceptAll")
accept_all.click()
while True:

    words = driver.find_element(by=By.CSS_SELECTOR,value=".word.active")
    current_word =words.text
    
    for char in current_word:
        keyboard.press(char)
        time.sleep(0.02)
    time.sleep(0.05)
    keyboard.press(Key.space)
    keyboard.release(Key.space)