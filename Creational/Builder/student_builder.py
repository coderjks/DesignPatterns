from student import Student


class StudentBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.phone = None
        self.email = None
        self.address = None
        self.subjects = None

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_address(self, address):
        self.address = address
        return self

    def set_subjects(self):
        pass

    def build(self):
        return Student(self)


class EngineeringStudentBuilder(StudentBuilder):
    def __init__(self):
        super().__init__()

    def set_subjects(self):
        self.subjects = ["Physics", "Mathematics", "Chemistr"]
        return self


class MBAStudentBuilder(StudentBuilder):
    def __init__(self):
        super().__init__()

    def set_subjects(self):
        self.subjects = ["Commerce", "Econonics", "Accounts"]
        return self
