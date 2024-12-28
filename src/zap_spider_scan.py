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


# This script attack the juice shop test platform running on the localhost for security vulnerabilities
target_url = "https://public-firing-range.appspot.com"

# a sample api key used here to connect to the zap api
api_key = "myTestKey"

# start zap api instance with providing api_key and proxy settings
zap = ZAPv2(apikey=api_key, proxies={'http': 'http://localhost:8080', 'https': 'https://localhost:8080'})

# Check the readiness of zap service
logger.info(f"ZAP Version: {zap.core.version}")

# check the readiness of the target url
logger.info(f"Target URL: {target_url}")

logger.info(f"Spidering target: {target_url}")

# Capturing scan ID that returned by the scan to support other operations like getting the scan status and perform concurrent scans
scanID = zap.spider.scan(target_url)
while int(zap.spider.status(scanID)) < 100:
    logger.info(f"Spider progress: {zap.spider.status(scanID)}")
    time.sleep(1)

logger.info("Spider completed")
logger.info("\n".join(map(str, zap.spider.results(scanID))))