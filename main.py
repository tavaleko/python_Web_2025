# number_to_str = {
#     0:'ноль',
#     1:'один',
#     2:'два',
#     3:'три',
#     4:'четыре',
#     5:'пять',
#     6:'шесть',
#     7:'семь',
#     8:'восемь',
#     9:'девять',
#     10:'десять',
#     11:'одинадцать',
#     12:'двенадцать',
#     13:'тринадцать',
#     14:'четырнадцать',
#     15:'пятнадцать',
#     16:'шеснадцать',
#     17:'семнадцать',
#     18:'восемнадцать',
#     19:'девятнадцать',
#     20:'двадцать',
#     30:'тридцать',
#     40:'сорок',
#     50:'тридцать',
#     60:'шестьдесят',
#     70:'семьдесят',
#     80:'восемьдесят',
#     90:'девяносто',
# }
# #функция с анотацией
# def number_to_word (n):
#     if len(str(n)) > 2:
#         return 'вводите двухзначное число'
#     if len(str(n)) == 1 or n in number_to_str:
#         return number_to_str[int(n)]
#     return number_to_str[int(str(n)[0]+ '0')] + '' + number_to_str[int(str(n)[1])]
#
#
# print(number_to_word(83))
#############################################
# ОБЛАСТЬ ВИДИМОСТИ
# ПРИМЕР ТАК ДЕЛАТЬ НЕ НАДО

# a = [1,2]# список
# def change_array():
#     a[0] = 0
#
# change_array()
# print(a)# так делать не надо это список или кортеж его можно менять выведет[0, 2]
#
# def print_array(array: list)-> None:
#     for item in array:
#         print(item)
# words =['Привет','мир']
# print_array(words)
# ПРИМЕР ТАК ДЕЛАТЬ  НАДО (->None:) для списков!!!!!!! и изменяемых данных

