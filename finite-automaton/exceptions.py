# TODO unite these into one exception class

class AlphabetError(Exception):
    def __init__(self):
        self.message = "Transition symbol not in alphabet."
        super().__init__(self.message)
    
    def __str__(self):
        return self.message
        
class NoInitStateError(Exception):
    def __init__(self):
        self.message = "DFA has no initial state."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class PresentInitStateError(Exception):
    def __init__(self):
        self.message = "Initial state already present in the DFA."
        super().__init__(self.message)

    def __str__(self):
        return self.message