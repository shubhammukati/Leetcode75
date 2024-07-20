class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def tree1():
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)
    root.right = TreeNode(12)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(4)
    return root

def tree2():
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)
    return root

def tree3():
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)
    return root
