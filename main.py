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



# class Person:
#     def __init__(self, name='Bill', age=1):
#         # свойства (поля) класса
#         self._name = name
#         self._age = age
#
#     # setters
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#     def set_age(self, new_age):
#         if 0 < new_age < 150:
#             self._age = new_age
#         else:
#             print('Некорректный возраст — ', new_age)
#
#     # getters
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def person_info(self):
#         print(f'Человек с именем {self._name}. Возраст: {self._age}')
#
# class Student:
#     def __init__(self, name='Bill', univ=''):
#         self._name = name
#         self._univercity = univ
#
#     def get_univercity():
#         return self._univercity
#
# class Employee:
#     def __init__(self, name='Bill', comp=''):
#         self._name = name
#         self._company = comp
#
#     def get_company():
#           return self._company
#
#
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий','ГУАП'),
#     Employee('Петр','Авангард'),
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univercity())
#     elif isinstance(person,Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())
#
lst =list(range(1,15))
# lst += [a]
#
# class Selector:
#     def __init__(self,vals):
#         self.values = vals[:] # получаем копию
#
#     def get_odd(self):
#        return [x for x in self.values if x %2 ==1]# остаток от деление True  то есть четные
#     def get_even(self):
#         return [x for x in self.values if x % 2 == 0]## остаток от деление False то есть не четные
#
#
# s = Selector(lst)
# print(s.get_odd())
# print(s.get_even())

# class Stat:
#     def __init__(self, vals):
#          self.values = vals[:] # получаем копию
#
#     def get_min(self):
#         return [ x for x in self.values if x == 1]
#     def get_max(self):
#         return [ x for x in self.values if x == 1]
#     def get_aver(self):
#         return [ x for x in self.values if x != 1]
#
# s = Stat(lst)
# print(s.get_min())
# print(s.get_max())
# # print(s.get_aver())
#
# class Stat:
#     def __init__(self, vals):
#          self.values = vals[:] # получаем копию
#
#     def is_all_int(self)-> bool:
#         return all(isinstance(item,int) for item in self.values)
#
#     def is_min(self):
#         if is_int():
#             return min(self.values)
#         return None
#
#     def is_max(self):
#         if is_int(self):
#             return max(self.values)
#         return None
#
#     def get_aver(self):
#         if self.is_all_int():
#             return sum(self.values) / len(self.values)
#         return None
#
# s = Stat(lst)
# print(s.is_int())
# print(s.is_int())
# print(s.get_aver())
##############################################
### OOP magic methods
###method override; operator overloading
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#          return f'<Point: ({self.x},{self.y})>' #<Point: (0,0)>  если без этой строки то вывод ниже
# p =Point()
# print(p)#<__main__.Point object at 0x000001F59E4A9BB0>
# # str(a)-> a.__str__()
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#          return f'<Point: ({self.x},{self.y})>'# str  выведет строку
#     def __repr__(self):
#         return f'<Point: ({self.x},{self.y})>'# report представитель он переводит если несколько аргументов
# p = [Point(),Point() ]
# print(p)#[<Point: (0,0)>, <Point: (0,0)>]
# # str(a)-> a.__str__()
#
#
#
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#          return f'<Point: ({self.x},{self.y})>'# str  выведет строку
#     def __repr__(self):
#         return f'<Point: ({self.x},{self.y})>'# report представитель он переводит если несколько аргументов
#
#     def __sub__(self, other):
#         return Point(abs(self.x -other.x), abs(self.y - other.y))# (abs)абсолютные значения без разницы что из чего вычитать
#
# p1 = Point(5,7)
# p2 = Point(9,12)
# print(p1-p2)#<Point: (4,5)>
#
#
#
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#          return f'<Point: ({self.x},{self.y})>'# str  выведет строку
#     def __repr__(self):
#         return f'<Point: ({self.x},{self.y})>'# report представитель он переводит если несколько аргументов
#
#     def __add__(self):
#         return ((self.x -other.x)**2 + (self.y - other.y)**2)**0.5
#
# p1 = Point(5,7)
# p2 = Point(9,12)
# print(p1+p2)#<Point: (4,5)>
# шпаргалка по спец методам питона (у алисы) Alice.yandex.ru
# from math import hypot
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#          return f'<Point: ({self.x},{self.y})>'# str  выведет строку
#     def __repr__(self):
#         return f'<Point: ({self.x},{self.y})>'# report представитель он переводит если несколько аргументов
#
#     def __add__(self,other):
#         return hypot (self.x -other.x, self.y - other.y)
#
# p1 = Point(5,7)
# p2 = Point(9,12)
# print(p1 + p2)#

