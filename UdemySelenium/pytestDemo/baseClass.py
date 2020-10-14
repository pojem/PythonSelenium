import inspect
import logging


class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)  # set level
        return logger

        # level order
        #logger.debug("this is debug")
        #logger.info("this is info")
        #logger.error("this is error")
        #logger.critical("this is critical")
        #logger.warning("this is warning")