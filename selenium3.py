# Вход в Лабиринт: Откройте указанный веб-сайт с помощью Selenium.
# Ключи к Сокровищам: Извлеките данные из каждого тега <p> на странице.
# Сложение Фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
# Отчет о Сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное значение вставьте в поле ответа степик.

import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    p_tags = browser.find_elements(By.TAG_NAME, 'p')
    p_sum = sum([int(p_tag.text) for p_tag in p_tags])
    print(p_sum)
    time.sleep(5)
pyperclip.copy(str(p_sum))