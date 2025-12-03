class Rec:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l*self.w

r1 = Rec(1,2)
r2 = Rec(2,4)
print(r1.getArea())
print(r2.getArea())

