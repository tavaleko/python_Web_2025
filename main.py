# База данных чтение
# 1. импорт библиотеки sqlite3
# 2. Подключаемся к бд
# 3. Назначить "курсор"
# 4. работаем с бд
# 5. отключаеся от бд

# import sqlite3
# подключаемся
# connection = sqlite3.connect('db/movies.sqlite')
# назначим курсор
# cursor = connection.cursor()
# запрос (помощью курсора)
# result = cursor.execute(
#     """
#     SELECT title,year FROM films
#     WHERE year Between 2001 and 2005
#     """
# )
# # print(result)#<sqlite3.Cursor object at 0x000001D2816D54C0>
# # если будет ошибка смотри может где буквы не хватает
# #
# # возвращает список кортежей
#
# array = result.fetchall()
# for title, year in array:
#     print(title, year)

# result = cursor.execute(
#         """
#         SELECT title FROM films
#         WHERE year Between 2001 and 2005
#         """
#     )
    # print(result)#<sqlite3.Cursor object at 0x000001D2816D54C0>
    # если будет ошибка смотри может где буквы не хватает
    # print(result.fetchall())#[('Алиса в стране чудес',), ('Железный человек 2',), ('Ноттингем',), ('Утомленные солнцем: Предстояние',)]
    # возвращает список кортежей

# print(result.fetchall())
# fetchall --всё
# fetchone -- один первый
# fetchmany(N)--- первые N соответствий
# connection.close()
# ###############################################
#  Запись баз данных
##############################################
# добавление через sql
# INSERT INTO
# users(name, age)
# VALUES('Bill',21)
# насколько одновременно
# INSERT INTO
# users(name, age)
# VALUES('TOM',20),
# ('Tim',41)
# меняем параметры лучше по id  так как других параметров может быть насколько
# UPDATE users
# SET age =22
# WHERE id = 2
# удобно по названию фирмы что то нужно поменять сколпом

# удаляем по id
# DELETE FROM users
# WHERE id = 3
# удалили тех кто старше 30
# DELETE FROM users
# WHERE age>30
#########################################
# добавление через питон
# 1. импорт библиотеки sqlite3
# 2. Подключаемся к бд
# 3. Назначить "курсор"
# 4. работаем с бд
# 5. отключаеся от бд
# подключаемся
# connection = sqlite3.connect('db/movies.sqlite')
# # назначим курсор
# cursor = connection.cursor()
# # запрос (помощью курсора)
# result = cursor.execute(
#     """
#     INSERT INTO
#     users(name, age)
#     VALUES('TOM',20),
#     ('Tim',41)
#     """
# )
# connection.commit()
# connection.close()
# import sqlite3
# import csv
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f,delimiter=',')
#     next(reader) # приём пропустить заголовок(первая запись- строка)
#     connection = sqlite3.connect('db/movies.sqlite')
#     cursor = connection.cursor()
#     for name, age in reader:
#         # print(name, age)
#         cursor.execute(
#             f"""
#             INSERT INTO
#             users(name,age)
#             VALUES ({name},{age})
#             """
#         )
# connection.commit()
#
# import sqlite3
# connection = sqlite3.connect('db/movies.sqlite')
# cursor = connection.cursor()
# import csv
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f,delimiter=',')
#     next(reader) # приём пропустить заголовок(первая запись- строка)
#
#     for name, age in reader:
#         # print(name, age)
#         cursor.execute(
#             f"""
#             INSERT INTO
#             users(name,age)
#             VALUES(?,?)
#             """, (name,int(age))
#         )
# connection.commit()# сколько раз будем запускать столько раз добавится. добавили из csv в sql
# #########################################
# # создадим класс
# import sqlite3
# from idlelib.rpc import response_queue
#
#
# class Crud:
#     def __init__(self, db_path):
#        self._conn =sqlite3.connect(db_path)
#        self._cur = self._conn.cursor()
#
#     def create(self, table_name, name, age):
#         self._cur.execute(
#             f"""
#                INSERT INTO {table_name}(name, age)
#                 VALUES(?, ?)
#                 """, (name, int(age))
#         )
#         self._conn.commit()
#
#     def read(self, table_name):
#         res = self._cur.execute(
#             f'SELECT * FROM {table_name}'
#         ).fetchall()
#
#         for num, name, age in res:
#             print(num, name, age)
#
#     def update(self, table_name, id_num, name=None, age=None):
#         query = f'UPDATE {table_name} SET name="{name}", age={age} WHERE id={id_num}'
#         # print(query)
#         self._cur.execute(
#             query
#         )
#         self._conn.commit()
#
#     def delete(self, id_num, table_name):
#         self._cur.execute(
#             f'DELETE FROM {table_name} WHERE id={id_num}'
#         )
#         self._conn.commit()
#
# db = Crud('db/movies.sqlite')
# db.delete(3, 'users')
# db.create('users', 'Дмитрий', 18)
# db.update('users', 8, 'Евгений', 19)
# db.read('users')

