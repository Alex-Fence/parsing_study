# Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
# Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
# Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
# Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    p_tags = browser.find_elements(By.CSS_SELECTOR, 'p:nth-child(2)')
    p_sum = sum([int(p_tag.text) for p_tag in p_tags])
    print(p_sum)
pyperclip.copy(str(p_sum))