class Student:
    def __init__(self,name,marks):
        self.student_name = name
        self.marks = marks
    def updateName(self,newName):
        self.student_name = newName
    def updateMarks(self,newMarks):
        self.marks = newMarks
    def getName(self):
        return self.student_name
    def get(self):
        return self.marks

s1 = Student("mihir",7)
s2 = Student("mihir2",21)

print(f"Student name is {s1.getName()} and marks is {s1.get()}")
s2.updateName("new Name ")
print(f"Student name is {s2.getName()} and marks is {s2.get()}")
