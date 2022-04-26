class BasicException(Exception):
    
    def __init__(self, message, HTTPCode):
        self.message = message
        self.HTTPCode = HTTPCode