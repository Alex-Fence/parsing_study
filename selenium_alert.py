# На старт, внимание, марш!: Откройте указанную веб-страницу с помощью Selenium.
# Операция 'Чистый Лист': На странице расположены 100 текстовых полей с текстом.
# Ваша задача — пройтись по каждому и удалить его содержимое. Причём быстро, у вас всего 15 секунд!
# Завершающий этап: После того как все поля будут очищены, нажмите на кнопку на странице.
# Секретный Код: Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.

import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    txt_fields_lst = browser.find_elements(By.CLASS_NAME, 'text-field')
    for txt_field in txt_fields_lst:
        txt_field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    alert = browser._switch_to.alert
    pyperclip.copy(alert.text)
    print(alert.text)
    time.sleep(10)
