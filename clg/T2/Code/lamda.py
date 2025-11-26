from functools import reduce

a = "mihir"
print(lambda a : a)

def sq(n):
    return n*n
print(sq(4))

print()

s = lambda n:n*n
print(s(4))
print(s(5))

print()

Max = lambda a,b : a if(a>b) else b
print(Max(1,3))

print()

print("--------  lamda with filter() ----------")

li = [5,7,22,97,54,62,77,23,73,61]
f = list(filter(lambda x:(x % 2 != 0),li))
print(f)

f = list(filter(lambda x:(x > 18),li))
print(f)
print()
print("--------  lamda with map() ----------")
print()
li = [5,7,22,97,54,62,77,23,73,61]
f = list(map(lambda x:x*2,li))
print(f)
print(li)

li = ["avcx","gvhbj"]
f = list(map(lambda x: str.upper(x) , li))
print(f)
print(li)

li = [1,2,3,4,5]
# reduce(function, iterable[, initial]) -> value
sum = reduce(lambda x,y:x+y , li)
print(sum)
print()
li = [87,2,3,4,5,-1,-7,88]
sum = reduce(lambda x,y:x if x>y else y, li)
print(sum)

