#!/usr/bin/python3

class Employee:
    #class variables
    total=0
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.total+=self.salary
        Employee.count+=1

    @staticmethod
    def getTotal():
        print("Total Ssalary = ",Employee.total)

    #if we have a class variables, we need class methods to access it
    @classmethod
    def getAvg(cls):
        print("Avg sal = ",cls.total/cls.count)


e1=Employee("Rohith",50000)
e2=Employee("Gokul",90000)

e1.getTotal()
Employee.getAvg()
    
