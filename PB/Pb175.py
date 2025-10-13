# 1234 --> 4231
number = 1234
ld =  number % 10
fd = 0
c = 0
temp = number
while temp > 0:
    fd = temp % 10
    temp //= 10
    c += 1
number = number - ld + fd
c -= 1
number = number - (fd*(10**c)) + (ld*(10**c) )
print(number)


# 1234 - 4 = 1230 -> 1230 + 1 = 1231
# 1231 - 10*c*1= 1000 --> 231 + 10*c*ld = 4231
