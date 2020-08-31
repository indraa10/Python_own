class Purchase():
    #total_price=0
    #final_price=0
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
        #print("constructor executed")
    def getdiscount(self):
        if self.brand == 'samsung' and self.ram == 4 :
            #print("condition satisfied for discount 10")
            return int(10)
        elif self.brand == 'samsung' and self.ram == 6 :
            #print("condition satisfied for discount 8")
            return int(8)
        elif self.brand == 'apple' and self.ram == 6 :
            #print("condition satisfied for discount 5")
            return int(5)
    def purchasemob(self):
       #print("execution start for purchase mobile")
       return self.price*(100-self.getdiscount())*0.01
       #print("total price: ",total_price)
    def setgst(self):
        if self.ram==4 :
            return int(5)
        else :
            return int(12)
    def finalprice(self):
        #print("purchase mob: :",self.purchasemob())
        #print("return gst: ",self.setgst())
        return (self.purchasemob() + self.purchasemob()*self.setgst()*0.01)
    def printprice(self):
        print("final price: ",self.finalprice())

p=Purchase('samsung',4,18500)

#p.getdiscount()
#p.purchasemob()
p.printprice()
