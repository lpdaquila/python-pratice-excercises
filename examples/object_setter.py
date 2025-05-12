
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        # self = instance method
        
    def set_user(self, user):   
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
    @classmethod # constructor
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG', msg)
        

        
    
        