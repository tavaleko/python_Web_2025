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
#CSV файлы
with open('people.csv','r', encoding='utf-8') as f:
    reader= csv.reader(f, delimeter=';',quotechar='"')
    for row in reader:
       print(row)