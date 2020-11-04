import pytest
from src import state

def test_init():
    s = state.State('s1', True, False)
    assert(s.label == 's1')
    assert(len(s.edges) == 0)
    assert(s.accepting)
    assert(not s.initial)


def test_change():
    s = state.State('s', False, False)
    s.set_acc()
    assert(s.accepting)


def test_edge():
    s1 = state.State('s1', False, True)
    s2 = state.State('s2', False, False)
    s1.add_edge('a', s2)
    assert(len(s1.edges) == 1)
    assert(len(s2.edges) == 0)