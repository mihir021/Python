#  Write a program to check whether a number is Armstrong number or not.
# 1^3 + 5^3 + 3^3 = n
import math

n = 153
number_of_digits = 0
temp = n
# count the number of digits in this number...
while temp > 0:
    number_of_digits += 1
    temp //= 10
sum_digits = 0
temp = n
sum_temp = 0
while temp > 0:
    sum_temp += math.pow(temp % 10, number_of_digits)
    temp //= 10
if sum_temp == n:
    print("AN")
else:
    print("NAN")