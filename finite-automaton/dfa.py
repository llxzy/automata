import typing
import exceptions

#TODO
# importing automata setup from a json/other file
# error if automaton doesnt contain accepting/initial states
# add accepted alphabet only
# add printing out the automaton
# python typing for own classess
# REALLY LATE -> add GUI for automata creation -> output to graphviz?

"""
----------------------------------------------
"""

class State:
    def __init__(self, label = "", accepting = False, initial = False):
        self.label = label
        self.edges = dict()
        self.accepting = accepting
        self.initial = initial

    def addEdge(self, symbol: str, st):
        if symbol in self.edges.keys():
            print("WARNING: Overwriting existing edge")
        self.edges[symbol] = st

    def printState(self):
        return self.label

class DFAutomaton:
    def __init__(self, alphabet = set()):
        self.states = []
        self.initNode = None
        self.accNodes = set()
        self.alphabet = alphabet

    def addNode(self, st):
        if st.label in [state.label for state in self.states]:
            """
            Checks whether the automata already contains a state with the label.
            """
            raise exceptions.NodeLabelError

        if not self.alphabet.issuperset(st.edges.keys()):
            """
            Checks whether the automata alphabet is a superset of the keys of the state.
            If keys contain an entry that is outside the alphabet, raises an error.
            """
            raise exceptions.AlphabetError

        if st.accepting:
            self.accNodes.add(st)

        if st.initial:
            if self.initNode:
                print("ERROR: automaton already contains an initial state")
            else:
                self.initNode = st
                self.states.append(st)
        else:
            self.states.append(st)

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
        print("INITIAL STATE: ", self.initNode.label)
        print("ACCEPTING STATES: ", set(map(lambda state: state.printState(), self.accNodes)))
        print()


"""
----------------------------------------------
"""

def accepts(word: str, dfa) -> bool:
    currentNode = dfa.initNode
    currentWord = word
    while currentWord:
        symbol = currentWord[0]
        try:
            currentNode = currentNode.edges[symbol]
            currentWord = currentWord[1:]
        except KeyError:
            return False
    return currentNode.accepting
