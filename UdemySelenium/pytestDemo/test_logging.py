import logging #!!!!!!!!!!!!!!

def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.ERROR) # set level

    # level order
    logger.debug("this is debug")
    logger.info("this is info")
    logger.error("this is error")
    logger.critical("this is critical")
    logger.warning("this is warning")