import account
import persons

class Bank:
    def __init__(
        self,
        agencies: list[int] | None = None, 
        clients: list[persons.Person] | None = None,
        accounts: list[account.Account] | None = None,
    ) -> None:
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []
        
    def _check_agency(self, account) -> bool:
        if not account.agency in self.agencies:
            return False
        return True
        
    def _check_client(self, client) -> bool:
        if not client in self.clients:
            return False
        return True
        
    def _check_account(self, account) -> bool:
        if not account in self.accounts:
            return False
        return True
    
    def _if_acc_is_own_client(self, client, account) -> bool:
        if not account is client.account:
            return False
        return True
        
    def auth(self, client: persons.Person, account: account.Account):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._if_acc_is_own_client(client, account)
            
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.accounts!r}, {self.clients!r})'
        return f'{class_name} {attrs}'
            
if __name__ == '__main__':
    c1 = persons.Client('Mary', 30)
    ci1 = account.InvestAccount(111, 222, 0)
    c1.account = ci1
    
    c2 = persons.Client('Lucas', 27)
    cc2 = account.CurrentAccount(112, 227, 0, 100)
    c2.account = cc2
    
    bank = Bank()
    bank.clients.extend([c1, c2])
    bank.accounts.extend([ci1, cc2])
    bank.agencies.extend([111, 222, 112])
    if bank.auth(c2, cc2):
        cc2.deposit(10.50)
        cc2.withdraw(120)