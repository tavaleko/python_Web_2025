# это закладка
# https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js необходимо для карусели
#   <link rel="stylesheet" href="css/style.css"> обязательно поставить!!!!
# .go-top--show {
# display: block;
# } точка в начале это обращение к классу
# .go-top {
# position: fixed;
# right: 20px;
# bottom: 50px;
# cursor: pointer; курсор навести тбудет реагировать
# display: none; чтоб было не видно
# font-size: 18pt
# }
###########################################
# сегодня мы создаем много файлов csv!!!!
#CSV файлы
# import csv
# data = [
#     ['name','age','city'],
#     ['Борис','28','Воронеж'],
#     ['Ирина','32','Тверь'],
#     ['Владимир', '18', 'СПб'],
#     ['Светлана', '27', 'Москва'],
# ]
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
#
# with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
# # если пишет нет интерпритарора его искать в низу в правом углу
# import csv
#
# from urllib3.filepost import writer
#
# with open ('people.csv', 'r', encoding='utf-8') as f:
#     dict_reader = csv.DictReader(f)
#     for row in dict_reader:
#         print(f' {row['name']} живёт в городе {row['city']}.')
#
# field_names = ['name','age','city']
#
# data = {
#     'name': 'Борис',
#     'age': '27',
#     'city': 'Москва'
# }
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writerow(data)
# import csv
#
# data = ['name', 25,'town']
# with open('sample.csv','w', newline='', encoding='utf-8') as f:
#     writer= csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)# это для того чтобы только сиволы были в кавычках а цифры были int
#     writer.writerow(data)
#################################
# создавать и раскрывать папки zip
##############################
#
# from zipfile import ZipFile
# import os
# #  создали zip
# csv_files = [f for f in os.listdir() if f.endswith('.csv')]
# with ZipFile('archive.zip', 'w') as myzip:
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)
# files_to_extract = ['people.csv', 'file.csv']# если надо распоковать конкретные файлы
# with ZipFile('archive.zip', 'r') as zip_obj:
#     zip_obj.extractall()# распокавать все файлы
# with ZipFile('archive.zip', 'r') as zip_obj:
#     print(zip_obj.namelist())# имена
###########################################
#JSON -(JAVA SCRIPT OBJECT NOTATION)
# для чтения метод
# load() он читает из файла
# loads() он читает строковое представление
#############################################
# //{"pets":["name": "Rex","age": 8,"meals": ["Purina", "Royal Canin"]],["name": "Roex","age": 5,"meals":
# ["Purnina", "Royal Canin"]]} //если несколько животных */ в файле json не может быть коментариев иначе выдает ошибку!
# я перенесла из него данные этот формат для json
#
# import json
# with open('dogs.json', 'rt') as d:
#     data = json.load(d)
#
# print(data)
# for k, v in data.items():
#     if type(v) == list: # читаем файл как словарь
#         print(f'{k}:{', '.join(v)}')
#     else:
#         print(f'{k}: {v}')
#
# import json
#
# with open('dogs.json', 'rt') as d:
#     temp = d.read() # читаем файл как строку
#     data = json.loads(temp)
#
# print(data)
# for k, v in data.items():
#     if type(v) == list:
#         print(f'{k}:{', '.join(v)}')
#     else:
#         print(f'{k}: {v}')

import json

with open('dogs_.json', 'rt') as d:
    temp = d.read() # читаем файл как строку
    data = json.loads(temp)# строковое значение JSON


for i in range(len(data)):
    print(f'Питомец №{i+1}')
    for k,v in data[i].items():
        if type(v) == list:
            print(f'{k}:{', '.join(v)}')
        else:
            print(f'{k}: {v}')



