# Изучите указанную страницу для получения информации о часах с четырёх страниц в разделе "ЧАСЫ".
# Вам потребуется заходить в каждую товарную карточку и собирать данные, отмеченные на
# предоставленном изображении.
# Сохраните данные в формате CSV с разделителем ;
import csv
import os
import requests
from bs4 import BeautifulSoup

# создание супа
def make_soup(url_link: str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# формируем основную часть строки данных по продукту
def get_good_data(good_link: str) -> list[str]:
    description_lst = []
    cur_soup: BeautifulSoup = make_soup(good_link)
    good_name = cur_soup.find('p', id='p_header').text
    description_lst.append(good_name)
    article = cur_soup.find('p', class_='article').text.split(': ')[1].strip()
    description_lst.append(article)
    li_items = [i.text.split(': ')[1] for i in cur_soup.find_all('li')]
    for li_item in li_items:
        description_lst.append(li_item)
    description_lst.append(cur_soup.find('span', id='in_stock').text.split(': ')[1])
    description_lst.append(cur_soup.find('span', id='price').text)
    description_lst.append(cur_soup.find('span', id='old_price').text)
    description_lst.append(good_link)
    return description_lst


# формирование записи строк в общий список со страницы
def add_to_main_rows_list(page_link: str) -> None:
    soup_page: BeautifulSoup = make_soup(page_link)
    goods_links_by_page_lst: list[str] = [item.get('href') for item in soup_page.select('a.name_item')]
    print(goods_links_by_page_lst)
    for goods_link in goods_links_by_page_lst:
        rows_lst.append(get_good_data(main_url + goods_link))


# запись данных в файл
def write_to_csv(filename: str) -> None:
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'a', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(t_headers_lst)
        for row in rows_lst:
            writer.writerow(row)


if __name__ == '__main__':
    t_headers_lst: list[str] = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
                                'Материал корпуса', 'Материал браслета',
                                'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                                'Ссылка на карточку с товаром']
    firs_url = 'https://parsinger.ru/html/index1_page_1.html'
    main_url = 'https://parsinger.ru/html/'
    soup: BeautifulSoup = make_soup(firs_url)

    rows_lst = []  # сюда записывать строки для последующей таблицы
    pagen_lst = soup.find('div', class_='pagen').find_all('a', href=True)
    # получить список страниц из пагинации
    pagen_lst: list[str] = [i.get('href') for i in pagen_lst]
    for page_link in pagen_lst:
        add_to_main_rows_list(main_url + page_link)
    # запись данных в файл
    write_to_csv('data.csv')
