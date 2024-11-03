# Перейти на сайт и найти таблицу.
# Произвести парсинг данных из таблицы.
# Отфильтровать и извлечь все уникальные числа, исключая числа в заголовке таблицы.
# Посчитать сумму этих чисел.

import requests
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    url: str = 'https://parsinger.ru/table/1/index.html'
    soup = make_soup(url)
    table_data: set = set(float(data.text) for data in soup.find('table').find_all('td'))
    print(sum(table_data))
