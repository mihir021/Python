# 3 angles are given and print yes if area is +ve and valid triangle else print no

a1,a2,a3 = 50,65,80

if a1 == 0 or a2 == 0 or a3 == 0:
    print("No")
else:
    if (a1+a2+a3)==180 and (a1+a2)>=a3 and (a1+a3)>=a2 and (a3+a2)>=a1:
        print("Yes")
    else:
        print("No")