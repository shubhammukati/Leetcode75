from implementation import tree1, TreeNode

# insert a node in BST note after insertion the tree should follow bst preperties
def insertNode(root, node):
    current = root
    if current == None:
        return TreeNode(node)
    
    while current:
        if current.data <= node:
            if current.right != None:
                current = current.right
            else:
                current.right = TreeNode(node)
                break
        else:
            if current.left != None:
                current = current.left
            else:
                current.left = TreeNode(node)
                break
    return root

def iterate(root):
    if root == None:
        return
    print(root.data)
    iterate(root.left)
    iterate(root.right)

if __name__ == '__main__':
    root = tree1()
    nroot = insertNode(root,50)
    iterate(nroot)
