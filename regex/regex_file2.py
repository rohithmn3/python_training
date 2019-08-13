#!/usr/bin/python3
import re

mesg="rohith                      is  a  good      boy"

print(mesg)

output=re.sub("\s+"," ",mesg)
print(output)
