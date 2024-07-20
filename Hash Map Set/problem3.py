# 1657. Determine if Two Strings Are Close
'''
Two strings are considered close if you can attain
one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character 
into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1
and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa,
in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
'''

def solutionone(word1, word2):
    if len(word1) != len(word2):
        return False
    
    freq_checker1 = [0]*26
    freq_checker2 = [0]*26

    char_checker1 = [0]*26
    char_checker2 = [0]*26

    for i in range(len(word1)):
        freq_checker1[ord(word1[i])-ord('a')] += 1
        char_checker1[ord(word1[i])-ord('a')] = 1

    for i in range(len(word2)):
        freq_checker2[ord(word2[i])-ord('a')] += 1
        char_checker2[ord(word2[i])-ord('a')] = 1

    freq_checker1.sort()
    freq_checker2.sort()

    return freq_checker1==freq_checker2 and char_checker1==char_checker2

from collections import Counter
def solutiontwo(word1, word2):
    cnt1 = Counter(word1)
    cnt2 = Counter(word2)

    return cnt1.keys() == cnt2.keys() and sorted(cnt1.values()) == sorted(cnt2.values())

def solutionthree(word1, word2):
    l1 = []
    l2 = []

    for i in set(word1):
        l1.append(word1.count(i))
        l2.append(word2.count(i))
    
    return l1==l2
    

if __name__=='__main__':
    word1 = "aba"
    word2 = "aab"
    print(solutionthree(word1,word2))


    
 