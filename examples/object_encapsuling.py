# public private protected
# In python doesn't have access modifiers
# Conventions in Python
# (no underscore) = public
# Can be accessed in any place
# _ (one underscore) = protected
# it CAN'T be used out of class and your subclasses
# __(two underscores) = private
# "name mangling" MUST only be used in class it was declared

class Foo:
    def __init__(self):
        self.public = 'this is public'
        self._protected = 'this is protected'
        self.__private = 'this is private'
        
    def public_method(self):
        return 'public method'
    
    def _method_protected(self):
        return 'protected method'
    
    def __method_private(self):
        return 'private method'
    
f = Foo()
# print(f.public)
# print(f.public_method())
# f.__private # error it returns a "name mangling" naming this attr with _<class name>_<attr or method name>
# f.__method_private # error

# It will work but you must not use 
# print(f._protected)
# print(f._method_protected())