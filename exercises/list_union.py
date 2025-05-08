# List Union
# Create a zipper function
# This function must join two lists in order
# Use all values of minor list 
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lst1, lst2): # This is how zip function works
    interval = min(len(lst1), len(lst2))
    return [
        (lst1[i], lst2[i]) for i in range(interval)
    ]
    
print(zipper(l1, l2))
# it equals to 
z = zip(l1, l2) # returns an object
print(list(z)) # you can list this object
zl = zip_longest(l1, l2) # uses the major list
print(list(zl))