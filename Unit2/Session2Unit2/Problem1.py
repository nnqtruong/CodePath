def find_balanced_subsequence(art_pieces):
    from collections import Counter     
    art_counter = Counter(art_pieces)

    for i in art_counter.key():
        if i - 1 in art_counter:
            answer = max(art_counter[i]+art_counter[i-1], answer)
        if i + 1 in art_counter:
            answer = max(art_counter[i]+art_counter[i+1], answer)
    return answer



art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))