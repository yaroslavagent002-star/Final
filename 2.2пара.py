class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Auto:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add(self, *args):
        for i in args:
            self.passengers.append(i)

    def info(self):
        if self.passengers == []:
            print("Пасажири відсутні")
        else:
            print("Авто:", self.model)
            for i in self.passengers:
                print("Ім'я:", i.name, "вік:", i.age)
                p1 = Human()
                p2 = Human(name='Саша', age: 32)
                p3 = Human(name='Маша', age: 20)
                c1 = Auto('BMW')
                c2 = Auto('Audi')
                c1.add(p1)
                c2.add(*args: p2, p3)
                c1.info()
                c2.info()