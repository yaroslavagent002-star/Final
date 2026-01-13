class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def attack(self, other):
        pass

    def take_damage(self, amount):
        self.__health -= amount

    def is_alive(self):
        if self.__health > 0:
            print(True)
        else:
            print(False)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)
    def attack(self, other):
        other.take_damage(20)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80)
    def attack(self, other):
        other.take_damage(30)