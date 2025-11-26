f = open('frd.txt','r+')
c = 0
while f.readline() != "":
    c += 1

print(c)
