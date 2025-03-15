def build_skyscrapers(floors):
    count = 1 
    for i in range(1,len(floors)):
        if floors[i] < floors[i-1]:
            count = count + 1
    return count


print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 