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
from zipfile import ZipFile
import os

csv_files = [f for f in os.listdir() if f.endswith('.csv')]
with ZipFile('archive.zip', 'w') as myzip:
    for file in csv_files:
        myzip.write(file)
        os.remove(file)