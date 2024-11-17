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

def make_soup(url_link:str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "html.parser")

if __name__ == "__main__":
    url_link = "https://parsinger.ru/4.8/6/index.html"
    soup: BeautifulSoup = make_soup(url_link)
    num_items_lst: list = [0, 1, 4, 7]

    headers_lst: list = [th.text for th in soup.find_all("th")]
    print(headers_lst)
    rows_lst: list = [tr for tr in soup.find_all("tr")]
    json_lst: list = []
    for row in rows_lst[1:]:
         # print(row.find_all("td"))
         row_dt_lst : list = [dt.text for dt in row]
         print(row_dt_lst)
         json_lst.append(dict(zip(headers_lst, row_dt_lst)))
    for item in json_lst:
        print(item)