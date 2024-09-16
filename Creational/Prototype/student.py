from prototype import Prototype


class Student(Prototype):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clone(self):
        return Student(self.name, self.age)
