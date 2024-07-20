from implementation import tree1

# LCA in Binary Search Tree
def lca(root, p, q):
    while root:
        current = root.data
        if current < p and current < q:
            root = root.right
        elif current > p and current > q:
            root = root.left
        else:
            return root 
    return None

root = tree1()
p = 10
q = 5
a = lca(root,p,q)
if a:
    print(a.data)
else:
    print('None')
    
    
