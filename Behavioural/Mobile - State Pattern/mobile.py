from state import RingState


class Mobile:

    def __init__(self, model):
        self.model = model
        self.state = RingState()

    def set_state(self, new_state):
        self.state = new_state

    def ring(self):
        self.state.behave()
