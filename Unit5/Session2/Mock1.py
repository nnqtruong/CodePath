def reverse_list(lst):
    ans = []
    n=len(lst)
    for i in range(n):
        ans.append(lst[n-i-1])
    return ans

lst1 = [1,3,5,7,9]
lst2 = [2,4]
lst3 = []
print(reverse_list(lst1))
print(reverse_list(lst2))
print(reverse_list(lst3))