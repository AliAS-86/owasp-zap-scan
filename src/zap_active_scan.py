import time
from zapv2 import ZAPv2
import logging
import requests
import os
# Configure the logging module
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(os.path.splitext(os.path.basename(__file__))[0])
logging.getLogger("urllib3").setLevel(logging.WARNING)