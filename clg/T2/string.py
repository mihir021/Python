greeting = "welcome to t2"
# greeting[0] = 'hello' --> TypeError: 'str' object does not support item assignment
print(greeting)

print("---------------------------------------------------")

a= "hello"
print(a)

b = "hello"
print(b)

c = '''this is a class of c1 '''
print(c)

d = """this is a class of c1"""
print(d)

print("---------------------------------------------------")

# accessing char of string

a = "hello world!"
print(a[1])
print(a[-1])
print(a[3])
# print(a[14]) --> IndexError: string index out of range
# print(a[2.0]) CE

print("---------------------------------------------------")

# By using slicing
# [start : end : step]

print(a[2:5])
print(a[:5])
print(a[2:])
print(a[:])
print(a[::])
print(a[5::3])
print(a[-5:-2])
print(a[-2:-5])
print(a[-2:-5:-1])
print(a[-5:-2:-1])

print("---------------------------------------------------")

# By using loop

for x in "India":
    print(x)

print("---------------------------------------------------")

a = "mom"
if a == a[::-1]:
    print("P")
else:
    print("NP")

print("---------------------------------------------------")

a = "hello"
b = "world"
c = a + b
print(c)

print("---------------------------------------------------")

a = "hello"
b = 2
#c = a + b --> TypeError: can only concatenate str (not "int") to str

print(c)

print("---------------------------------------------------")

a = "hello"
b = "world"
c = a + ' ' + b
print(c)

print("---------------------------------------------------")

a = 2
b = "hello"
c = a * b
print(c)

print("---------------------------------------------------")

a = "h"
b = "hello"
# c = a * b --> TypeError: can't multiply sequence by non-int of type 'str'
print(c)

print("----------------- length of string ----------------------------------")

a = "hello world"
print(len(a))
a = "123py"
print(len(a))

print("----------------- capitalization in string ----------------------------------")

a = "this is my first "
y = a.capitalize()
print(y)

print("---------------------------------------------------")

a = "this is my first class"
y = a.capitalize()
print(y)
# title make all word first letter capital

print("---------------------------------------------------")

a = "this IS my Code"
y = a.capitalize()
print(y)

print("--------------------- title swap case ------------------------------")

a = ""

print("--------------------- enumerate ------------------------------")

f = "orange"
for i,j in enumerate(f):
    print(i,j)
print()
f = "orange"
for i,j in enumerate(f,start=2):
    print(i,j)

print("--------------------- isalnum ------------------------------")

a = "Apple#12"
b = "Apple"
c = "12345"
d = "Apple@12"
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())
print()
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())
print()
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print()
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())
print(d.isdigit())

print("--------------------- isLower ------------------------------")

a = "Hello World"
b = "Hello 123"
c = "my name is "
print(a.islower())
print(b.islower())
print(c.islower())

print("--------------------- isUpper ------------------------------")

a = "HELLOWORLD"
b = "HELLO"
c = "123"
print(a.isupper())
print(b.isupper())
print(c.isupper())

print("--------------------- Lower ------------------------------")

a = "Hello World"
y = a.lower()
print(y)

print("--------------------- Upper ------------------------------")

a = "Hello World!"
y = a.upper()
print(y)

print("--------------------- find() ------------------------------")

a = "Hello World!"
print(a.find("H"))
print(a.find("H",5,10))

print("--------------------- index() ------------------------------")

a = "Hello welcome to python"
# print(a.index("z")) --> ValueError: substring not found
print(a.index("e",5,10))

print("--------------------- split() ------------------------------")

a = "I Am IronMan , txt"
print(a.split(","))
print(a.split(" "))

a = "I#Am#IronMan#txt"
print(a.split("#"))
print(a.split("#",2))
