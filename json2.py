# Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
# (всего 160шт).
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

import json
import requests
from bs4 import BeautifulSoup


# создание супа
def make_soup(url_link: str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# создание списка url страниц пагинации по определенному виду товаров
def make_pagen_list(page_url: str) -> list[str]:
    soup: BeautifulSoup = make_soup(page_url)
    pagen_lst: list[str] = [page_link.get('href') for page_link in
                            soup.find('div', class_='pagen').find_all('a', href=True)]
    main_url = page_url[:-len(pagen_lst[0])]
    pagen_lst = [main_url + pagen_page for pagen_page in pagen_lst]
    return pagen_lst


# создание списка пунктов описания товара( в этом варианте они у каждого товара даже в одной категории могут отличаться)
def make_header_lst(item_soup: BeautifulSoup) -> list[str]:
    soup = item_soup
    headers_lst: list[str] = ['Наименование']
    description_lst = [d.text.split(':')[0] for d in soup.find('div', class_='description').find_all('li')]
    for d in description_lst:
        headers_lst.append(d)
    headers_lst.append('Цена')
    return headers_lst


# создание списка url страниц по меню слева, категории товаров
def make_menu_lst(url: str) -> list[str]:
    soup: BeautifulSoup = make_soup(url)
    menu_list: list[str] = [m_url.get('href') for m_url in soup.find('div', class_='nav_menu').find_all('a')]
    return [main_url + menu_url for menu_url in menu_list]

# формирование словаря свойств по каждому товару на странице и запись в глобальный список
def make_res_lst_by_page(page_url: str) -> None:
    page_soup: BeautifulSoup = make_soup(page_url)
    items_soup: BeautifulSoup = page_soup.find_all('div', class_='item')
    for item_soup in items_soup:
        headers_lst = make_header_lst(item_soup)
        description_lst = [item_soup.find('a', class_='name_item').text.strip()] + [d.text.split(':')[1].strip() for d
                                                                                    in item_soup.find('div',
                                                                                                      class_='description').find_all(
                'li')]
        description_lst.append(item_soup.find('p', class_='price').text)
        res_lst.append(dict(zip(headers_lst, description_lst)))
        description_lst.clear()

# запись глобального списка в json
def save_to_json(res_lst, file_name):
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(res_lst, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    res_lst: list[dict] = []
    first_url = 'https://parsinger.ru/html/index1_page_1.html'
    main_url = 'https://parsinger.ru/html/'
    menu_lst = make_menu_lst(first_url)

    for menu_url in menu_lst:
        pagen_lst = make_pagen_list(menu_url)
        for page_url in pagen_lst:
            make_res_lst_by_page(page_url)
    for res in res_lst:
        print(res)
    save_to_json(res_lst, 'result_for_json2.json')
