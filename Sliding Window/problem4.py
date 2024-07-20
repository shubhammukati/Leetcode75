# 1493. Longest Subarray of 1's After Deleting One Element
'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only
1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers
with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray
with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
'''

def longestSubarray(nums):
    left = 0
    right = 0
    maxlen = 0
    zero = 0

    while right < len(nums):
        if nums[right] == 0:
            zero += 1

        if zero > 1:
            if nums[left] == 0:
                zero -= 1
            left += 1
        
        if zero <= 1:
            maxlen =  max(maxlen, right-left )
        
        right += 1
        
    return maxlen

if __name__=='__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    print(longestSubarray(nums))

    

         
 