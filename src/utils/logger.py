# src/utils/logger.py
# A simple, centralized logging utility for Project Chimera.

import datetime
import config

def log(source, message, level="INFO", header=False):
    """
    A centralized logging function.
    - source: The component of the system generating the log (e.g., "CRC", "SFE").
    - message: The log message.
    - level: The severity of the message (e.g., "INFO", "WARN", "ERROR").
    - header: If True, prints a decorative header for major events.
    """
    if config.OPERATION_MODE == 'development' or level != "INFO":
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        if header:
            print(f"\n{'='*20} {message} {'='*20}")
        else:
            print(f"[{timestamp} | {source:<20} | {level:<5}] {message}")
