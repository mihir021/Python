n = 31590218
ans = 0
while n > 0:
    ans = ans*10 + (((n%10)+1)%10)
    n //= 10
temp = ans
ans2 = 0
while temp > 0:
    ans2 = ans2*10 +(temp % 10)
    temp //= 10
print(ans2)
# 42601329