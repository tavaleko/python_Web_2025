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
