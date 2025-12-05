class Store:
    def __init__(self, name, price):
        self.quantity = None
        self.total = None
        self.name = name
        self.price = price
    def setQ(self,q):
        self.quantity = q
    def getTotal(self):
        return self.quantity*self.price
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getQ(self):
        return self.quantity


l = []
n1 = int(input("Enter how many items you want to add ?"))
while n1 > 0:
    name = input("Enter name of product :")
    price = float(input("Enter price of the product"))
    c1 = Store(name,price)
    l.append(c1)
    n1 -= 1
for x in l:
   print(x.getName() , x.getPrice())
for x in l:
    quantity = int(input("Enter quantity:"))
    x.setQ(quantity)

print("--------------- Bill -------------------------")
fTotal = 0
for x in l:
    print(x.getName() , x.getPrice() , x.getQ() , x.getTotal() )
    fTotal += x.getTotal()
print("----------------------------------------------")

print(fTotal)






