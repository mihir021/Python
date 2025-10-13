#  Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by
# ‘c’.
a = 1
b = 10
c = 2
for x in range(a,b+1):
    if x % c == 0:
        print(x,end=" ")
        