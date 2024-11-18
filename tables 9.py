# Запрашивайте данные с веб-сайта, который содержит таблицу автомобилей.
# Фильтруйте автомобили по заданным критериям:
# Cтоимость не выше 4 000 000 (Стоимость авто <= 4000000),
# Год выпуска начиная с 2005 года (Год выпуска >= 2005),
# Тип двигателя - Бензиновый (Тип двигателя == "Бензиновый").
# Выводите результат в формате JSON, при отправке данных в валидатор, важен каждый пробел и перенос строки.
# Используйте эти параметры для формирования JSON
# json.dumps(sorted_cars, indent=4, ensure_ascii=False)
# Обратите внимание на тип данных.
#         "Марка Авто": str("Nissan"),
#         "Год выпуска": int(2009),
#         "Тип двигателя": str("Бензиновый"),
#         "Стоимость авто": int(891048)
# Сортируйте отфильтрованный JSON  автомобилей по стоимости от меньшего к большему
# sorted(filtered_cars, key=lambda x: x["Стоимость авто"])

import requests
import json
from bs4 import BeautifulSoup
import pyperclip

def make_soup(url_link:str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "html.parser")

if __name__ == "__main__":
    url_link = "https://parsinger.ru/4.8/6/index.html"
    soup: BeautifulSoup = make_soup(url_link)
    # номера пунктов которые нужно выбрать
    num_items_lst: list = [0, 1, 4, 7]
    # список ключей для словаря
    headers_lst: list = [th.text for th in soup.find_all("th")]
    headers_lst = [th for th in headers_lst if headers_lst.index(th) in num_items_lst]

    rows_lst: list = [tr for tr in soup.find_all("tr")]
    # словарь для списков, который будет передаваться в json
    json_lst: list = []
    for row in rows_lst[1:]:
        # получил список значений без тегов
        row_dt_lst : list = [dt.text for dt in row]
        # убрал лишние значения в списке
        row_dt_lst = [dt for dt in row_dt_lst if row_dt_lst.index(dt) in num_items_lst]
        # преобразовал год выпуска и цену с числовой формат
        row_dt_lst = [int(row_dt) if row_dt_lst.index(row_dt) in (1, 3) else row_dt for row_dt in row_dt_lst]
        # получил словарь значений
        row_dict = dict(zip(headers_lst, row_dt_lst))
        # проверка на соответствие фильтру, если да то добавляю в словарь
        if row_dict['Стоимость авто'] <= 4000000 and row_dict['Год выпуска'] >= 2005 and row_dict['Тип двигателя'] == "Бензиновый":
            json_lst.append(row_dict)
    # сортировка полученного списка словарей
    json_lst = sorted(json_lst, key=lambda x: x["Стоимость авто"])
    # валидация для json
    sorted_cars = json.dumps(json_lst, indent=4, ensure_ascii=False)
    print(sorted_cars)
    pyperclip.copy(sorted_cars)