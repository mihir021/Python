nUppercase = 0
nLowercase = 0

s = "abcAfgUIBGo"

for x in s:
    if x.islower():
        nLowercase += 1
    if x.isupper():
        nUppercase += 1

print("total upper :",nUppercase)
print("total lower :",nLowercase)
