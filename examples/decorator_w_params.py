
# def decorator(func): # It works like a function factory
#     print('decorator 1')
#     def nested(*args, **kwargs):
#         print('nested')
#         res = func(*args, **kwargs)
#         return res
#     return nested

# def decorator_factory(a, b, c):
#     def decorator(func):
#         print('decorator 1')
#         def nested(*args, **kwargs):
#             print('nested')
#             res = func(*args, **kwargs)
#             return res
#         return nested
#     return decorator

# Decorator orders
def decor_params(name):
    def decorator(func):
        print('Decorator: ', name)
        
        def new_func(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return new_func
    return decorator

# @decor_params(name='third') 
@decor_params(name='second')
@decor_params(name='first')
def summ(x, y):
    return x + y

ten_plus_five = summ(10, 5)
print(ten_plus_five)
