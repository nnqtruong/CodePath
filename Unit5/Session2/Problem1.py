'''
U:
    Edge cases: 
        - Empty list, return null
        - 2 values, return what is greater
        - 1 value, return that value
P: while next variable is not none, have a max variabl running 
I: linear search
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    if not head:
        return None
    max_value = head.value
    current = head.next
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value


'''Problem2
U: remove_tail def is incorrect, remove the last node, but always keep the head node and create test cases.
    Edge case: 
        - 1 Node, return None
        - 0 Nodes, return None
        - 2 Nodes, return 1st Node
    
P: 1 2 3 returns 1 2
I: 
'''

def remove_tail(head):
    if head is None:
        return None
    if head.next is None: 
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head


'''
Problem 3
U: 1 2 3 3 4 5, returns 1 2 4 5
    edge cases:
    - 1 Node, return 1 Node
    - 0 Node, return None
    - 2 Nodes same, return None
P: 
I: 

'''

def delete_dupes(head):
    if head is None:
        return None
    if head.next is None: 
        return head
    
    temp_head = Node(0,head)
    previous = temp_head
    current = head

    while current:
        if current.next and current.value == current.next.value:
            dup_val = current.value
            # skip all nodes with dup_val
            while current and current.value == dup_val:
                current = current.next
            previous.next = current
        else:
            previous = current
            current = current.next
    return temp_head.next
            

'''
Problem 4
U: 
P: 
I: 

'''

def has_cycle(head):
    

# Problem 4
peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))
peach = Node("Peach")
peach.next = luigi
luigi = Node("Luigi")
luigi.next= mario
mario = Node("Mario")
mario.next= toad
toad = Node("Toad")
toad.next= luigi

print(has_cycle(peach))

# #Problem 1
# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))

# #Problem 2
# head1 = Node(5, Node(6, Node(7, Node(8))))
# print_linked_list(remove_tail(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))
# print_linked_list(remove_tail(head2))

# # Problem 3
# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))