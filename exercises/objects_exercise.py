
class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._maker = None
        
    @property
    def motor(self):
        return self._motor
    
    @property
    def maker(self):
        return self._maker
    
    @motor.setter
    def motor(self, value):
        self._motor = value
        
    @maker.setter
    def maker(self, value):
        self._maker = value
        
class Motor:
    def __init__(self, name):
        self.name = name
        
class Maker:
    def __init__(self, name):
        self.name = name
        

beetle = Car('Beetle')
volkswagen = Maker('Volkswagen')
motor_1_0 = Motor('1.0')
beetle.maker = volkswagen
beetle.motor = motor_1_0
print(beetle.name, beetle.maker.name, beetle.motor.name)

uno = Car('Uno')
fiat = Maker('Fiat')
motor_1_0 = Motor('1.0')
uno.maker = fiat
uno.motor = motor_1_0
print(uno.name, uno.maker.name, uno.motor.name)

focus = Car('Focus')
ford = Maker('Ford')
motor_2_0 = Motor('2.0')
focus.maker = ford
focus.motor = motor_2_0
print(focus.name, focus.maker.name, focus.motor.name)
