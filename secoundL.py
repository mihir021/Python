n = [10,10,10,10,10,10,10,10,10,10]

first = second = float("inf")

for number in n:
    if number <= first:
        second = first
        first = number
    elif first <= number <= second:
        second = number

print("Second l :",second)
print("first l:",first)

