"""
3. Swap commas and dots in a string.

    Write a Python program to swap commas and dots in a string.

    Sample string: "32.054,23"
    Expected Output:"32,054.23"
"""
string = "32.054,23"
ans = ""
for x in string:
    if x == ".":
        ans += ","
    elif x == ",":
        ans += "."
    else:
        ans += x
print(" ans is" , ans)