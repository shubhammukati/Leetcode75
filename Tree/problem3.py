from implementation import tree1,tree2


def treeNode(root, p, q):
    if root == None:
        return

    left = treeNode(root.left, p, q)
    right = treeNode(root.right, p, q)

    if left == p:
        return left
    elif right == q:
        return right
    else:
        return root

if __name__ == '__main__':
    root = tree1()
    print(treeNode(root,37,43))

