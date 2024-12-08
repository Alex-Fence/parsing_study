# В данной задаче вы должны выполнить аналогичные действия, как и в предыдущей задаче, но с небольшим изменением. Вам необходимо определить, откуда приходят данные и в каком формате, а затем обработать эти данные следующим образом:

# Получение данных: Используйте инструменты разработчика для определения источника данных(вкладка Network). В нашем случае, данные лежат на этом веб-сайте.
# Обработка данных: Извлеките данные со страницы и создайте словарь, в котором для каждой карточки вычислите произведение значений "article" и "rating".
# Сбор значений: Суммируйте результаты произведений для каждой категории.
# Формирование словаря: Завершая задачу, создайте словарь, в котором ключами будут категории, а значениями - суммы произведений "article" и "rating".
# Вставьте полученный результат в поле для ответа.
# Пример словаря который нужно отправить на проверку.

# {'watch': 00000000000, 'mobile': 000000000000, 'mouse': 000000000000, 'hdd': 000000000000, 'headphones': 0000000000000}

import pyperclip
import requests

url = 'https://parsinger.ru/4.6/1/res.json'
res_dict: dict[int] = {'watch': 00000000000, 'mobile': 000000000000, 'mouse': 000000000000, 'hdd': 000000000000, 'headphones': 0000000000000}
response = requests.get(url).json()
for item in response:
    res_dict[item['categories']] += int(item['article']) * int(item['description']['rating'])
print(res_dict)
pyperclip.copy(str(res_dict))
