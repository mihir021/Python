n = 5
for x in range(n,0,-1):
    for y in range(0,n-x):
        print("   ",end="")
    for y in range(x):
        print(" * ",end="")
    print()