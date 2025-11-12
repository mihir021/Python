print("---------------- Q1 -----------------------")

s = 54321101112
sString = str(s)
target = "1"
i = 0
for x in sString:
    if target==x:
        print(f"index of {target} is {i}")
        break
    i+=1
else:
    print(f"index of {target} is {-1}")

print("---------------- Q2 -----------------------")

l = [4,6,6,4,2,4]
ans = {}
l.sort()
temp = [l[0]]
i = 0
for x in range(len(l)-1):
    if l[i]==l[i+1]:
        temp.append(l[i])
    else:
        ans.setdefault(l[i],temp)
        temp = [l[i+1]]
    i+=1
else:
    ans.setdefault(l[i], temp)
print(ans)

print("---------------- Q3 -----------------------")

l = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    for j in range(i,len(l)):
            l[i][j],l[j][i] = l[j][i],l[i][j]
print(l)
for i in range(len(l)):
    l[i].reverse()
print(l)

print("---------------- Q4 -----------------------")

l = [5,5,2,5,8]
ans = 0
for i in range(len(l)):
    oddSum = 0
    evenSum = 0
    temp = l.copy()
    temp.pop(i)
    for j in range(len(temp)):
        if j % 2 == 0:
            evenSum += temp[j]
        else:
            oddSum += temp[j]
    if evenSum == oddSum:
        ans += 1
print(ans)

print("---------------- Q5 -----------------------")

a = [['A',35],['B',21],['C',26],['D',20]]

for x in range(len(a)):
    for y in range(len(a)-1):
        if a[y][1] > a[y+1][1]:
            a[y] , a[y+1] =   a[y+1], a[y]
print(a)


print("---------------- Q6 -----------------------")

a = [3,0,0,2,0,4]
max1 = 0
temp = 0

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

print(max1)