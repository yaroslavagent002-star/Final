import random as r

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = r.randint(50, 100)
        self.happy = r.randint(50, 100)
        self.money = r.randint(20, 50)
        self.life = True

    def study(self):
        self.progress += r.randint(10, 20)
        self.happy -= r.randint(5, 10)

    def sleep(self):
        self.happy += r.randint(10, 20)
        self.progress -= r.randint(1, 3)

    def chill(self):
        self.happy += r.randint(5, 15)
        self.progress -= r.randint(5, 10)
        self.money -= r.randint(5, 10)

    def work(self):
        print('\n\033[1mЧас працювати\033[0m')
        self.progress += r.randint(5, 15)
        self.happy -= r.randint(10, 20)
        earned = r.randint(15, 30)
        self.money += earned

    def money_info(self):
        print("Гроші:", self.money)

    def isStudent(self):
        if self.progress <= 30:
            print(self.name, 'відраховують із закладу')
            self.life = False
        elif self.progress < 80:
            print(self.name, 'намагається по навчанню, але потрібно краще')
        else:
            print(self.name, 'встигає по навчанню')

    def dayStudy(self):
        print('Показники\nЩастя:', self.happy, '\nНавчання:', self.progress)

    def day_info(self, day):
        print(f"День {day} | Прогрес: {self.progress} | Щастя: {self.happy} | Гроші: {self.money}")

    def live_day(self, day):
        if self.money < 20:
            self.work()
        elif self.progress < 50:
            self.study()
        elif self.happy < 40:
            self.chill()
        else:
            action = r.choice([self.study, self.sleep, self.chill, self.work])
            action()

        self.money_info()
        self.isStudent()
        self.dayStudy()
        self.day_info(day)


st = Student("Вася")

for day in range(1, 366):
    if not st.life:
        print("Студент не дожив до кінця року...")
        break
    st.live_day(day)
