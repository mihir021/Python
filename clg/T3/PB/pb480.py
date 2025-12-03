f = open('pb480','r+')
x = "1"
ans = ""
while x != "":
    x = f.readline()
    for temp in x.split():
        if temp.startswith("#"):
            break
        else:
            ans += (temp+" ")
    ans += "\n"
f.close()
print(ans)