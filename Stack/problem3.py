# 394. Decode String
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are well-formed, etc. Furthermore,
you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''


def decodeString(s):
    stack = []
    currentstring = ''
    currentnumber = 0

    for char in s:
        if char == '[':
            stack.append(currentstring)
            stack.append(currentnumber)
            currentstring = ''
            currentnumber = 0
        elif char == ']':
            prevnumber = stack.pop()
            prevstring = stack.pop()
            currentstring = prevstring + prevnumber * currentstring
        elif char.isdigit():
            currentnumber = currentnumber * 10 + int(char)
        else:
            currentstring += char
    return currentstring

if __name__ == '__main__':
    s = "3[a2[c]]"
    print(decodeString(s))
    

 