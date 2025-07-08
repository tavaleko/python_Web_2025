from operator import index
# txt =[4,2,4,6,3,5,9,7]
# txt1 =[5,1,8,2,6,8,1,2]
# txt2 =txt + txt1
# print(sorted(set(txt2)))

# res = []
# with open(('info.txt','rt')) as f:
#     while temp := f.readline():
#         res =temp.split(', ')
# res = list(map(lambda x: x.rstrip('\n'), res))
# res = set (res)
# res = sorted(int(x) for x in res)
# print(res)
#  res = []

# with open(('info.txt','rt')) as f:
#     while temp := f.readline():
#         res =temp.split(', ')
# res = set (list(map(lambda x: x.rstrip('\n'), res)))
# res = sorted(int(x) for x in res)
# print(res)

# res = []
# with open(('info.txt','rt')) as f:
#     while temp := f.readline('\n'):# читаем каждую строку по курсору
#         res =temp.split(', ')
#
# res = sorted(int(x) for x in set(res))
# print(res)
############################
# сериализация  это когда сложная структура которая превращается в последовательность байтов
# десериализация это последовательность байтов превращаются структуру
# pickling процесс консирвирования (не безопасный так как может проникнуть вирус в сеть нельзя использовать
# только на чистые файлы из своего компьютора)
# сериализация
# import pickle
# import pprint
#
# d = {
#     'стол':'table',
#     'стул':'chair'
# }# сериализация
# with open('dictfile.dat', 'wb') as p:
#     # d - что сериализуем, p - куда сериализуем
#     pickle.dump(d, p)
#
# # дессириализация
# with open('dictfile.dat', 'rb') as p:
#     d = pickle.load(p)
# pprint.pprint(d, width=15)
from pathlib import *
from tkinter.font import names

# from paht_lib import img_dir
#
# print(img_dir)# организация пути
######################################
# Работа с исключениями TRY-EXCEPT

# print(name) #NameError: name 'name' is not defined. Did you mean: 'names'? это не ошибка это исключение
# это не ошибка это типовая ситуация которая выбрасывает из программы деление на 0, не соотвествие типа данных
# fo = open('information.txt')#FileNotFoundError: [Errno 2] No such file or directory: 'information.txt'
# есть обертка try: execept:
# try:
#     fo = open('information.txt')
# except FileNotFoundError:
#     print('Такого файла нет')#Такого файла нет то есть в случае исключения можно записать ошибку и она выдаваться не будет
#
# try:
#     fo = open('information.txt')
#     print(fo.read())
#     fo.close()
# except FileNotFoundError:# веток ексепт может быть сколько угодно
#     print('Файл не обноружен  и создан с парометрами по умолчанию')#
#     with open('information.txt','wt',encoding='utf-8') as fo:
#         fo.write('По умолчанию')
# ######################################
# # Исключения
# # try:
# #     что пытаемся сделать
# # except:
# #     обрабатываем исключения
# # else:
# #      ветка которая отработает если исключений не было
# # finally:
# #     выполняется в любом случае
#########################################
# Полное написание при необходимости если открываем файл то надо делать его в обертке try-except или  finally
# только try использовать нельзя
# try:
#     fo = open('information.txt')
#     print(fo.read())
#     fo.close()
# except FileNotFoundError:# веток ексепт может быть сколько угодно
#     print('Файл не обноружен  и создан с парометрами по умолчанию')#
#     with open('information.txt','wt',encoding='utf-8') as fo:
#         fo.write('По умолчанию')
# else:
#     print('Файл открыт успешно. Читаем его и закрываем')
#     print(fo.read())
#     fo.close()
# finally:
#     print('Продолжаем работать')
######################################################
# Исключения они runtime в процессе работы
# flag = False# открывался ли на запись
# try:
#   fo = open('informations.txt', encoding='utf-8')
#   print(fo.read())
#
# except FileNotFoundError:# веток ексепт может быть сколько угодно
#     open('informations.txt', 'wt', encoding='utf-8')
#     flag = True
#     print('Файл не обноружен  и создан с парометрами по умолчанию')#
#
# else:
#     print('Файл открыт успешно. Читаем его и закрываем')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag:
#         fo.write('По умолчанию')
#         fo.close()
#         print('Продалжаем работать')
###########################################################
# print('Остаток от деления')
#
# try:
#     value = int(input('На что делим число 10:'))
#     res = 10% value
#     print(f'Остаток от деления 10 на {value} = {res}')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Надо вводить только целые числа')
# except Exception as exp:
#     print('Произошло исключение:', exp)
#     print('Остаток от деления')
# print('Остаток от деления')
# try:
#     value = int(input('На что делим число 10:'))
#     res = 10 % value
#     print(f'Остаток от деления 10 на {value} = {res}')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#
# except Exception as exp:
#     print('Произошло исключение:', exp.__class__.__name__)

# print('Остаток от деления')
# while ( value := int(input('На что делим число 10:'))):
#     try:
#         res = 10 % value
#         print(f'Остаток от деления 10 на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#
#     except Exception as exp:
#         print('Произошло исключение:', exp.__class__.__name__)

#
# print('Остаток от деления')
# flag = True
# while flag:
#     try:
#         value = int(input('На что делим число 10:'))
#         res = 10 % value
#         print(f'Остаток от деления 10 на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#
#     except Exception as exp:
#         print('Произошло исключение:', exp.__class__.__name__)
#     else:
#         flag = False
###################################################
# # "Бросаемся исключениями" - throw в питоне raise
#####################################################
# max_val = 10
# min_val = 1
#
# try:
#     val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
#     if not min_val < val < max_val:
#         raise ValueError ('введеное число вне диапазона ')
#     print(f'Введеное число {val} лежит в задоном диапазоне')
# except ValueError as exp:
#     print('Надо быть внимательнее:',exp)
#########################################
# Для целей отладки используют утверждения (assertions)
# В основном для нужд тестирования
#########################################
# try:
#     text = input('Введите текст: ')
#     assert  len(text) >3
# except AssertionError:
#     print('Слишком короткий текст')
# Задача 1
# text = [1,2,3,4,5,6,7,8,9]
#
# try:
#     index = int(input('Введите индекс: '))
#     if not 0 < index < 8:
#         raise ValueError('введеное число вне диапазона ')
#     print(f'Число по индексу {index}:{text[index]}')
# except ValueError as exp:
#     print('Надо быть внимательнее:',exp)
#
# lst = [1,2,3,4,5,6,7,8,9]
#
# try:
#     index = int(input('Введите индекс: '))
#     if -len(lst)< index<len(lst)-1:
#        raise ValueError ('Индекс вне диапазона')
#     res = lst[index]
#     print(f'Число по индексу {index}:{res}')
# except ValueError as exp:
#     mess = exp.args
#     if mess[0].startswith('invalid literal'):
#         print(f'водить надо число')
#     else:
#         print(exp)
#
# loop =True
# try:
#     index = int(input('Введите индекс: '))
#     print(f'Число по индексу {index}:{res}')
#2 задача
# while True:
#     a = input('ведите первое число: ')
#     b = input('ведите первое число: ')
#
#     if a.isdigit() and b.isdigit():
#         if int(b) ==0:
#             print('На ноль делить нельзя')
#         else:
#             print(int(a)/ int(b))
#             break
#     else:
#         print('водить надо только числа')
#

while True:
    a = input('ведите первое число: ')
    b = input('ведите первое число: ')
    try:
        res = int(a)/int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print(f'водить надо число')
    else:
        print(res)
        break
