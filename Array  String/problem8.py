# 334. Increasing Triplet Subsequence
'''
Given an integer array nums, return true if there exists a
triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
'''

def brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]<nums[j]<nums[k]: return True
    return False

import sys
def triplet(nums):
    small = sys.maxsize
    mid = sys.maxsize
    large = 0

    for i in range(len(nums)):
        if nums[i] > mid : 
            return True
        if nums[i] <= small:
            small = nums[i]
        elif nums[i] <= mid:
            mid = nums[i]
    return False

if __name__=='__main__':
    nums = [5,4,3,2,1]
    if triplet(nums):
        print('Acceptable')
    else:
        print('Rejected')
