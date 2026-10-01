import socket
import sys
import argparse
from dataclasses import dataclass

@dataclass
class Service:
    port: int
    protocol: str
    status: str

def check_port(host, port):
    sock = socket.socket()
    sock.settimeout(2)

    res = sock.connect_ex((host, port))

    if(res == 0):
        sock.close()
        return(Service(port, protocol="tcp", status="open"))
    
    else:
        sock.close()
        return(Service(port, protocol="tcp", status="closed"))
    
parser = argparse.ArgumentParser(description="NetRecon: Network recon tool")  # parser
parser.add_argument("target", help="IP address to scan")  # args.target
parser.add_argument("--ports", default="8000", help="comma-separated ports")  # args.ports

args = parser.parse_args()  # args
nports = args.ports.split(",")  # nports

for p in nports:
    print(check_port(args.target, int(p)))


