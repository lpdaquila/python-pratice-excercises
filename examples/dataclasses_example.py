from dataclasses import dataclass, field

@dataclass
class Person:
    name: str = 'missing'
    age: int = 30
    _cpf: int = field(repr=False, default_factory=int)
    address: list[str] = field(default_factory=list)
    
    @property
    def cpf(self):
        return self._cpf
# DevLuke
if __name__ == '__main__':
    p1 = Person()
    p1.name = 'Luke'
    # p1.cpf = 32212321 # error
    print(p1)