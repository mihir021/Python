"""
     ip = "255.024.01.01"
     ans = "255.24.1.1"
"""
ip = "255.024.01.01"
ans = ""
for x in ip:
    if x != "0":
        ans += x
print(ans)
