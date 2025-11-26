fName = input("Enter file name") + ".txt"
f = open(fName,'r')
i = 1
while i < 26:
    x = f.readline()
    if x == "":
        print("file is clear now ")
        break
    if i == 25:
        print(x)
        fix = input("do you want to print next 25 lines ? (YES/NO)")
        fix.lower()
        if fix == "yes":
            i = 1
        else:
            break
    i+=1
    print(x)

