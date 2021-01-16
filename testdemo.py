#!/usr/bin/python
import random
def Maopaopaixu_Test(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

enumerate=[10,18,15,199,0,99,3,2,8]
print(Maopaopaixu_Test(enumerate))