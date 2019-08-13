#!/usr/bin/python3

numlist=[10,20,30,40,50]
atab={"red":10,"blue":20,"green":30}

index=input("enter the index: ")
index=int(index)

try:
    color=input("enter the valid color: ")
    val=atab[color]
except KeyError as k:
    print("Error/Exception: {}".format(k))

try:
    ans=numlist[index] + val
except IndexError as i:
    print("Error/Exception: {}".format(i))


try:
    print(ans)
except NameError as n:
    print(n)
