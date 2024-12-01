# Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
# (всего 160шт).
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

import json
import requests
from bs4 import BeautifulSoup
from json1 import ParsingSite


def make_soup(url_link: str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

def make_header_lst(url: str) -> list[str]:
    soup = make_soup(url)
    headers_lst: list[str] = ['Наименование']
    description_lst = [d.text.split(':')[0] for d in soup.find('div', class_='description').find_all('li')]
    for d in description_lst:
        headers_lst.append(d)
    headers_lst.append('Цена')
    return headers_lst

def make_menu_lst(url: str):
    soup: BeautifulSoup = make_soup(url)
    menu_list: list[str] = [m_url.get('href') for m_url in soup.find('div', class_='nav_menu').find_all('a')]
    return menu_list

if __name__ == '__main__':
    first_url = 'https://parsinger.ru/html/index1_page_1.html'
    headers_lst = make_header_lst(first_url)
    #["Наименование", "Бренд", "Тип подключения", "Цвет", "Тип наушников", "Цена"]
    parser = ParsingSite(first_url, headers_lst)
    pagen_list = parser.make_pagen_list('https://parsinger.ru/html/index1_page_1.html')
    main_url = parser.main_url
    menu_lst = [main_url+menu_url for menu_url in make_menu_lst(first_url)]
    print(pagen_list)
    print(headers_lst)
    print(main_url)
    print(menu_lst)