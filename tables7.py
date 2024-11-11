# Загрузить страницу с шестью таблицами.
# Пройтись по каждой ячейке каждой таблицы и проверить значение на кратность трём.
# Если число кратно трем, добавить его к общей сумме.

import requests
from bs4 import BeautifulSoup
import pyperclip


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# поиск чисел кратных 3м  в определенной таблице
def search_3(table: BeautifulSoup):
    sum_table = 0
    for td in table.find_all('td'):
        td_value = int(td.text)
        if td_value % 3 == 0:
            sum_table += td_value
    return sum_table


if __name__ == '__main__':
    url_link = 'https://parsinger.ru/4.8/7/index.html'
    soup = make_soup(url_link)
    tables = soup.find_all('table')
    sum_tables = 0
    for table in tables:
        print(search_3(table))
        sum_tables += search_3(table)
    print(f'{sum_tables=}')
    # запись в буфер обмена
    pyperclip.copy(str(sum_tables))
