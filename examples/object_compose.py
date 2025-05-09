# class compose

class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []
        
    def insert_address(self, street, num):
        self.addresses.append(Address(street, num)) # This need the class "Adress" to work
        
    def list_address(self):
        for address in self.addresses:
            print(address.street, address.num)
        
class Address:
    def __init__(self, street, num):
        self.street = street
        self.num = num
        
cli1 = Client('Mary')
cli1.insert_address('Rosebush St.', 64)
cli1.insert_address('Spruce St.', 144)
cli1.list_address()