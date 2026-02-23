import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime

# Project root: src/logger/__init__.py -> go up 3 levels
ROOT_DIR = Path(__file__).parent.parent.parent

# Constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

# Construct log file path
log_dir_path = os.path.join(ROOT_DIR, LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

# Configure logging at module level so it's ready on import
logging.basicConfig(
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT),
        logging.StreamHandler()
    ]
)