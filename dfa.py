from automata.fa.dfa import DFA

def automata():
    palabra = DFA(
        states = {'q0', 'q1', 'q2', 'q3', 'q4'},
        input_symbols = {'r', 'i', 'c', 'o'},
        transitions = {
            'q0': {'r': 'q1'},
            'q1': {'i': 'q2'},
            'q2': {'c': 'q3'},
            'q3': {'o': 'q4'}
        },
        initial_state = 'q0',
        final_states = {'q4'},
        allow_partial = True
    )
    return palabra