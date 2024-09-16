from student_builder import StudentBuilder, EngineeringStudentBuilder, MBAStudentBuilder
from director import StudentDirector

if __name__ == '__main__':
    engineering_student: StudentBuilder = EngineeringStudentBuilder()
    student_director: StudentDirector = StudentDirector(engineering_student)

    student = student_director.create_student()
    print(student)

    student_director.student_builder = MBAStudentBuilder()
    student = student_director.create_student()
    print(student)
