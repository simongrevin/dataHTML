class User:

    def __init__(self,login,email,password):
        self.login = login
        self.email = email
        self.password = password
        self.history = []

    def serialize(self):
        return {
    		'login': self.login,
    		'email': self.email,
    		'password': self.password,
            'history': self.history
    	}
