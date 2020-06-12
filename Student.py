class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def is_honor_role(self):
        if self.gpa <=2 :
            return True
        else:
            return False

