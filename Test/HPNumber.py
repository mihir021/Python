a = 321
while a != 4:
    temp = a
    sum_num = 0
    while temp > 0:
        sum_num += (temp%10)**2
        temp //= 10
    if sum_num == 1:
        print("true")
        break
    else:
        a = sum_num