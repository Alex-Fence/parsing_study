# Изучите указанную страницу для получения информации о часах с четырёх страниц в разделе "ЧАСЫ".
# Вам потребуется заходить в каждую товарную карточку и собирать данные, отмеченные на
# предоставленном изображении.
# Сохраните данные в формате CSV с разделителем ;
import requests
from bs4 import BeautifulSoup

def make_soup(url_link: str)->BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

# формируем основную часть строки данных по продукту
def get_good_data(good_link: str) -> list[str]:
    description_lst = []
    cur_soup: BeautifulSoup = make_soup(good_link)
    good_name = cur_soup.find('p', id = 'p_header').text
    print(good_name)
    description_lst.append(good_name)
    article = cur_soup.find('p', class_ = 'article').text.split(': ')[1]
    description_lst.append(article)
    li_items = [i.text.split(': ')[1] for i in cur_soup.find_all('li')]
    for li_item in li_items:
        description_lst.append(li_item)
    description_lst.append(cur_soup.find('span', id='in_stock').text.split(': ')[1])
    description_lst.append(cur_soup.find('span', id='price').text)
    description_lst.append(cur_soup.find('span', id='old_price').text)
    description_lst.append(good_link)
    print(description_lst)
    return description_lst


# формирование записи строк в общий список со страницы
def add_to_main_rows_list(page_link: str)-> None:
    pass

if __name__ == '__main__':
    t_headers_lst: list[str] = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса', 'Материал браслета', 
    'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']
    firs_url = 'https://parsinger.ru/html/index1_page_1.html'
    main_url = 'https://parsinger.ru/html/'
    soup: BeautifulSoup = make_soup(firs_url)
    # сбор наименований продуктов на текущей странице
    # watchs_names_lst: list[str] = [i.text for i in soup.find_all('a', class_= 'name_item')]
    # print(watchs_names_lst)

    rows_lst = [] # сюда записывать строки для последующей таблицы
    goods_links_by_page_lst: list[str] = [item.get('href') for item in soup.select('a.name_item')]
    print(goods_links_by_page_lst)
    get_good_data(main_url+goods_links_by_page_lst[0])