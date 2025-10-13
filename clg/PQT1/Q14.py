# Enter months and output will be the days in months
"""
1 - 31
2 - 28 and 29 for ly
3 - 31
4 - 30
5 - 31
6 - 30
7 - 31
8 - 31
9 - 30
10 - 31
11 - 30
12 - 31
"""
n = 12
if n in (1,3,5,7,8,10,12):
    print("31")
elif n in (4,6,9,11):
    print("30")
elif n == 2:
    print("28")
else:
    print("Enter valid number :( ")