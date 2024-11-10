# Открыть веб-сайт и обнаружить интересующую таблицу.
# Для каждого столбца вычислить сумму всех чисел в этом столбце.
# Округлить каждое получившееся значение до трех знаков после запятой.
# row: round(sum(column), 3)
# Формировать словарь, где ключами будут названия столбцов, а значениями - рассчитанные суммы.
# Вставить полученный словарь в поле ответа на веб-сайте.

import requests
from bs4 import BeautifulSoup
import pyperclip

def make_soup(url: str)->BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, "lxml")

if __name__ == '__main__':
    url ='https://parsinger.ru/table/5/index.html'
    soup = make_soup(url)
    rows = soup.find('table').find_all('tr')
    res_columns_dict = {td.text: 0 for td in rows[0]}
    print(res_columns_dict)
    for row in rows[1:]:
        for key in res_columns_dict.keys():
            for td in row.find_all('td'):
                res_columns_dict[key] += float(td.text)
    res_columns_dict.pop('\n')
    res_columns_dict = {k: round(v, 3) for k, v in res_columns_dict.items()}
    print(res_columns_dict)
    pyperclip.copy(str(res_columns_dict))

