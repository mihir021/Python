# midden of given 3 numbers
a,b,c = 5,15,10

if a > b > c:
    print(b)
elif c > b > a:
    print(b)
elif c > a > b:
    print(a)
elif b > a > c:
    print(a)
else:
    print(c)