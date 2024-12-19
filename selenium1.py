#Основные Этапы:
# Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
# Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
# Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
# Инициация: Найдите кнопку на странице и нажмите на неё.
# Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёхсекундный интервал.
# Фиксация: Запишите результат в отдельную переменную или вставьте ответ в поле ответа степик.

import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    for input_form in input_forms:
        input_form.send_keys('Текст')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    pyperclip.copy(str(browser.find_element(By.ID, 'result').text))
    time.sleep(5)
