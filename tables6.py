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
    # получение названий столбцов
    headers_lst = [th.text for th in rows[0].find_all('th')]
    # создание списка для записи суммированых значений по каждому столбцу
    result_lst = [0 for _ in range(len(headers_lst))]
    for row in rows[1:]:
        # получаем список значений по данной строке
        row_data = [float(td.text) for td in row.find_all('td')]
        # добавляем значения в результирующий список
        for i in range(len(headers_lst)):
            result_lst[i] += row_data[i]
    # объединяем список заголовков с результирующим списком в словарь
    res_columns_dict = dict(zip(headers_lst, result_lst))
    # округление значений по условию задачи
    res_columns_dict = {k: round(v, 3) for k, v in res_columns_dict.items()}
    print(res_columns_dict)
    # запись результата в буфер обмена для вставки в веб-сайт
    pyperclip.copy(str(res_columns_dict))

