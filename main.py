from sensor.exception import SensorException
import sys
from sensor.logger import logging


def test_exception():
    try:
        logging.info("There is a division by zero error here")
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Raise the custom exception with the original exception and sys for traceback details
        raise SensorException(e, sys)

if __name__ == "__main__":  # Correct the main block
    try:
        test_exception()  # Call the test_exception function to simulate the error
    except SensorException as e:
        raise SensorException(e,sys) # Print the error message from the SensorException
