"""
8. Sort words alphabetically by first character.

Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"
("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")
"""
a = "Red Green Black White Pink"
b = a.split()
b.sort()
print(b)
