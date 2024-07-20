from implementation import TreeNode
import sys

def consBST(preorder, index, maxBound):
    if index[0] == len(preorder) or preorder[index[0]] > maxBound:
        return None
    root = TreeNode(preorder[index[0]])
    index[0] += 1
    root.left = consBST(preorder, index, root.data)
    root.right = consBST(preorder, index, maxBound)
    return root

def constructBST(arr)-> TreeNode:
    i = [0]
    return consBST(arr, i, float('inf'))

def traversal(root):
    if root==None:
        return
    print(root.data,end=' ')
    traversal(root.left)
    traversal(root.right)

arr = [8,1,5,7,10,12]
a = constructBST(arr)
traversal(a)



        

