# trailing zeros
n = 20
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("factorial is :",factorial,end=" and trailing zeros are :")
c = 0
while factorial % 10 == 0:
    c += 1
    factorial //= 10
print(c)