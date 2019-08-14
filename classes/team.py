#!/usr/bin/python3


class Team:
    def __init__(self,name,mem,location):
        self.name=name
        self.mem=mem
        self.location=location

    def __eq__(self, rhs):
        if len(self.mem) == len(rhs.mem):
            return True
        else:
            return False


t1 = Team("alpha", ["a", "b", "c"], "blr")
t2 = Team("delta", ["s", "t", "u"], "mys")

if t1 == t2:
    print("same size")
else:
    print("Diff size")
