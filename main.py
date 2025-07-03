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
# frutes = ['слива','банан','ананас','яблоко']
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
# text ='Однажды, теперь и потом.'.lower()
# text1 = ''.join(filter(lambda x: x in ABC ^ {''}, text1))
# print(text1)#однаждытеперь
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
# # print(list(long_words(txt)))
# # есть списочные выражения есть словарные
# numbers1 = [1,2,3,4,5,] #list(range(1,6)
# squares1 = {n: n**2 for n in numbers1}
# print(squares1)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# numbers2 = range(1,11,2) #не четные числа
# squares2 = {n: n**2 for n in numbers2}
# print(squares2)#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# numbers = range(2,11,2)  # четные числа
# squares = {n: n**2 for n in numbers}
# print(squares)#{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# squares3 = {n: n**2 for n in range(1,10)if n %2==0}
# print(squares3)#{2: 4, 4: 16, 6: 36, 8: 64}
# source_dict ={
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
# dest_dict ={k: v*2 for k, v in source_dict.items()}
# print(dest_dict)#{'x': 2, 'y': 4, 'z': 6}
