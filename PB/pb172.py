def isH(n):
    sum_d = 0
    temp = n
    while n > 0:
        sum_d += n % 10
        n //= 10
    if temp % sum_d == 0:
        return True
    else:
        return False

def isD(n):
    number_of_digits = 0
    temp = n
    sum = 0
    while temp > 0:
        number_of_digits += 1
        temp //= 10
    temp = n
    while temp > 0:
        sum += ((temp%10) ** number_of_digits)
        number_of_digits -= 1
        temp //= 10
    if sum == n:
        return True
    else:
        return False

n = 1
while n <= 100:
    if isD(n) and isH(n):
        print(n , end=" ")
    n += 1
