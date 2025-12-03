a = [1,2,3]

try:
    print(f"first {a[0]}")
    print(f"5th {a[4]}")
except:
    print("arr error")

def fun(a):
    if (a < 4):
        b = a/(a-3)
    print(b)

try:
    fun(4)
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("Name Error")

def aByb(a,b):
    try:
        c = (a+b)/(a-b)
    except ZeroDivisionError:
        print('A/B rws in 0')
    else:
        print(c)
aByb(2.0,3.0)
aByb(3.0,2.0)


try:
    k = 5//0
except Exception as e:
    print(e)
else:
    print("else")
finally:
    print("f")


try:
    a = 2/0
except:
    print("error")
else:
    print("else")
finally:
    print("finally")
