import pytest
from src import dfa
from src import state
from src import error

def test_set_alphabet():
    d = dfa.DFA()
    alphabet = {'a', 'b'}
    d.set_alphabet(alphabet)
    assert(d.alphabet == {'a', 'b'})


def test_add_state():
    d = dfa.DFA()
    print([s.label for s in d.states])
    assert(len(d.states) == 1)
    s = state.State('s2', True, False)
    d.add_state(s)
    assert(len(d.states) == 2)
    assert(s in d.states)


def test_add_state_exc():
    d = dfa.DFA()
    s = state.State('s1', True, False)
    s_ninit = state.State('si', True, True)
    with pytest.raises(error.StateError):
        d.add_state(s)
    with pytest.raises(error.StateError):
        d.add_state(s_ninit)


def test_add_edge():
    d = dfa.DFA()
    s = state.State('s2', True, False)
    d.add_state(s)
    d.set_alphabet({'a'})
    d.add_edge(d.initial_state, s, 'a')
    assert(len(d.initial_state.edges) == 1)


def test_add_edge_exc():
    d = dfa.DFA()
    s = state.State('s2', True, False)
    d.set_alphabet({'a'})
    with pytest.raises(error.StateError):
        d.add_edge(d.initial_state, s, 'a')
    
    d.add_state(s)
    with pytest.raises(error.AlphabetError):
        d.add_edge(d.initial_state, s, 'b')
        