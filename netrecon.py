import socket
import sys
import argparse

def check_port(host, port):
    sock = socket.socket()
    sock.settimeout(2)

    res = sock.connect_ex((host, port))

    if(res == 0):
        print(f"[+] {port}/tcp responded")
    else:
        print(f"[-] {port}/tcp didn't respond")
    sock.close()
    
parser = argparse.ArgumentParser(description="NetRecon: Network recon tool")
parser.add_argument("target", help="IP address to scan")
parser.add_argument("--ports", default="8000", help="comma-separated ports")

args = parser.parse_args()

nports = args.ports.split(",")

for port in nports:
    check_port(args.target, int(port))
