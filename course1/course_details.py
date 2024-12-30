import os, sys

from os.path import dirname,join,abspath


sys.path.insert(0,abspath(join(dirname(__file__),'..')))

#from payment1 import payment_details

#payment_details.payment()

def course1():
    print("this is course module")