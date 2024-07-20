# 345. Reverse Vowels of a String
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
more than once.

Example 1:
Input: s = "hello"  Output: "holle"

Example 2: Input: s = "leetcode" Output: "leotcede"
'''

def reverseVowel(s):
    rs = ''
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    v = ''

    for i in range(len(s)):
        if s[i] in vowel:
            v += s[i]
    
    right = len(v)-1
    for i in range(len(s)):
        if s[i] in vowel:
            rs += v[right]
            right -= 1
        else:
            rs += s[i]
    
    return rs

if __name__=='__main__':
    s = "leetcode"
    print(reverseVowel(s))