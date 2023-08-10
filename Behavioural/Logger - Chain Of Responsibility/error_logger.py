from logger import Logger


class ErrorLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == Logger.ERROR:
            print('Error: ' + message)
        else:
            super().log(log_level, message)
