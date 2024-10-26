# Цель: Посетить указанный веб-сайт, систематически пройти по всем категориям, страницам и карточкам товаров
# (всего 160 шт.). Из каждой карточки товара извлечь стоимость и умножить ее на количество товара в наличии.
# Полученные значения агрегировать для вычисления общей стоимости всех товаров на сайте.

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://parsinger.ru/html/index1_page_1.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
links_lst = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
print(links_lst)
#item_cards = [link['href'] for link in soup.find_all('div', class_='img_box')]
item_cards = soup.find_all('div', class_='img_box')
print(item_cards[0].find_all('a', class_='name_item')[0].find('href')) #выводим ссылку на карточку товара
