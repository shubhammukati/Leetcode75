# 443. String Compression
'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

   ** If the group's length is 1, append the character to s.

   ** Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately,
but instead, be stored in the input character array chars.

*Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
'''

def brute(stringar):
    length = len(stringar)
    freq = dict()
    for i in range(length):
        freq[stringar[i]] = freq.get(stringar[i], 0)+1
    
    ptr = 0
    for x, y in freq.items():
        if y==1:
            stringar[ptr] = x
            ptr += 1
        else:
            stringar[ptr] = x
            ptr += 1
            number = str(y)
            for i in range(len(number)):
                stringar[ptr] = number[i]
                ptr += 1
    return ptr

def stringCompression(chars):
    length = len(chars)
    if length<2:
        return length
    left = 0
    right = 0

    while(left<length):
        currentchar = chars[left]
        currentocurrence = 0
        while left<length and chars[left] == currentchar:
            currentocurrence += 1
            left += 1
        chars[right] = currentchar
        right += 1

        if currentocurrence>1:
            for char in str(currentocurrence):
                chars[right] = char
                right += 1
    
    return right


if __name__=='__main__':
    chars = ["a","a","b","b","b","b","b","b","b","b"]
    ptr = stringCompression(chars)
    for i in range(ptr):
        print(chars[i], end = ' ')
    





