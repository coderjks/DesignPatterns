class State:

    def behave(self):
        pass


class RingState(State):

    def behave(self):
        print('Ringing Ringing !! Trr Trr ...')


class SilentState(State):

    def behave(self):
        print('Ghrr Ghrr !! No Sound ... only vibration')
