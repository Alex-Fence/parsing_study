# Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта.
# Охота на Сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище.
# Проблема в том, что оно появляется очень редко. Вам придется обновлять страницу множество раз,
# пока не увидите это число.
# Клад в Руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого
# поле ответа на вашем курсе

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = browser.find_element(By.ID, 'result').text
    while res == 'refresh page':
        browser.refresh()
        res = browser.find_element(By.ID, 'result').text
    print(res)
