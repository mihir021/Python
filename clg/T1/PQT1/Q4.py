def sum_s(n: int) -> int:
    total = 0
    while n > 0:
        d = n % 10
        total += d * d
        n //= 10
    return total


def is_happy_number(n: int) -> bool:
    slow = n
    fast = n
    while True:
        slow = sum_s(slow)
        fast = sum_s(sum_s(fast))

        if slow == 1 or fast == 1:
            return True
        if slow == fast:  
            return False


# Input range
sp = int(input("Enter Starting point: "))
ep = int(input("Enter Ending point: ")) + 1

# Print happy numbers in range
for x in range(sp, ep):
    if is_happy_number(x):
        print(x)
