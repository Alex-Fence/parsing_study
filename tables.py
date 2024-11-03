import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.8/1/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')

# Извлекаем все строки таблицы
rows = table.find_all('tr')

# Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
for row in rows[1:]:
    # Извлекаем ячейки текущей строки
    columns = row.find_all('td')
    # Первая ячейка содержит имя
    name = columns[0].text
    # Вторая ячейка содержит возраст
    age = columns[1].text
    # Выводим результат
    print(f'Имя: {name}, Возраст: {age}')
