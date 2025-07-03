# Домашняя работа
# def square(num):
#     return num **2
# nums =[1,2,3,4,5,6,7,8,9]
# squares = map(square, nums)
# print(list(squares))
#
# #у нас есть список 123456789 с помощью map  превратить с сторку и с помощью join соединить
# nums =[1,2,3,4,5,6,7,8,9]
#
# print(''.join(map(str,nums)))
##list(range(1,10)
# def square(num):
#     return num **2
# nums =[1,2,3,4,5,6,7,8,9]
# squares = map(square, nums)
# print(*list(squares), sep='')
# Критерий -вхождение подстроки
# в часности 'ан'
fruits = ['слива','банан','ананас','яблоко']
# # def string_contain(s):
# #     return 'ан'is s
# # print()
# #   res =list(filter(string_contain,frutes))
#
# # анонимные функции (анонимные однострочники)
# # lambda- функции
# # lambda <аргументы>:<выражение>
#
# is_longer_six = lambda word: len(word) >6
# is_first_letter_a =lambda word: word[0]=='а'
# string_contain = lambda s: 'ан' in s
#
# res=list(filter(lambda x: x[0]=='а',frutes))# заменяет функцию
# print(res)
# print(list(filter(lambda s: 'ан' in s,frutes)))# заменяет функцию
# # в одну строку вывести список квадратьов чисел от 3 до 15
# # [9,16,25,....]
# # print(list(map(lambda b: b**2,range(3,16))))# [9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225] дольше обработка
# # print([b**2 for b in range(3,16)])# [9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225] списочное выражение быстрее
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
# long_words = [word for word in words if len(word)>6]#списочное выражение
# print(long_words)
# ENGLICH_ABC = [chr(ch) for ch in range(ord('a'),ord('z')+1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'),ord('я')+1)]+['ё']
# print(ENGLICH_ABC)
# print(RUSSIAN_ABC)
# ENGLICH_ABC1 = set([chr(ch) for ch in range(ord('a'),ord('z')+1)])
# RUSSIAN_ABC1 = set([chr(ch) for ch in range(ord('а'),ord('я')+1)]+['ё'])
# ABC= ENGLICH_ABC1 ^ RUSSIAN_ABC1
# ABCD = set(ENGLICH_ABC)^set(RUSSIAN_ABC)^ set(map(str.upper,ENGLICH_ABC))^ set([x.upper()for x in RUSSIAN_ABC])
# print(ABCD)
#
# text1 ='Однажды, теперь и потом.'.lower()
# txt ='Однажды, теперь и потом.'
# # text1 = ''.join(filter(lambda x: x in ABC ^ {''}, text1))
# # print(text1)#однаждытеперь
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^{' '},text))
#
#
# def get_words(text: str)-> list:
#     return remove_punctuation(text).split()
#
#
# def long_words(text, lenght=4)-> list:
#     return filter(lambda x: len(x)>= lenght, get_words(txt))
# print(list(long_words(txt)))
# # # есть списочные выражения есть словарные
# # numbers1 = [1,2,3,4,5,] #list(range(1,6)
# # squares1 = {n: n**2 for n in numbers1}
# # print(squares1)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # numbers2 = range(1,11,2) #не четные числа
# # squares2 = {n: n**2 for n in numbers2}
# # print(squares2)#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# # numbers = range(2,11,2)  # четные числа
# # squares = {n: n**2 for n in numbers}
# # print(squares)#{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# # squares3 = {n: n**2 for n in range(1,10)if n %2==0}
# # print(squares3)#{2: 4, 4: 16, 6: 36, 8: 64}
# # source_dict ={
# #     'x': 1,
# #     'y': 2,
# #     'z': 3,
# # }
# # dest_dict ={k: v*2 for k, v in source_dict.items()}
# # print(dest_dict)#{'x': 2, 'y': 4, 'z': 6}
#
# txt ='Однажды, теперь и потом.'
# d = {}
# words =get_words(txt)
# # считаем частоту слов
# for word in words:
#     if words in d:
#         d[word] +=1
#     else:
#         d[word] =1
# res = {k:v for k,v in sorted(d.items(),key=lambda item: item[1])}
# # print(fruits.sort())# ни чего не возвращает так как показывает что выражение вернуло а оно не возвращает ни чего
# # # правильно
# # fruits.sort
# # print(fruits)
# # # или
# # print(sorted(fruits))
# print(sorted(fruits, key=lambda ch: len(ch)))
#############################################
# ключ сортировки
#####################################
# print(sorted(fruits))# ['ананас', 'банан', 'слива', 'яблоко'] отсортировал
# print(sorted(fruits, key=lambda s: (s[-1])))#['слива', 'банан', 'яблоко', 'ананас'] сортировка по последней букве слова
#
# good = [
#     ['Утюг',1500],
#     ['Фен',1000],
#     ['Телевизор',8000],
# ]
# goods = [
#     ['Утюг',1500,2],# товар,цена, количества
#     ['Фен',1000,1],
#     ['Телевизор',8000,3],
# ]
# print(sorted(good))#[['Телевизор', 8000], ['Утюг', 1500], ['Фен', 1000]]
# print(sorted(good, key=lambda s:s[1]))#[['Фен', 1000], ['Утюг', 1500], ['Телевизор', 8000]]
# print(sorted(goods,key=lambda s:(s[1],s[2],s[0])))#[['Фен', 1000, 1], ['Утюг', 1500, 2], ['Телевизор', 8000, 3]]
##############################################
# проверка коллекций any(), all()  применяется ко всем итерируемым объектам(колекциям)
#any любой элемент коллекции вернет true
# all все элементы коллекции возрращают true
######################################
# print(all([1,2,3]))# все элементы не нулевые True
# print(all([1,2,0]))# все элементы есть нулевой False вернет
# print(all([]))# пустой список возвращает True
# print(all([1,2,-3]))# все элементы отрицательные вернет True
# print(all([0]))# если 0 возвращает False
# words = 'один два три'.split()#>3
# list_for_analize = list(map(lambda x:len(x)>3,words))
# print(list_for_analize)#[True, False, False] больше трёх букв только "один"
# list_for_analize = list(map(lambda x:len(x)>2,words))
# print(list_for_analize)#[True, True, True] больше двух букв все слова
# print(any(list(map(lambda x: len(x)>5,words))))#False
#########################################
# потоковый ввод sys.stdin (стандартный ввод клавиатура стандартный вывод экран)
# это итератор (ctrl-z консоль виндоус)
# ctrl + d консоль в pycharp(параметры системной среды puth) системное окружение
# ctrl + d консоль в pycharp(параметры системной среды puth) системное окружение
###############################
# import sys
#
# for line in sys.stdin:
#     print(line) # после этого можно печатать внизу в консоли выйти из нее можно ctrl + d
# data=sys.stdin.readlines()
# data = [d.strip('\n')for d in data]
# print(data)#можно скопировать текст в консоль его увидет програма после ввода сначала нажимаю enter потом ctrl + d