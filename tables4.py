# Открыть веб-сайт и найти целевую таблицу.
# Провести анализ данных в таблице, фокусируясь на ячейках зелёного цвета.
# Выделить и подсчитать сумму всех чисел из зелёных ячеек.

import requests
from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    url: str = 'https://parsinger.ru/table/4/index.html'
    soup = make_soup(url)
    t_rows = soup.find_all('tr')
    # получаем список чисел с зеленым фоном
    green_nums = [float(gr_num.text) for gr_num in soup.select('td.green')]
    # альтеративный вариант
    # green_nums = [int(gr_num.text) for gr_num in find_all('td', class_='green')]
    print(sum(green_nums))
