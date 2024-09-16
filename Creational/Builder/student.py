class Student:
    def __init__(self, student_builder):
        self.name = student_builder.name
        self.age = student_builder.age
        self.phone = student_builder.phone
        self.email = student_builder.email
        self.address = student_builder.address
        self.subjects = student_builder.subjects

    def __str__(self):
        return f"""
        name: {self.name},
        age: {str(self.age)},
        phone: {self.phone},
        email: {self.email},
        address: {self.address},
        subjects: {", ".join(self.subjects)}
        """
