# Загрузить страницу на которой расположена таблица с объединёнными ячейками.
# Извлечь данные из каждой объединённой ячейки(всего 16 ячеек),
# объединённую ячейку можно определить по атрибуту colspan

import requests
from bs4 import BeautifulSoup


def make_soup(url_link: str)-> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

def make_tables(tables):
    tables = tables.find_all('table')

if __name__ == '__main__':
    url_link = 'https://parsinger.ru/4.8/8/index.html'
    soup = make_soup(url_link)
    tables_all = soup.find_all('table')

    # for table in tables:
    #     print(table.find_all('td', attrs={'colspan': True}))

    print(tables[1].find_all('table'))
    #colspan_data = [table.find_all('th', attrs={'colspan': True}) for table in tables]
    #print(colspan_data)