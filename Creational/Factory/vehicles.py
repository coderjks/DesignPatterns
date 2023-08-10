from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_type, wheels):
        self.vehicle_type = vehicle_type
        self.wheels = wheels

    @abstractmethod
    def drive(self):
        pass


class Truck(Vehicle):

    def __init__(self, vehicle_type, wheels):
        super().__init__(vehicle_type, wheels)

    def drive(self):
        print('This is a {0} having {1} wheels.'.format(self.vehicle_type, self.wheels))


class Bicycle(Vehicle):

    def __init__(self, vehicle_type, wheels):
        super().__init__(vehicle_type, wheels)

    def drive(self):
        print('This is a {0} having {1} wheels.'.format(self.vehicle_type, self.wheels))


class Car(Vehicle):

    def __init__(self, vehicle_type, wheels):
        super().__init__(vehicle_type, wheels)

    def drive(self):
        print('This is a {0} having {1} wheels.'.format(self.vehicle_type, self.wheels))


class MotorCycle(Vehicle):

    def __init__(self, vehicle_type, wheels):
        super().__init__(vehicle_type, wheels)

    def drive(self):
        print('This is a {0} having {1} wheels.'.format(self.vehicle_type, self.wheels))
