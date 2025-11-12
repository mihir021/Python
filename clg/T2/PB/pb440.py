msg = "abc abcd hi abcde ha haaa xyz haaaaaaa xyxw"
msg.lower()
listA = msg.split()
ans = {}
for i in listA:
    if i[0] in ans.keys():
        ans[i[0]] = ans.get(i[0]) + [i]
    else:
        ans.setdefault(i[0],[i])
print(ans)
