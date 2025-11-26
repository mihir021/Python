f = open('frd.txt','r+')
c = 0
x = "1"
while x != "":
    x = f.readline()
    if c % 2 != 0:
        print(x)
    c+=1
f.close()
