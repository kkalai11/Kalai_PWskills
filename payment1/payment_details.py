
import os , sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course1 import course_details

course_details.course1()

def payment():
    print ("this is payment module")