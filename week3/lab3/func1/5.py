from itertools import permutations
def permutation(strrr):
    return [' '.join(p) for p in permutations(strrr)]

print(permutation('str'))