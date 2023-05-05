#!/usr/bin/env python3

import os
import sys
import time
import logging
import psutil
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def get_running_processes():
    return len(psutil.pids())

def log_system_stats(interval=60):
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        running_processes = get_running_processes()

        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_usage}%")
        logging.info(f"Disk Usage: {disk_usage}%")
        logging.info(f"Running Processes: {running_processes}")

        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            print("Invalid interval value. Using default 60 seconds.")
            interval = 60
    else:
        interval = 60

    print(f"Starting system monitoring with an interval of {interval} seconds.")
    print("Press Ctrl+C to stop monitoring.")
    
    try:
        log_system_stats(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
