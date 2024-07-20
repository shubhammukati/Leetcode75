# 2095. Delete the Middle Node of a Linked List
'''
You are given the head of a linked list. Delete the middle node,
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from
the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def deleteNode(head):
    slow = head
    fast = head
    prev = head

    while fast.next !=  None:
        fast = fast.next
        if fast.next != None:
            fast = fast.next
        prev = prev.next
        prev = slow
        slow = slow.next
        
        
    
    prev.next = slow.next 
    slow.next = None

    print(prev.data)
    print(slow.data)


if __name__ == '__main__':
    root = Node(2)
    head = root
    root.next = Node(1)
    root.next.next = Node(4)
    root.next.next.next = Node(7)
    root.next.next.next.next = Node(1)
    root.next.next.next.next.next = Node(2)
    root.next.next.next.next.next.next = Node(6)

    deleteNode(head)
    while root:
        print(root.data, end=' ')
        root = root.next

 
