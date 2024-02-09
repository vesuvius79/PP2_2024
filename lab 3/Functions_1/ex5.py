from itertools import permutations

def permutation(string):
    return (''.join(x) for x in permutations(string))

print(*list(permutation(input())))