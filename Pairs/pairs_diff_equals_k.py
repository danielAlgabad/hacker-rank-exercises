#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pairs(k, arr):
    d = dict.fromkeys(arr)
    count = 0

    for c in d:
        i = c + k
        if i in d:
            count += 1
    return count


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    print(pairs(k, arr))
