# 1768. Merge Strings Alternately

'''You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r'''


def mergeStrings(str1,str2):
    str3 = ''
    left = 0
    right = 0
    len1 = len(str1)
    len2 = len(str2)

    while left<len1 and right<len2:
        str3 += str1[left]
        str3 += str2[right]
        right += 1
        left += 1
    
    while left < len1:
        str3 += str1[left]
        left += 1
    
    while right < len2:
        str3 += str2[right]
        right += 1
    
    return str3

if __name__=='__main__':
    str1 = 'abc'
    str2 = 'pqr'
    print(mergeStrings(str1, str2))
else:
    print('you dont have access')
