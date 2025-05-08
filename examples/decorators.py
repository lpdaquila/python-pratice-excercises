# Decorators 

# def summ(x, y):
#     return x + y

# def multiply(x, y):
#     return x * y

# def execute(function, x): # Decorator functions 
#     # can put something before
#     def inner(y): # This is how decorators works
#         return function(x, y)    
#     # and after this 'decorator' function
#     return inner

# sum_with_five = execute(summ, 5) # Using directely decorated function
# multiply_by_ten = execute(multiply, 10)

# Decorator = Add / Remove / Restrict / Alter 
def execute(func): # This is a decorator function
    def inner(*args, **kwargs): # (closure)
        # It 'decorates' the function
        print('I will decorate you')
        for arg in args:
            e_string(arg) 
        result = func(*args, **kwargs)
        print('Your result is: ', result)
        print('You are decorated')
        return result
        # Decorated function returns 
    return inner 

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param must be "str"')

@execute # Using @syntax_sugar to call this decorator
def invert_string(string):
    return string[::-1]

inverted = invert_string('123')
print(inverted)


