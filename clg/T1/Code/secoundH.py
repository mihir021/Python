n = [97,88,45,10,1]

first = second = float("-inf")

for number in n:
    if number >= first:
        second = first
        first = number
    elif first >= number >= second:
        second = number

print("Second highest :",second)
print("first highest:",first)

