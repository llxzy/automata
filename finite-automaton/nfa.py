import typing

class NoInitStateError(Exception):
    def __init__(self):
        self.message = "No initial state found."
        super().__init__(self.message)

    def __str__(self):
        return self.message



class State:
    def __init__(self):
        self.label = ""
        self.edges = dict()
        self.initial = False
        self.accepting = False

    def __str__(self):
        return self.label

    def setInitial(self, initial: bool):
        self.initial = initial

    def getInitial(self) -> bool:
        return self.initial

    def setAccepting(self, accepting: bool):
        self.accepting = accepting

    def getAccepting(self) -> bool:
        return self.accepting

    def addEdge(self, symbol: str, state):
        symbolTo = set()
        if symbol in self.edges.keys():
            symbolTo = self.edges[symbol]
        symbolTo.add(state)
        self.edges[symbol] = symbolTo


class NFAutomaton:
    def __init__(self):
        self.states = []

    def addState(self, state: State):
        self.states.append(state)

    def isValid(self):
        return len(list(filter(State.getInitial, self.states))) == 1

    def accepts(self, nfaInput: str) -> bool:
        if not self.isValid():
            return False # maybe an error would be better?

        initial = list(filter(State.getInitial, self.states))
        if not initial:
            raise NoInitStateError
        currentInput = nfaInput
        currentStates = set()
        currentStates.add(initial[0])
        
        while currentInput:
            symbol = currentInput[0]
            currentInput = currentInput[1:]
            newStates = set()
            for state in currentStates:
                try:
                    newStates = newStates.union(state.edges[symbol])
                except KeyError:
                    continue
            if not newStates and currentInput:
                return False
            currentStates = newStates

        return True in list(map(State.getAccepting, currentStates))


n = NFAutomaton()
q0 = State()
q1 = State()
q2 = State()
q3 = State()

q0.addEdge("a", q0)
q0.addEdge("b", q1)
q0.addEdge("b", q2)
q2.addEdge("a", q3)
q3.setAccepting(True)
q0.setInitial(True)

n.addState(q0)
n.addState(q1)
n.addState(q2)
n.addState(q3)

print(n.accepts("ab"))