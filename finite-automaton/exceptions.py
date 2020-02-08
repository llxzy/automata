# TODO unite these into one exception class

class AlphabetError(Exception):
    def __init__(self):
        self.message = "Transition symbol not in alphabet."
        super().__init__(self.message)
    
    def __str__(self):
        return self.message

class NodeLabelError(Exception):
    def __init__(self):
        self.message = "Node with that label already present."
        super().__init__(self.message)

    def __str__(self):
        return self.message