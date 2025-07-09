class Car:
    def __init__(self,brand, model, color):
        self.brand = brand#'Skoda'
        self.model = model#'Octavia'
        self.color = color#'red'
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True# он вызывался из нутри капсулы

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model} {self.color}')
        else:
            print('Двигатель не заведен, не едем')

class Person:
    def __init__(self, name='Bill',age=1):
        # свойства (поля) класса
        self._name = name# так правильно
        self._age = age



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
    def get_age(self):
        return self._name

