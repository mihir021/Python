# pb - 159
n = 5
for i in range(n):
    for j in range(i) :
        print("* ",end=" ")
    print()

# pb - 160
print()
n = 4
for i in range(n,0,-1):
    for j in range(n-i):
        print("  ",end=" ")
    for j in range(i) :
        print("* ",end=" ")
    print()

# pb - 161
print()
n = 6
for i in range(n):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i) :
        print(" * ",end=" ")
    print()

# pb - 162
print()
n = 4
for i in range(n,0,-1):
    for j in range(i) :
        print(" * ",end=" ")
    print()

# pb - 163
print()
n = 4
for i in range(n,0,-1):
    for j in range(i) :
        print(" ",(j+1)," ",end=" ")
    print()

# pb-164
print()
n = 5
for i in range(n):
    for j in range(i) :
        print(" ",(j+1)," ",end=" ")
    print()

# pb-165
print()
n = 5
for i in range(n):
    for j in range(i) :
        print(" ",i," ",end=" ")
    print()

# pb-166
print()
n = 5
for i in range(n):
    for j in range(i) :
        if i%2!=0 :
            print("* ",end=" ")
        else:
            print("# ",end=" ")
    print()

# pb - 167
n = 5
for i in range(n):
    for j in range(i) :
        if (i+j)%2==0 :
            print("0 ",end=" ")
        else:
            print("1 ",end=" ")
    print()

# pb - 168
print()
n = 6
for i in range(n):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i) :
        print(" ",(j+1)," ",end="")
    print()

# pb - 169
print()
n = 6
for i in range(n):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i) :
        print(" ",i," ",end="")
    print()

# pb - 170
print()
n = 6
for i in range(n):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i) :
        if i % 2 != 0:
            print(" * ", end=" ")
        else:
            print(" # ", end=" ")
    print()

# class
print()
n = 5
for i in range(n):
    for j in range(n):
        print(" * ",end=" ")
    print()