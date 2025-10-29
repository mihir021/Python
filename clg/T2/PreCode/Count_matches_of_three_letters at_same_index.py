"""
7. Count matches of three letters at same index.

Write a Python program that takes two strings. Count the number of times each string contains the same three letters at the same index.
Sample Data:
("Red RedGreen") -> 1
("Red White Red White) -> 7
"""

a = "Red"
b = "RedGreen"
count = 0
min_len = min(len(a), len(b))

for i in range(min_len - 2):  # -2 because we're checking groups of 3 chars
    if a[i:i + 3] == b[i:i + 3]:
        count += 1

print(count)