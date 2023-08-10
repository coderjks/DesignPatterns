class DriveStrategy:
    def drive(self):
        pass


class OffRoadDriveStrategy(DriveStrategy):

    def drive(self):
        print('This vehicle has off-road strategy')


class SportsDriveStrategy(DriveStrategy):

    def drive(self):
        print('This vehicle has sports strategy')


class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print('This vehicle has normal drive strategy')
