class Car:
    # счетчик машин
    counter = 0
    def __init__(self,brand='noname', model='nomodel', color='nocolor'): # для старта значений нужен __init__
    #в капсулу не кто не лезет
        self.brand = brand#'Skoda'
        self.model = model#'Octavia'
        self.color = color#'red'
        self.engine_on = False
        Car.counter += 1

    # setters
    def set_name(self, new_brand='noname', new_model='nomodel', new_color='nocolor'):
        if brand:
            self._brand = new_brand
        if model:
            self._model = new_model
        if color:
            self._brand = new_color

    def start_engine(self):
        self.engine_on = True# он вызывался из внутри капсулы

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model} {self.color}')
        else:
            print('Двигатель не заведен, не едем')

    @staticmethod
    def get_counter():
        return Car.counter

    # getter
    def get_age(self):
        return self._name




    def person_info(self):
        print(f'Человек с именем: {self._name}. Возраст:{self._age}')

    #setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name


    def set_age(self, new_age):
        if 0< new_age <150:
            self._age = new_age
        else:
            print('Некоректный возраст-',new_age)

    # getter
    def get_name(self):
        return self._name

