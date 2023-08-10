from error_logger import ErrorLogger
from warning_logger import WarningLogger
from info_logger import InfoLogger


logger = InfoLogger(WarningLogger(ErrorLogger(None)))
logger.log(1, 'This is info logger')
logger.log(2, 'This is warning logger')
logger.log(3, 'This is error logger')
logger.log(4, 'This is unknown logger')


