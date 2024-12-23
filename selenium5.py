# Взлом Кодового Замка: Откройте веб-сайт с помощью Selenium.
# Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
# Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
# Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.

import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/4/4.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
    for checkbox in checkboxes:
        checkbox.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    res = browser.find_element(By.ID, 'result').text
    print(res)
    time.sleep(10)
pyperclip.copy(str(res))


