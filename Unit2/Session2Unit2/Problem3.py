def organize_exhibition(collection):
    from collections import Counter
    art_collection = Counter(collection)
    gallery_wall = []
    
    for i in range(max(art_collection.values())):
        new_array =  [k for k, v in art_collection.items() if v > i]
        gallery_wall.append(new_array)
    return gallery_wall




collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))