# регулярные выражения делают валидацию емайлов
# Жадные и не жадные регуляторы
# # Регулярные выражения (поиск по паттерну)
# # Regular Expressions (re)
# # r-строка - raw-string ("сырая" строка)
# # Квантификаторы (quantity)
# # {m} - ровно m раз
# # {m,} - m раз m более
# # {,n} - не более n раз
# # {m,n} - от m до n (без пробела)
# # ? - от нуля до одного (аналог {0,1})
# # * - от нуля до бесконечности (32767) {0,}
# # + - от 1 до бесконечности (32767) {1,}
#
import re
#
# # pattern = r'\b\w{4}\b' # все слова из 4 символов
# # pattern = r'\d' # все цифры от 0 до 9
# # pattern = r'\d{3}'  # три цифры подряд
# # pattern = r'начало!\Z' # на что заканчивается
# # pattern = '[0-5][0-9]' # две идущие подряд
# # pattern = '[а-яА-я]' # все буквы от а до я и от А до Я
# # pattern = '[^ерм]'  # исключить символы
# # pattern = r'\((.+?)\)' # вытащить текст из скобок
# pattern = 'Go{2,}gle' # Google где 2 и более o
# test_string = 'Google, Gooogle, Gooooooogle'
#(.+?)  ленивый квантификатор
# "жадный" квантификатор (greedy quantifier)
# result = re.findall(pattern, test_string)
# print(result)
# pattern = r'стеклянн?ый'# вторая н может присутствовать, но не обязана
# test_string = 'стеклянный, стеклянный, оловянный, серебряный'
# result = re.findall(pattern, test_string)
# print(result)#['стеклянный', 'стеклянный']
# # "жадный" квантификатор (greedy quantifier)
# # pattern = r'<img[^>]+src="([^">]+)"'
# # pattern = r'<img.*>'# "жадный" квантификатор
# # test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'
# # result = re.findall(pattern, test_string)
# # print(result)#['<img src="bg.jpg"> в тексте</p>']
# # ленивый квантификатор (lazy, non greedy)
# pattern = r'<img.*?>'# ленивый квантификатор (lazy, non greedy)
# test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'
# result = re.findall(pattern, test_string)
# print(result)#['<img src="bg.jpg">']
# pattern = r'<img[^>]+src="([^">]+)"'# только путь к картинке
# test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'
# result = re.findall(pattern, test_string)
# print(result)#['bg.jpg']
#
# test_string = '<b>от начало: </b><p>Содержимое</p><i>и т.д.</i>'
# pattern = r'<p>(.*?)</p>'# производит захват содержимое абзаца HTML
# result = re.findall(pattern, test_string)
# print(result)#['Содержимое']
#
# test_string = '<b>от начало: </b><p>Содержимое</p><i>и т.д.</i>'
# pattern = r'<p>(.*)</p>'# производит захват содержимое абзаца HTML жадный захват
# result = re.findall(pattern, test_string)
# print(result)#['Содержимое']
#
# test_string = '<b>Центрируем</b> <p align="center">Содержимое</p><i>и т.д.</i>'
# pattern = r'<p>(.*)</p>'# производит захват содержимое абзаца HTML жадный захват
# result = re.findall(pattern, test_string)
# print(result)#[]
#
# test_string = '<b>Центрируем</b> <p align="center">Содержимое</p><i>и т.д.</i>'
# pattern = r'<p[^>]*>(.*)</p>'# производит захват содержимого абзаца HTML с атрибутом жадный
# result = re.findall(pattern, test_string)
# print(result)#['Содержимое']
#
# test_string = '<b>Центрируем</b> <p align="center">Содержимое</p><i>и т.д.</i>'
# pattern = r'<p[^>]*>(.*?)</p>'# захват содержимого абзаца HTML с атрибутом ленивый! лучше ленивый
# result = re.findall(pattern, test_string)
# print(result)#['Содержимое']
# ## ## Https://regex101.com _ популярный сайт по этой теме есть в метадичке
# # EУбираем все знаки припинания
# def remove_punctuation(input_str: str)->str:
#     """
#     Методом sub() заменяем все найденые совпадения
#      пустой строкой и возвращает очищенную
#     :param input_str: строка со знаками припинания
#     :return: строку, очищенную от зн. преп.
#     """
#     return re.sub(r'[^\w\s]','',input_str)
#
# test_string = 'Язык Python, являясь интуитивным понятным, прост для изучения. Pep 8'
# result = remove_punctuation( test_string)
# print(result)#Язык Python являясь интуитивным понятным прост для изучения Pep 8
#
# test_string = 'Язык Pyt!hon, являясь интуи?тивным пон,ятным, прост для изучения. Pep 8'
# result = remove_punctuation( test_string)
# print(result)#Язык Python являясь интуитивным понятным прост для изучения Pep 8


# pattern = r'[,.;:!]'
# test_string = 'яблоко,груша.банан;слива!абрикос'
# result = re.split(pattern, test_string)
# print(result)#['яблоко', 'груша', 'банан', 'слива', 'абрикос']
#
# # через map
# pattern = r'[,.;:!]'
# test_string = '  яблоко, груша. банан ; слива! абрикос'
# result = re.split(pattern, test_string)
# result = list(map(lambda x: x.strip(), result))
# print(result)#['яблоко', 'груша', 'банан', 'слива', 'абрикос']
#
# # методом Join
# pattern = r'[,.;:!]'
# test_string = '  яблоко, груша. банан ; слива! абрикос'
# test_string = ''.join(test_string.split(' '))
# result = re.split(pattern, test_string)
# print(result)#['яблоко', 'груша', 'банан', 'слива', 'абрикос']
#
# # через лист
# pattern = r'[,.;:!]'
# test_string = '  яблоко, груша. банан ; слива! абрикос'
# result = re.split(pattern, test_string)
# result = sorted(x.strip() for x in result)
# print(result)#['абрикос', 'банан', 'груша', 'слива', 'яблоко']

pattern = r'<img[^>]+src="([^">]+)"'# только путь к картинке
# test_string = '<img height="50" width="150" src="images/sunny.day_2.jpg><>'
# result = re.split(pattern, test_string)
# print(result)#['яблоко', 'груша', 'банан', 'слива', 'абрикос']
#pip install requests # чтобы прочитать сайт
#pip freeze >requirements.txt
# import requests
# html = requests.get('https://skillbox.ru')
# print(html)#<Response [200]> ответил что всё хорошо сервер ответил такой сайт существует
#
# import requests
# html = requests.get('https://skillbox.ru').text
# print(html)#выведет большой объем данных
import requests # парсинг
html = requests.get('https://skillbox.ru').text
result = re.findall(pattern, html)
print(result)#выведет большой объем данных
# это всё было операционое програмирование, далее мы будем проходить
# Объектно Оринтированое програмирование(инкапсериаованое програмирование)(encapsulation)
