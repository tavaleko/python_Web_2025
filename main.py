

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

try:
    fo = open('information.txt')
    print(fo.read())
    fo.close()
except FileNotFoundError:
    print('Файл не обноружен  и создан с парометрами по умолчанию')#
    with open('information.txt','wt',encoding='utf-8') as fo:
        fo.write('По умолчанию')