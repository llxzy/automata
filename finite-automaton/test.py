from dfa import *
import pytest
import copy


ALPHABET = {"a", "b", "c"}
DFA = DFAutomaton(ALPHABET)
Q_INIT = State("q0", False, True)
DFA.addState(Q_INIT)
Q1 = State("q1")
Q2 = State("q2")
Q_FINAL = State("q3", True)
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
    q = State("q", True, True)
    s = State("s", True)
    q.addEdge("g", s)
    with pytest.raises(exceptions.AlphabetError):
        m.addState(q)
        

def test_remove_unreachable():
    dfa = copy.deepcopy(DFA)
    redundantState = State("qred", True)
    dfa.addState(redundantState)
    
    dfa = removeUnreachable(dfa)
    assert not redundantState in dfa.states

