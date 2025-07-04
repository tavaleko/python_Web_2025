# # домашняя работа
# strings = [d.strip('\n')for d in sys.stdin.readlines()]
# lenght = len(strings)
# rem = lenght % 3
#
# if rem:
#     strings = strings[:lenght -rem]# отрезаем
# for x in range(0,lenght - rem, 3):# просто перебираеет тройки строк
#     summ = sum(len(a) for a in strings[x:x + 3])# sum([1,2,3]) применима только для списков!!!! выдаст 6
#     result= []
#     for s in strings[x:x +3]:
#         temp = s.lower().split()
#         result += filter(lambda a: len(a) % 2 ==summ % 2, temp)
#     result = sorted(set(map(lambda b:b.capitalize(), result)))[:5]
#     print((*result, sep='. '))
# lst =[1,2,3,4,5]
# res=0
# for x in lst:
#     res += x
# res = sum(lst)
#####################################
# Встроенные библиотеки
# PyPi
###############################
# import math
#
# print('Число Пи:', math.pi)# Число Пи: 3.141592653589793
# import math as m # пространство имен всей библиотеки
# from math import pi
# from math import sqrt
# from math import factorial
# print('квадратный корень 4:', sqrt(4))# квадратный корень 4: 2.0
# # from math import * # всю библиотеку вытягиваем сразу засорят пространство имен не стоит
# print('Факториал 5:',factorial(5))# Факториал 5: 120
# import math as m
# print(dir(m))
# # 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign',
# # 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial',
# # 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
# # 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
# # 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh',
# # 'tau', 'trunc', 'ulp'# косинус выводит в радианах туту показываются все функции которые есть в math
# from math import pi, sqrt, sin, radians, hypot

# print('Синус  30°:', round(sin(radians(30U00B0)), 2))# Синус 30: 0.5
# print('Синус  30°:', round(sin(radians(30U00B0)), 2))# Синус 30: 0.5
# print('Гипотинуза для 3 и 2: ', hypot(3,2))# Гипотинуза для 3 и 2:  3.605551275463989
#################################
# # Модуль рандом встроеный модуль
##############################
# import random as r
#
# for _ in range(10):
#     print(r.randint(0,10))
#     #print(r.randrange(0,10,2))
# import random as r
# lst = [1,2,3,45,6,7,8,9]
# res = r.choice(lst)
# print(res) # вывел 8 но каждый раз будет выводить разное число от 1 дл 9
# print(r.choice('орёл'))# в строке выбирает любые буквы
# не работает со словарями и множествами!!!!
# d = {'a': 1,
#      'b':2,
#      'c':3,
# }
# keys = list(d.keys())# перевели в лист
# key = r.choice(keys)
# print(d[key]) # на прямую к словарю обратиться нельзя
#
# zara = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
# for _ in range(10):
#     print(r.choice(zara), r.choice(zara)) # бросаем кубики выведет кубики
#################################################
# choice и sample отличия sample будет без повторов
#############################################
# lst = [1,2,3,45,6,7,8,9]
# res = r.sample(lst, k=5)# вторая часть пишется через именованый элемент обязательно!
# print(res) # вывел [8, 3, 7, 1, 6]
# for _ in range(10):
#     print(r.sample(lst, k=5))# каждый раз выводит разные, но уникальные числа без повторов
# ####################################################
# # shuffle перетосовать
############################################
# abc = 'qwerrytyuiopasdfghhjklzxcvbnm'
#
# lst1 = list(abc)
# r.shuffle(lst1)
# print(lst1)
# abc = 'qwerrytyuiopasdfghhjklzxcvbnm'
#
# lst1 = list(abc)+ ['1','2']+['#','$']
# r.shuffle(lst1)
# res = ''.join(lst1[:8])
# print(res)
############ задача сгенерировать пароль!!!!
# N = 8
# abc = 'qwerytyuiopasdfghhjklzxcvbnm'
# num ='1234567890'
# spec ='@#$&'
#
# abc = list(abc)# переводим в лист
# num = list(num)
# spec = list(spec)
#
# r.shuffle(abc)
#
# temp = abc[:N - 3]# вычитаем 3 символа под спец символы
# temp.append(r.choice(abc).upper())# переводим в Верхний регистр для большой буквы
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
# res = ''.join(temp)# объеденяем
# print(res)
#############################################################
# seed разобраться самим
# r.seed()
# print(r.random()) # 0.4842436831029522 всегда разное число
#########################################
# data time - встроеные часы нашего компьютора
########################################
# import datetime as dt
# from time import strftime
#
# print(dt.datetime.now())# 2025-07-04 12:24:30.189750 сейчас по мировому стандарту
# print(dt.datetime.now().date())#2025-07-04
# print(dt.datetime.now().time())#12:25:56.487988


