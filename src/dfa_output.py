from src import dfa
import json


def outgoing_edges_to_str(state):
    output = ""
    for k, v in state.edges.items():
        output += f"{{{k}:{v.label}}},"
    return output


def outgoing_edges_to_dict(state):
    output = dict()
    for k, v in state.edges.items():
        output[k] = v.label
    return output
    

def to_string(input_dfa):
    lines = []
    for state in list(input_dfa.states):
        line = f"{{{state.label};"
        line += f"outgoing={outgoing_edges_to_str(state)};"
        line += f"accepting={state.accepting};initial={state.initial}}}"
        lines.append(line)
    return "\n".join(lines)


def state_to_dictionary(state):
    out = dict()
    out["accepting"] = state.accepting
    out["initial"] = state.initial
    out["outgoing"] = outgoing_edges_to_dict(state)
    return out


def to_dictionary(input_dfa):
    output = dict()
    states = dict()
    for state in input_dfa.states:
        states[state.label] = state_to_dictionary(state)
    output["states"] = states
    output["alphabet"] = list(input_dfa.alphabet)
    return output


def to_file(input_dfa, filename="output.txt"):
    with open(filename, 'w') as w_file:
        w_file.writelines(to_string(input_dfa))


def to_json(input_dfa, filename="output.json"):
    with open(filename, 'w') as w_file:
        data = json.dump(to_dictionary(input_dfa), w_file)
        #w_file.writelines(data)
        