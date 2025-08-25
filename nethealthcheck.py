#!/usr/bin/env python3
"""
The nethealthcheck uses Python netmiko library to audit the health check of network devices, mainly Cisco IOSs using the SSH connection. 
The result will save as a CSV format.
"""

import csv
import argparse
import getpass
from netmiko import ConnectHandler


def check_device(ip, username, password):
    """
        use Netmiko library to connect and send the command.
    Args:
        ip (_str_): _remote network device IP_
        username (_str_): _user account_
        password (_str_): _pass key_

    Returns:
        _dict_: _device info result_
    """
    result = {"ip": ip,
              "version": "",
              "cpuinfo": "", 
              "meminfo": "",
              "intinfo": "",
              "connStatus": False}
    
    connection = {
        "ip": ip,
        "username": username,
        "password": password,
        "device_type": "cisco_ios"}

    try:
        # netmiko library for the connection to send command
        with ConnectHandler(**connection) as conn:
            # made the connection successfully
            result["connStatus"] = True
            # send command
            verinfo = conn.send_command("show version")
            cpuinfo = conn.send_command("show processes cpu")
            meminfo = conn.send_command("show processes memory")
            intinfo = conn.send_command("show interfaces status")
            
            # assign the valus
            result["version"] = verinfo
            result["cpu_uil"] = cpuinfo
            result["mem_use"] = meminfo
            result["int_status"] = intinfo

    except Exception as err:
        print(f'device {ip} is unreachable!')
    return result

    
def get_devicehealth(devicelist, output):
    devices = []
    results = []

    with open(devicelist, newline="", encoding="utf-8-sig") as infile:
        readed = csv.DictReader(infile)
        for device in readed:
            devices.append(device)

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    for device in devices:
        device["username"] = username
        device["password"] = password
        deviceresult = check_device(device["ip"], device["username"], device["password"])
        results.append(deviceresult)

    # {'ip': '10.0.0.1', 'version': '', 'cpuinfo': '', 'meminfo': '', 'intinfo': '', 'connStatus': False}
    # {'ip': '10.0.0.2', 'version': '', 'cpuinfo': '', 'meminfo': '', 'intinfo': '', 'connStatus': False}
    if output:
        with open(output, "w", encoding="utf-8") as outfile:
            for result in results:
                print(result)

def main():
    parser = argparse.ArgumentParser(description="Network Device Health Checker")
    parser.add_argument("--input", required=True, help="Load the CSV (ex. devices.csv) with IP Address, Useername, and Password")
    parser.add_argument("--out", help="Output as a JSON file")
    args = parser.parse_args()
    get_devicehealth(args.input, args.out)

if __name__ == "__main__":
    main()