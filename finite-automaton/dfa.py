import typing

#TODO
# importing automata setup from a json/other file
# add accepted alphabet only
# add printing out the automaton
# python typing for own classess

"""
----------------------------------------------
"""

class Node:
    def __init__(self, accepting = False, initial = False):
        self.edges = dict()
        self.accepting = accepting
        self.initial = initial

    def addEdge(self, letter: str, nd):
        if letter in self.edges.keys():
            print("WARNING: Overwriting existing edge")
        self.edges[letter] = nd


class DFAutomaton:
    def __init__(self):
        self.nodes = []

    def addNode(self, nd):
        self.nodes.append(nd)

    def loadFromJson(self, filename: str):
        # json format is specified in TODO add
        # with open(filename, "r") as fnm:
        pass

    def printAutomaton(self):
        pass


"""
----------------------------------------------
"""

def accepts(word: str, initialNode) -> bool:
    currentNode = initialNode
    currentWord = word
    while currentWord:
        letter = currentWord[0]
        try:
            currentNode = currentNode.edges[letter]
            currentWord = currentWord[1:]
        except KeyError:
            return False
    return currentNode.accepting


## VERY UGLY INITIAL TESTS

m = DFAutomaton()
qinit = Node(False, True)
q1 = Node()
q2 = Node()
qfinal = Node(True)
qinit.addEdge("a", q1)
qinit.addEdge("b", qinit)
q1.addEdge("a", q2)
q1.addEdge("b", qinit)
q2.addEdge("a", qfinal)

print(accepts("babaaa", qinit))
print(accepts("babaab", qinit))
print(accepts("a", qinit))
print(accepts("aaaaaaaaaaa", qinit))
print(accepts("aaa", qinit))
