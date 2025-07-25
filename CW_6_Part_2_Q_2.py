class SchoolStaff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def set_grade(self, student_name, grade):
        if self.role != "teacher":
            raise PermissionError("Can't Set a grade for student")
        if grade < 0 or grade >= 20:
            raise ValueError("invalid grade")
        return f"{student_name}: {grade}"
    
    def __str__(self):
        return f"Name: {self.name} | Role: {self.role} "




class Student:
    def __init__(self, student_name, grade):

        self.student_name = student_name
        self.grade = grade


teach1 = SchoolStaff("nameee", "admin")

stud1 = Student("ariyan", 15)

print(teach1.set_grade("ariyan", 15))


print(teach1.role)
