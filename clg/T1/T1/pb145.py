n = 123547
p = 0
while n>0:
    d = n % 10
    if d % 2 != 0:
        if p == 0:
            p = 1
        p *= d
    n //= 10
print("product is",p)