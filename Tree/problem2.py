from implementation import tree1,tree2,TreeNode

def helper(root, temp):
    if root == None :
        return
    if root.left == None and root.right == None:
        temp.append(root.data)
    helper(root.left, temp)
    helper(root.right, temp)


def checker():
    temp1 = []
    temp2 = []
    root1 = tree1()
    root2 = tree2()
    helper(root1, temp1)
    helper(root2, temp2)
    result = True if temp1==temp2 else False
    if result:
        print('Accepted')
    else:
        print('Rejected')

c = checker()
