from datetime import date, datetime, time

from clg.T3.calculator.cal import *

today = date.today()
print(today)

d = date(2025, 12, 3)
print(d)

n = time(23, 59, 50)
print(n)

no = datetime.now()
print(no)

no = datetime.today()
print(no)

print(add(1,2))
print(sub(1,2))
print(divide(1,2))
print(mod(1,2))
print(mul(1,2))



