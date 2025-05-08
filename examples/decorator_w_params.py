
def decorator(func):
    print('decorator 1')
    def nested(*args, **kwargs):
        print('nested')
        res = func(*args, **kwargs)
        return res
    return nested