from command import *
from remote_control import RemoteControl
from air_condition import AirCondition

if __name__ == '__main__':
    air_condition = AirCondition()
    remote_control = RemoteControl()
    remote_control.set_command(TurnOnAcCommand(air_condition))
    remote_control.press_button()

    remote_control.set_command(TurnOffAcCommand(air_condition))
    remote_control.press_button()
