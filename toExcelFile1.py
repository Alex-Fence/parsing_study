import requests
from bs4 import BeautifulSoup
import csv


def make_soup(url_link: str) -> BeautifulSoup:
    response = requests.get(url_link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# создание списка пагинации
def make_pages_list(first_page_link: str) -> list[str]:
    soup = make_soup(first_page_link)
    pagen = soup.find('div', class_='pagen').find_all('a', href=True)
    pagen_lst: list[str] = [p['href'] for p in pagen]
    print(pagen_lst)
    main_url = first_page_link[:-len(pagen_lst[0])]
    return [main_url + page for page in pagen_lst]



# список товаров в каждой странице добавляет в общий список
def make_goods_list(soup: BeautifulSoup)-> None:
    good_items = soup.find_all('div', class_='description')
    names_lst: list[str] = [i.text.strip() for i in soup.find_all('a', class_='name_item')]
    price_lst: list[str] = [i.text.strip() for i in soup.find_all('p', class_='price')]

    for index, good in enumerate(good_items):
        #    goods_lst_dicts.append({d.text.split(': ')[0]: d.text.split(': ')[1]for d in good.find_all('li')})
        data_row: list[str] = [d.text.split(': ')[1].strip() for d in good.find_all('li')]
        data_row.insert(0, names_lst[index])
        data_row.append(price_lst[index])
        goods_lst_lists.append(data_row)
        print(data_row)

# Запись в файл
def write_to_csv(goods_lst_lists: list[list]) -> None:
    with open('goods_res.csv', 'a', encoding='utf-8-sig', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(t_header)
        for goods_row in goods_lst_lists:
            writer.writerow(goods_row)


if __name__ == '__main__':
    t_header: list[str] = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
    goods_lst_lists: list[list] = []
    # получаем первую страницу
    first_page: str = 'https://parsinger.ru/html/index4_page_1.html'
    pages_lst: list[str] = make_pages_list(first_page)
    # print(pages_lst)
    for page in pages_lst:
        soup: BeautifulSoup = make_soup(page)
        make_goods_list(soup)

    write_to_csv(goods_lst_lists)
