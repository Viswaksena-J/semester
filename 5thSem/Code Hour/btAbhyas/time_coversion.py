

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[8] == "A":
        if s == "12:00:00AM":
            print("00:00:00")
        elif s[0:2] == "12":
            print(f'00{s[2:8]}')
        else:
            print(s[0:8])
    elif s[8] == "P":
        if s == "12:00:00PM":
            print("12:00:00")
        else:
            # s[0,1] = int(s[0,1])
            a = int(s[0:2])+12
            print(f'{a}{s[2:8]}')
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
