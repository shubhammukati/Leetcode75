# 1004. Max Consecutive Ones III
'''
Given a binary array nums and an integer k, return the maximum number
of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''



def maxConsecutive(nums,k):
    maxlen = 0
    left = 0
    right = 0
    zeros = 0
    
    while right < len(nums):
        if nums[right] == 0:
            zeros += 1
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        if zeros <= k:
            maxlen = max(maxlen,right-left+1)
        right += 1
    return maxlen

if __name__ == '__main__':
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(maxConsecutive(nums,k))

