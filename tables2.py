# Перейти на сайт и найти таблицу.
# Произвести парсинг данных из первого столбца таблицы.
# Суммировать все числа, найденные в первом столбце.

import requests
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    url: str = 'https://parsinger.ru/table/2/index.html'
    soup = make_soup(url)
    rows: list = soup.find('table').find_all('tr')
    first_col: list = [float(cell.find_all('td')[0].text) for cell in rows[1:]]
    print(f'Sum by first column: {sum(first_col)}')
