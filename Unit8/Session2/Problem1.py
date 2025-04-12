from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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


#Problem 1
# class TreeNode:
#     def __init__(self, val, key, left=None, right=None):
#         self.key = key      # Plant price
#         self.val = val      # Plant name
#         self.left = left
#         self.right = right


# def sort_plants(collection):
#     def inorder_traversal(node, result):
#         if node is not None:
#             inorder_traversal(node.left,result)
#             result.append((node.key,node.val))
#             inorder_traversal(node.right,result)

#     result = []
#     inorder_traversal(collection,result)
#     return result

# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

#Problem 2
def find_flower(inventory, name):
    if inventory is None:  # Base case: empty node
        return False

    print(f"Checking: {inventory.val}")

    if name == inventory.val:  # Match found
        return True
    elif name < inventory.val:  # Search left subtree
        return find_flower(inventory.left, name)
    else:  # Search right subtree
        return find_flower(inventory.right, name)
    

# """
#          Rose
#         /    \
#       Lily   Tulip
#      /  \       \
#   Daisy  Lilac  Violet
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
# garden = build_tree(values)
# print_tree(garden)
# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 


#Problem 3 
def add_plant(collection, name):
    if collection is None:
        # If the tree/subtree is empty, create a new node for the plant
        return TreeNode(name)

    if name < collection.val:
        # Insert into the left subtree
        collection.left = add_plant(collection.left, name)
    else:
        # Insert into the right subtree (if a duplicate, add to the right)
        collection.right = add_plant(collection.right, name)

    return collection

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))

#Problem 4
def remove_plant(collection, name):
    if collection is None:
        return None

    if name < collection.val:
        collection.left = remove_plant(collection.left,name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right,name)
    else:
        #No children
        if collection.left is None and collection.right is None:
            return None
        
        #One Child:
        if collection.left is None:
            return collection.right
        elif collection.right is None:
            return collection.left
        
        #Two childen
        predecessor = find_max(collection.left)
        collection.val = predecessor.val
        collection.left = remove_plant(collection.left,predecessor.val)
    return collection

def find_max(node):
    while node.right is not None:
        node = node.right
    return node

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(remove_plant(collection, "Pilea"))

