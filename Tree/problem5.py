from implementation import tree1
import sys

def largestTreeNode(root):
    if root == None :
        return 0
    
    left = largestTreeNode(root.left)
    right = largestTreeNode(root.right)
    return max(root.data, left, right)

if __name__ == '__main__':
    root = tree1()
    currentNode = -sys.maxsize-1
    print(largestTreeNode(root))
