print("------------------------------------------------------------------")

c = 0
a = "12345"
for i in a:
    c += 1
print(c)

print("------------------------------------------------------------------")

a1 = "mom"
a2 = "mom"
if a1 == a2[::-1]:
    print("p")
else:
    print("NP")

print("------------------------------------------------------------------")

a = "mihir"
ans = a[0] + a[int(len(a)/2)] + a[-1]

print(ans)
print("------------------------------------------------------------------")

a = "python is very interesting"
ans = a[0:2] + a[-2] + a[-1]
print(ans)

print("------------------------------------------------------------------")

s1 = "12345"
s2 = "123"
l1 = 0
l2 = 0
for i in s1:
    l1 += 1
for j in s2:
    l2 += 1
if l1 > l2:
    print(s1)
elif l2 > l1:
    print(s2)
else:
    print("len same ",s1)

print("------------------------------------------------------------------")

nc = 0
nd = 0
s = 0
a = "p@yn2at&#i5ve"
for i in a:
    if i.isdigit():
        nd += 1
    elif i.isalpha():
        nc += 1
    else:
        s += 1
print(f"number of char {nc} number of digits {nd} symbol {s}")
print("------------------------------------------------------------------")

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

print("------------------------------------------------------------------")

sum = 0
c = 0
a = "1234iop%@6"
for i in a:
    if i.isdigit():
        sum += int(i)
        c += 1
print(f"sum is {sum} ans avg is {sum/c}")

print("------------------------------------------------------------------")

x = "abcabcabc".lower()
subString = "abc"
print(f"all occ of {subString} is {x.count(subString)}")

print("------------------------------------------------------------------")

sum = 0
a = (1,3,4,7,8,2)
for i in a:
    sum += i
print("sum is ",sum)

print("------------------------------------------------------------------")

min = float("inf")
max = float("-inf")
a = (1,3,4,7,8,2)
for i in a:
    if min < i:
        min = i
    if max > i:
        max = i

print(f"min is {min} max is {max}")

print("------------------------------------------------------------------")

even = []
odd = []
a = (1,3,4,7,8,2)
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"odd number {odd} even {even}")

print("------------------------------------------------------------------")

even = 0
odd = 0
a = (1,3,4,7,8,2)
for i in a:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f"sum of odd number is : {odd} sum of even number {even}")

print("------------------------------------------------------------------")

a = "Mr.Ed"
ans = ""
for i in a:
    if i.isupper():
        ans += i.lower()
    elif i.islower():
        ans += i.upper()
    else:
        ans += i
print(ans)
print("------------------------------------------------------------------")

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

print("------------------------------------------------------------------")
ans = ""
a = "AAAABBCCDDAAB"
pre = a[0]
c = 0
for i in a:
    if i == pre:
        c += 1
    else:
        ans += str(c) + pre
        pre = i
        c = 1
else:
    ans += str(c) + pre
print(ans)

print("------------------------------------------------------------------")


a = 12345
shift = 5

numberInString = str(a)
if shift > len(numberInString):
    print(numberInString[::-1])
else:
    while shift > 0:
        numberInString = numberInString[1:] + numberInString[0]
        shift -= 1

print(numberInString)


