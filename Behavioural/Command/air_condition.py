class AirCondition:
    def __init__(self, is_on: bool = False, cur_temp: int = 27):
        self.is_on = is_on
        self.cur_temp = cur_temp

    def turn_on_ac(self):
        print('Turning on the air condition')
        self.is_on = True

    def turn_off_ac(self):
        print('Turning off the air condition')
        self.is_on = False

    def set_cur_temp(self, cur_temp: int):
        self.cur_temp = cur_temp

    def get_cur_temp(self):
        return self.cur_temp