# class MyTime:
#     def __init__(self, minutes,seconds):
#         if 0<= minutes < 60:
#             self.minutes = minutes
#         if 0 <= seconds < 60:
#             self.seconds = seconds
#
#     def __str__(self):
#          return f'<Time: ({self.minutes} : {self.seconds})>'# str  выведет строку
#          # чтобы между ними была : нужно место , ее поставить
#     def __repr__(self):
#         return f'<Time: ({self.minutes},{self.seconds})>'# report представитель он переводит если несколько аргументов
#
#
# t = MyTime(13,15)
# print(t)
#
# #
#
# class MyTime:
#     def __init__(self, minutes,seconds):
#         if 0<= minutes < 60:
#             self.minutes = minutes
#         if 0 <= seconds < 60:
#             self.seconds = seconds
#     def __add__(self,other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s//60
#         s =s %60
#         m = m %60
#         return MyTime(m,s)
#
#     def __str__(self):
#          return f'<Time: ({self.minutes}:{self.seconds})>'# str  выведет строку
#          # чтобы между ними была : нужно место , ее поставить
#     def __repr__(self):
#         return f'<Time: ({self.minutes},{self.seconds})>'# report представитель он переводит если несколько аргументов
#
#
# t1 = MyTime(13,15)
# t2 = MyTime(53,25)
# print(t1 + t2)
#
#
# class MyTime:
#     def __init__(self, minutes,seconds):
#         if 0<= minutes < 60:
#             self.minutes = minutes
#         if 0 <= seconds < 60:
#             self.seconds = seconds
#     def __add__(self,other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s//60
#         s =s %60
#         m = m %60
#         return MyTime(m,s)
#
#     def __str__(self):
#          return f'<Time: ({self.minutes:02}:{self.seconds:02})>'# str  выведет строку
#          # чтобы между ними была : нужно место , ее поставить
#     def __repr__(self):
#         return f'<Time: ({self.minutes},{self.seconds})>'# report представитель он переводит если несколько аргументов
#
#
# t1 = MyTime(13,15)
# t2 = MyTime(53,25)
# print(t1 + t2)
#########################################################
# Метод __call__ экземпляр класса становится вызываемым как функция
# Позволяет экземплярам пользовательских типов представляться объектами, поддерживающими вызов. self : Ссылка на экземпляр
# y = ax^2 + bx + c
# class SquareFunction:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __call__(self, x):
#         return self.a* x **2 + self.b * x + self.c
#
# s = SquareFunction(1,2,3)
# print(s(2))
###########################################################
## Наследование
# Класс от которого наследование: базовый, родительский, супер класс
# Класс, который наследуется дочерний
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
# class Square(Rectangle):
#     # можно использовать базовый класс и добавлять что то свое наследований может быть много
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#         self.name = 'квадрат'# сначала берет своё потом уже к классу выше
# # по-этому пишет имя квадрат если бы не было указано имя писал бы прямоугольник т.к. Rectangle имеет имя прямоугольник
#
#     # def perimetr(self):# так как мы использовали супер функцию
#     #     return 4 * self.side
#     #
#     # def area(self):
#     #     return self.side ** 2
#     #
#     # def get_name(self):
#     #     return self.name
#
# s = Square(5)
# print(s.area())
# print(s.perimetr())
#########################################################
# from math import pi
# # Shape не нуждается в супер функции так как не несет в себе переменных, если есть переменные обязательно нужет super
# #  чтобы перенести переменные в нвследующий класс
# class Shape(object):# object это наивысший класс если ни чего не писать тоже сработает он идёт по умолчанию
#     def info(self):
#         print(f'Класс: {self.__class__.__name__}')
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return round(2 * pi * self.radius, 2)
#
#     def area(self):
#         return round(pi * self.radius ** 2, 2)
#
#     def get_name(self):
#         return self.name
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
# class Square(Rectangle):# можно добавить через запятую Shape так даже правильнее будет
#     # можно использовать базовый класс и добавлять что то свое наследований может быть много
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#         self.name = 'квадрат'# сначала берет своё потом уже к классу выше
# # по-этому пишет имя квадрат если бы не было указано имя писал бы прямоугольник т.к. Rectangle имеет имя прямоугольник
#
#     def perimetr(self):# так как мы использовали супер функцию
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
#     def get_name(self):
#         return self.name
# s = Square(5)
# print(s.area())
# print(s.perimetr())
# s.info()#Класс: Square
###################################################
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#
#         return 2 * (self.width + self.height)
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#         self.name = 'квадрат'#
# class Triangle(Square):
#     def __init__(self, side):
#         super().__init__(side)#
#         self.name = 'Треугольник'#
#
#     def perimetr(self):
#         return 3 * (self.side )
#
#     def area(self):
#         return self.side**2 * 3**0.5 / 4
#
# tr = Triangle(8)
# print(tr.area())
# print(tr.perimetr())

# class Triangle(Square):
#     def __init__(self, side):
#         Square.__init__(self,side)# если нужно использовать несколько наследоваений супер два раза не используют,
#         # вызывают вторую функцию ее названием только обязательно писать в скобках self
#         self.side = side
#         self.name = 'Треугольник'#
#
#     def perimetr(self):
#         return 3 * (self.side )
#
#     def area(self):
#         return self.side**2 * 3**0.5 / 4
#
# tr = Triangle(8)
# print(tr.area())
# print(tr.perimetr())

############################################
# # так можно делать по правильномуу если есть наследование вызывая эту библиотеку
# from abc import ABC, abstractmethod
# class Shape(object):#
#     @abstractmethod
#     def info(self):
#         print(f'Класс: {self.__class__.__name__}')
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return round(2 * pi * self.radius, 2)
#
#     def area(self):
#         return round(pi * self.radius ** 2, 2)
#
#     def get_name(self):
#         return self.name
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
# class Square(Rectangle):# можно добавить через запятую Shape так даже правильнее будет
#     # можно использовать базовый класс и добавлять что то свое наследований может быть много
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#         self.name = 'квадрат'# сначала берет своё потом уже к классу выше
# # по-этому пишет имя квадрат если бы не было указано имя писал бы прямоугольник т.к. Rectangle имеет имя прямоугольник
#
#     def perimetr(self):# так как мы использовали супер функцию
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
#     def get_name(self):
#         return self.name
# s = Square(5)
# print(s.area())
# print(s.perimetr())
# s.info()#Класс: Square

# ООП ДЗ

# Задача: смоделировать зоопарк с разными животными.
# Условия:
# 	Базовый класс Animal с методом make_sound().
# 	Классы-наследники: Dog, Cat, Elephant с переопределением звуков.
# 	Класс Zoo хранит список животных и метод make_all_sounds().

