n = 7
debt = 100000
while n > 0:
    debt *= 1.05
    if debt % 1000 != 0:
        debt = int(1+debt//1000)*1000
    n = n - 1
print('Amount of debt', debt)