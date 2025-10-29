#  Write a python program to display the Fibonacci sequence up to n-th term.
# 0,1,1,2,3,5,8.........
n = 8

a = 0
b = 1
c = 1
while n>0:
    print(a , end=" ")
    c = a + b
    a,b = b,c
    n -= 1
