import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where log files will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Construct the full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log messages will be written to this file
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set the logging level to INFO
)
