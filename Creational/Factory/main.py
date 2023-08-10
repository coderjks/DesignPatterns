from factory import VehicleFactory

if __name__ == "__main__":
    truck = VehicleFactory.get_vehicle('Truck')
    truck.drive()

    car = VehicleFactory.get_vehicle('Car')
    car.drive()

    VehicleFactory.get_vehicle('Ship')

