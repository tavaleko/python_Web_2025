from flask import Flask, request, render_template
import os
from templates.forms.loginform import LoginForm
from werkzeug.utils import  secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS =['txt','pdf','zip','jpg','png']
debug= False
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# шаблонизатор JINJA переменные циклы и тд
@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)


@app.route('/about')
def about():

    return render_template('about.html',
                           title= 'о нас')
@app.route('/contacts')
def contact():

    return render_template('contact.html',
                           title= 'свяжитесь с нами')


@app.route('/login', methods=['GET','POST'])
def login0():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/login1', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login1.html', title='Авторизация', form=form)

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


@app.route('/numbers/')
@app.route('/numbers/<int:num>')
def odd_even_num(num=None):
    if num is None:
        return render_template('numbers.html',
                               title='Нет числа', number='')
    return render_template('numbers.html',
                           title='Чет-нечёт', number=num)

if __name__ == '__main__':
    app.run(host = 'localhost', port=5000, debug=debug) # lockalhost адрес 127.0.0.1
    # debug=True чтобы не было разницы между приложением и браузером

# return '<a href="http://localhost:500/get-user
# pip install flask-wtf
# pip freeze > requirements.txt
# #######################################
# ORM --object Relational Mapping
# pip install sqlalchemy
# pip freeze > requirements.txt

