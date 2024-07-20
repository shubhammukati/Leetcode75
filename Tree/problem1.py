from implementation import TreeNode, tree1

def highestHeight(root):
    if root == None:
        return 0 
    
    return 1 + max(highestHeight(root.left), highestHeight(root.right)) 

if __name__ == '__main__':
    root = tree1()
    print(highestHeight(root))




