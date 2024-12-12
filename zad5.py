#Napisac obiektowo program, ktory realizuje automat stanow (np. Mealy'ego albo Moore'a),
#czyli nalezy stworzyc odpowiednie klasy z funkcjami, a nastepnie z nich utworzyc konkretna przykladowe instancje

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, next_state, output):
        self.transitions[symbol] = (next_state, output)

    def get_transition(self, symbol):
        return self.transitions.get(symbol)

class Moore:
    def __init__(self, start_state):
        self.current_state = start_state

    def process_input(self, input_symbol):
        transition = self.current_state.get_transition(input_symbol)
        if transition:
            next_state, output = transition
            self.current_state = next_state
            return output
        return None



# Przykłady dla Moore'a
s0 = State("s0")
s1 = State("s1")
s0.add_transition("0", s0, "A")
s0.add_transition("1", s1, "B")
s1.add_transition("0", s1, "C")
s1.add_transition("1", s0, "D")
moore_machine = Moore(s0)
print(moore_machine.process_input("0"))  # A
print(moore_machine.process_input("1"))  # B
print(moore_machine.process_input("0"))  # C
print(moore_machine.process_input("1"))  # D
print(moore_machine.process_input("1"))  # B
print(moore_machine.process_input("1"))  # D
print(moore_machine.process_input("1"))  # B
