#!/usr/bin/python3

import program1

program1.add(2,3)
program1.greet()



print("##############################################")
## *args- tuple ; **kwargs- dict
program1.fun_wrapper(program1.add,2,3)
program1.fun_wrapper(program1.greet)
