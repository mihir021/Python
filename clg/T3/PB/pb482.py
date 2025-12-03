f1 = open('pb482-1','r')
f2 = open('pb482-2','r')

p = 0
lineCount = 0
fix = True
line1 = "1"
line2 = "1"

while fix and (line1!="" and line2!=""):
    line1 = f1.readline()
    line2 = f2.readline()
    lineCount += 1
    minV = min(len(line1),len(line2))

    for i in range(minV):

        if line1[i] != line2[i]:
            print(f"line number {lineCount} and w {i+1}")
            fix = False
            break
    else:
        if len(line1) != len(line2):
            print(f"line number {lineCount} and w {i+1}")
            fix = False
            break
if fix:
    print("All are same ")