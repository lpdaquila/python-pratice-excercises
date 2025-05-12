# To get data:
# member = Class(value), Class['key']
# key = Class.key.name
# value = Class.key.value
import enum

Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])

def move(direction: Directions):
    if not isinstance(direction, Directions): # type: ignore
        raise ValueError('Direction not found.')
    
    print(f'Moving {direction}')
    
move(Directions.LEFT)
move(Directions.RIGHT)
# move('up')
