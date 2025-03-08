def is_balanced(code):
    a = dict()

    hashmap = {}
    for c in code:
        hashmap(c) = 1 + hashmap.get(c,0)
    a = set(hashmap.values())
    if len(a) !=2:
        return False
    else if abs(a[1]-a[0]) = 1:
        return True
    else:
        return False

    

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 