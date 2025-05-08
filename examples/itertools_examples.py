# Combinations, Permutations and Product - Itertools
# Combinations = Order doesn't matter 
# Permutation = Order matters
# Product = Order matters and repeat unique values
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    
people = [
    'John', 'Mary', 'Luke', 'Heather'
]
shirts = [
    ['black', 'white'],
    ['p', 'm', 'g'],
    ['male', 'female'],
]

print_iter(combinations(people, 2))
print()
print_iter(permutations(people, 2))
print()
print_iter(product(*shirts))
