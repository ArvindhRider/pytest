import logging


def test_logger():
 logger = logging.getLogger(__name__) # like __dirName we use this to print test name
 fileHandler = logging.FileHandler('logfile.log')
 formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
 fileHandler.setFormatter(formatter)
 logger.addHandler(fileHandler)


# we can set levels to provide logs only for errors
 logger.setLevel(logging.ERROR)
 logger.debug("TTEST")
 logger.error("Error file")


