years = int(input("Enter year :"))
if (years % 400 == 0) or (years % 4 == 0 and years % 100 != 0): # nested kri nakhvu if need
    print("ly")
else:
    print("not ly")
