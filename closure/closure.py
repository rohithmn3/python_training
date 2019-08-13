#!/usr/bin/python3

def outer(mesg):
  a=10
  b=20
  print(mesg)
  def inner():
    c=30
    ans = a + b + c + d
    print("INNER BOOK = ",locals())
    print(ans)
  print("OUTER BOOK = ",locals())
  return inner

if __name__ == "__main__":
 d=40
 #everytime we get a new address when we print
 
 fnptr = outer("Hello world")
 print(fnptr)
 
# fnptr2 = outer("some mesg")
# print(fnptr2)
 
# fnptr3 = outer("hai some other mesg")
# print(fnptr3)
 
 print(fnptr.__name__)
 print(fnptr.__doc__)
 print(fnptr.__defaults__)
 print(fnptr.__code__)
 print(fnptr.__closure__)
 fnptr()
