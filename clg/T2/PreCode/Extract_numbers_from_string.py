"""
5. Extract numbers from string.

Write a Python program to extract numbers from a given string.
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string:[12,45]
"""
a = "red 12 black 45 green"
ans = []
for x in a.split():
    if x.isnumeric():
        ans.append(x)
print(ans)