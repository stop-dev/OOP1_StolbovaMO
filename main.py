def average_rating(rates: dict) -> float:
    r_num = 0
    r_sum = 0

    for rate_values in rates.values():
        r_num += len(rate_values)
        r_sum += sum(rate_values)
    return round((r_sum / r_num), 2)


class Human:

    def __init__(self, name, surname, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender

    def __str__(self):
        return f"Имя: {self.__name}\nФамилия: {self.__surname}\n"

    def _cmp_grades(self, a, b, operator):
        match operator:
            case '<':
                return a < b
            case '<=':
                return a <= b
            case '==':
                return a == b
            case '!=':
                return a != b
            case '>=':
                return a >= b
        return False


class Student(Human):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        s = super().__str__()
        s += f"Средняя оценка за лекции: {average_rating(self.grades)}\n"
        s += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        s += f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return s

    def isoncourse(self, cource):
        return True if cource in self.courses_in_progress else False

    def rate_lecture(self, lecture, course, grade):
        if (isinstance(lecture, Lecture) and self.isoncourse(course) and
                                            lecture.is_attached_course(course)):
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __cmp(self, other, operator):
        if not isinstance(other, Student):
            print("Ошибка сравнения")
            return False
        return (super()._cmp_grades(average_rating(self.grades),
                                    average_rating(other.grades), operator))

    def __lt__(self, other):
        return  self.__cmp(other, '<')

    def __le__(self, other):
        return  self.__cmp(other, '<=')

    def __eq__(self, other):
        return  self.__cmp(other, '==')
    
    def __ne__(self, other):
        return  self.__cmp(other, '!=')

    def __ge__(self, other):
        return  self.__cmp(other, '>=')


class Mentor(Human):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.courses_attached = []

    def is_attached_course(self, course):
        return True if course in self.courses_attached else False


class Lecture(Mentor):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.grades = {}

    def __str__(self):
        s = super().__str__()
        s += f"Средняя оценка за лекции: {average_rating(self.grades)}\n"
        return s

    def __cmp(self, other, operator):
        if not isinstance(other, Lecture):
            print("Ошибка сравнения")
            return False
        return (super()._cmp_grades(average_rating(self.grades),
                                    average_rating(other.grades), operator))

    def __lt__(self, other):
        return  self.__cmp(other, '<')

    def __le__(self, other):
        return  self.__cmp(other, '<=')

    def __eq__(self, other):
        return  self.__cmp(other, '==')
    
    def __ne__(self, other):
        return  self.__cmp(other, '!=')

    def __ge__(self, other):
        return  self.__cmp(other, '>=')


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (self.is_attached_course(course) and
                                            student.isoncourse(course)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def cource_average_rating(objs: list, cource: str) -> float:
    r_num = 0
    r_sum = 0

    for obj in objs:
        r_num += len(obj.grades[cource])
        r_sum += sum(obj.grades[cource])
    return round((r_sum / r_num), 2)

def student_average_rating(students: list, cource: str) -> float:
    return cource_average_rating(students, cource)

def lecture_average_rating(lectures: list, cource: str) -> float:
   return cource_average_rating(lectures, cource)


if __name__ == "__main__":
    
    ## STUDENT1
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['Psychology']
    best_student.grades['Psychology'] = [10, 9, 10, 5]
    best_student.finished_courses = ["SQL for beginners"]
    ## STUDENT2
    student = Student('John', 'Slime', 'your_gender')
    student.courses_in_progress += ['Java']
    student.courses_in_progress += ['Psychology']
    student.grades['Psychology'] = [10, 3, 10, 10]
    student.grades['Java'] = [7, 3, 5, 0, 9, 4, 2]

    ## REVIEWER1
    cool_reviewer = Reviewer('Some', 'Buddy', "Male")
    cool_reviewer.courses_attached += ['Python', 'SQL for beginners']
    ## REVIEWER2
    reviewer = Reviewer('Anastasia', 'Komarova', "Female")
    reviewer.courses_attached += ['Java', 'Psychology']

    ##LECTURE1
    cool_lecture = Lecture("Jordan", "Peterson", "Male")
    cool_lecture.courses_attached += ['Psychology']
    ##LECTURE2
    lecture = Lecture("Son", "Lee", "Male")
    lecture.courses_attached += ['HR']
    lecture.courses_attached += ['Psychology']
    lecture.grades['HR'] = [7, 5, 10, 3, 7, 8, 9, 7]
    lecture.grades['Psychology'] = [9, 9, 10, 9, 7, 10, 9, 7]

    print("\n  ######### Check Reviewer and Student #########")
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    print(best_student.grades)

    print("\n  ############## Check Lecture #############\n")
    best_student.rate_lecture(cool_lecture, 'Psychology', 10)
    best_student.rate_lecture(cool_lecture, 'Psychology', 10)
    print(cool_lecture.grades)

    print("\n  ############## Check __str__ ##############\n")
    print(cool_reviewer)
    print(cool_lecture)
    print(best_student)

    print("\n  ############## Check _cmp_grades ##############\n")
    print("\t## LECTURE ##")

    print("<: ", cool_lecture < lecture)
    print("<=: ", cool_lecture <= lecture)
    print("==: ", cool_lecture == lecture)
    print("!=: ", cool_lecture != lecture)
    print(">=: ", cool_lecture >= lecture)
    print("Error check for lecture")
    print(cool_lecture < best_student)

    print("\t## STUDENT ##")

    print("<:  ", student < best_student)
    print("<=: ", student <= best_student)
    print("==: ", student == best_student)
    print("!=: ", student != best_student)
    print(">=: ", student >= best_student)
    print("Error check for student")
    print(cool_lecture < best_student)

    print("\n  ############## EX #4 ##############\n")
    print(student_average_rating([best_student, student], 'Psychology'))
    print(student_average_rating([cool_lecture, lecture], 'Psychology'))