# Decorators 

def summ(x, y):
    return x + y

def multiply(x, y):
    return x * y

def execute(function, x):
    def internn(y):
        return function(x, y)    
    return internn

sum_with_five = execute(summ, 5)
multiply_by_ten = execute(multiply, 10)