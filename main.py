# # Внешние библиотеки
# # Графика
# # PIL - Python Imagine Library
# # pip freeze > requirements.txt - создание файла зависимости
# # pip install -r requirements.txt - установка списка библиотек
# from PIL import Image, ImageDraw, ImageFont
#
# # https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# W = 600
# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     font='arial.ttf',  # можно использовать любой установленный шрифт
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# image.save('images/sunny_day.jpg')
#################################################
#from PIL import Image, ImageDraw, ImageFont

# convert and paste
################################################
# orgig = Image.open('images/sunny_day.jpg').convert('RGB')
# up = orig.crop((0,0,600,200)) # половина изображения верхня часть
# down = orig.crop((0,200,600,400))
# new = Image.new('RGB',(600,400))
# new.paste(down, (0,0))# верхний левый угол с этими координатами
# new.paste(down, (0,0))

# new.show()
# from PIL Image, ImageFilter, ImageEnhance
# orig = Image.open('images/kukla-labubu.webp')
# #размытие
# blu_image = orig.filter(Image)# дописать скопирорвать

#Усиление резкости
# enchacer = ImageEnhance.Sharpness(orig)#ДОПИСАТЬ


# edges = orig.filter(ImageFilter.FIND_EDGES)# ДОПИСАТЬ
# edges.show()
# #############################
#Документы
# word - DOCX(python-docx)
# pip install python docx # на консоли
# pip freeze > requirement.txt
# pip install -r requirement.txt
# Word - DOCX (docxtpl)
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
###########p##############################
# документы по шаблону(template.docx)
from docx import Document
# from docx.enum.text import WD_ALING_PARAGRAPH
# from docx.shared import Cm, Inches, Mm
# # Добавим в заголовок
# doc = Document()# создание документа
# doc.add_heading('Отчёт за месяц', 1)
# paragraph = doc.add_paragraph('В этом отчёте представлены')
# paragraph.add_run('ключевые показатели')
# doc.save('docs/report.docx')
# #run - это что то внутри обзаца
# paragraph = doc.add_paragraph()
# paragraph_format = paragraph.paragraph_format
# paragraph_format.aligment = WD_ALING_PARAGRAPH.LEFT
#
# paragraph = doc.add_paragraph('Первый пункт', style = 'List Bulet')
# paragraph = doc.add_paragraph('Второй пункт', style = 'List Bulet')
#
# paragraph = doc.add_paragraph('Первый пункт', style = 'List Number')
# paragraph = doc.add_paragraph('Второй пункт', style = 'List Number')
# paragraph = doc.add_paragraph()
# table = doc.add_table(row = 3, cols=3)
#
# for i, row in enumerate(table.rows):
#     for j, cell in enumerate(table.columns):
#         cell.text = f'Строка {i+1} Столбец {j+1}'
#
# doc.add_paragraph()
# doc.add_picture('images/sunny_day.jpg',width = Mm(100))
# doc.save('docs/report.docx')
#####################################
# pip install python docxtpl # на консоли
#######################################
# from docxtpl import DocxTemplate
#
# #Загрузка шаблона
# doc = DocxTemplate('doc/template(1).docx')
# #Word - Docx(docxtpl)
#
# content = {
#     'company': 'ООО Монолит',
#     'employee': 'Петров Д.И',
#     'position': 'Менеджер',
#     'date':'01/01/2025',
# }
# doc.render(content)
# doc.save('doc/about.docx')
#############################
#Внешние библиотеки
#exel
# pip install openpyxl # на консоли
#####################################
# Пустой документ
from openpyxl import Workbook # ЭТО КОНСТРУКТОР
#
# wb = Workbook() # wb - Workbook
# ws = wb.active
# ws.title = 'Отчет'
# wb.save('doc/report.xlsx') # readind butten в самом низу (с помощью текста открывать нельзя)
# если не правильно выбрала то меню - settings - editor - file types - files opened -file name нажать на плюс и
# добавить формат в данном случае xlsx

###########################
# Запись данных в существующих данных
from openpyxl import load_workbook
# Открываем
# wb = load_workbook('doc/report.xlsx')
# # Активный лист
# ws = wb.active # ожно обратится по имени если вы это имя знаете
# #Способы записи
# # ws = wb['Отчёт']
# ws['F1'] ='Привет мир'
#
# ws.cell(row=1, column=3,value='Hello')
# ws.cell(row=3, column=3, value= 'home')
# ws['A1'] = 'ФИО'
# ws['B1'] = 'Должность'
# ws['C1'] = 'Отдел'
# # данные
# employees = [
#     ['Иванов И.И','Менеджер','Продажи'], # список списков
#     ['Петров П.П','Бухгалтер','Финансы'],
#    ['Сидорова С.С','Аналитик','IT'],
# ]
# for row, data in enumerate(employees, start = 2):
#     ws.cell(row = row, column=1, value= data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])
#
# wb.save('doc/newtable.xlsx')
###################################
# Чтение данных
# wb = load_workbook('doc/newtable.xlsx')
# ws = wb.active
# # число заполненых строк
# row_couns = ws.max_row # обращаемся к рабочему листу
# for row in ws.iter_rows(values_only=True):
#
#     print(row)
# row_couns = ws.max_row # обращаемся к рабочему листу
# for row in ws.iter_rows(values_only=True):
#     fio, pos, dept = row
#     print(f'Фамилия:{fio}, Должность: {pos}, Отдел: {dept}')
#
# # Робота с формулами:
# for openpyxl import  Font,
#     ws = wb.active
# ws['A1'].font = Font(bold .....)# =SUM(A1:A10)
###################################################
# Пишем и подключаем свои модули мы создали доп файл lib и в нее записали две функции
import lib

# lib.diff()
#
# from lib import diff
# a=7
# print(diff(7,3)) # вывел 4
#
# print(type(a).__name__)
#
# print(__name__)
#
# ###
# # if __name__ == '__main__'
# # from . lib import summ - из текущей дериктории
# # from ..lib import summ - уровнем выше
# # from .lib import summ - относительный импорт
###############################################
# # пакет

# # file- new - python package - название задаем
############################################
# from package_1.module import greet
# print(greet('Мир!'))
# import package_1
# from package_1.module import * # * означает __all__  все функции к которым можно обращаться
# from package_1 import greet # это относительный импорт
# ### init__.py нужен для 2 вещей определить версию пакета
# ## эта публичная функция
# # есть скрытые функции для внутреннего пользования

from package_1 import greet, add

print(greet('Мир!'))
print(add(3,7))
print('Автор', __author__)# подумать!!! как вывести автора это домашняя
# методичка модули!!! посмотреть