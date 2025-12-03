class stu:
    def __init__(self,name):
        self.name = name
    def show(self):
        print('My name is ',self.name)
s1 = stu('Emma')
s1.show()

# default constructor

class Emp:
    def display(self):
        print("inside display")

emp = Emp()
emp.display()

# 2.Non parametrized cons

class C:
    def __init__(self):
        self.name = "python"
        self.add = "ABC"
    def show(self):
        print(self.add)
d = C()
d.show()

# 3 . Parametrize

class Emp:
    def __init__(self):
        self.name = "a"
        self.age = 41
        self.sal = 1234
    def show(self):
        print(self.name , self.sal , self.age )
    def __del__(self):
        print("d")

e1 = Emp()
e1.show()
del Emp

# getter setter

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
    def set(self,age):
        self.age = age
stu = Student('Js',14)
print('Name :',stu.name,stu.get_age())
stu.set(19)
print('Name :',stu.name,stu.get_age())


def g():
    yield 10
    yield 20
    yield 30
for i in g():
    print(i,type(i))

def g1():
    return 10
    return 20
    return 30

print(g1())

def g5():
    return 10,20,2
print(g5())























