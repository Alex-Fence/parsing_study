# Цель: Посетить указанный веб-сайт, систематически пройти по всем категориям, страницам и карточкам товаров
# (всего 160 шт.). Из каждой карточки товара извлечь стоимость и умножить ее на количество товара в наличии.
# Полученные значения агрегировать для вычисления общей стоимости всех товаров на сайте.

import requests
from bs4 import BeautifulSoup
import lxml


def make_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def make_list_of_goods_items_links(url):
    soup = make_soup(url)
    # формирование ссылок на товары страницы
    item_cards = soup.select('a.name_item')
    item_links_lst = [item.get('href') for item in item_cards]
    print(item_links_lst)
    return item_links_lst

def load_cost_counts_by_good(url):
    soup = make_soup(url)
    in_stock = int(soup.find('span', id='in_stock').text[11:]) # товара в наличии
    price = int(soup.find('span', id='price').text[:-4]) # цена товара
    cost = in_stock * price
    print(f'{url}: {in_stock}, {price}, {cost}')
    return cost

def load_cost_counts_by_page(page_url):
    goods_lst = make_list_of_goods_items_links(page_url)
    sum_costs = sum([load_cost_counts_by_good(main_url+url_good) for url_good in goods_lst])
    return sum_costs




main_url = 'https://parsinger.ru/html/'
url1 = 'https://parsinger.ru/html/index1_page_1.html'
soup = make_soup(url1)
# список ссылок из раздела пагинации
links_lst = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
print(links_lst)

print(load_cost_counts_by_good(main_url+make_list_of_goods_items_links(url1)[0]))
print(f'{links_lst[0]}: {load_cost_counts_by_page(main_url+links_lst[0])}')
