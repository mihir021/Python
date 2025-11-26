f = open('frd.txt','r+')
c = 0
x = "1"
ans = ""
while x != "":
    x = f.readline()
    ans += x.capitalize()
    c+=1
f.close()
print([x.capitalize() for x in ans.split()])
