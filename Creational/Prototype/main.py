from student import Student

if __name__ == '__main__':
    student = Student("Jitendra", 30)

    for i in range(10):
        clone_student = student.clone()
        print(clone_student)