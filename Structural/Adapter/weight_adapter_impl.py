from weight_adapter import WeightAdapter
from weight_machine import WeightMachine


class WeightAdapterImpl(WeightAdapter):

    def __init__(self, weight_machine: WeightMachine):
        self.weight_machine = weight_machine

    def get_weight_in_kgs(self):
        return self.weight_machine.get_weight_in_pounds() * 0.45
