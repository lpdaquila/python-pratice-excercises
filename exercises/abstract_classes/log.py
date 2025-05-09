from pathlib import Path
# Abstraction
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Method log not implemented')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
        
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        formated_msg = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as file:
            file.write(formated_msg)
            file.write('\n')
        
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
        
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('test')
    lp.log_success('yepsy')
    lf = LogFileMixin()
    lf.log_error('oh no!')
    lf.log_success('yepsy!')
    