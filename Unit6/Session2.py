'''
U:
    Edge cases:
    -
    -
    -
P:
I:
'''



class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_value = self.front.value
        self.front = self.front.next
        return dequeued_value
    
    def peek(self):
        return self.front.value if not self.is_empty() else None

'''
U: 2 linked lists, length n & m , a nd b are positions on playlist 1 put playlist 2 into playlist 1.
    Edge cases:
    - playlist2 is empty, return playlist 1 without songs between a and b positions
    - playlist1 is empty, return None
    - out of bound a and b values, return 
        e.g.: if p1 has 5, and b = 6, a = 3, return playlist1 song 1->2 then playlist 2
P: iterate playlist1 
I:
'''
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    if not playlist1:
        return None

    if a < 0 or b < a:
        return playlist1

    dummy = Node(0,playlist1)
    prev = dummy
    # a-1 
    for i in range(a):
        if prev.next is None:
            return playlist1
        prev = prev.next

    curr = prev.next

    # a = 2, b = 6, find pos 1 and 7 
    # b+1 
    for i in range(b-a+1):
        if curr:
            curr = curr.next
        else:
            break

    if playlist2:
        prev.next = playlist2
        tail =playlist2
        while tail.next:
            tail = tail.next
        tail.next =curr
    else:
        prev.next = curr

    return dummy.next





# # Problem 1:# Create a new Queue
# q = Queue()

# # Add elements to the queue
# q.enqueue(('Love Song', 'Sara Bareilles'))
# q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
# q.enqueue(('Hug from a Dinosaur', 'Torres'))
# print_queue(q)

# # View the front element
# print("Peek: ", q.peek()) 

# # Remove elements from the queue
# print("Dequeue: ", q.dequeue()) 
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty: ", q.is_empty()) 

# # Remove the last element
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty:", q.is_empty()) 

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))