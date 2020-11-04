
class State:
    def __init__(self, label, accepting, initial):
        self.label = label
        self.accepting = accepting
        self.initial = initial
        self.edges = dict()
    
    def set_acc(self):
        self.accepting = True
    
    def set_init(self):
        self.inital = True

    def add_edge(self, edge_label, to_state):
        self.edges[edge_label] = to_state
