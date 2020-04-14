#using loop
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter any integer: "))
    multi=0
    for i in range(1,11):
        result=n*i
        print("{a} x {b} = {c}".format(a=n,b=i,c=result))