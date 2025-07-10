# ООП polymorphism полиморфизм
# method override; operator overloading -перегрузка оператора
# # когда мы вызываем принт и пишем 1+2 будет три это будет целое число потому что оператор + полиморфный
# print(1+2)#3 -> int
# print(1+2.0)#3.0-> float
# print('abc'+'def')#abcdef-> str
# print([1,2]+[3,4])#[1, 2, 3, 4] сложили списки
# def func(x,y):
#     return x+y
# print(func(2,3.0))#5.0 -> float
from multiprocessing.util import sub_debug


#
# def get_author():
#     return set._author
#
#
# class Book:
#     def __init__(self, title,author):
#         self.title = title
#         self.author = author
#
#     def get_title(self):
#         return self.get_title
#
#
#     def get_author(self):
#         return self.get_author
#
#
# book = Book('Язык С++', 'Бьярн Страупструп')
#
# print(f'{book.get_title()},{get_author()}')

# полиморфизм это спойство кода работать с разными типами данных
# from math import pi
PI = 3.14
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def perimetr(self):
#         return 2 * PI * self.radius
#
#     def area(self):
#         return PI*self.radius **2
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
# def shape_info(shape):
#     print(f'Площадь: {shape.area()}, Периметр: {shape.perimetr}')
#
#
# s =Square(10)
# shape_info(s)#Площадь: 100, Периметр: <bound method Square.perimetr of <__main__.Square object at 0x000002292A2DAC90>>
#
# cr = Circle(10)
# shape_info(cr)#Площадь: 314.0, Периметр: <bound method Circle.perimetr of <__main__.Circle object at 0x000001D623ADAE40>>
#
# print(dir(s))#->'side'] все остальные параметры одинаковые
# print(dir(cr))#->'radius'] все остальные параметры одинаковые
# # утиная типизация у питона- Полиморфизм
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def perimetr(self):
#         return 2 * self.width + 2 * self.height
#
#     def area(self):
#         return self.width * self.height
#
#     def shape_info(shape):
#         print(f'Площадь: {shape.area()}, Периметр: {shape.perimetr}')
#
# r = Rectangle(10)
# shape_info(r)# не работает
#
# class Circle:
#     def __init__(self):
#         self.radius = radius
#         self.radius = "Круг"
#     def perimetr(self):
#          return 2 * PI * self.radius
#
#     def area(self):
#         return PI*self.radius **2
# def shape_info(shape:object):
#     print(f'Площадь{shape.get_name()}a: {shape.area()}')
# #
# # посмотри нужно копировать
# isinstance(объект, тип) -> True
# isinstance(объект, (тип1, тип2, типN)) -> True если не совпадет вернет False
# rect,c,sqr = 'Прямоугольник', 'круг', 'квадрат'
#
# def shape_info(shape:object):
#     if isinstance(shape,Circle):
#         fig = c
#     elif isinstance(shape,Rectangle):
#         fig = rect
#     elif isinstance(shape,Square):
#         fig = sqr
#     print(f'Площадь: {fig}a:{shape.area}, Периметр: {shape.perimetr()}')



class Person:
    def __init__(self, name='Bill', age=1):
        # свойства (поля) класса
        self._name = name
        self._age = age

    # setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст — ', new_age)

    # getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name}. Возраст: {self._age}')

class Student:
    def __init__(self, name='Bill', univ=''):
        self._name = name
        self._univercity = univ

    def get_univercity():

class Employee:
    def __init__(self, name='Bill', comp=''):
        self._name = name
        self._company = comp

    def get_company():


people = [
    Person('Александр', 27),
    Student('Дмитрий','ГУАП'),
    Employee('Петр','Авангард'),
]

for person in people:
    if isinstance(person, Student):
        print(person.get_univercity())
    elif isinstance(person,Employee):
        print(person.get_company())
    else:
        print(person.get_name())

