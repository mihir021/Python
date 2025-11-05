print("-------------------------------------")

d = {}
print(type(d))

print("-------------------------------------")

d[1] = "athahbugd"
d[2] = "ygednjk"
d[3] = "ygednjkwewedw"
print(d)

print("-------------------------------------")

d = {1:"hjefghw",2:"erfyigueirufgh",3:"jfheijker"}
print(d)

print("-------------------------------------")

d = {1:"hjefghw",'x':"erfyigueirufgh",3:"jfheijker"}
print(d[1])
print(d['x'])
print(d[3])
# print(d['p']) KeyError: 'p'

print("-------------------------------------")

d = {1:"hjefghw",2:"erfyigueirufgh",3:"jfheijker"}
print(d)
d[4] = "sumit"
print(d)
d[1] = 'sum'

print("-------------------------------------")

d = {'brand':'Fode','b1':'Fode1','b2':None,'b3':None,None:9,None:None}
d1 = d.copy()
print(d1)
print(d)
if d1 == d:
    print("same ")
else:
    print("ns")
print(id(d))
print(id(d1))

print("--------------------- keys ------------------------")

print(d.keys())
for i in d.keys():
    print(i)

print("--------------------- values ------------------------")

print(d.values())
for i in d.values():
    print(i)

print("--------------------- items ------------------------")

print(d.items())
for i in d.items():
    print(i)

print("--------------------- items ------------------------")

car = {'brand ':'Fode','mode':'Mustang','year':1964 }
x = car.get('year')
print(x)

x = car.get('prize')
print(x)
print(car)

x = car.get('prize',15000)
print(x)
print(car)

x = car.get('year',1985)
print(x)
print(car)

print("--------------------- setdefult() ------------------------")

x = car.setdefault('year',9090)
print(x)
print(car)

x = car.setdefault('color','aq')
print(x)
print(car)

print("--------------------- Update() ------------------------")

d = {1:'aa',2:'py',3:'asx'}
x =  {4:'aza',5:'drftgyh'}

print(d)
print(x)

car.update({'color':'whight'})
print(car)

print("--------------------- set() ------------------------")

s = {"app","ban","che"}
print(s)
print(type(s))
print()
t = {1,5,7,8,3}
t2 = {True,False,True}
# var = t2[0] TypeError: 'set' object is not subscriptable
t3 = {"abc",34,True,1,0,False}
print(t)
print(t2)
print(t3)
print(type(t))
print(type(t2))
print(type(t3))
print()
l = [1,2,3,4]
s = set(l)
print(s)
print(type(s))
print()
a = {}
print(type(a))
a = set()
print(type(a))

t = {12,3,3}
t.add(2)
print(t)

print("---------------------- union() ----------------------")
x = {'a','b','c'}
x1 = {'d','e','f'}
x2 = {'d','e','c'}

r = x|x1|x2
print(r)

r = x.union(x1,x2)
print(r)
print(type(r))
print()

print("---------------------- intersection() ----------------------")
x = {'a','b','c'}
x1 = {'d','e','f'}
x2 = {'d','e','c'}

r = x.intersection(x1,x2)
print(r)
print(type(r))
print()

print("---------------------- diff() ( - ) ----------------------")
x = {'a','b','c'}
x1 = {'g','m','a'}
r = x1.difference(x)
print(r)
print(type(r))
print()

print("---------------------- symmetric() ----------------------")
x = {'a','b','c'}
x1 = {'g','m','a'}
r = x1.symmetric_difference(x)
print(r)
print(type(r))
print()
print("---------------------- issubset() ----------------------")
x = {'a','b','c'}
x1 = {'f','e','b','d','c'}
r = x1.issubset(x)
print(r)
print(type(r))
print()

print("---------------------- issuperset() ----------------------")

x = {'a','b','c'}
x1 = {'f','e','b','d','c'}
r = x1.issuperset(x)
print(r)
print(type(r))
print()

print("---------------------- frozenset() ----------------------")

l = ['a','b','c']
f = frozenset(l)
print(f)
print(type(f))

# f[1] = '3'
# TypeError: 'frozenset' object does not support item assignment






















