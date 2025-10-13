import math

number = 3435
c = 0
temp = number
while temp > 0:
    c += 1
    temp //= 10
sum_n = 0
temp = number
while temp > 0:
    sum_n += math.pow(temp % 10, c)
    c -= 1
    temp //= 10
if sum_n == number:
    print("DN")
else:
    print("NDN")