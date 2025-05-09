import json
from json_class_a import FILE_PATH, Person, dump_json

dump_json()

with open(FILE_PATH, 'r') as file:
    data = json.load(file)
    
    p1 = Person(**data[0])
    p2 = Person(**data[1])
    p3 = Person(**data[2])

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)
