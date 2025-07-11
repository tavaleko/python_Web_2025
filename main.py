# # OOП Проектирование классов
# from abc import ABC, abstractmethod
#
#
# class Animal:
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гаф"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу"
#
#
# class Elephant(Animal):
#     def make_sound(self):
#         return "Протрубил"
#
#
# class Zoo:
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#
#     def make_all_sounds(self):
#         for animal in self.animals:
#             print(animal.make_sound())
#
#
# dog = Dog()
# cat = Cat()
# elephant = Elephant()
#
# zoo = Zoo()
#
# zoo.add_animal(dog)
# zoo.add_animal(cat)
# zoo.add_animal(elephant)
#
# zoo.make_all_sounds()

# написать приложение видео урок
# ОРГАНИЗАЦИЯ СЕТИ ИНТЕРНЕТ -> конпьюторная сеть-> интернет это сеть сетей.
# протакол - это совокупность правил регламентирующее функнции управления передачи данных сети.
# сесмитричный и не семитричный канал
# TCP рансмишен контрол протакол -протакол управления передачи
# IP интернет протокол
# IP организовывает разбивку на пакеты (IP - дейтаграммы)
# TCP это управляет потоком по этим маршрутам исправляет ошибки и гарантирует получение этих пакетов.
# TCP/IP
# HTTP(S)ПРОТОКОЛ ПЕРЕДАЧИ гипертекс трансфер протокол (S)sequre защищенный
# HTML ФОРМАТ ДОКУМЕНТА
# https://www.......
# FTP протокол заточеный на передачу данных (можно качать файлы с серверов)
# SMTP простой протокол пересылки электронной почты
# компьютор или сервер является частью сети к которой другие компьюторы подключаются как клиенты - хост система
# две кодировки
# 1.первая обязательная (очень дружественная компьютору) IP -адрес : 195.34.32.11 -> (195) это определение сети класса,
# последняя цифра 11 это адрес компьютора сети
# 2. вторая не обязательнвая(удобная человеку но не удобная комп.) DNS (domin name system)
# https://www.yandex.ru - .yandex домен первого уровня .spb  это региональный уровень каждый dns имеет свой ip адрес.
# ASCII (%20) 16 - ричный код символа пробела (%2С) это запятая
#nic.ru
#reg.ru
# whois.ru
# URL -uniform Resource Locator (купить доменное имя)
# http(s):// доменное-имя.зона/page1/?param1=value1&param2=value2
# на любой странице работает скрипт -бэк энд- по параметрах ищут скрипт
# капча
# Команда  для командной строки
# 1 командная строка нужна для простоты удаленной работы
# 2 механизмы автоматизации
# dir пролистать содержимое нашего каталога (файл, когда создан)
# cd (например images) далеее мы в это ветви ./images/ выйти ../images/ Заглубится в дерикторию
# чтобы выйти cd .. выйти выше в дерикторию
# mkdir и адрес папки
# rm  удаляем файл
# ls пролистать коталог для линокса
# rm -r с ключом -r удалит файл с ее содержимым без возвратно
#  cp info.txt docs/info.txt для линекс cp info.txt ./docs/info.txt
# ~ тильда возвращает в домашнюю дирикторию
# cp copy
# cp info.txt ./docs
# mv переместить файл
# mv info.txt./templace/iii.txt
# print('hello, world')
# python main.py
# C:\Users\LCIMS1\PycharmProjects\firstProject\.venv\Scripts\python.exe
# import sys
# if (len(sys.argv)) >=2:
#     print('Я',sys.argv[0], 'и мой аргумент', sys.argv[1])

import sys

print('Я',sys.argv[0], 'и мой аргумент', sys.argv[1])

if len(sys.argv) >=2:
    match sys.argv[1]:
        case 'p':
           print('Привет')
        case 'g':
           print('Пока')
        case _:
            print('Не понял')
# это для утилиты скрипт создает нужное количество дирикторий
# кнопки винд(значек виндоус) +r открывает командную строку далее cmd
