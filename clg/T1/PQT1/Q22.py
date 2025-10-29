
a = 21
b = 5
countOfNumber1 = 0
if a == b:
    print("Invalid")
elif a < b:
    print("Infinite sol")
else:
    for x in  range(1,a):
        if a%x==b:
            countOfNumber1 += 1
print(countOfNumber1)