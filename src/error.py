class AlphabetError(Exception):
    def __init__(self,  character, message):
        self.message = message
        self.character = character
        super().__init__(message)
    
    
    def __str__(self):
        return f'{self.character} -> Error: {self.message}'


class StateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        