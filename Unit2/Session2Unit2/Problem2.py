def is_authentic_collection(art_pieces):
    from collections import Counter
    art_counter = Counter(art_pieces)
    max_key = max(art_counter, key=int)
    if art_counter[max_key] !=2:
        return False 
    art_counter[max_key] = 1 
    for i in art_counter.values():
        if i != 1:
            return False
    return len(set(art_pieces)) != max_key +1 

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))