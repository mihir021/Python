class dog:
    pass

class c1:
    x = 5

a = c1()
print(a.x)

class p:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = p('As',30)
print(p1.name)
print(p1.age)

# atributes
# class atribute

class human:
    species = "homo sp"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self,v):
        return v

