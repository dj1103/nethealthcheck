# nethealthcheck


## Description

The nethealthcheck uses Python netmiko library to audit the health check of network devices, mainly Cisco IOSs using the SSH connection. The result will save as a JSON format.

     Testing version: Connect via SSH (username/password) to Cisco devices to check the uptime, hardware/software version, CPU usage, memory usage, and interface status.

     
## Usage

    python3 nethealthcheck --input devices.csv --out result.json

    devices.csv format
      ip,username,password
      10.0.0.1,admin,123456
      10.0.0.2,admin,122234
    

## Version

     Testing with Python 3.12, published on 2023-10-02, expires on 2028-10, PEP 693
          https://www.python.org/downloads/


## Dependency

     [required] apt install python3 or download the bianry    # python 3.10 or above
     [required] python3 -m pip install        
     [required] pip install netmiko     # main Python library for network devices to send commands
