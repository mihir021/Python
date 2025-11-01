a = "abcABCxyzXYZ"
key = 3
ans = ""
for x in a:
    if x.isspace():
        ans += " "
        continue
    if x.isupper():
        temp = ((ord(x) + key) % 90)
        if temp < 65:
            temp += 65
        ans = ans + chr(temp)
    else:
        temp = ((ord(x) + key) % 122)
        if temp < 97:
            temp += 97
        ans = ans + chr(temp)
print(ans)

a = " ab ab tfgh abc"
print(a.count("ab"))