#######################################
# # strftime встроеный модуль
##########################################
# time =dt.datetime.now()
#
# ftime = time.strftime('%d')
#
# print(ftime)# получили что сегодня 4 число
# ftime = time.strftime('%d-%m-%y')
# print(ftime)# 04-07-25
# ftime = time.strftime('%d/%m/%y')
# print(ftime)# 04/07/25
# ftimeh = time.strftime('%H:%M')
#
# print('Сегодня: ', ftime)#Сегодня:  04/07/25
# print('Время: ', ftimeh)# Время:  12:32
# # время заказа
# my_time = dt.time(15,27,35)
# print(my_time)#15:27:35 не обязательно писать секунды
# my_date =dt.date(2025,7,4)
# print(my_date)#2025-07-04 стандартное написение через дефис!!!!
# my_day_time = dt.datetime.combine(my_date,my_time)
# print(my_day_time)#2025-07-04 15:27:35
# date1 = dt.date(2025,6,15)
# date2 = dt.date(2025,7,3)
# delta = date1-date2
# print(delta)# -18 days, 0:00:00
# print(dir(dt))
# #'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo' методы datetime есть
# # обривиатура месяца
#############################################
## pprint еще один встроеный модуль
############################################
# from pprint import pp
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# print(matrix)
# pp(matrix)
##############################################
## ВНЕШНИЕ БИБЛИОТЕКИ
##Графика
## PIL -Python Imagine Library
## pip - пакет для установки дополнительных библиотек! установщик он тоже может устареть
## pip install pillow (в консоли)
## pip uninstall (в консоли)убирает
## pip list (в консоли) показывает сколько програм есть в окружении
### PIL удалится с проектом
### pip.exe
### file-> tools-> Sync ->requirements.txt
##############################
## ВНЕШНИЕ БИБЛИОТЕКИ
##Графика
## PIL -Python Imagine Library(растровые изображения еще бывают векторные)
## pip install pillow
## pip.exe
### pip freeze >requirements.txt создает сайла зависимости заморозка
# pip install -r requirements.txt устанавливает все библиотеки из requirements.txt
# синхронгизация file-> tools-> Syns Python ->requirements.txt(там все рухнет перед этим лучше комитить)
# RGB -> 0 ДО 256 (растровые изображения)
####################################
# загрузить фото в python
# new-> Directory-> назовем image
# нажимаем image -> Open in -> Explorer-> откроется рабочий стол -> перетащить рисунок
########################
# thumbnail (скрип)
######################
# from PIL import Image
#
# image = Image.open('images/python.jpg')
# print(image) #<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=800x600 at 0x25A83D7DC10>
# print(image.size)#(800, 600) возвращает кортеж
# # делаем распоковку
# x,y = image.size
# mode = image.mode
# pixels = image.load()# загрузить таблицу пикселей
# # y растет сверху в низ, х растет в слева на право как в декарте
# print(f'Ширина = {x}, высота = {y}')
# print(f'Цветовая схема: {mode}')
# # for i in range(x):
# #     for j in range(y):
# #         r,g,b = pixels[i,j]
# #         pixels[i,j] = b,r,g
#
# image.save('images/python2.jpg')# все собой представляет RGB кортеж
# # негатив инвертируем пиксили
# инверсия неготив
# for i in range(x):
#     for j in range(y):
#         r,g,b = pixels[i,j]
#         pixels[i,j] = 255-b,255-r,255-g
#
# image.save('images/python2.jpg')# все собой представляет RGB кортеж
# # Grayscale
# for i in range(x):
#     for j in range(y):
#         r,g,b = pixels[i,j]
#         average = (r+b+g)//3
#         pixels[i,j] = average,average, average# серая картинка
#
# image.save('images/python2.jpg')# все собой представляет RGB кортеж
##########################
# поворот картинки
# image_rotate = image.rotate(60)
#
# image_rotate.save('images/python2.jpg')  # все собой представляет RGB кортеж
# # Перевернёт рисунок
# image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)#FLIP_UP_DOWN верх ногами
# image_flip.save('images/python2.jpg')# перевернутый рисунок
###################################
## обрезать рисунок
#
# cropped = image.crop((250,0,550,300))# обрезаем рисунок
# cropped.save('images/python2.jpg')# обрезаем рисунок
#################
# расширение сжатия
# x, y = image.size
# ratio = x//y # только целочисленное деление
# resized = image.resize((400,300))
# resized.save('images/python2.jpg')# сжатие расширение пропорции соблюдаем мы! уменьшаем увеличиваем
#########################################
# Pillow drawing- как рисовать
from PIL import Image, ImageDraw

image = Image.new('RGB',(600,400),(0,0,255))
draw = ImageDraw.Draw(image)
draw.line((0,0,600,400),fill=(255,0,0),width=5)
RED = (255,0,0)
draw.line((600,0,0,400),fill=RED,width=5)
draw.rectangle((10,10, 590,390),outline=RED,width=10)
draw.ellipse((8,8, 550,350),outline=RED,width=10)
# коды цветов https://colorscheme.ru/html-colors.html?ysclid=mcots3rdx9171568779
#Текст
draw.text((150,50),'Текст', fill=RED)
#Полигон
POLI = [
    (150,150),
    (320,150),
    (580,400)
]
draw.polygon(POLI, outline='green',width=15)
image.save('images/blue.jpg')
# Голубое небо 600 на 400 в углу солнце выглядывать и написать солнечный день
image = Image.new('RGB',(600,400),(135,206,250))
draw.ellipse((90,9, 500,40),outline='yellow',width=10)
image.save('images/light_blue.jpg')
