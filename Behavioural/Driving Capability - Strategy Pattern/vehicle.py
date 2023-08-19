from drive_strategy import OffRoadDriveStrategy, NormalDriveStrategy, SportsDriveStrategy


class Vehicle:

    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()

    def set_strategy(self, new_strategy):
        self.drive_strategy = new_strategy


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(OffRoadDriveStrategy())


class NormalVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())
