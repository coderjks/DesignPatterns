from weight_adapter_impl import WeightAdapterImpl
from weight_machine_impl import WeightMachineForAdults

if __name__ == "__main__":
    weight_adapter = WeightAdapterImpl(WeightMachineForAdults())
    print(weight_adapter.get_weight_in_kgs())
