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
    # числа из заголовков таблиц
    th_lst = soup.find_all('th', attrs={'colspan': True})
    th_sum = sum([int(th.text) for th in th_lst])
    # числа из ячеек
    td_row = soup.select('td[colspan]')
    td_lst = [int(td.text) for td in td_row[0].find_all('td', attrs={'colspan': True})]
    td_sum = sum(td_lst)
    print(td_sum + th_sum)
