#!/usr/bin/python3


class Alpha:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("alpha fun2")
        
class Beta:
    def fun2(self):
        print("fun2")

class Delta(Alpha, Beta):
    def fun3(self):
        print("fun3")
        
class Omega(Delta):
    def fun4(self):
        print("fun4")
        
        
ob=Omega()
ob.fun2()
print(Omega.__mro__)
