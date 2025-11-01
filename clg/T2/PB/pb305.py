a = "abcpqr"
b = "bcpqar"
if len(a) == len(b):
    for x in b:
        if a.count(x) != b.count(x):
            print("not same")
            break
    else:
        print("same")
else:
    print("not same ")
