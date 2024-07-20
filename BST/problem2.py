from implementation import tree1

# find the maximum root node in BST
def findMax(root):
    while root.right:
        root = root.right
    return root


# find the minimum root node in BST
def findMin(root):
    while root.left:
        root = root.left
    return root

root = tree1()
print(findMin(root).data)