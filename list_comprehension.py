from pprint import pprint

products = [
    {'name': 'p1', 'price': 30},
    {'name': 'p2', 'price': 36},
    {'name': 'p3', 'price': 14},
    {'name': 'p4', 'price': 20},
    {'name': 'p5', 'price': 5},
]

# map
new_mapped_products = [
    {**product, 'price': product['price'] * 1.1} 
    if product['price'] >= 20 else {**product} 
    for product in products
]

print('Mapped:')
print(*new_mapped_products, sep='\n') # unpacked
print()

# filter 
new_filtered_products = [
    {**product, 'price': product['price'] * 1.1}
    if product['price'] >= 20 else {**product}
    for product in products 
    if product['price'] >= 20
]

print('Filtered w/ pprint')
pprint(new_filtered_products, width=40) # packed
print()

# # double 'for'
# lst = [
#     (x, y)
#     for x in range(3)
#     for y in range(5)
# ]

# pprint(lst)
