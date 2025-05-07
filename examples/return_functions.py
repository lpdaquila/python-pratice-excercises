
x, y, *_ = 1, 2, 3, 4, 5 # desempacotamento

# def par_impar(num):
#     return 'par' if num % 2 == 0 else 'impar'
def par_impar(num):
    multiplo_de_dois = num % 2 == 0
    if multiplo_de_dois:
        return '%d eh par' % num
    return '%d eh impar' % num

pr = par_impar(2)
im = par_impar(3)
print(pr, im)

exit()

def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total

multi = multiplica(1, 2, 3, 4, 5)
print(multi)

exit()

def soma(*args):
    total = 0
    for num in args:
        print(total, num)
        total += num
        print(total)
    return total
    # return sum(args)

soma(x, y)
soma(1, 2, 3, 4, 5)

# # return 

# def soma(x, y, z=None):
#     if z is not None:
#         return x + y + z
#     else:
#         return x + y