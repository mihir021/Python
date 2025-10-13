a = 12
b = 6
temp = 0
while b != 0:
    temp = a % b
    a = b
    b = temp

print(a)