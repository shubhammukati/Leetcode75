from implementation import tree1

def findFloor(root, x):
    floor = -1
    while root:
        if root.data == x:
            return root.data
        elif root.data < x:
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor

if __name__ == '__main__':
    root = tree1()
    print(findFloor(root,1))