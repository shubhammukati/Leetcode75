from implementation import tree2, tree1, tree3

# Check if a tree is a BST or BT
def isBST(root, maxRange=float('inf'), minRange=float('-inf')):
    if root == None:
        return True
    
    if root.data <= minRange or root.data >= maxRange:
        return False
    
    return isBST(root.left, root.data, minRange) and isBST(root.right, maxRange, root.data)

if __name__ == '__main__':
    root = tree3()
    print(isBST(root))