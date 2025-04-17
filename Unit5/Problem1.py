class Villager:
    def __init__(self, name, species, personality, catchphrase,neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        self.personality = personality
        self.neighbor = neighbor
        
    def add_item(self,item_name):
        valid_item = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_item:
            self.furniture.append(item_name)

def of_personality_type(townies, personality_type):
    " townies: list of villagers"
    names = []
    for villager in townies:
        if villager.personality == personality_type:
            names.append(villager.name)
    return names

def message_received(start_villager, target_villager):
    current = start_villager
    visited = set()
    
    while current is not None:
        if current == target_villager:
            return True
        if current in visited:
            return False
        visited.add(current)
        current = current.neighbor
    return False

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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Problem 1
# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)

# Problem 2
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# Problem 3
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Problem 4
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# Problem 5
print_linked_list(kk_slider)