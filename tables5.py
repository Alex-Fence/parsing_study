# Открыть веб-сайт и обнаружить необходимую таблицу.
# Для каждой строки таблицы найти числа в оранжевой и голубой ячейках,
# после чего умножить их друг на друга.
# Сложить все получившиеся произведения, чтобы получить общую сумму.

import requests
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    url = 'https://parsinger.ru/table/5/index.html'
    soup = make_soup(url)
    t_raws = soup.find('table').find_all('tr')
    res = 0
    for t_raw in t_raws[1:]:
        orange_cell = float(t_raw.select('.orange')[0].text)
        blue_cell = float(t_raw.select('td:last-child')[0].text)
        res += orange_cell * blue_cell
    print(res)
