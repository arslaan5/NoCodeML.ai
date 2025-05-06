import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="AppLogger", log_dir="logs", log_file="app.log", log_level=logging.INFO):
    """
    Sets up a logger with a rotating file handler and console output.

    Args:
        name (str): Name of the logger.
        log_dir (str): Directory to store log files.
        log_file (str): Name of the log file.
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure log file path
    log_path = os.path.join(log_dir, log_file)

    # Create handlers
    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=3)  # 5MB per file, 3 backups
    console_handler = logging.StreamHandler()

    # Set log format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger(log_level=logging.DEBUG)
    logger.info("Logger initialized successfully.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")