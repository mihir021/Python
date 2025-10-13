import math

stations = int(input("Enter number of stations: "))
stops = int(input("Enter number of stops: "))

n = stations - stops + 1
r = stops

if n < r or r < 0:
    print("Invalid input: n must be >= r and r must be non-negative.")
else:
    ans = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    print("Number of ways:", ans)
