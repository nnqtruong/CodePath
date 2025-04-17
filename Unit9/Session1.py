from collections import deque 

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
'''
U: Understanding Breadth First Search Traversal
P: Queue data structure. Array to store each level.
        empty -> empty 

I: Implement. While loop through the queue. For loop inside 
'''
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    if not design:
        return []
    
    output = []
    queue = deque([design])

    while queue:
        level = []

        # Loops through level
        for i in range(len(queue)):
            puff = queue.popleft()
            level.append(puff.val)

            if puff.left:
                queue.append(puff.left)
            if puff.right:
                queue.append(puff.right)
        
        output.append(level)
    return output

# #Problem 1 usage
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print(listify_design(croquembouche))


def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    
    output = []
    queue = deque([cupcakes])
    left_to_right = True

    while queue:
        level = deque()

        # Loops through level
        for i in range(len(queue)):
            puff = queue.popleft()
            if left_to_right:
                level.append(puff.val)
            else:
                level.appendleft(puff.val)

            if puff.left:
                queue.append(puff.left)
            if puff.right:
                queue.append(puff.right)
        
        output.extend(level)
        left_to_right = not left_to_right

    return output


"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# # Problem 2 usage
# flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
# cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))
# #['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']


def larger_order_tree(orders):
    
    # DFS traversal
    def reverse_inorder(node, total):
        if not node:
            return total
        total = reverse_inorder(node.right, total)
        node.val += total
        total = node.val
        # total = reverse_inorder(node.left, total)

        return reverse_inorder(node.left, total)

    reverse_inorder(orders, 0)
    return orders
        

# # Problem 3 usage
# """
#          4
#        /   \
#       /     \
#      1       6
#     / \     / \
#    0   2   5   7
#         \       \
#          3       8   
# """
# # using build_tree() function included at top of page
# order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# orders = build_tree(order_sizes)

# # using print_tree() function included at top of page
# print_tree(larger_order_tree(orders))

# # [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]

def larger_order_tree(order_tree, order):
    if not order_tree:
        return None

    queue = deque([order_tree])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

        if node == order:
            return queue[0] if i < level_size - 1 else None 
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

# Problem 4 usage:
"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)

"""
Eclair
None
"""