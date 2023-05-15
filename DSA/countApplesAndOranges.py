#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # print(f"house is from {s} - {t}")
    apple_tree_pos = a
    orange_tree_pos = b
    apple_dist, orange_dist = [],[]
    apple_count, orange_count = 0,0
    for apple in apples:
        # apple_dist.append(apple_tree_pos+apple)
        if apple_tree_pos+apple in range(s,t+1):
            # print(f"Adding apple: {apple}")
            apple_count += 1
    # print(apple_dist)
    
    for orange in oranges:
        # orange_dist.append(orange_tree_pos+orange)
        if orange_tree_pos+orange in range(s,t+1):
            # print(f"Adding orange: {orange}")
            orange_count += 1
    # print(orange_dist)
    
    print(apple_count)
    print(orange_count)
    
    
    
if __name__ == '__main__':
    s, t = 7,11
    a,b= 5,15
    apples, oranges = [-2,2,1],[5,-6]
    countApplesAndOranges(s, t, a, b, apples, oranges)
