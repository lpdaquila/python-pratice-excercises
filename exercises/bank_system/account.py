# Create a bank system with clients, accounts an a bank. The role is the client
# have a account (invest or current) an it can withdraw, deposit. Current accounts
# have an extra limit.;
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance
        
    @abstractmethod
    def withdraw(self, value: float) -> float: pass
        
    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'(DEPOSIT {value:.2f})')
        return self.balance
        
    def details(self, msg: str = '') -> None:
        print(f'Your balance is {self.balance:.2f} | {msg}')
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance!r})'
        return f'{class_name} {attrs}'
        
class InvestAccount(Account):
    def withdraw(self, value: float) -> float:
        new_value = self.balance - value
        
        if new_value >= 0:
            self.balance -= value
            self.details(f'(WITHDRAW {value})')
            return self.balance
        print('Cannot withdraw the value.')
        self.details(f'(WITHDRAW DENIED {value})')
        return self.balance
        
class CurrentAccount(Account):
    def __init__(self, 
                 agency: int, 
                 account: int, 
                 balance: float = 0, 
                 limit: float = 0
        ):
        super().__init__(agency, account, balance)
        self.limit = limit
        
    def withdraw(self, value: float) -> float:
        new_value = self.balance - value
        max_limit = -self.limit
        
        if new_value >= max_limit:
            self.balance -= value
            self.details(f'(WITHDRAW {value})')
            return self.balance
        
        print('Cannot withdraw the value.')
        print(f'Your limit is: {self.limit:.2f}')
        self.details(f'(WITHDRAW DENIED {value})')
        return self.balance
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance!r}, {self.limit!r})'
        return f'{class_name} {attrs}'
        
if __name__ == '__main__':
    # ci1 = InvestAccount(111, 222, 0)
    # ci1.deposit(1)
    # ci1.withdraw(1)
    # ci1.withdraw(1)
    
    ci1 = CurrentAccount(111, 222, 0, 100)
    ci1.deposit(1)
    ci1.withdraw(1)
    ci1.withdraw(1)
    
        