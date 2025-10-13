# GCD of a number
n1,n2 = 7,21

if n1>n2:
    temp = n2
else:
    temp = n1

while temp > 0:
    if n1 % temp == 0 and n2 % temp == 0:
        print(temp)
        break
    temp -= 1