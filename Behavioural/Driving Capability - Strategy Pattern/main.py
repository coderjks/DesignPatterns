from drive_strategy import OffRoadDriveStrategy, SportsDriveStrategy, NormalDriveStrategy
from vehicle import OffRoadVehicle, NormalVehicle, SportsVehicle

if __name__ == "__main__":
    sports_car = SportsVehicle()
    sports_car.drive()

    normal_car = NormalVehicle()
    normal_car.drive()

    off_road_car = OffRoadVehicle()
    off_road_car.drive()
