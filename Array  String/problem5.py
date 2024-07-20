# 151. Reverse Words in a String
'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Example 1: Input: s = "the sky is blue"  Output: "blue is sky the"
'''

def reverseWords(s):
    l = s.split()
    returnlist = []
    for i in range(len(l)-1,-1,-1):
        returnlist.append(l[i])
    return ' '.join(returnlist)

if __name__=='__main__':
    s = "the sky is blue"
    print(reverseWords(s))
    

