l = []


def shift1():
    if len(l) == 0:
        raise Exception("Q is empty")
    else:
        return l.pop(0)


def pop1():
    if len(l) == 0:
        raise Exception("Q is empty")
    else:
        return l.pop()


def remove1():
    m1 = max(l)
    return l.remove(m1)



class SQ:
    def __init__(self,val):
        self.val = val

    def unShift(self):
        l.insert(0,self.val)
    def push1(self):
        l.append(self.val)


a1 = SQ(1)
a2 = SQ(2)
a3 = SQ(3)
a4 = SQ(4)
a5 = SQ(5)

a1.push1()
a2.push1()
a3.unShift()
a5.push1()
a4.push1()
remove1()

print(l)





