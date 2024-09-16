from abstract_factory import AbstractFactoryProducer
from vehicle_factory import VehicleFactory

if __name__ == "__main__":
    factory_producer: AbstractFactoryProducer = AbstractFactoryProducer()
    luxury_vehicle_factory: VehicleFactory = factory_producer.get_factory("LuxuryFactory")
    economic_vehicle_factory: VehicleFactory = factory_producer.get_factory("EconomicFactory")

    print(luxury_vehicle_factory.get_vehicle("BMW"))
    print(economic_vehicle_factory.get_vehicle("Hyundai"))
