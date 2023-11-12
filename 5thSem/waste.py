

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumr=0
    suml=0
    sum=0
    j=n-1
    for i in range(0, n):
        sumr+=arr[j][i]
        suml+=arr[i][i]
        print(sumr)
        print(suml)
        j-=1
    sum=abs(suml-sumr)
    return (sum)
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)