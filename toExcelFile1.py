import requests
from bs4 import BeautifulSoup
import csv

def make_soup(url_link: str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    t_header: list[str] = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
    #создание списка пагинации
    url_first = 'https://parsinger.ru/html/index4_page_1.html'
    soup = make_soup(url_first)
    pagen = soup.find('div', class_='pagen').find_all('a', href=True)
    pagen_lst: list[str] = [p['href'] for p in pagen]
    print(pagen)
    main_url = url_first[:-len(pagen_lst[0])]
    for page in pagen:
        print(main_url+page)
