import logging
import os

def setup_logger():
    logger = logging.getLogger("Mon100_app") # to create a logger instance
    logger.setLevel(logging.INFO)

    ## important or same logs will be printed multiple times
    # Avoid duplicate logs
    if logger.hasHandlers():
        return logger

    # Create logs folder if not exists
    os.makedirs("mon100logs", exist_ok=True)

    # Format of logs
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console handler (prints to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler (writes to file)
    file_handler = logging.FileHandler("mon100logs/app.log")
    file_handler.setFormatter(formatter)

    # Attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Create a global logger
logger = setup_logger()