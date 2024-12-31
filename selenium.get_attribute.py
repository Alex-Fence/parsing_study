
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/2/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    txt_fields_lst = browser.find_elements(By.CLASS_NAME, 'text-field')
    for txt_field in txt_fields_lst:
        if not txt_field.get_attribute('disabled'):
            txt_field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    alert = browser._switch_to.alert
    pyperclip.copy(alert.text)
    print(alert.text)
    time.sleep(10)