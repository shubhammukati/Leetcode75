from implementation import tree1, TreeNode
import sys

class Solution:
    def __init__(self):
        self.prev = TreeNode(float('-inf'))
        self.first = None
        self.last = None
        self.middle = None
    
    def recoverBST(self,root):
        if root == None:
            return
        self.recoverBST(root.left)

        if self.prev != None and root.data < self.prev.data:
            if self.first == None:
                self.first = self.prev 
                self.middle = root
            else:
                self.last = root
        
        self.prev = root
        
        self.recoverBST(root.right)
    
    def recoverTree(self, root):
        self.recoverBST(root)
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data
        print(self.first.data)
        print(self.last.data)


if __name__ == '__main__':
    root = tree1()
    solution = Solution()
    solution.recoverTree(root)
    
