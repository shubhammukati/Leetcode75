from implementation import tree1


def searchBST(root, desired):
    while root != None and root.data != desired:
        root =  root.left if desired < root.data else root.right
    return root 


if __name__ == '__main__':
    root = tree1()
    print(searchBST(root,30))