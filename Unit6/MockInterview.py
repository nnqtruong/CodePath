'''
U: understanding, have singly linked list, return the middle node if # nodes is odd, and second middle node if even
P: define __init__ and def middleNode and use the fast and slow pointer 
I: def middlenode to start out as s = f = h

Input: head = [1, 2, 3, 4, 5]
Output:3

Feedback: Broke down question, clarify questions, thinking out loud.
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

print(middleNode(head).val)