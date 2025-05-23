from abc import ABC, abstractmethod

class AbstractFoo(ABC): # it's like a thought in your mind, you can't use it directely
    def __init__(self, name):
        self._name = None
        self.name = name
        
    @property
    def name(self): 
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name):
        ...
    
class Foo(AbstractFoo): # 
    def __init__(self, name):
        super().__init__(name)
        # print("I'm useless")
        
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name
    
foo = Foo('Name')
print(foo.name)