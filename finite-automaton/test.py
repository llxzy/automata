from dfa import *
import pytest
import copy


ALPHABET = {"a", "b", "c"}
DFA = DFAutomaton(ALPHABET)
Q_INIT = State(False, True)
DFA.addState(Q_INIT)
Q1 = State()
Q2 = State()
Q_FINAL = State(True)
Q_INIT.addEdge("a", Q1)
Q_INIT.addEdge("b", Q_INIT)
Q1.addEdge("a", Q2)
Q1.addEdge("b", Q_INIT)
Q2.addEdge("a", Q_FINAL)
DFA.addState(Q1)
DFA.addState(Q2)
DFA.addState(Q_FINAL)


def test_accepting():
    assert accepts("babaaa", DFA)
    assert accepts("aaa", DFA)
    assert accepts("abbbbbbbbabaaa", DFA)


def test_not_accepting():
    assert not accepts("babaa", DFA)
    assert not accepts("a", DFA)
    assert not accepts("aaabaaaa", DFA)


def test_state_not_in_alphabet():
    m = DFAutomaton(ALPHABET)
    q = State(True, True)
    s = State(True)
    q.addEdge("g", s)
    with pytest.raises(exceptions.AlphabetError):
        m.addState(q)
        

def test_remove_unreachable():
    dfa = copy.deepcopy(DFA)
    redundantState = State(True)
    dfa.addState(redundantState)

    dfa = removeUnreachable(dfa)
    assert not redundantState in dfa.states

