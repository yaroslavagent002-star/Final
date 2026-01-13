class Animal:
    def __init__(self, Respiration, eat):
        self.Respiration = Respiration
        self.eat = eat


class Cat(Animal):
    def __init__(self, Respiration, eat):
        super().__init__(Respiration, eat)


class Dog(Animal):
    def __init__(self, Respiration, eat):
        super().__init__(Respiration, eat)