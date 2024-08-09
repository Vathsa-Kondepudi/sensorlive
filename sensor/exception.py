import sys
import os


def error_message_detail(error, error_detail: sys):
    # Retrieve exception traceback object
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename where the exception occurred
    filename = exc_tb.tb_frame.f_code.co_filename
    # Construct the detailed error message
    error_message = "Error occurred in the file [{0}] at line number [{1}]: {2}".format(
        filename, exc_tb.tb_lineno, str(error))
    
    return error_message

class SensorException(Exception):
    def __init__(self, error, error_detail: sys):
        # Call the base class constructor with the parameters it needs
        super().__init__(str(error))
        # Store the detailed error message
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
