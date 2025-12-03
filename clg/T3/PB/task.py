import os

os.mkdir("task")
f = open("task\mihir","w")
f.write("blah "
        "blah blah"
        " blah")
f.close()
f = open("task\mihir",'r')
print(f.read())
f.close()

os.remove("task\mihir")
os.rmdir("task")
print(os.listdir())


