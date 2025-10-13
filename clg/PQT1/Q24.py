number = 120
sum_n = 0
temp = number
while temp > 0:
    sum_n += temp%10
    temp //= 10
if number % sum_n == 0:
    print("HN")
else:
    print("NHN")