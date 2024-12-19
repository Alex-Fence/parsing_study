# Вашей задачей является обработка данных в формате JSON, полученных по ссылке ​.
# Для подсчета общего количества товаров в разных категориях. Каждая карточка товара содержит информацию
# о количестве данного товара.
# Ожидаемый вывод:
# На выходе вашей программы должен быть словарь в одну строку в формате Python:
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
# где N — это общее количество товаров для каждой категории.

import requests
import pyperclip

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url).json()
res_dict = {'watch': 0, 'mobile': 0, 'mouse': 0, 'hdd': 0, 'headphones': 0}
for item in response:
    res_dict[item['categories']] += int(item['count'])
print(res_dict)
pyperclip.copy(str(res_dict))