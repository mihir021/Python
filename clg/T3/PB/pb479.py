def countWords(ansP):
    return len(ansP.split())

def countOfState(ansP):
    return len(ansP.split(" "))-1

f = open('frd.txt','r+')
c = 0
x = "1"
ans = ""
numberOfChar = 0
while x != "":
    x = f.readline()
    numberOfChar += len(x)
    ans += x
    c+=1
f.close()

print(countWords(ans))
print(countOfState(ans))

