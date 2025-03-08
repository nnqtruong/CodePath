def total_treasures(treasure_map) -> int:
    '''
    U: Understand, sum up all values in dictionary
    P: Plannning: Initializar variable to keep track of total amount
    I:
    '''
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 