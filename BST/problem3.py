from implementation import tree1

# you are given a root and a value 
# you have to find the ceil of a given value in a tree
# Ceil :- ceil(x) is a number that is either equal to X or is immediately greater
# than X
# if ceil could not be found then return -1

def findCeil(root, value):
    ceil = -1
    while root:
        if root.data == value:
            return root.data
        elif root.data < value:
            root = root.right
        else:
            ceil = root.data
            root = root.left
    return ceil

if __name__ == '__main__':
    root = tree1()
    print(findCeil(root, 11))