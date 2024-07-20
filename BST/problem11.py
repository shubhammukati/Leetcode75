from implementation import tree2, TreeNode
# return True if in bst is there any two nodes are present that sum
# is equal to the target

class Solution:
    def __init__(self):
        self.temp = []

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.temp.append(root.data)
        self.inorder(root.right)

    def twoSum(self, root, target):
        self.inorder(root)
        left = 0
        right = len(self.temp)-1

        while left < right:
            if self.temp[left] + self.temp[right] == target:
                return True
            elif self.temp[left] + self.temp[right] > target:
                right -= 1
            else:
                left += 1
        return False

if __name__ == '__main__':
    root = tree2()
    solution = Solution()
    target = 17
    print(solution.twoSum(root,target))

            
        


