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
#     print('Файл не обноружен  и создан с параметрами по умолчанию')#
#
# else:
#     print('Файл открыт успешно. Читаем его и закрываем')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag:
#        fo.write('По умолчанию')
# #         fo.close()
# #         print('Продолжаем работать.')
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

# while True:
#     a = input('ведите первое число: ')
#     b = input('ведите первое число: ')
#     try:
#         res = int(a)/int(b)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#     except ValueError:
#         print(f'водить надо число')
#     else:
#         print(res)
#         break
##########################################
# Обучаемый словарь
# минимальная версия если dict.dat отсутствует
# import pickle
# voc = {
#     'стол':'table',
#     'стул':'chair',
# }
# # функция для распечатки словоря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k,v in voc.items():
#         print(k, '-',v)# Alt -0151 длинное тире
#
#
# # загружаем словарь из файла
# try:
#     with open ('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open ('dict.dat', 'wb') as dump_out:
#         pickle.dump((voc, dump_out))
#     print('Создан минимальный словарь')
#     print_voc()
#
# while True:
#      temp = input('\n Введите слово для перевода или"# " для завершения: ')
#      word = temp.strip().lower()
#      if word == '#' or word == '№':
#          break
#      if word in voc.keys():
#          translate = voc[word]
#          print(f'Слово "{word}" переводится как {translate}. \n')
#      else:
#          print(f'Значение слова {word} отсутствует в словаре.')
#          newkey =f'А как слово {word} переводится'
#          newkey += 'Если ни чего не вводите нажмите ENTER, \n'
#          newkey += 'или введите его здесь: '
#          new_word = input(newkey)
#
#          if new_word != '' or len(new_word) >2:
#              voc[word] = new_word
#              print(f'Слово {word} с переводом {new_word} внесено в словарь')
#          else:
#              print('Ничего не введено или слишком короткое слово')
#              continue
# # сохронить словарь
# with open ('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc, dump_out)
# print('До новых встречь!')
#
# import pickle
#
# # минимальная версия, если файл dict.dat отсутствует
# voc = {
#     'стол': 'table',
#     'стул': 'chair',
# }
#
#
# # функция для распечатки словаря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k, v in voc.items():
#         print(k, '—', v)  # Alt + 0151
#
#
# # загружаем словарь из файла
# try:
#     with open('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open('dict.dat', 'wb') as dump_out:
#         pickle.dump(voc, dump_out)
#     print('Создан минимальный словарь: ')
#     print_voc()
#
# while True:
#     temp = input('\nВведите слово для перевода или "#" для завершения: ')
#     word = temp.strip().lower()
#     if word == '#' or word == '№':
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f'Слово "{word}" переводится как {translate}.\n')
#     else:
#         print(f'Значение слова {word} отсутствует в словаре.')
#         newkey = f'А как слово {word} переводится.\n'
#         newkey += 'Если ничего не вводите нажмите ENTER,\n '
#         newkey += 'или введите его здесь: '
#         new_word = input(newkey)
#
#         if new_word != '' or len(new_word) > 2:
#             voc[word] = new_word
#             print(f'Слово {word} с переводом {new_word} внесено в словарь')
#         else:
#             print('Ничего не введено или слишком короткое слово')
#             continue
#
# # Сохранить словарь
# with open('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc, dump_out)
#
# print('До новых встреч!!!')

##########################################################
# Библиотека pymorphy
# pip install pymorphy3
# pip install -U pymorphy3-dicts-ru
#
###############################################
# import pymorphy3

# morph = pymorphy3.MorphAnalyzer()
# print(morph.parse('Дмитрий'))# [Parse(word='дмитрий', tag=OpencorporaTag('NOUN,anim,masc,Name sing,nomn'),
# normal_form='дмитрий', score=0.985915, methods_stack=((DictionaryAnalyzer(), 'дмитрий', 61, 0),)),
# Parse(word='дмитрий', tag=OpencorporaTag('NOUN,anim,femn,Name plur,gent'), normal_form='дмитрия',
# score=0.007042, methods_stack=((DictionaryAnalyzer(), 'дмитрий', 64, 8),)), Parse(word='дмитрий',
# tag=OpencorporaTag('NOUN,anim,femn,Name plur,accs'), normal_form='дмитрия', score=0.007042,
# methods_stack=((DictionaryAnalyzer(), 'дмитрий', 64, 10),))]

# from pymorphy3 import MorphAnalyzer
#
#
# form = MorphAnalyzer().parse('бутылка')[0]
#
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl +1}{form.make_agree_with_number(btl+1).word} пива')
#     print('Возьмём одну и выпьем')
#     if btl %10 == 1 and btl != 11:
#         remain = 'Осталось'
#     else:
#         remain = 'Осталось'
#     print(f' {remain}{btl} {form.make_agree_with_number(btl+1).word}пива')
######################################################
# Линтеры -контролирует следование хорошим практикам
# pip install flake8
# (flake8-bugbeear- для нахождения логических ошибок в коде)
# (pep8-naming- проверяет на соответствие pep8)
# pip install flake8-bugbear pep8-naming
########################################################
# file-setting-tools-terminal- shell puth- powershell
# prrogect- venv-flake 8- равая кнопка мыши абсолютный путь
#$ where flake8
#C:\Users\LCIMS1\PycharmProjects\firstProject\.venv\Scripts\flake8.exe
#--max-complexity 10 $FileDir$/$FileName$
# main- правой кнопкой мыши-external tools- flake8
# Arguments: --max-complexity 10 $FileDir$/$FileName$
# Path: $FileDir$
# Advanced Options/OutputFilter: $FILE_PATH$:$LINES$
