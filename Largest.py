#!/bin/python3

import sys

def sorter(nums):
    for i in range (0, len(nums)):
        for j in range (i+1,len(nums)):
            temp1 = 0
            if nums[i] > 9:
                temp1 = nums[i]//10
            else:
                temp1 = nums[i]
            temp2 = 0
            if nums[j] > 9:
                temp2 = nums[j]//10
            else:
                temp2 = nums[j]
            if temp1 < temp2:
                temp3 = nums[j]
                nums[j] = nums[i]
                nums[i] = temp3
                        
    return nums
    
print("Enter non-negative numbers (1 4 50)")
numbers = list(map(int, input().strip().split(' ')))
print(''.join(str(x) for x in sorter(numbers)))
