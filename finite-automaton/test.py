from dfa import *

# VERY UGLY INITIAL

alphabet = {"a", "b", "c"}
m = DFAutomaton(alphabet)
qinit = State("q0", False, True)
q1 = State("q1")
q2 = State("q2")
qfinal = State("q3", True)
qinit.addEdge("a", q1)
qinit.addEdge("b", qinit)
q1.addEdge("a", q2)
q1.addEdge("b", qinit)
q2.addEdge("a", qfinal)

# node outside alphabet
# q3 = State()
# q2.addEdge("d", q3)

m.addNode(qinit)
m.addNode(q1)
m.addNode(q2)
# m.addNode(q3)
m.addNode(qfinal)

m.printAutomaton()

print("yeet")
print(accepts("babaaa", m))
print(accepts("babaab", m))
print(accepts("a", m))
print(accepts("aaaaaaaaaaa", m))
print(accepts("aaa", m))