from vehicle import BMW, Audi, Maruti, Hyundai
from abc import ABC, abstractmethod


class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self, luxury_brand):
        pass


class LuxuryVehicleFactory(VehicleFactory):
    def get_vehicle(self, luxury_brand):
        if luxury_brand == 'BMW':
            return BMW()
        elif luxury_brand == 'Audi':
            return Audi()
        else:
            return None


class EconomicVehicleFactory(VehicleFactory):
    def get_vehicle(self, economic_brand):
        if economic_brand == 'Hyundai':
            return Hyundai()
        elif economic_brand == 'Maruti':
            return Maruti()
        else:
            return None
