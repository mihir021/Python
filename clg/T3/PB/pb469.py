from os.path import split


def countWords(ansP):
    return len(ansP.split())

def countOfState(ansP):
    return len(ansP.split(","))

f = open('frd.txt','r+')
c = 0
x = "1"
ans = ""
while x != "":
    x = f.readline()
    ans += x
    c+=1
f.close()

print(countWords(ans))
print(countOfState(ans))

