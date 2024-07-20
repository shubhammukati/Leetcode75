from implementation import tree1

# Find K-th smallest/largest element in BST
def findkThSmallest(root, k, cnt, smallest):
    if not root or cnt[0] >= k:
        return
    
    findkThSmallest(root.left,k,cnt,smallest)
    cnt[0] += 1
    if cnt[0] == k:
        smallest[0] = root.data
    findkThSmallest(root.right,k,cnt,smallest)

def findkThLargest(root, k, cnt, largest):
    if not root or cnt[0] >= k:
        return
    
    findkThLargest(root.right, k, cnt, largest)

    cnt[0] += 1
    if cnt[0] == k:
        largest[0] = root.data

    findkThLargest(root.left, k, cnt, largest) 

if __name__ == '__main__':
    smallest = [0] 
    cnt = [0]
    root = tree1()
    findkThLargest(root,1,cnt,smallest)
    print(smallest)
