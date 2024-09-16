from air_condition import AirCondition


class ICommand:
    def execute(self):
        pass

    def undo(self):
        pass


class TurnOnAcCommand(ICommand):

    def __init__(self, air_condition: AirCondition):
        self._air_condition = air_condition

    def execute(self):
        self._air_condition.turn_on_ac()

    def undo(self):
        self._air_condition.turn_off_ac()


class TurnOffAcCommand(ICommand):
    def __init__(self, air_condition):
        self._air_condition = air_condition

    def execute(self):
        self._air_condition.turn_off_ac()

    def undo(self):
        self._air_condition.turn_off_ac()
