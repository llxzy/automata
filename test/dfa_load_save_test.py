import pytest
import os
from src import dfa
from src import dfa_create as create 
from src import dfa_output as output
from . import seed_dfa

d = seed_dfa.two_state_dfa()
expected_json_path = "./output.json"
expected_txt_path = "./output.txt"
expected_string = "{s1;outgoing={a:s1},;accepting=False;initial=True}"


def test_write_to_read_from_json():
    output.to_json(d)
    assert(os.path.exists(expected_json_path))
    new_dfa = create.from_json(expected_json_path)
    assert(d == new_dfa)

    #cleanup
    if os.path.exists(expected_json_path):
        os.remove(expected_json_path)


def test_text_output():
    d = dfa.DFA()
    d.set_alphabet({'a'})
    d.add_edge(d.initial_state, d.initial_state, 'a')
    assert(output.to_string(d) == expected_string)


def test_text_file_output():
    d = dfa.DFA()
    d.set_alphabet({'a'})
    d.add_edge(d.initial_state, d.initial_state, 'a')
    output.to_file(d)
    with open(expected_txt_path, 'r') as f:
        assert(f.readline() == expected_string)
    
    #cleanup
    if os.path.exists(expected_txt_path):
        os.remove(expected_txt_path)

