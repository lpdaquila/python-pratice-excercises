
class Car:
    def __init__(self, name):
        self.name = name
        
    def accelerate(self):
        print('%s is running...' % self.name)
        
beetle = Car('Beetle')
beetle.accelerate()

