#  Write a program to reverse a number.

n = 1234

temp = n
rev = 0
while temp > 0:
    rev = rev*10 + (temp % 10)
    temp //= 10
print("rev number is :",rev)