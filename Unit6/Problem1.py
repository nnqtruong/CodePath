'''
U: dna_strand, m, n
    m for keeping
    n for deleting
    return head

    Edge case 1: empty, return empty head
    Edge case 2: the dna_strand ends when we are deleting, within n, returns head
    Edge case 3: if m > dna_strand, return head of original dna_strand

P: while self.next is not None, iterate through m and n? 
    set pointer when iterate n+1

I: 
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

def edit_dna_sequence(dna_strand, m, n):
    a = dna_strand
    counter_m = 0
    counter_n = 0
    while a is not None:
        counter_m +=1 
        b = a.next
        if counter_m == m:
            while b.next is not None:
                counter_n += 1
                if counter_n == n:
                    counter_n = 0
                    break
                b = b.next
            a.next = b.next
            counter_m = 0
        a = a.next
    return dna_strand

'''
U: FOLDING protein, return the proteins in the loop
P: step 1: findd the loop, step 2: identify the cycle
I: step 1: detect cycle, 2 pointers, step 2: agther the values
'''

def cycle_length(protein):
    slow = protein
    fast = protein


    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return []

    cycle_start = protein
    while cycle_start != slow:
        cycle_start = cycle_start.next
        slow = slow.next
    
    cycle_value = [] 
    pointer = slow
    while True:
        cycle_value.append(pointer.value) 
        pointer = pointer.next
        if pointer == slow:
            break

    return cycle_value


# Problem 2
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))


# # Problem 1 
# dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))


