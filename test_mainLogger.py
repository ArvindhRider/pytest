import inspect
import logging
class Logger:
    def getLogs(self):

        #To get the exact file path
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # like __dirName we use this to print test name
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        # we can set levels to provide logs only for errors
        logger.setLevel(logging.DEBUG)

        return logger

