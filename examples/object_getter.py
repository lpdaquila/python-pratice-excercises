
# use it to dont break the client codes
# habilits setter
# client code is the 'code' that uses your code 
class Pen:
    def __init__(self, color):
        # private protected public
        self.color = color 
        
    @property # this is a 'method' that acts like an 'attribute'
    # This is a getter accessed by '<obj name>.color' and returns the code above
    def color(self):
        return self._color
    
    @color.setter
    # This is a setter it sets a new value to a private attribute 
    def color(self, value):
        # # You can protect and restric some values given to the setter
        # if value == 'Pink'
        #     raise ValueError('Pink is not accepted.')
        self._color = value
    
    @property
    def pen_protection(self):
        return 'nothing'
    
    
pen = Pen('Blue')
pen.color = 'Pink'
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)

# class Pen:
#     def __init__(self, color):
#         # private protected public
#         self.color = color
        
#     def get_color(self): # it protects your attribute
#         return self.color