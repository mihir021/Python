# custom Error Generation


# class Age(Exception):
#     pass
#
# def validateAge(InputAge):
#     if InputAge >= 18:
#         return True
#     return False
#
# age = int(input("Enter age :"))
# if validateAge(age):
#     print("done")
# else:
#     raise Age("Enter valid age")


# or

def validateAge(InputAge):
    if InputAge >= 18:
        return True
    return False

age = int(input("Enter age :"))
if validateAge(age):
    print("done")
else:
    raise TypeError("Enter valid Age")