import math

number = 1234    # input number

# storing 1st and last digits.
last_d = number%10
first_d = number // (10**int(math.log(number,10)))

print(last_d , first_d)

# swaping the digits
number = number - last_d + first_d
number = number - first_d*(10**int(math.log(number,10))) + last_d*(10**int(math.log(number,10)))

print(number)  # ans
