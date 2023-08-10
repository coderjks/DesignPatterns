from logger import Logger


class WarningLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == Logger.WARNING:
            print('Warning: ' + message)
        else:
            super().log(log_level, message)
