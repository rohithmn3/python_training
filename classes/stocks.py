#!/usr/bin/python3


class Stocks:
    def __init__(self,name=None,qty=0):
        self.name=name
        self.qty=qty

    def buy(self,howmuch):
        self.qty+=howmuch

    def sell(self,howmuch):
        self.qty-=howmuch

    def isThere(self):
        return True if self.qty>0 else False

    def show(self):
        print(self.name)
        print(self.qty)


s1=Stocks("Rohith",20)
s2=Stocks("Gokul",3)

if s1.isThere:
    s1.sell(2)
else:
    s1.buy(10)

if s2.isThere:
    s2.sell(2)
else:
    s2.buy(10)


s1.show()
s2.show()
