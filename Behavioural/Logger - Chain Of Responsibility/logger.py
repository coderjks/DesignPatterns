from abc import ABC, abstractmethod


class Logger(ABC):
    INFO = 1
    WARNING = 2
    ERROR = 3

    def __init__(self, next_logger):
        self.logger = next_logger

    @abstractmethod
    def log(self, log_level, message):
        if self.logger:
            self.logger.log(log_level, message)

