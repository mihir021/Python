# largest prime factor

def isPrime(number : int) -> bool:
    a = number
    c = 0
    while number > 0:
        if a % number == 0:
            c += 1
        if c > 2:
            return False
        number -= 1
    if c == 2:
        return True
    else:
        return False

# main code
n = 6
temp = n - 1
while temp > 0:
    if n % temp == 0 and isPrime(temp):
        print("largest prime factor is :",temp)
        break
    temp -= 1

