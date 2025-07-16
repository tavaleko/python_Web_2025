# #########################
# Введение во  Flask
############################
# удалить любую библиотеку pip uninstall  дальше название библиотеки
# MVC -(Model View Controller)
from flask import Flask, url_for

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
if __name__ == '__main__':
    app.run(host = 'localhost', port=5000, debug=True) # lockalhost адрес 127.0.0.1
    # debug=True чтобы не было разницы между приложением и браузером
################################################################


