import logging
import inspect

def customLogger(logLevel = logging.DEBUG):
    """
    print the log in logger
    :param logLevel: get logging level to print in log
    :return: logger
    """
    #get the name of class/method where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    #by default,log all the messsage since logging level is set to DEBUG
    logger.setLevel(logLevel)

    fileHandler = logging.FileHandler("automation.log", mode = "a")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s %(message)s",
                                  datefmt= "%m/%d/%Y %I:%M:%S %p")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

