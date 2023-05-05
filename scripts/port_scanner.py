#!/usr/bin/env python3

import os
import sys
import socket
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="open_ports.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(ip, port):
            open_ports.append(port)
    return open_ports

def log_open_ports(ip, start_port, end_port):
    open_ports = scan_ports(ip, start_port, end_port)
    logging.info(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            try:
                ip = sys.argv[1]
                start_port = int(sys.argv[2])
                end_port = int(sys.argv[3])
            except ValueError:
                print("Invalid IP or port range. Exiting.")
                sys.exit(1)
        else:
            print("Usage: ./port_scanner.py <IP> <start_port> <end_port>")
            sys.exit(1)

        print(f"Scanning {ip} for open ports between {start_port} and {end_port}.")
        log_open_ports(ip, start_port, end_port)
        print("Scan completed. Open ports logged in open_ports.log.")
    
    except KeyboardInterrupt:
        print("\nExiting script...")
        sys.exit(0)
