# #########################
# Введение во  Flask
############################
# удалить любую библиотеку pip uninstall  дальше название библиотеки
# MVC -(Model View Controller)
from flask import Flask, url_for
import sqlite3
app = Flask(__name__)

# декоратор @ начинается
@app.route('/')
@app.route('/index')
def index(): # функция не должна повторятся!!!!!!!!! иначе ошибка назавания должны быть разные
    print('Вызвана функция о index')
    return 'Привет, Flask'# call back def  функция обратного пути

@app.route('/about')
def about():
    print('Вызвана функция о about')
    return 'О нас' # функция обратного вызова возвращает только строку даже если нужно число оно должно быть в скобках

@app.route('/countdown')
def cd():
    lst= [str(x) for x in reversed(range(10))]
    lst.append('Полетели!')
    return '<br>'.join(lst) # вернет строку через <br>
 # функция обратного вызова возвращает только строку даже если нужно число оно должно быть в скобках
# статический контент
@app.route('/image')
def show_image():
    return f'<img scr="{url_for('static', filename= 'images/map.jpg')}">'# или '<img scr="./static/images/map.jpg">'
# для изображений видео музыка она должна храниться в специальной папке  именно так! static!

@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Картинка питона</title>
    </head>
    <body>
    <img src = "{url_for('static', filename = 'images/piton.jpg')}" alt="python">
    </body>
    </html>
"""
@app.route('/sample-page2')
def sample_page_2():
    with open('temp2.html','r', encoding = 'utf-8') as html:
        return html.read()

#  так делать нельзя
# x=5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# конвектор <string> по умолчанию строка
@app.route('/greeting/<user>')
def greeting(user):
    return f'Привет! {user}'
# конвектор <int:number> целое число

@app.route('/greeting/<user>/<int:id_num>')
def greeting_1(user, id_num):
    return f'Привет! {user} с id ={id_num}'
# конвектор <float:number> десятичная дробь
# конвектор <path:p> может содержать слеши для указания пути
# конвектор <uuid:id> строка индефикатор (16 байт в HEX- формате) ля оплаты по ссылке


@app.route('/greet-user/<int:id_num>')
def greet_user_1(id_num):
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    cur.close()
    con.close()
    return str(result[0])

@app.route('/get-user/<int:id_num>')
def get_user(id_num):
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    # print(result)
    name, city = result
    cur.close()
    con.close()
    return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''

if __name__ == '__main__':
    app.run(host = 'localhost', port=5000, debug=True) # lockalhost адрес 127.0.0.1
    # debug=True чтобы не было разницы между приложением и браузером
################################################################


