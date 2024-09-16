from vehicle_factory import EconomicVehicleFactory, LuxuryVehicleFactory


class AbstractFactoryProducer:
    @staticmethod
    def get_factory(factory_name):
        if factory_name == "LuxuryFactory":
            return LuxuryVehicleFactory()
        elif factory_name == "EconomicFactory":
            return EconomicVehicleFactory()
        else:
            return NotImplemented
