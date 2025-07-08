from os import path

# __file__ встроенная пересменная содержащая путь к исполняемому скрипту
img_dir = path.join(path.dirname(__file__), 'images')
print(img_dir)

font_dir = path.join(path.dirname(__file__), 'fonts')
print(img_dir)# прием который рекомендуют использует всегда будет находить ту папку которая необходима
# формирует директорию пути к папке если поменяли имя проекта то структура не нарушится