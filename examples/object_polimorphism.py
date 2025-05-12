
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg) -> None:
        self.message = msg
        
    @abstractmethod
    def send(self) -> bool: ... # <- this is the method signature
    
class EmailNotification(Notification):
    def send(self) -> bool: # <- all subclasses must have the same method signature of abstract class
        print('Email sent - ', self.message)
        return True
    
def notify(notification: Notification):
    if notification.send:
        pass