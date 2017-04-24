#!/bin/python3

import sys

def recursion(nums, n, sum):
    sum += nums[n]
    if not n == len(nums)-1:
        return recursion(nums, n+1, sum)
    else:
        return sum
    
print("Enter your numbers, enter non-numbers to quit.")
while True:
    try:
        nums = list(map(int, input().strip().split(' ')))
        print(recursion(nums, 0, 0))
    except ValueError:
        break;
