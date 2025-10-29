"""
4. Find similarity between two strings.

Write a Python program to find string similarity between two given strings.
Sample Output:
Original string:
Python Exercises
Python Exercises
Similarity between two said strings:
1.0

Original string:
Python Exercises
Python Exercise
Similarity between two said strings:
0.967741935483871

Original string:
Python Exercises
Python Ex.
Similarity between two said strings:
0.6923076923076923

Original string:
Python Exercises
Python
Original string:
Python Exercises
Python
Similarity between two said strings:
0.5454545454545454

Original string:
Java Exercises
Python
Similarity between two said strings:
0.0
"""

a1 = "Python Exercises"
a2 = "Python"

i = 0
while i < min(len(a1), len(a2)) and a1[i] == a2[i]:
    i += 1

print((2*i)/(len(a1)+len(a2)))