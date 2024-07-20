class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
def tree1():
    t = TreeNode(10)
    t.left = TreeNode(20)
    t.right = TreeNode(30)
    t.left.left = TreeNode(37)
    t.left.right = TreeNode(43)
    t.right.left = TreeNode(32)
    t.right.right = TreeNode(5)
    t.right.right.right = TreeNode(4)
    return t 

def tree2():
    t = TreeNode(10)
    t.left = TreeNode(20)
    t.right = TreeNode(30)
    t.left.left = TreeNode(37)
    t.left.right = TreeNode(4)
    t.right.left = TreeNode(32)
    t.right.right = TreeNode(5)
    t.right.right.right = TreeNode(4)
    return t 