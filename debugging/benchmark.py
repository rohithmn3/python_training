#!/usr/bin/python3


import timeit

def fun():
    a=0
    for i in range(1,200):
        a+=1
    print(a)


t=timeit.Timer("fun()", setup="from __main__ import fun")
print("TIMEIT:")
print(t.timeit(1))
