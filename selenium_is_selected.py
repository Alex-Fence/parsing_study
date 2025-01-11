# Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из
# них будут чекбоксы. Главная загвоздка: чекбоксы и их состояние ("checked" или "unchecked") определяются
# случайным образом.

# Пройдитесь по всем текстовым полям и соберите числа только из тех, которые имеют рядом активные чекбоксы.

import pyperclip
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/3/temp/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    boxes_lst = browser.find_elements(By.CLASS_NAME, 'field-wrapper')
    sel_box_lst = [box.find_element(By.CSS_SELECTOR, "input[type='text']").get_attribute('value') for box in boxes_lst if box.find_element(By.CLASS_NAME, 'field-checkbox').is_selected()]
    sel_box_lst = list(map(int, sel_box_lst))
    print(sum(sel_box_lst))
