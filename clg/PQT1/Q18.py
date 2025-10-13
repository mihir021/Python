# seq 1,1,1,1,4,7,13
n = 1
a,b,c,d = 1,1,1,1
ans = 0
while n > 1:
    ans = a
    next = a+b+c+d
    a,b,c,d = b,c,d,next
    n -= 1
print(a)