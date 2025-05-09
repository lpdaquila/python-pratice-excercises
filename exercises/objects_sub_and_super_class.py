
class Person:
    def __init__(self, fname, lname):
        self.name = fname
        self.last_name = lname
        
    def show_class_name(self):
        print(self.name, self.last_name, self.__class__.__name__)
        
class Client(Person):
    def show_class_name(self):
        return super().show_class_name() # it calls the method from super instance
    
class Studant(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    ...
    
c1 = Client('Lucas', 'Daquila')
c1.show_class_name()

a1 = Studant('Heather', 'Smith')
a1.show_class_name()