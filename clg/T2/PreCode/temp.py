from functools import reduce
from os.path import split

print("---------------- Q6 -----------------------")

def trap(height):
    n = len(height)

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1
    return trapped_water

print("---------------- Q6 -----------------------")

p = "1 2 3 5 6 1 2 5 2 1 7 8 "
p.lower()
listp = split(" ")
ans = {}
sorted(listp)
for x in range(len(listp)):
    c = 0
    for y in range(len(listp)):
        if listp[x] == listp[y]:
            c += 1
        else:
            ans.setdefault(listp[x],c)

print(ans)

d1 = {1:1,2:2,3:3}
d2 = {4:4,5:5,7:7,8:8}

for i in d1.keys():
    d2[i] = d1.get(i)

print(d2)
