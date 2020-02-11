import typing
import exceptions
import copy

# TODO
# importing automata setup from a json/other file
# error if automaton doesnt contain initial states
# REALLY LATE -> add GUI for automata creation -> output to graphviz
# changing which state is initial - probably will need a rework of how init state is stored

"""
----------------------------------------------
"""

class State:
    def __init__(self, 
                 accepting: bool = False, 
                 initial: bool = False):
        self.label = ""
        self.edges = dict()
        self.accepting = accepting
        self.initial = initial

    def addEdge(self, symbol: str, st):
        # replace with automata addEdge
        if symbol in self.edges.keys():
            print("WARNING: Overwriting existing edge")
        self.edges[symbol] = st

    def printState(self):
        return self.label


class DFAutomaton:
    def __init__(self, alphabet = set()):
        self.states = []
        self.initState = None
        self.accStates = set()
        self.alphabet = alphabet
        self.stateCount = 0

    def addState(self, st: State):
        if not self.alphabet.issuperset(st.edges.keys()):
            """
            Checks whether the automata alphabet is a superset of the keys of the state.
            If keys contain an entry that is outside the alphabet, raises an error.
            """
            raise exceptions.AlphabetError

        if st.initial and self.initState:
            raise exceptions.PresentInitStateError
        
        st.label = "q" + str(self.stateCount)
        self.states.append(st)
        self.stateCount += 1

        if st.accepting:
            self.accStates.add(st)
        if st.initial:
            self.initState = st


    def loadFromJson(self, filename: str):
        # json format is specified in TODO add
        # with open(filename, "r") as fnm:
        pass

    def printAutomaton(self):
        print("DFA")
        print("---")
        print("STATES (Q): ", set([state.label for state in self.states]))
        print("ALPHABET (Sigma): ", self.alphabet)
        print("TRANSITION FUNCION (delta): Q x Sigma -> Q")
        print("INITIAL STATE: ", self.initState.label)
        print("ACCEPTING STATES: ", set(map(lambda state: state.printState(), self.accStates)))
        print()


"""
----------------------------------------------
"""

def accepts(word: str, dfa: DFAutomaton) -> bool:
    if dfa.initState:
        currentState = dfa.initState
    else:
        raise exceptions.NoInitStateError

    currentWord = word
    while currentWord:
        symbol = currentWord[0]
        try:
            currentState = currentState.edges[symbol]
            currentWord = currentWord[1:]
        except KeyError:
            return False
    return currentState.accepting


def makeTotal(dfa: DFAutomaton) -> DFAutomaton:
    totalDFA = copy.deepcopy(dfa)

    p = State()
    for state in totalDFA.states:
        for symbol in totalDFA.alphabet:
            if symbol not in state.edges.keys():
                state.addEdge(symbol, p)

    for symbol in dfa.alphabet:
        # adds looping edges to P
        p.addEdge(symbol, p)
    
    totalDFA.addState(p)
    return totalDFA


def removeUnreachable(dfa: DFAutomaton) -> DFAutomaton:
    currentReachable = set()
    newReachable = set()
    currentReachable.add(dfa.initState)
    while True:
        for state in currentReachable:
            edgesTo = set(map(lambda x: state.edges[x], state.edges.keys()))
            currentReachable = currentReachable.union(edgesTo)
        if newReachable == currentReachable:
            break
        else:
            newReachable = currentReachable

    newDFA = DFAutomaton(dfa.alphabet)
    newDFA.initState = dfa.initState
    newDFA.states = list(currentReachable)
    newDFA.accStates = set(filter(lambda x: x.accepting, currentReachable))
    return newDFA
            

def minimize(dfa: DFAutomaton) -> DFAutomaton:
    """
    Creates a minimal state machine
    """
    pass
