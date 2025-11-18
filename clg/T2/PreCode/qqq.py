from functools import reduce

print("---------------- Q6 -----------------------")

a = [3,0,0,2,0,4]
max1 = 0
temp = 0

for i in range(len(a)):
    mid = 0
    temp = 0
    tempA = a[:i] + a[i+1:]
    maxNext = reduce(lambda x, y: x if x > y else y, tempA)

    for j in range(i+1,len(a)):
        if a[i] < a[j] & a[j] == maxNext:
            temp = abs((j - i - 1) * min(a[i], a[j]) - mid)
            max1 += temp
            i = j
            break
        if a[j] > 0 & a[j] == maxNext:
            temp = abs((j - i - 1) * min(a[i], a[j]) - mid)
        mid += a[j]

print(max1)