class Car():
    def __init__(self, speed, diametr, color):
        self.speed = speed 
        self.diametr = diametr
        self.color = color

    def ride(self):
        print("Я ЕДУ")

    def breakk(self):
        print('СЛОМАЛАСь')

largus = Car(speed=100, diametr=16, color='blue')
wallzwagen = Car(speed=130, diametr=18, color='red')
bugati = Car(speed=300, diametr=20, color='black')

largus.ride()
largus.breakk()

class Fruits():
    def __init__(self, color, weight, count):
        self.color = color
        self.weight = weight
        self.count = count

    def sell(self):
        print('стоит 100 рублей за штуку')

    def country(self):
        print('Уругвай')

banana = Car(color='yellow', weight=100, count=3)
