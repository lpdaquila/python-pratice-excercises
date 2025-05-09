from log import LogPrintMixin, LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._ison = False
        
    def turn_on(self):
        if not self._ison:
            self._ison = True
            
    def turn_off(self):
        if self._ison:
            self._ison = False
            
class Smartphone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
        
        if self._ison:
            msg = f'{self._name} is on!'
            self.log_success(msg)
        
    def turn_off(self):
        super().turn_off()
        
        if not self._ison:
            msg = f'{self._name} is off!'
            self.log_error(msg)
            