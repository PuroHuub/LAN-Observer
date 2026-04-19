from main import logger
import pathlib
import logging

logger = logging.getLogger(__name__)

def loggingSet():
    logging.basicConfig(
    level=logging.DEBUG, #большими потому что константа 
    filename="py_log.log",
    filemode="w", 
    ) 
    
    FORMATTER = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s: %(lineno)d - %(message)s"
    )
    
    file = pathlib.Path("py_log.log")
    console_logger = logging.FileHandler(file)
    console_logger.setFormatter(FORMATTER)
    
    logger.addHandler(console_logger)