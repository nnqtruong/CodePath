def find_duplicate_chests(chests):
    a = set()
    b = []
    for num in chests:
        if num in a:
            b.append(num)    
        a.add(num)
    return b 


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))