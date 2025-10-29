"""
6. Extract name from email address.

Write a Python program to extract and display the name from a given Email address.
Sample Data:
("john@example.com") -> ("john")
("john.smith@example.com") -> ("johnsmith")
("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")
"""
a = "fully-qualified-domain@example.com"
a = a.split("@")
ans = ""
for x in a[0]:
    if x.isalpha():
        ans += x
print(ans)