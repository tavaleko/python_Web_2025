

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

from paht_lib import img_dir

print(img_dir)# организация пути
