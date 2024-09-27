import socket
import subprocess
import sys
from IPy import IP
from termcolor import colored


"""
target = "scanme.nmap.org"
targetID = socket.gethostbyname(target)

tstart = datetime.now()
print("Scanning...")

try:
    for port in range(1, 10000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetID, port))

        if result == 0:
            print(f"Offene Verbindung in Port {str(port)}")
        sock.close()
except Exception:
    print("Error")
    sys.exit()

tend = datetime.now()
ttime = tend - tstart
print(f"Beendet in {ttime} Sekunden")
"""

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        real_ip = socket.gethostbyname(ip)
        return real_ip


def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(colored(f"[+] Port {port} ist offen", "green"))
        open_ports.append(port)
        sock.close()
    except:
        print(colored(f"[-] Port {port} ist geschlossen", "red"))


ip = input("Welches Ziel soll gescannt werden? ")
converted_ip = check_ip(ip)
ports = int(input("Wie viele Ports möchtest du scannen? "))
open_ports = []


for port in range(1, ports + 1):
    scan_port(converted_ip, port)

print(colored(f"Offene Ports: {open_ports}"))
