a = 12345
shift = 5

numberInString = str(a)
shift = shift % len(numberInString)

while shift > 0:
    numberInString = numberInString[1:] + numberInString[0]
    shift -= 1

print(numberInString)