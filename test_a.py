import sys
import common.logger
import os 



def func():
    print(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    print(os.getcwd())
func()