# # метод override(переопределяет метод унчтожения объекта)
# def __del__(self):
#     self._cur.close()
#     self._conn.close()


# https://www.deepseek.com/ - запрос на семантическое ядро
#  погода

# import requests
# from PIL import Image
# import io
#
# API_KEY = 'd301456e6513c2bb8655eb095834a3ac'
# URL = 'http://api.openweathermap.org/data/2.5/weather'
# CITY = 'вятские поляны'
#
# params = {
#     'q': CITY,
#     'appid': API_KEY,
#     'units': 'metric',
#     'lang': 'ru'
# }
#
# response = requests.get(URL, params=params)
# result = response.json()
# # print(result)
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# data = result['coord']
# ll = f'{data['lon']},{data['lat']}'
# # print(ll)
#
#
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1f}\xB0C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind} м/с')
# link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
# image = requests.get(link).content
# if image:
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.jpg')
#####################################################
# Декораторы!!!!!!!!!
# def answer(question):
#     return 'думайте сами'
# def dialog():
#     def answer(question):
#         if question.lower().startswith('когда'):
#               return 'Никогда'
#         else:
#               return 'УППС'
#     question =input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()

# Декаторы
# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         args_up_case = [str(arg).upper() for arg in args]
#         old_func(*args_up_case, **kwargs)
#     return new_func
# new_print =upper_case_print(print)
# new_print('Привет, Пока')
#
# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         case = kwargs.pop('case',None)
#         if case=='U':
#             args_up_case = [str(arg).upper() for arg in args]
#         elif case == 'L':
#             args_up_case = [str(arg).lower() for arg in args]
#         return old_func(*args, **kwargs)
#     return new_func
# new_print =upper_case_print(print)
# new_print('Привет, Пока')
# new_print('Привет, Пока',case='L')
# new_print('Привет, Пока',case='U')

# def outer():
#     x = 5
#
#
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#     inner()
#     print('New x=', x)
#
# outer()

# def logger(func):
#     counter = 0
#     def decorated_func(*args,**kwargs):
#         nonlocal counter
#         counter +=1
#         print(counter, '->', 'Аргументы: ', args,
#               'Именованые агрументы: ', kwargs)
#         result = func(*args, **kwargs)
#         print('____', 'Результат: ', result)
#         return result
#     return decorated_func
# @logger
# def make_burger(meal='говядиной',onion=False,tomato=False):
#     print('Булочка')
#     if onion:
#         print('Луковые кольца')
#     print('Котлета с', meal)
#     if tomato:
#         print('Помидоры')
#     print('Булочка')
#
# make_burger(meal='говядина', onion=True)

# import time
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         finish = time.time()
#         print(f'Функция исполнялась: {finish -start: .4f} cek.')
#         return result
#     return wrapper()
# @timeit
# def test():
#     time.sleep(0.8)
test()

