# 605. Can Place Flowers
'''
You have a long flowerbed in which some of the plots are planted,
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the
flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
'''

def flowerBed(flowerbed, n):
    if n == 0 : return True
    length = len(flowerbed)-1

    for i in range(length+1):
        if flowerbed[i] == 0:
            prevSpace = i==0 or flowerbed[i-1] == 0
            nextSpace = i==length or flowerbed[i+1] == 0

            # checking both the spaces if there flower exist
            if prevSpace and nextSpace:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
    return False

if __name__=='__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    if flowerBed(flowerbed,n):
        print('possible to plant flower')
    else:
        print('not possible to plant a flower')

