import time
import random
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

for _ in range(10):
    logging.info(f"Simulated log entry: {random.randint(100,999)}")
    time.sleep(1)
