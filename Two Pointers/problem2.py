# 392. Is Subsequence
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
# brute force is to generate all the subsequences and check whether  the given sequence 
# is are in sequence list or not 


# optimal :- we are using two pointer approach in this to check whether it is present or not
def isSequence(s, t):
    j = 0 # j is pointing to s string
    for i in range(len(t)):
        if t[i]==s[j]:
            j += 1
        if j==len(s):
            return True
    return False

if __name__=='__main__':
    s = "axc"
    t = "ahbgdc"
    if isSequence(s, t):
        print('Present')
    else:
        print('Not Present')



        

    

