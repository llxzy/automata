from src import error
from src.state import State

class DFA():
    def __init__(self):
        s = State('s1', False, True)
        self.states = set()
        self.states.add(s)
        self.initial_state = s


    def __eq__(self, other):
        return self.alphabet == other.alphabet\
            and self.initial_state.label == other.initial_state.label\
                and set(map(lambda s: (s.label, s.initial, s.accepting), self.states))\
                == set(map(lambda s: (s.label, s.initial, s.accepting), other.states))
            

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet


    def add_state(self, new_state):
        if new_state.initial and self.initial_state != None:
            raise error.StateError("DFA already has an initial state")
        if new_state.label in map(lambda x: x.label, self.states):
            raise error.StateError("A state with that label is already present")
        self.states.add(new_state)


    def add_edge(self, state_from, state_to, label):
        if not set([state_from, state_to]).issubset(self.states):
            raise error.StateError("State not found in DFA")
        if label not in self.alphabet:
            raise error.AlphabetError(label, "Given label not present in DFA alphabet.")

        state_from.add_edge(label, state_to)


    def accepts(self, dfa_input):
        dfa_input = dfa_input.strip()
        if not all(map(lambda c: c in self.alphabet, dfa_input)):
            return False
        return rec_travel(self.initial_state, dfa_input)
        

def rec_travel(state, dfa_input):
    if len(dfa_input) == 0:
        return state.accepting
    try:
        next_state = state.edges[dfa_input[0]]
    except KeyError:
        return False
    return rec_travel(next_state, dfa_input[1:])


def get_state_by_label(label, states):
    for state in states:
        if state.label == label:
            return state