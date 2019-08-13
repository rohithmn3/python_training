#!/usr/bin/python3

import getpass
import logging
import traceback
import sys

class UserError(Exception):
    def __init__(self,mesg):
        super().__init__(self,mesg)

class AuthError(Exception):
    def __init__(self,mesg):
        Exception.__init__(self)
        self.mesg = mesg
    def __str__(self):      # toString() of python
        return self.mesg


#log=logging.getLogger(__name__)
#print(log)
#handler=logging.Filehandler("err.log")
#log.addHandler(handler)


def accept_user():
    log=logging.getLogger(__name__)
    print(log)
    handler=logging.Filehandler("err.log")
    log.addHandler(handler)

    try:
        user = input("Login : ")
        if " " in user:
            raise UserError("Invalid User name")
        pwd= getpass.getpass()
    except UserError as u:
        print("User name error: {}".format(u))
        log.error(u)
    try:
        if user=="admin" and pwd=="admin":
            print("Valid user")
        else:
            raise AuthError("user name/ password is invalid")
    except Exception as e:
        print("username and password doesnt match: {} type is {}".format(e,type(e)))
        log.error(e)
        log.error(type(e))

try:
    accept_user()
except Exception:
    traceback.print_exc()
    print(sys.exc_info())
