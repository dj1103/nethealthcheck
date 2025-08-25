# nethealthcheck


## Description

The nethealthcheck uses Python netmiko library to audit the health check of network devices, mainly Cisco IOSs using the SSH connection. The result will save as a CSV format.

     Testing version: Connect via SSH (username/password) to Cisco devices to check the uptime, hardware/software version, CPU usage, memory usage, and interface status.

     
## Usage

    python3 nethealthcheck --input list.csv --out result.json

    list.csv
         ip
         10.0.0.1
         10.0.0.2
         10.0.0.3

    prompt username and password in a secure method to send commands

## Version

     Testing with Python 3.12, published on 2023-10-02, expires on 2028-10, PEP 693
          https://www.python.org/downloads/


## Dependency

     [required] apt install python3 or download the bianry    # python 3.10 or above
     [required] python3 -m pip install        
     [required] pip install netmiko     # main Python library for network devices to send commands
