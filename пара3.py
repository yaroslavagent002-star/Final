# наслідування, інкапсуляція, поліморфізм
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def info(self):
        print("\nІнформація про студента")
        print("Ім'я:", self.name)
        print("Вік:", self._age)


class StudentSchool(Student):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def info(self):
        super().info()
        print("Школа:", self.school)


class StudentUniversal(Student):
    def __init__(self, name, age, nameUniversal):
        super().__init__(name, age)
        self.nameUniversal = nameUniversal

    def info(self):
        super().info()
        print("Назва спеціальності:", self.nameUniversal)


stud = [
    StudentUniversal(name='Сашко', age=20, nameUniversal='розробник'),
    StudentSchool(name='Глаша', age=11, school=101),
    Student(name='Гриша', age=4)
]

st = Student(name='Світлана', age=20)
st.info()

for stu in stud:
    print(stu.name, stu._age, end=': ')
    stu.info()
# class Dani:
# def __info__( self,password):
# self.__passworld = passworld
# def cange 