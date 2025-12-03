f = open('pb481','w+')
ans = ""
while True:
    temp = input("Enter input val :")
    if temp.upper()=="END":
        break
    f.write(temp+"\n")
    if temp[0].isupper():
        ans += temp+"\n"

print(ans)
