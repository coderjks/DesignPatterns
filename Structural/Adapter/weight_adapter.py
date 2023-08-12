from abc import abstractmethod


class WeightAdapter:

    @abstractmethod
    def get_weight_in_kgs(self):
        pass
