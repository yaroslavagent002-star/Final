class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print("Ім'я:", self.__name, "\nВік:", self.__age)

    def old(self):
        return self.__age


class School(Human):
    def __init__(self, name, age, clas, ball):
        super().__init__(name, age)
        self.clas = clas
        self.__ball = ball

    def grade(self):
        return sum(self.__ball) / len(self.__ball)

    def info(self):
        super().info()
        print('Середній бал учня:', self.grade())


class Worker(Human):
    def __init__(self, name, age,stavka,hour):
        super().__init__(name, age)
        self.stavka = stavka
        self.hour = hour
    def salary(self):
        return self.stavka * self.hour
    def info(self):
        super().info()
        print("Зарплатня",self.salary())

people=[
School('Оля',15, 9, [12,6,7,10]),
School('Коля',14, 8, [5,6,1,2,10]),
Worker('Коля',20, 300, 80),
Worker('Коля',21, 150, 45)
        ]

for p in people:
    p.info()
    print('Повнолітній',p.old())
    print()