# def print_array(array: list)->None:
#     #нужно обязательно поставить -> None чтобы случайно не внести изменения в список
#     for item in words:
#         print(item)
#
# words =['Привет','мир']
# print_array(words)
# print_array(['a','b','c'])
# square = 'Дворцовая площадь'
# PI =3.14
# def circile_length(radius):
#     perimetr = 2*PI* radius
#     print(f'Длина окружности c радиусом {radius} = {perimetr:.2f}')
# circile_length(9)
# # Shadows name 'Square' from outer scope
#
# def square_area(length:int, width:int)-> None:
#
#     area = length * width # если есть глобальная переменная то внутри функции переменна не должна быть названа так же!
#     print(f'Площадь площади"{square}"={area}')
#
#
# #
# print('Давай встеретимся, где', square)
# square_area(320,240)
#
# def greet(name: str)->None:
#     print('Привет', name)
#     name = 'Друг' # Переназначаем переменную
#     print('Здравствуй,',name)
#
# greet('Пётр')
#
# def main():
#     print('Давай встеретимся, где', square)
#     square_area(320, 240)
#     greet('Пётр')
#
# main()# можно создать общую функцию в которой будет выходить ряд функций, чтобы не выводить которые были определены выше
#########################
#return vs yield _ функция возвращает значение, но не выходит из функции
###########################
# def generate_list():
#     for i in range(5):
#         yield i # генератор (возвращает, но не завершает)
#
#
# array = list(generate_list())# если мы не вложим в лист то он сгененирует номер
# яцейки, но преобразить ее может только форма может быть разные tuple,list
#
# print(array)
#
# def print_goodbye(arg):
#     print('Goodbye', end =' ')
#
#
# def print_cruel(arg):
#     print('cruel', end =' ')
#
#
# def print_world(arg):
#     print('world', end =' ')
#
# def main():
#     print_goodbye(1)
#     print_cruel(1)
#     print_world(1)
# main()# показана как работает функция main()
################################################
#Оператор is: a is b -> true будет только тогда это один и тот же объект a и b
#################################################
# a = 1
# print(id(a))# 140722130520504
# a += 1
# print(id(a))#140722130520536  был создан новый объект !!!!
#
# a = [0]
# print(id(a))#1679329464704
# a[0]+=1
# print(id(a)) #1679329464704 адрес не изменился так как это список(изменяемы еще множество и словари)
#
# d ={'a':1}
# print(id(d))#2566036565376
# d['a']+=1
# print(id(d))#2566036565376 это словарь он изменяемый
#
# my_refregirator = ['колбаса','сыр','масло']
# his_refregirator = ['колбаса','сыр','масло']
# print(my_refregirator == his_refregirator) # True он сравнивает по содержимому
# print(id(my_refregirator) == id(his_refregirator)) #False он сравнивает id они разные
# my_refregirator = ['колбаса','сыр','масло']
# his_refregirator = my_refregirator.copy() #[:]
# print(id(my_refregirator) == id(his_refregirator))# True мы прировняли значения
# my_refregirator += ['мясо']
# print(his_refregirator) # ['колбаса', 'сыр', 'масло', 'мясо'] выведет так как мы применяли равенство между переменными
# is это один и тот же объект
# print(my_refregirator is his_refregirator) #False is сравнивает по id
# temp = None
# print(type(temp))# <class 'int'>
# print(temp is None) # True id одинаковые
##################################
# Напишите функцию которая выводит массив
# def print_array(array:list, start:int = None):
#     if start is None:
#         for i in array:
#             print(i)
#     else:
#         for i in range(start, len(array)):
#             print(i) # не правильно, но работать будет
#
# a = [1,2,3]
# print_array(a, 1)
#
# def print_array(array:list, start:int = None):
#     if start is None:
#         for i in array:
#             print(i)
#     else:
#         for i in range(start, len(array)):
#             print(array[i])
#
# a = [1,2,3]
# print_array(a, 1)
# def print_array(array:list, start:int = None):
#     if start >len(array):
#         return
#     if start is None:
#         for i in array:
#             print(i)
#     else:
#         for i in range(start, len(array)):
#             print(array[i])
#
# a = [1,2,3]
# print_array(a, 1)
#
# print_array(a, 1)
# def print_array(array:list, start:int = None):
#     if start is not None and start > len(array):
#         return
#     if start is None:
#         start = 0
#         for i in range(start, len(array)):
#             print(array[i])
#
# a = [1,2,3]
# print_array(a, 1)
# Возврат нескольких значений из функции
# def coordinates()-> tuple:
#     return 5.4, 3.2 # будет кортеж
# x,y, *z = coordinates() # распоковка кортежей
# print(f'x={x}, y={y}, z ={z}') # если за ранее не знаешь сколько элементов будет можно использовать рест остаток
# #  вернёт x=5.4, y=3.2, z =[]
# def coordinates()-> tuple:
#     return 5.4, 3.2, 5.6,2.3 # будет кортеж
# x,y, *z = coordinates() # распоковка кортежей
# print(f'x={x}, y={y}, z ={z}') # если за ранее не знаешь сколько элементов будет можно использовать рест остаток
# # вернёт  x=5.4, y=3.2, z =[5.6, 2.3]
# def coordinates()-> tuple:
#     return 5.4, 3.2, 5.6,2.3 # будет кортеж
# x,*y, z = coordinates() # распоковка кортежей
# print(f'x={x}, y={y}, z ={z}') # если за ранее не знаешь сколько элементов будет можно использовать рест остаток
# # вернёт  x=5.4, y=[3.2, 5.6], z =2.3
# #--- * может быть только одна иначе будет ошибка * может быть только у одного аргумента
# # (где * там и остаток если в начале то сначала остаток а потом заданые параметры!)
# *names,surname = 'Кирилл Сулейман Бендорчук'.split()
# print(names,surname)# ['Кирилл', 'Сулейман'] Бендорчук
# names = 'Кирилл Сулейман Бендорчук'.split()
# print(*names)# Кирилл Сулейман Бендорчук
##############################################
#Функция с переменным числом переменных
# def multy(*args):
#     print(len(args))# подсчет числа аргутентов
#     print(args)# можем общащаться к каждому элементу по индексу перебором в цикле
#
# multy(1,2)# возвращает кортеж
# result = 1
#
# def multy(*args):# * говорит что аргументов может быть как один так и много
#     # if args is None:# не нужно
#     if not args:
#         return 0
#     for arg in args:
#         result *= arg
#     return result
#
# print(multy())  # возвращает кортеж
# result = 1
# def multy(*args):# * говорит что аргументов может быть как один так и много
#     if not args:
#         return 0
#     for arg in args:
#         result *= arg
#     return result
#
# print(multy(5.4,3.2,4,7))  # возвращает кортеж
# #UnboundLocalError: cannot access local variable 'result' where it is not associated with a value
# def multy(first, *args):# * говорит что аргументов может быть как один так и много
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
# print(multy(5.4,3.2,4,7))#483.84000000000003
# print(multy(2))#2
# def multy(*args, first):# *args переменные а First именованый
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
# # print(multy(5.4,3.2,4,7))#483.84000000000003
# print(multy(2))#ulty() missing 1 required keyword-only argument: 'first'
# def fio(name,surname):
#     return f'{name} {surname}'
#
# print(fio(name='Ирилл', surname='Парос'))
#
# def multy(*args, first=0):# *args переменные а First именованый
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
# print(multy(5.4,3.2,4,7))#0.0

# def summ(*args, operator='+'):
#     if not args:
#         return 0
#     for arg in args:
#         results += arg
#     return results
# print(summ(5,8,9,3)) # не работает



# программа сендвич
# def sandwich(type_of_meal,with_onion=False,with_tomato=False):
#     print('Булочка')
#     if with_onion:
#         print('лук')
#     print(type_of_meal)
#     if with_tomato:
#         print('Томат')
#     print('Булочка')
# print(sandwich('котлета', with_onion=True))# работает столбец Булочка лук котлета булочка
#######################################
# *args, **kwargs
def print_any(*args, **kwargs):
