#!/usr/bin/python3
import datetime

def fun_wrapper(fnptr, *args, **kwargs):
    print("Hello..! i am adding extra features")
    print(datetime.date.today())
    res=fnptr(*args, **kwargs)
    return res

def express(a,b,c):
    print(a)
    print(b)
    print(c)

def add(a,b):
    print(a+b)

def square(a):
    print(a*a)

def greet():
    print("Hello Python..!")
