date = int(input("Enter the date : "))
months = int(input("Enter the month : "))
years = int(input("Enter the year : "))

mn_31 = False
ly = False
fix = True

if date < 0 or date > 31 or months < 0 or months > 12 or years < 0:
    print("Invalid valid date ")
    fix = False
if (years % 400 == 0) or (years % 4 == 0 and years % 100 != 0):
    ly = True
    fix = False
if months == 1 or  months == 3 or  months == 5 or months == 7 or months == 8 or  months == 10 or months == 12:
    mn_31 = True
if (date == 31 and not mn_31) or (months == 2 and date > 29) or (months == 2 and (not ly) and date == 29):
    print("Invalid valid date")
    fix = False
if fix:
    date += 1
    if (date > 31 and mn_31) or (date > 30 and not mn_31):
        months += 1
        date = 1
    elif months == 2 and ly and date == 30:
      months += 1
      date = 1
    elif months == 2 and date == 29:
        months += 1
        date = 1
    if months > 12:
        months = 1
        years += 1

print("date / month / year :", date,months,years)

'''
1 - 31
2 - 28 and 29 for ly
3 - 31
4 - 30 
5 - 31
6 - 30 
7 - 31
8 - 31
9 - 30
10 - 31
11 - 30
12 - 31
'''



