
n = 5
first = second = float("-inf")
first1 = second1 = float("inf")
sum = 0
c = 0
while n > 0:
    number = int(input("Enter number :"))
    # h
    if number >= first:
        second = first
        first = number
    elif first >= number >= second:
        second = number
    # l
    if number <= first1:
        second1 = first1
        first1 = number
    elif first1 <= number <= second1:
        second1 = number
    sum += number
    c += 1
    n -= 1
    
print("highest ",first)
print("second highest ",second)
print("lowest ",first1)
print("sec lowest ",second1)
print("sum is :",sum)
print("ang is :",(sum/c))


