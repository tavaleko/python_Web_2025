from flask import Flask, url_for, request, render_template
from openpyxl.styles.builtins import title
from werkzeug.utils import  secure_filename
import sqlite3
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS =['txt','pdf','zip','jpg','png']
debug= False
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# шаблонизатор JINJA переменные циклы и тд
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)

@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return "Ошибка загрузки"


@app.route('/numbers')
def odd_even():
    return render_template('numbers.html',
                           title='Чет-нечёт', number=2)


@app.route('/deals')
def printlist():
    deal = ['Помыть посуду', 'Выгулять собаку',
            'Снять показания счётчика', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)

@app.route('/queue')
def queue():
    # loop index 0 номер итерации начинается с 0
    # loop first True  если этерация первая
    # loop last True если итерация последняя
    # loop index номер итерации начинается с 1
    return render_template('vars.html', title='Стоим в очереди')

if __name__ == '__main__':
    app.run(host = 'localhost', port=5000, debug=debug) # lockalhost адрес 127.0.0.1
    # debug=True чтобы не было разницы между приложением и браузером
