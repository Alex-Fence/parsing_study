# Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
# Извлечение Ключей: Получите значения всех элементов выпадающего списка.
# Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
# Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
# Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.
import time

import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    options_lst = [int(num.text) for num in browser.find_elements(By.TAG_NAME, 'option')]
    sum_code = sum(options_lst)
    browser.find_element(By.ID, 'input_result').send_keys(str(sum_code))
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    res = browser.find_element(By.ID, 'result').text
print(res)
pyperclip.copy(str(res))
