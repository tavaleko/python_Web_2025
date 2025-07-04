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
#
# print('Синус 30:', sin(radians(30)))#Синус 30: 0.49999999999999994 градусы- &#176
# print('Синус 30:', round(sin(radians(30)), 2))# Синус 30: 0.5
# print('Гипотинуза для 3 и 2: ', hypot(3,2))# Гипотинуза для 3 и 2:  3.605551275463989
#################################
# # Модуль рандом
##############################
# import random as r
#
# for _ in range(10):
#     print(r.randint(0,10))
#     #print(r.randrange(0,10,2))






