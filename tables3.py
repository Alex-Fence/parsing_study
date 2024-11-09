# Перейти на сайт и обнаружить требуемую таблицу.
# Cобрать только числа, отформатированные жирным шрифтом.
# .find('b')  или .find_all('b')
# Суммировать выделенные числа.

import requests
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    url: str = 'https://parsinger.ru/table/3/index.html'
    soup = make_soup(url)
    t_rows = soup.find_all('tr')
    # print(t_rows)
    b_nums = []
    # получаем список списков чисел выделеных жирным шрифтом в тегах b
    for t_row in t_rows:
        b_nums_td = [t_row.find_all('b') for t_row in t_rows[1:]]
    # получаем суммы таких чисел по каждой строке
    for b_num in b_nums_td:
        b_nums.append(sum([float(num.text) for num in b_num]))
    print(f'Итоговая сумма выделеных чисел равна {sum(b_nums)}')
