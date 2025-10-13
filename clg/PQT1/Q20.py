from clg.PQT1.Q2 import isPrime

n = 10 + 1
c = 0
for x in range(n):
    if isPrime(x):
        c += 1
print(c)