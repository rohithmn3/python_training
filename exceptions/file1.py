#!/usr/bin/python3

try:
    f1=open("openfile.txt")
    ans=f1.read()
    print(ans)
    f1.close()

except FileNotFoundError as e:
    print("Error/exception: {}".format(e))
