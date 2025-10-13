min = 0
max = 0
fix = 0
sum = 0
c = 0
while True:
    n = input("Enter number :")
    if n == "Q":
        break
    n = int(n)
    if fix==0:
        min = n
        max = n
        fix = 9
    if n >= max:
        max = n
    if n <= min:
        min = n
    c += 1
    sum += n
print("sum is :",sum)
print("avg is :",sum/c)
print("max number is ",max)
print("min number is ",min)