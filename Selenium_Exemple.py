# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Создание объекта ChromeOptions для дополнительных настроек браузера
# options_chrome = webdriver.ChromeOptions()
#
# # Добавление аргумента '--headless' для запуска браузера в фоновом режиме
# options_chrome.add_argument('--headless')
#
# # Инициализация драйвера Chrome с указанными опциями
# # Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/a/104774'
#     browser.get(url)
#
#     # Ищем элемент по тегу 'a' (ссылку)
#     a = browser.find_element(By.TAG_NAME, 'a')
#
#     # Выводим атрибут 'href' найденного элемента (URL ссылки)
#     print(a.get_attribute('href'))

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://2ip.ru/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver= webdriver.Chrome()
# driver.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = driver.find_element(By.ID, "sale_button")
# time.sleep(2)
# button.click()
# time.sleep(2)
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    time.sleep(5)