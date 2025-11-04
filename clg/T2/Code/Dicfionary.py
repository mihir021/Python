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

print("--------------------- keys ------------------------")

print(d.values())
for i in d.values():
    print(i)

print("--------------------- keys ------------------------")

print(d.items())
for i in d.items():
    print(i)






















