import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with the given name, log file, and level.
    
    Parameters:
    name (str): The name of the logger.
    log_file (str): The log file path.
    level (int): The logging level (default: logging.INFO).
    
    Returns:
    logging.Logger: The configured logger.
    """
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create file handler
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Create formatter and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_exception(logger, exception):
    """
    Logs an exception with traceback.
    
    Parameters:
    logger (logging.Logger): The logger object.
    exception (Exception): The caught exception to log.
    """
    logger.error("Exception occurred", exc_info=True)
