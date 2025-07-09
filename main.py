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
from http.client import CannotSendRequest

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

# pattern = r'<img[^>]+src="([^">]+)"'# только путь к картинке
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
# import requests # парсинг
# html = requests.get('https://skillbox.ru').text
# result = re.findall(pattern, html)
# print(result)#выведет большой объем данных
# это всё было операционое програмирование, далее мы будем проходить
# Объектно Оринтированое програмирование(инкапсериаованое програмирование)(encapsulation)
# Любой сервер поддерживает php (нужно иметь пайтон шелл на сервере) php  язык програмирования самый распрастраненный
# битрикс написан основном на языке PHP. Он также использует другие технологии, такие как JavaScript и CSS
# word press написан на php
# сейчас пишут на React (иногда React.js или ReactJS) — JavaScript-библиотека с открытым исходным кодом для
# разработки пользовательских интерфейсов
# все написано на
# всё состоит из
# свойства
# методы
# класс это прототип будущего объекта который описывает модель свойства и поведение
# класс это данные и методы по работе с ними
# экземпляр это объект поражденный классом
# объект
# атрибут свойства присущие объекту (класс это набор атрибутов)
# # методы
# # питон является объекто оринтированым языком
#####################################################
# Свойства класса
# a = 3
# print(a.__class__)#<class 'int'>
# print(a.__class__.__name__)#int
#
# a = 3.
# print(a.__class__.__name__)#float
#
# a= None
# print(a.__class__)#<class 'NoneType'>
# # класс начинается с большой буквы!!!!
# class Fruit:
#     pass
#
# a = Fruit()# Конструкция или метод
#
# print(a)#<__main__.Fruit object at 0x000001C71258A570>
# print(a.__class__)#<class '__main__.Fruit'>
# a.name ='Яблоко'
#
# print(a.name)#Яблоко
# a.weight = 120
# print(a.weight)
# d = Fruit()
# d.name = 'мёд'
# d.weigth = 150
# print(d.name)#мёд
# print(d.weigth)#150
# #атрибуты это принятые переменные не сущестующее свойство и не существующий метод
####################################
# # Методы класса
# class Greater:
# # метод это та же функция приведенная класс
#     def hello(self):
#         print('Привет, мир!')
#
#
# g = Greater()# без присвоения работать не будет! метод может быть определен только внутри класса
# g.hello()#Привет, мир!
# Метод
# cclass Great:
#     def hello(self):
# # в место self может быть любое слово но програмисты договорились использовать self работает и с горшком
#         print('Привет, мир!')
#     def bye(self)-> None:
#         print('Пока Мир!')
#
#
# g = Great()
# g.hello()#Привет, мир!
# g.bye()#Пока Мир!
# что такое (self) в него передается тот объект через который вызван метод.
# (self) это контекстный объект в, который передается выбраный метод.
# Ссылка на который вызван класс в данных памяти ссылаентся на адрес памяти который он создаётся.
#
# class Great:
#     def hello(self, name = 'Noname'):
# # можно добавить второй элемент в данном случае name его надо добавить и ниже для вывода
#         print('Привет,', name)
#     def bye(self)-> None:
#         print('Пока Мир!')
#
#
# g = Great()
# g.hello('Ольга')#Привет, Ольга
# g.bye()#Пока Мир!
###############################################
# Конструктор
#Методы классов и анализ предыдущих вызовов
# class Car:
#     def __init__(self):
#         print('Конструктор вызван')
#
#     def start_engine(self):
#         self.engine_on = True# присвоен адрес памяти self
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place}')
#         else:
#             print('Двигатель не заведен, не едем')
#
#
# car = Car()
# car.start_engine()
# car.drive_to('Город')
#
# class Car:
#     def __init__(self):
#         self.engine_on = False
#
#     def start_engine(self):
#         self.engine_on = True# присвоен адрес памяти self
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place}')
#         else:
#             print('Двигатель не заведен, не едем')
#
#
# car = Car()
# # car.start_engine()
# car.drive_to('Город')
#
# car = Car()
# car.start_engine()
# car.drive_to('Город')
#
# class Car:
#     def __init__(self,brand, model, color):
#         self.brand = brand#'Skoda'
#         self.model = model#'Octavia'
#         self.color = color#'red'
#         self.engine_on = False
#
#     def start_engine(self):
#         self.engine_on = True# он вызывался из нутри капсулы
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place} на {self.brand} {self.model} {self.color}')
#         else:
#             print('Двигатель не заведен, не едем')
#
#
# car = Car('Skoda','Actavia','red')
# car.start_engine()
# car.drive_to('Город')
#
# car2 = Car('noname','nomodel','nocolor')
# car2.start_engine()
# car2.drive_to('Город')
#
# # from libs import Car
#
# class Person:
#     def __init__(self, name='Bill',age=1):
#         self.name = name# так нельзя нельзя обращаться на прямую можно испортить
#         self.age = age# так нельзя
# #
# # p = Person()
# print(p.age)# 1
# print(p.name)#Bill
# ###############################################
# #Геттеры и сеторы
# ####################################
# class Person:
#     def __init__(self, name='Bill',age=1):
#         # свойства (поля) класса
#         self._name = name# так правильно
#         self._age = age
#
#
#
#     def person_info(self):
#         print(f'Человек с именем: {self._name}. Возраст:{self._age}')
#
#     #setters
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#
#     def set_age(self, new_age):
#         if 0< new_age <150:
#             self._age = new_age
#         else:
#             print('Некоректный возраст-',new_age)
#
#     # getter
#     def get_age(self):
#         return self._name
#
# p = Person()
# p.set_age(548)
# print(p._age)# 1
# print(p._name)#Bill
# #metaspace
#########################################################
# Статичные члены класса
# class Car:
#     # счетчик машин
#     counter = 0
#     def __init__(self,brand='noname', model='nomodel', color='nocolor'): # для старта значений нужен __init__
#     #в капсулу не кто не лезет
#         self.brand = brand#'Skoda'
#         self.model = model#'Octavia'
#         self.color = color#'red'
#         self.engine_on = False
#         Car.counter += 1
#
#     def start_engine(self):
#         self.engine_on = True# он вызывался из внутри капсулы
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place} на {self.brand} {self.model} {self.color}')
#         else:
#             print('Двигатель не заведен, не едем')
#     @staticmethod
#     def get_counter():
#         return Car.counter
#
# car1 =Car()
# car2 =Car()
# car3 =Car()
# car4 =Car()
# car5 =Car()
# print('В парке',Car.get_counter(),'машин')
####################################################
# инплементация
#
# class Clicker:
#     def __init__(self):
#         self.counter =0
#
#     def click(self):
#         self.counter += 1
#
#     def get_counter(self):
#         return  self._counter
#
#     def reset(self):
#         self.counter = 0
#
# cl = Clicker()
# cl.click()
# cl.click()
# cl.click()
# print(cl.get_counter())

class Separator:
    def __init__(self):
        self.odd = []
        self.even = [] # не четные
    def add_num(self, num):

    def get_odd(self):
        return self.odd


    def get_even(self):
        return self.even

