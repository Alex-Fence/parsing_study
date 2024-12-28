# Откройте Таинственную Страницу: Используя Selenium, откройте веб-страницу, где хранится первая подсказка.
# # Решение Загадки: Вычислите значение математического выражения.
# ((12434107696 * 3) * 2) + 1
# Ключ к Выпадающему Списку: Откройте выпадающий список и выберите элемент с числом, которое у вас получилось на предыдущем этапе.
# Активация Механизма: Нажмите на кнопку на странице, если значение верное, вы получите код.
# Завершение Миссии: Скопируйте число, которое появится на странице после нажатия на кнопку, и вставьте его в поле ответа степик.

import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = 'https://parsinger.ru/selenium/6/6.html'
temp_key = ((12434107696 * 3) * 2) + 1

with webdriver.Chrome() as browser:
    browser.get(url1)
    # Ключ к Выпадающему Списку: Откройте выпадающий список и выберите элемент с числом, которое у вас получилось на предыдущем этапе.
    [num.click() for num in browser.find_elements(By.TAG_NAME, 'option') if int(num.text) == temp_key]
    # нажатие кнопки
    browser.find_element(By.CLASS_NAME, 'btn').click()
    res = browser.find_element(By.ID, 'result').text
    # копирование результирующего значения в буфер обмена
    pyperclip.copy(str(res))
    time.sleep(5)

