# Соберите данные о HDD с четырёх страниц в категории HDD.
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

import json
import requests
from bs4 import BeautifulSoup


class ParsingSite:
    def __init__(self, first_url: str):
        self.headers_lst: list[str] = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти',
                                       'Цена']  # Заголовки для запроса
        self.main_url: str = ''
        self.first_url: str = first_url
        self.goods_lst: list[str] = []

    def make_soup(self, url_link: str) -> BeautifulSoup:
        response = requests.get(url_link)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')

    def make_pagen_list(self, page_url: str) -> list[str]:
        soup: BeautifulSoup = self.make_soup(first_url)
        pagen_lst: list[str] = [page_link.get('href') for page_link in soup.find('div', class_='pagen').find_all('a', href=True)]
        self.main_url = page_url[:-len(pagen_lst[0])]
        pagen_lst = [self.main_url+pagen_page for pagen_page in pagen_lst]
        print(pagen_lst)
        return pagen_lst

    def make_goods_lst(self, page_url: str) -> list[str]:
        good_description_lst: list[str] = []
        soup: BeautifulSoup = self.make_soup(page_url)
        # ["Наименование", "Бренд", "Форм-фактор", "Ёмкость", "Объем буферной памяти", "Цена"]
        good_items_lst = soup.find_all('div', class_='item')
        #print((good_items_lst))
        for item in good_items_lst:
            # Наименование
            good_description_lst.append(item.find('a', class_='name_item').text.strip())
            # Бренд,форм-фактор,Ёмкость,Объем буферной памяти
            description_lst = item.find('div', class_='description').find_all('li')
            description_lst = [description.text.split(': ')[1].strip() for description in description_lst]
            for description in description_lst:
                good_description_lst.append(description)
            # Цена
            good_description_lst.append(item.find('div', class_='price_box').text)
            self.goods_lst.append(dict(zip(self.headers_lst, good_description_lst)))
            good_description_lst.clear()
        for good in self.goods_lst:
            print(good)
        return self.goods_lst

    def save_json(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(self.goods_lst, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    first_url: str = 'https://parsinger.ru/html/index4_page_1.html'
    parser = ParsingSite(first_url)
    #print(parser.make_goods_lst(first_url))

    for page in parser.make_pagen_list(first_url):
        parser.make_goods_lst(page)
    parser.save_json('result_for_json1.json')
