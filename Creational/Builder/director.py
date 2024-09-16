from student_builder import *


class StudentDirector:
    def __init__(self, student_builder: StudentBuilder):
        self.student_builder = student_builder

    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.__create_engineering_student()
        else:
            return self.__create_mba_student()

    def __create_engineering_student(self):
        return (self.student_builder.set_name("Jitendra").set_age(2).set_email("jks@gmail.com")
                .set_phone("9601055029").set_address("Noida").set_subjects().build())

    def __create_mba_student(self):
        return (self.student_builder.set_name("Lavi").set_age(2).set_email("jks@gmail.com")
                .set_phone("9601055029").set_address("Noida").set_subjects().build())
