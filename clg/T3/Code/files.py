print("---------------- read files ----------------------------")

f = open('txt','r') # FileNotFoundError # NameError if '' not +nt
print(f.read())
f.close()

print("--------------------------------------------")

f = open('txt','r+') # FileNotFoundError # NameError if '' not +nt
print('file name :',f.name)
print('file mode :',f.mode)
print('file readable :',f.readable())
print('file writable :',f.writable())
print('file is closed :',f.closed)
f.close()
print('file is closed :',f.closed)

print("--------------------------------------------")

f = open('xyz.txt','w+')
f.write('123\n')
f.write('123\n')
f.write('123\n')
# f.write([1,'2','3'])  # TypeError#
# f.writelines([1,'2','3'])  # TypeError
f.writelines(['1','2','3','4'])  # TypeError
f.close()

print("--------------------- read -----------------------")

f = open('xyz.txt','r')
print(f.read(9))
f.close()
print()
f = open('xyz.txt','r')
print(f.readline(60))
print(f.readline(1))
print(f.readlines(4))
f.close()

print("--------------------- tell -----------------------")

f = open('xyz.txt','r')
print(f.read(2))
print(f.seek(0))
print(f.tell())
print(f.read())
print(f.tell())
print()
f.close()

f = open('xyz.txt','r+')
f.write('my')
f.close()
print()




