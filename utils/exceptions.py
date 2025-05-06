import sys
import logging
from logger import setup_logger

# Set up the logger for this module
logger = setup_logger(name="ExceptionsLogger", log_level=logging.ERROR)

def get_error_details(error, error_detail: sys):
    """
    Extracts detailed error information including file name, line number, and error message.

    Args:
        error (Exception): The exception instance.
        error_detail (sys): The sys module to extract traceback details.

    Returns:
        str: Formatted error message with details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in file: [{file_name}] at line: [{line_number}] | Message: [{str(error)}]"

class CustomException(Exception):
    """
    Custom exception class that logs detailed error information.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the exception with a detailed error message.

        Args:
            error_message (str): The error message.
            error_detail (sys): The sys module to extract traceback details.
        """
        super().__init__(error_message)
        self.error_message = get_error_details(error_message, error_detail)
        logger.error(self.error_message)  # Log the error

    def __str__(self):
        """
        Return the detailed error message as a string.
        """
        return self.error_message


# Example usage
if __name__ == "__main__":
    try:
        # Simulate an error
        raise ValueError("Invalid value provided!")
    except ValueError as e:
        raise CustomException(e, sys)