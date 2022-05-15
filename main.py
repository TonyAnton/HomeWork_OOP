class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_students.append(self)

    def avg_rate(self):
        avg_rate = 0
        simple_list_grade = []
        list_grades = list(self.grades.values())
        for grade in list_grades:
            simple_list_grade.extend(grade)
            amount_grade = len(simple_list_grade)
            sum_grade = sum(simple_list_grade)
            avg_rate = sum_grade / amount_grade
        return round(avg_rate, 2)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and isinstance(self, Student) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Сравнивать можно только студентов')
        if other_student.avg_rate() < self.avg_rate():
            print(f"Cредний балл выше у студента: {self.name}")
        else:
            print(f"Cредний балл выше у студента: {other_student.name}")

    def __str__(self):
        output = f'Имя:{self.name}\nФамилия:{self.surname}\n' \
                 f'Средняя оценка за домашние задания:{self.avg_rate()}\n' \
                 f'Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return output


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_lecturers.append(self)

    def avg_rate(self):
        Student.avg_rate(self)
        return Student.avg_rate(self)

    def __str__(self):
        output = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.avg_rate()}'
        return output

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Сравнивать можно только лекторов')
        if other_lecturer.avg_rate() < self.avg_rate():
            print(f"Cредний балл выше у лектора: {self.name}")
        else:
            print(f"Cредний балл выше у лектора: {other_lecturer.name}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя:{self.name}\nФамилия:{self.surname}'
        return output


anton = Student('Anton', 'Andreev', 'M')
anton.finished_courses = ['Target']
anton.courses_in_progress = ['Java', 'Python', 'DevOps']

nastya = Student('Anastasia', 'Lavrenteva', 'F')
nastya.finished_courses = ['Java']
nastya.courses_in_progress = ['SMM', 'Project manager', 'Python']

jake = Reviewer('Jake', 'Tomson')
jake.courses_attached = ['Java', 'Python', 'DevOps', 'Project manager', 'SMM']

jake.rate_hw(anton, 'Java', 8)
jake.rate_hw(anton, 'Python', 7)
jake.rate_hw(anton, 'DevOps', 4)
jake.rate_hw(nastya, 'SMM', 8)
jake.rate_hw(nastya, 'Project manager', 10)
jake.rate_hw(nastya, 'Python', 4)


matt = Reviewer('Matt', 'Newman')
matt.courses_attached = ['Java', 'Python', 'DevOps', 'SMM', 'Project manager']

matt.rate_hw(anton, 'Java', 4)
matt.rate_hw(anton, 'Python', 9)
matt.rate_hw(anton, 'DevOps', 6)
matt.rate_hw(nastya, 'SMM', 6)
matt.rate_hw(nastya, 'Project manager', 6)

mike = Lecturer('Mike', 'Anderson')
mike.courses_attached = ['Java', 'Python', 'DevOps', 'Target', 'SMM', 'Project manager']

anton.rate_lecturer(mike, 'Java', 10)
anton.rate_lecturer(mike, 'Python', 10)
anton.rate_lecturer(mike, 'DevOps', 8)

tom = Lecturer('Tom', 'Johnson')
tom.courses_attached = ['Java', 'Python', 'DevOps', 'Target', 'SMM', 'Project manager']
nastya.rate_lecturer(tom, 'SMM', 10)
nastya.rate_lecturer(tom, 'Project manager', 7)
nastya.rate_lecturer(tom, 'Python', 7)

print(anton)
print(nastya)
print(mike)
print(tom)
print(jake)
print(matt)
better_student = anton < nastya
better_lecturer = tom < mike


def avg_rate_course_st(students, course):
    list_grade = []
    avg_rate = 0
    for student in students:
        for grade in student.grades[course]:
            list_grade.append(grade)
            sum_rate = sum(list_grade)
            avg_rate = sum_rate / len(list_grade)
    print(f"Cредний бал среди студентов на курсе {course}: {round(avg_rate, 2)}")


def avg_rate_course_lec(lecturers, course):
    list_grade = []
    avg_rate = 0
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            list_grade.append(grade)
            sum_rate = sum(list_grade)
            avg_rate = sum_rate / len(list_grade)
    print(f'Cредний бал среди лекторов на курсе {course}: {round(avg_rate, 2)}')


avg_rate_course_st(Student.all_students, 'Python')
avg_rate_course_lec(Lecturer.all_lecturers, 'Python')
