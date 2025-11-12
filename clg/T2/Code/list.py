from enum import unique

print("----------------------------------------")

color = ["red", "blue" , "green"]
print(color)
color[0] = "pink"
color[-1] = "orange"
print(color)

print("----------------------------------------")

l1 = []
print(l1)
print(type(l1))

print("----------------------------------------")

li = [1,4,7,8]
print(li)
print(type(li))

print("----------------------------------------")

li = ["a","b","c","d"]
print(li)
print(type(li))

print("----------------------------------------")

li = eval(input("Enter list "))
print(li)
print(type(li))

print("----------------------------------------")

l = list(range(0,5,1))
print(l)
print(type(l))

print("----------------------------------------")

# by using index

l = [1,3,5,7]
print(l[2])
print(l[0])
print(l[-2])
# print(l[6]) index error

print("----------------------------------------")

# by using slice

a = [1,2,3,4,5,7,8]
print(l[1:5:2])
print(l[3:5])
print(l[1:5])

print("----------------------------------------")

# by using loop

l = [5,7,9,2,3,8]
for i in l:
    print(i)

print("----------------------------------------")


i = 0
while i < len(l):
    print(l[i])
    i += 1

print("----------------------------------------")

l = ["a","b","c"]
x = len(l)
for i in range(x):
    print(l[i])

print("----------------------------------------")

l = ["ma","ba","ap"]
l.append(1)
l.append("st")
l.append('ch')
print(l)

print("-------------- append (add last)--------------------------")

l.append(["as","as"])
print(l)

print("----------------------------------------")

l1 = ["a","b","c"]
l2 = ["x","y","z"]
l1.extend(l2)
print(l1)
print(l2)

print("----------------------------------------")

l1 = ["aman", "daman"]
l2 = [1234]
l1.extend(l2)
print(l1)

print("------------------ insert ----------------------")

a = [1,4,7,9,1,1,1]
a.insert(2,7)
print(a)

print("------------------ count ----------------------")

print(a.count(1))
print(a.count(9))

print("------------------ index ----------------------")

a = [1,2,3,4,1,2,4,5,6,7]

print(a.index(1))
print(a.index(3))
print(a.index(6))
# ValueError\

print("------------------ remove ----------------------")

n = ["a","a","b","c","d"]
n.remove("a")
# print(n.remove("i")) # ValueError: list.remove(x): x not in list
print(n)

print("------------------ pop() ----------------------")

a = [1,5,4,6,8,9]
print(a.pop())
print(a.pop())
print(a)

print("----------------------------------------")

a = []
# print(a.pop(1)) IndexError: pop from empty list
# print(a.pop(3)) IndexError: pop from empty list
print(a)

print("------------------ revers() ----------------------")

a = [1,2,4,6,8,3,1]
a.reverse()
print(a)

print("------------------ sort() ----------------------")

n = [2,7,3,6,5]
n.sort()
print(n)

print("----------------------------------------")

n = [2,7,3,6,5]
n.sort(reverse=True)
print(n)

print("----------------------------------------")

n = ["v","s","r","0"]
n.sort(reverse=False)
print(n)

print("---------------- list comprehension------------------------")

sq = [x**2 for x in range(5)]
print(sq)


evenSq = [x**2 for x in range(10) if x%2==0]
print(evenSq)

print("---------------- set comprehension------------------------")

unique_sq = {x**2 for x in [1,2,2,3,3,4]}
print(unique_sq)

print("---------------- dictionary comprehension------------------------")

sqD = {x:x**2 for x in range(5)}
print(sqD)

evenSq = {x**2 for x in range(10) if x%2==0}
print(evenSq)

print("---------------- generator tuple compression ------------------------")

gen = (x**2 for x in range(5))
print(gen)
print(tuple(gen))

print("---------------- sort with key ------------------------")

a = ["xyz","tijkl","fsvj"]
print(a.sort())
print(a)
print(a.sort(key=len))
print(a)















