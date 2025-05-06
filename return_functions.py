
x, y, *_ = 1, 2, 3, 4, 5
numeros = 1, 2, 3, 4, 5, 78, 3 

def soma(*args):
    """
    Função que soma dois ou mais números.
    
    :param args: Números a serem somados.
    :return: Soma dos números.
    """
    total = 0
    for num in args:
        print(total, num)
        total += num
        print(total)
    return total
    # return sum(args)

soma(x, y)
soma(1, 2, 3, 4, 5)
exit()

# return 

def soma(x, y, z=None):
    """
    Função que soma dois ou três números.
    
    :param x: Primeiro número.
    :param y: Segundo número.
    :param z: Terceiro número (opcional).
    :return: Soma dos números.
    """
    if z is not None:
        return x + y + z
    else:
        return x + y