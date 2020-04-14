#array operation

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("number of element: "))

    arr = list(map(int, input("enter elements one after one with space: ").rstrip().split()))
    reversed_arr=[]
    for i in range(n):
        reversed_arr.append(arr[n-i-1])
    #print(reversed_arr)

reversed_str=''
for i in range(len(reversed_arr)):
    reversed_str=reversed_str + str(reversed_arr[i])+ ' '
print(reversed_str)


