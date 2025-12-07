class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id
        self.courses_and_grades = dict(courses_and_grades)

    def get_average_grade(self):
        total = 0
        count = 0
        for grade in self.courses_and_grades.values():
            total += grade
            count += 1
        return total / count if count > 0 else None

    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade

    def get_honors_courses(self, threshold=90):
        honors = []
        for course, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors.append(course)
        return honors

    def get_unique_grades(self):
        return set(self.courses_and_grades.values())




# Part 2
all_students = []

student1 = Student(
    "Adrian",
    "S01",
    {"Math": 85, "Science": 92, "History": 78}
)

student2 = Student(
    "Berk",
    "S02",
    {"Math": 70, "English": 75, "Art": 80}
)


student3 = Student(
    "Muhta",
    "S03",
    [("Art", 95), ("PE", 88)]
)

all_students.extend([student1, student2, student3])


for student in all_students:
    avg = student.get_average_grade()

    if avg is not None and avg > 80:
        honors = student.get_honors_courses()
        print(
            f"{student.name} has an excellent average of {avg} "
            f"and the following honor courses: {honors}"
        )
    else:
        student.add_course_and_grade("Study Skills", 100)
        print(
            f"Added 'Study Skills' with grade 100 to {student.name}'s record."
        )   