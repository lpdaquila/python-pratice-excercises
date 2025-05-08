import copy
from data import products
# copy, sorted, Products.sort
# Exercícios
# Aumente os preços dos Products a seguir em 10%
# Gere novos_Products por deep copy (cópia profunda)
def original():
    print(*products, sep='\n')

# new_products = copy.deepcopy(products)

new_products = [
    {**product, 'price': round(product['price'] * 1.1, 2)}
    for product in copy.deepcopy(products)
]

# Ordene os Products por name decrescente (do maior para menor)
# Gere Products_ordenados_por_name por deep copy (cópia profunda)

sorted_products = sorted(
    copy.deepcopy(products),
    key=lambda product: product['name']
)

original()
print()
print(*new_products, sep='\n')
print()
print(*sorted_products, sep='\n')

# Ordene os Products por price crescente (do menor para maior)
# Gere Products_ordenados_por_price por deep copy (cópia profunda)