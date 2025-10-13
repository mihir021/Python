def g(x):
    def h():
        nonlocal x
        x = 'abc'
    print("in g(x):x = ",x)
    h()
    print(x)
    return x
x = 3
z = g(x)
print(z)
print(x)

# g - change the var in out of the function
# nonlocal - change the var in side of the function also and not for out of the function

