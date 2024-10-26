# Цель: Посетить указанный веб-сайт, систематически пройти по всем категориям, страницам и карточкам товаров
# (всего 160 шт.). Из каждой карточки товара извлечь стоимость и умножить ее на количество товара в наличии.
# Полученные значения агрегировать для вычисления общей стоимости всех товаров на сайте.

import requests
from bs4 import BeautifulSoup
import lxml


# сварить суп
def make_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# получить список ссылок на карточки товаров
def make_list_of_goods_items_links(url):
    soup = make_soup(url)
    # формирование ссылок на товары страницы
    item_cards = soup.select('a.name_item')
    item_links_lst = [item.get('href') for item in item_cards]
    return item_links_lst


# получить стоимость товара
def load_cost_counts_by_good(url):
    soup = make_soup(url)
    in_stock = int(soup.find('span', id='in_stock').text[11:])  # товара в наличии
    price = int(soup.find('span', id='price').text[:-4])  # цена товара
    cost = in_stock * price
    return cost


# получить сумму стоимости всех товаров на странице
def load_cost_counts_by_page(page_url):
    goods_lst = make_list_of_goods_items_links(page_url)
    sum_costs = sum([load_cost_counts_by_good(main_url + url_good) for url_good in goods_lst])
    return sum_costs


# получить сумму стоимости всех товаров на страницах определенного типа товаров
def load_by_menu_items(url_menu_item):
    # список ссылок из раздела пагинации
    full_url_menu_item = main_url + url_menu_item
    soup = make_soup(full_url_menu_item)
    # список ссылок на страницы с конкретным товаром
    links_lst = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    sum_for_item = sum([load_cost_counts_by_page(main_url + link) for link in links_lst])
    print(f'{full_url_menu_item}: {sum_for_item}')
    return sum_for_item


if __name__ == '__main__':
    main_url = 'https://parsinger.ru/html/'
    full_sum = sum([load_by_menu_items(f'index{menu_item}_page_1.html') for menu_item in range(1, 6)])
    print(f'Сумма всех товаров на сайте: {full_sum}')
