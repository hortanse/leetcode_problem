#Leetcode 1 Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List
def twoSum(nums, target):
    prevMap = {} #val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
print("Test case 1")
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {twoSum(nums1, target1)}\n")