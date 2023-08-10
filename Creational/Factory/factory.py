from vehicles import Truck, Car, Bicycle, MotorCycle


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):
        match vehicle_type:
            case 'Truck':
                return Truck(
                    'Truck', 8
                )
            case 'Car':
                return Car('Car Maruti', 4)
            case 'Bicycle':
                return Bicycle('Hero Cycle', 2)
            case 'Motorcycle':
                return MotorCycle('Pulsar 250', 2)
            case _:
                print('Vehicle type not available.')
