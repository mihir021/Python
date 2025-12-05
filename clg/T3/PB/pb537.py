import math
class Cod:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def DFromOrigin(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    def trasFrom(self,TX,TY):
        self.x = self.x +TX
        self.y = self.y +TY
        return self.x,self.y
    def reflect(self):
        self.y = self.y*-1
        return self.x,self.y
    def bwTwoPoint(self,x2,y2):
        return math.sqrt(pow(self.x-x2,2) + pow(self.y-y2,2))


p1 = Cod(1,2)
print(p1.DFromOrigin())
print(p1.trasFrom(1,1))
print(p1.reflect())
print(p1.bwTwoPoint(3,4))
