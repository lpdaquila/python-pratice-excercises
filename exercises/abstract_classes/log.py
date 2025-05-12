from pathlib import Path
from abc import ABC, abstractmethod
# Abstraction
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ... # abstract class cannot be instanced directely
        # raise NotImplementedError('Method log not implemented')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
        
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg: str): # it must be implemented in subclasses only
        formated_msg = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as file:
            file.write(formated_msg)
            file.write('\n')
        
class LogPrintMixin(Log):
    def _log(self, msg: str):
        print(f'{msg} ({self.__class__.__name__})')
        
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('test')
    lp.log_success('yepsy')
    lf = LogFileMixin()
    lf.log_error('oh no!')
    lf.log_success('yepsy!')
    