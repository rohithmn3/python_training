#!/usr/bin/python3

import subprocess
import re

output=subprocess.check_output("ifconfig").decode("utf-8")
#print(output)


res=re.search("\s+inet.*?:(.*?)\s",output)
if res:
	print(res.group(1))
