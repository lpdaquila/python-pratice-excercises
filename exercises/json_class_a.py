import json
FILE_PATH = 'test.json'

class Person:
    year = 2025 # class attribute
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    @staticmethod # just like a function but inside the class
    def function_inside_class(*args, **kwargs): 
        """It dont't recieve 'self' or 'cls' is just
        a function inside the class (or instance)
        It can't access other methods or attributes
        inside the class
        
        It's like you have a function outside the class
        but if you want to use this for some reason
        you can 'protect' this method with class itself
        """
        print(args, kwargs)
        
    @classmethod # factory / constructor
    def class_method(cls): # Recives the Class, not 'self'
        """This can access all inside the class"""
        print('Hello')
        
    @classmethod
    def create_person_with_50_years(cls, name):
        return cls(name, 50) # Returns Class constructor with 
                             # This params
    @classmethod
    def create_no_named_person(cls, age):
        return cls('Unamed', age) 
        
p1 = Person.create_no_named_person(12)
p1.function_inside_class(1, 2, 3, note='any')
# p1 = Person('John', 33)
# p2 = Person.create_person_with_50_years('Abraham')
# print(p2.name, p2.age)
# print(Person.year)
# Person.class_method()


# p2 = Person('Helena', 25)
# p3 = Person('Heather', 13)

# db = [vars(p1), vars(p2), vars(p3)]

# def dump_json():
#     with open(FILE_PATH, 'w') as file:
#         json.dump(db, file, ensure_ascii=False, indent=2)
        
