from implementation import tree1

# search in BST
def seachinBST(root, node):
    while root != None and root.data != node:
        if root.data < node:
            root = root.right
        else:
            root = root.left
    return root

if __name__ == '__main__':
    root = tree1()
    result = seachinBST(root,11)
    if result:
        print('Node is Present :- ',result.data)
    else:
        print('Node isnt Present')
