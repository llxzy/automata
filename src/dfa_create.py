import json
from src.dfa import DFA
from src.state import State


def get_state_by_label(label, states):
    for state in states:
        if state.label == label:
            return state


def from_json(filename):
    d = DFA()
    d.states = set()
    d.initial_state = None
    with open(filename, 'r') as r_file:
        dfa_data = json.load(r_file)
    d.set_alphabet(set(dfa_data["alphabet"]))
    states = dfa_data["states"]

    for label, state_data in states.items():
        s = State(label, state_data["accepting"], state_data["initial"])
        d.add_state(s)
        if s.initial:
            d.initial_state = s

    for label, state_data in states.items():
        from_state = get_state_by_label(label, d.states)
        # need to iter twice to create transitions - better way might exist
        for transition_label, to_state_label in state_data["outgoing"].items():
            to_state = get_state_by_label(to_state_label, d.states)
            d.add_edge(from_state, to_state, transition_label)

    return d