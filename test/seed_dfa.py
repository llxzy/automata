import sys
sys.path.append("..")
print(sys.path)

from src import dfa
from src import state

def two_state_dfa():
    """
    alphabet: {a}
    s1 -> a -> s2 
    s2 -> a -> s2
    initial: s1
    accepting: s2
    """
    d = dfa.DFA()
    d.states = set()
    d.initial_state = None
    s1 = state.State("s1", False, True)
    s2 = state.State("s2", True, False)
    d.add_state(s1)
    d.add_state(s2)
    d.initial_state = s1
    d.set_alphabet({'a'})
    d.add_edge(s1, s2, 'a')
    d.add_edge(s2, s2, 'a')

    return d


def five_state_dfa():
    """
    alphabet: {a, b, c}
    s1 -> a -> s2
    s2 -> b -> s2
    s2 -> a -> s3
    s3 -> c -> s5
    s5 -> b -> s5
    s5 -> a -> s4
    s4 -> a -> s5
    initial: s1
    accepting: s2, s5
    """
    d = dfa.DFA()
    d.states = set()
    d.initial_state = None
    s1 = state.State("s1", False, True)
    s2 = state.State("s2", True, False)
    s3 = state.State("s3", False, False)
    s4 = state.State("s4", False, False)
    s5 = state.State("s5", True, False)
    d.add_state(s1)
    d.add_state(s2)
    d.add_state(s3)
    d.add_state(s4)
    d.add_state(s5)
    d.initial_state = s1
    d.set_alphabet({'a', 'b', 'c'})
    d.add_edge(s1, s2, 'a')
    d.add_edge(s2, s2, 'b')
    d.add_edge(s2, s3, 'a')
    d.add_edge(s3, s5, 'c')
    d.add_edge(s5, s5, 'b')
    d.add_edge(s5, s4, 'a')
    d.add_edge(s4, s5, 'a')

    return d


def three_state_loop_dfa():
    """
    alphabet: {p, b}
    s1 -> p -> s2
    s2 -> b -> s3
    s3 -> p -> s1
    initial: s1
    accepting: s1
    """
    d = dfa.DFA()
    d.states = set()
    d.initial_state = None
    s1 = state.State('s1', True, True)
    s2 = state.State('s2', False, False)
    s3 = state.State('s3', False, False)
    d.add_state(s1)
    d.add_state(s2)
    d.add_state(s3)
    d.initial_state = s1
    d.alphabet = {'p', 'b'}
    d.add_edge(s1, s2, 'p')
    d.add_edge(s2, s3, 'b')
    d.add_edge(s3, s1, 'p')

    return d