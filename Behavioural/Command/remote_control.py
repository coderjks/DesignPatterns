from command import ICommand
from typing import List


class RemoteControl:

    def __init__(self):
        self.command = None
        self.command_list: List[ICommand] = list()

    def press_button(self):
        self.command_list.append(self.command)
        self.command.execute()

    def undo(self):
        if self.command_list:
            last_command = self.command_list.pop()
            last_command.undo()

    def set_command(self, command):
        self.command = command
