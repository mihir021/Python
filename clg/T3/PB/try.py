with open("bytes", "wb") as f:
    f.write(b"\xff\xfe\xff\xff")
print(f.close())