import pytest
from . import seed_dfa

ts = seed_dfa.two_state_dfa()


def test_two_state_accepting():
    assert(ts.accepts('a'))
    assert(ts.accepts('aaaaa'))


def test_two_state_not_accepting():
    assert(not ts.accepts('b'))
    assert(not ts.accepts(''))


fs = seed_dfa.five_state_dfa()


def test_five_state_accepting():
    correct_examples = [
    "abbbb",
    "a",
    "aacbb",
    "aacbaab",
    "aacaab",
    "abac",
    "ab"
    ]
    for example in correct_examples:
        assert(fs.accepts(example))


def test_five_state_not_accepting():
    incorrect_examples = [
        "b",
        "abbba",
        "abacba",
        "abacaaa",
        "aacab",
        ""
    ]
    for example in incorrect_examples:
        assert(not fs.accepts(example))
        

ts_l = seed_dfa.three_state_loop_dfa()


def test_three_state_loop_accepting():
    assert(ts_l.accepts("pbp"))
    assert(ts_l.accepts(100*"pbp"))