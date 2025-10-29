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

print("------------------------------------------------------------")

txt = ",,,,rrrtr.bananarr,,.m..."
x = txt.strip(".gr,t") # oder is not imp
print(x)

print("---------- lstrip ----------------")

x = txt.lstrip("gt., r")
print(x)

print("---------- rstrip ----------------")

x = txt.rstrip("gt.,r")
print(x)

print("---------- translate ----------------")

txt = "hello sam!"
# myTable = txt.maketrans("s","pojo") --> ValueError: the first two maketrans arguments must have equal length
myTable = txt.maketrans("s","p")
print(txt.translate(myTable))

print()

txt = "hi Sam mmm!"
x = "mSa"
y = "eJo"
myTable = txt.maketrans(x,y)
print(type(myTable))
print(txt.translate(myTable))

print("---------------------------------")

txt = "Good morning Sam"
x = "mSa"
y = "eJo"
z = "odnght"  # element to remove

myTable = txt.maketrans(x,y,z)
# 1st remove element of z from string then -> make table and replace the x to y
print(txt.translate(myTable))

print("---------------------------------")

txt = "Good morning, Sam"

myTable = txt.maketrans(","," ")
# 1st remove element of z from string then -> make table and replace the x to y
print(txt.translate(myTable))

print("--------------- count ------------------")

txt = " I love apples , apple are my favourite fruit"
x = txt.count("apple")
print(x)

x = txt.count("apple",10,24)
print(x)

print("------------ sorted ---------------------")
py = "python"
print(sorted(py))
print(sorted(py,reverse=True))

print("------------ Tuple ---------------------")
t = ()
print(type(t))

t = (10)
p = (10,)
print(t)
print(p)

t = 1,2,3,4
print(t,type(t))

t = tuple(range(1,10,2))
print(t)
print()
t = 1,2,3,4
print(t[1])
# t[1] = 5 --> TypeError: 'tuple' object does not support item assignment
t = ("ap","ba","ch","or","ki","me","ma")
print(t[1])
print(t[-1])
print(t[2:5])
print(t[:4])
print(t[2:])
print(t[-4:-1])
print()
# del t[3] --> TypeError: 'tuple' object doesn't support item deletion
del t
# print(t) --> NameError: name 't' is not defined
print((1,2,3)+(4,5,6))

print("------------ repetition ---------------------")
print(("repeat",)*4)
print(("repeat","h")*4)
a = (1,2,3)
b = (1,4)   # --> (1,4,0)
print(a<b)

print()
a = (1,2,3)
b = (1,2,3)
print(a==b)

print()
a = (1,2,5)
b = (1,2,3)
print(a>b)

print()
t = (1,3,5,8,5,8,6,5)
x = t.count(5)
print(x)

print()

x = t.index(5)
print(x)

print()

t = ("e","a","o","u","i")
print(t)
print()
print(sorted(t))
print(sorted(t,reverse=True))

print("--------- max and min -------------------")

x = max(1457,267,464)
y = min(1457,267,464)
print(x,y)
x = max("mike","john","vicky")











