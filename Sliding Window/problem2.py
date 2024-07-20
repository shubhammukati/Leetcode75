# 1456. Maximum Number of Vowels in a Substring of Given Length
'''
Given a string s and an integer k, return the maximum number of vowel
letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

def maxLenVowel(s, k):
    vowels = ['a','e','i','o','u']
    maxvowel = 0
    for i in range(k):
        if s[i] in vowels :
            maxvowel += 1
    
    maxlen = maxvowel
    left = 0
    right = k

    while right < len(s):
        if s[left] in vowels:
            maxvowel -= 1
        left += 1

        if s[right] in vowels:
            maxvowel += 1
        right += 1

        maxlen = max(maxlen,maxvowel)

    return maxlen

if __name__ == '__main__':
    s = "leetcode"
    k = 3
    print(maxLenVowel(s,k))


