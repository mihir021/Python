x = 1
def a1():
    def a2():
        x = 9
        def a3():
            nonlocal x
            x = 7
        print(x)
        a3()
        print(x)
    print(x)
    a2()

print(x)
a1()
print(x)